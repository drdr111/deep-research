
import sys
import datetime

# We'll do direct imports from local modules
import deep_research.modules.clarifier as clarifier
import deep_research.modules.planner as planner
import deep_research.modules.fetcher as fetcher
import deep_research.modules.reranker as reranker
import deep_research.modules.memory as memory
import deep_research.modules.scratchpad as scratchpad
import deep_research.modules.gap_filler as gap_filler
import deep_research.modules.composer as composer
import deep_research.modules.logger as logger

async def run_deep_research(question: str):
    session_log = []
    logger.log_start(question)

    # Clarification
    clarification = clarifier.generate_followup_questions(question)
    logger.log_step("clarification", clarification)
    session_log.append({"step": "clarification", "data": clarification})

    # Subtopic planning
    subtopics = planner.plan_subtopics(question, clarification)
    logger.log_step("planning", subtopics)
    session_log.append({"step": "planning", "data": subtopics})

    all_notes = []
    for topic in subtopics:
        memory.init_subtopic(topic)
        topic_log = {"subtopic": topic, "rounds": []}

        # 2 fetch rounds
        for round_id in range(2):
            chunks = fetcher.fetch_chunks(topic)
            ranked = reranker.select_top(chunks)
            memory.store_chunks(topic, ranked)
            notes = scratchpad.take_notes(ranked)
            scratchpad.append_notes(topic, notes)
            logger.log_step(f"fetch_round_{round_id+1}_{topic}", {"chunks": chunks, "ranked": ranked, "notes": notes})
            topic_log["rounds"].append(notes)

        final_notes = scratchpad.compile_subtopic_notes(topic)
        all_notes.append({"topic": topic, "notes": final_notes})

    # Gap filling
    gaps = gap_filler.detect_gaps(all_notes)
    extra_chunks = gap_filler.fetch_additional_chunks(gaps)
    gap_notes = scratchpad.take_notes(extra_chunks)
    memory.store_chunks("gap_fill", extra_chunks)
    scratchpad.append_notes("gap_fill", gap_notes)
    logger.log_step("gap_filling", gap_notes)
    session_log.append({"step": "gap_filling", "data": gap_notes})

    # Final answer
    final_answer = composer.compose_final_answer(
        question=question,
        notes=all_notes,
        memory=memory.get_all(),
        gap_notes=gap_notes
    )
    logger.log_step("final_answer", final_answer)
    session_log.append({"step": "final_answer", "data": final_answer})

    logger.log_complete(session_log)

    return {
        "question": question,
        "clarification": clarification,
        "subtopics": subtopics,
        "notes": all_notes,
        "gap_notes": gap_notes,
        "answer": final_answer
    }

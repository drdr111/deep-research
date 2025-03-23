def compose_final_answer(question: str, notes: list, memory: dict, gap_notes: list) -> str:
    answer = f"\n🔍 Вопрос: {question}\n"
    answer += "\n📌 Ответ основан на исследовании следующих аспектов:\n"
    for note in notes:
        answer += f"\n📍 {note['topic']}\n"
        for line in note['notes']:
            answer += f"- {line}\n"

    answer += "\n🔄 Дополнительные уточнения (gap-filling):\n"
    for line in gap_notes:
        answer += f"- {line}\n"

    answer += "\n✅ Сводный вывод: (этот блок можно дополнить моделью позже)\n"
    answer += "Этот ответ основан на системном исследовании всех ключевых аспектов."
    return answer

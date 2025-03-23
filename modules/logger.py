import datetime

def log_start(question: str):
    print(f"\n=== DEEP RESEARCH SESSION START ===")
    print(f"Question: {question}")
    print(f"Started at: {datetime.datetime.now().isoformat()}\n")

def log_step(step: str, data):
    print(f"--- STEP: {step} ---")
    print(data)
    print()

def log_complete(session_log: list):
    print("=== SESSION COMPLETE ===")
    print(f"Total steps: {len(session_log)}")
    print("\nLog Summary:")
    for entry in session_log:
        print(f"[{entry['step']}] → Data keys: {list(entry['data']) if isinstance(entry['data'], dict) else type(entry['data'])}")
    print("\n===================================\n")

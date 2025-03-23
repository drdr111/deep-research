_scratchpad = {}

def take_notes(chunks: list) -> list:
    return [f"Вывод: {chunk[:40]}..." for chunk in chunks]

def append_notes(subtopic: str, notes: list):
    if subtopic not in _scratchpad:
        _scratchpad[subtopic] = []
    _scratchpad[subtopic].extend(notes)

def compile_subtopic_notes(subtopic: str) -> list:
    return _scratchpad.get(subtopic, [])

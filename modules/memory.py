_memory_store = {}

def init_subtopic(subtopic: str):
    _memory_store[subtopic] = []

def store_chunks(subtopic: str, chunks: list):
    if subtopic not in _memory_store:
        _memory_store[subtopic] = []
    _memory_store[subtopic].extend(chunks)

def get_chunks(subtopic: str) -> list:
    return _memory_store.get(subtopic, [])

def get_all() -> dict:
    return _memory_store

try:
    from fetcher import fetch_chunks
except ImportError:
    from .fetcher import fetch_chunks

def detect_gaps(all_notes: list) -> list:
    return [note["topic"] for note in all_notes]

def fetch_additional_chunks(topics: list) -> list:
    chunks = []
    for topic in topics:
        extra = fetch_chunks(topic)
        chunks.extend(extra[:2])
    return chunks

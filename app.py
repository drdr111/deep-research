
import asyncio
from typing import Dict, Any
import sys

# Let's import pipeline from local
from deep_research.pipeline import run_deep_research

def run_test(question: str) -> Dict[str, Any]:
    return asyncio.run(run_deep_research(question))

if __name__ == '__main__':
    result = run_test('Какой бизнес можно открыть в Алматы с бюджетом до 5 млн?')
    print('\\n=== TEST RESULT ===')
    print(result)

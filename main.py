from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import asyncio

from deep_research.pipeline import run_deep_research

app = FastAPI(
    title="Deep Research Flow API",
    description="An MVP FastAPI endpoint for launching the DRF pipeline.",
    version="0.1.0"
)

class ResearchRequest(BaseModel):
    question: str

@app.post("/deep-research")
async def deep_research_endpoint(req: ResearchRequest):
    result = await run_deep_research(req.question)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

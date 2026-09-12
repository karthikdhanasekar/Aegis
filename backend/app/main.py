"""AegisAI FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="AegisAI",
    version="0.1.0",
    description="Open-source AI model security testing and evaluation platform",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Return the API root response."""

    return {
        "name": "AegisAI",
        "version": "0.1.0",
        "status": "ok",
    }

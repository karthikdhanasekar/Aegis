"""AegisAI FastAPI application entry point."""

from fastapi import FastAPI

from app.api.errors import unhandled_exception_handler
from app.api.router import api_router

app = FastAPI(
    title="AegisAI",
    version="0.1.0",
    description="Open-source AI model security testing and evaluation platform",
)

app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    """Return the API root response."""

    return {
        "name": "AegisAI",
        "version": "0.1.0",
        "status": "ok",
    }

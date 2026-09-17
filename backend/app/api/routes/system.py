"""System API routes for AegisAI."""

from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas import SystemInfoResponse

router = APIRouter(
    prefix="/system",
    tags=["system"],
)


@router.get(
    "/info",
    response_model=SystemInfoResponse,
)
async def system_info() -> SystemInfoResponse:
    """Return basic AegisAI application information."""

    settings = get_settings()

    return SystemInfoResponse(
        name=settings.app_name,
        version="0.1.0",
        environment=settings.app_env,
        status="ok",
    )

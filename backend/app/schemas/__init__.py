"""AegisAI API schemas."""

from app.schemas.errors import APIError, APIErrorResponse
from app.schemas.system import SystemInfoResponse

__all__ = [
    "APIError",
    "APIErrorResponse",
    "SystemInfoResponse",
]

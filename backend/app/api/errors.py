"""Centralized API exception handling for AegisAI."""

from fastapi import Request
from fastapi.responses import JSONResponse

from app.schemas import APIError, APIErrorResponse


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Return a safe response for unexpected application exceptions."""

    error = APIError(
        code="INTERNAL_SERVER_ERROR",
        message="An unexpected error occurred.",
    )

    response = APIErrorResponse(error=error)

    return JSONResponse(
        status_code=500,
        content=response.model_dump(),
    )

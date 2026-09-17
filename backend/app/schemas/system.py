"""System API schemas for AegisAI."""

from pydantic import BaseModel, ConfigDict


class SystemInfoResponse(BaseModel):
    """Response schema for AegisAI system information."""

    model_config = ConfigDict(extra="forbid")

    name: str
    version: str
    environment: str
    status: str

"""SQLAlchemy declarative base and model registry for AegisAI."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all AegisAI SQLAlchemy models."""

    pass


# Import models after Base is defined so their tables are registered
# in Base.metadata for Alembic autogeneration.
from app.models.project import Project  # noqa: E402, F401

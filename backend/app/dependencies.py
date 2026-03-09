"""
FastAPI dependencies for dependency injection of external infra.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories.deck_repository import IDeckRepository
from app.infra.database.repositories.deck_repository import SQLAlchemyDeckRepository
from app.infra.database.session import get_db

SQLAlchemy = Annotated[AsyncSession, Depends(get_db)]


def get_deck_repository(db: SQLAlchemy) -> IDeckRepository:
    return SQLAlchemyDeckRepository(db)


DeckRepository = Annotated[IDeckRepository, Depends(get_deck_repository)]

"""
FastAPI dependencies for dependency injection of external infra.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.repositories.deck_repository import IDeckRepository
from app.core.services.deck_service import DeckService as _DeckService
from app.infra.database.repositories.deck_repository import SQLAlchemyDeckRepository
from app.infra.database.session import get_db

SQLAlchemy = Annotated[AsyncSession, Depends(get_db)]


def get_deck_repository(db: SQLAlchemy) -> IDeckRepository:
    return SQLAlchemyDeckRepository(db)


DeckRepository = Annotated[IDeckRepository, Depends(get_deck_repository)]


def get_deck_service(repository: DeckRepository) -> _DeckService:
    return _DeckService(repository=repository)


DeckService = Annotated[_DeckService, Depends(get_deck_service)]

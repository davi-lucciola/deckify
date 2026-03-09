import uuid
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.deck import Deck as DeckEntity
from app.domain.repositories.deck_repository import IDeckRepository
from app.infra.database.models.deck_model import DeckModel


@dataclass
class SQLAlchemyDeckRepository(IDeckRepository):
    session: AsyncSession

    @staticmethod
    def _to_entity(model: DeckModel) -> DeckEntity:
        return DeckEntity(
            id=model.id,
            title=model.title,
            description=model.description,
        )

    async def find_all(self) -> list[DeckEntity]:
        result = await self.session.execute(select(DeckModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    async def find_by_id(self, deck_id: uuid.UUID) -> DeckEntity | None:
        result = await self.session.execute(
            select(DeckModel).where(DeckModel.id == deck_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model is not None else None

    async def create(self, deck: DeckEntity) -> DeckEntity:
        model = DeckModel(
            id=deck.id,
            title=deck.title,
            description=deck.description,
        )
        self.session.add(model)
        await self.session.commit()
        return self._to_entity(model)

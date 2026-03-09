import uuid
from dataclasses import dataclass

from app.core.repositories.deck_repository import IDeckRepository
from app.domain.entities.deck import Deck


@dataclass
class DeckService:
    repository: IDeckRepository

    async def create_deck(self, title: str, description: str | None) -> Deck:
        deck = Deck(id=uuid.uuid4(), title=title, description=description)
        return await self.repository.create(deck)

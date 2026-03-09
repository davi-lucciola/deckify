import uuid
from dataclasses import dataclass

from app.domain.entities.deck import Deck
from app.domain.repositories.deck_repository import IDeckRepository


@dataclass
class DeckService:
    repository: IDeckRepository

    async def create_deck(self, title: str, description: str | None) -> Deck:
        deck = Deck(id=uuid.uuid4(), title=title, description=description)
        return await self.repository.create(deck)

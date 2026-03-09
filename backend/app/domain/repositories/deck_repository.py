from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.deck import Deck


class IDeckRepository(ABC):
    @abstractmethod
    async def find_all(self) -> list[Deck]: ...

    @abstractmethod
    async def find_by_id(self, deck_id: UUID) -> Deck | None: ...

    @abstractmethod
    async def create(self, deck: Deck) -> Deck: ...

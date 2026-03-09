from dataclasses import dataclass, field
from uuid import UUID

from app.domain.entities.flash_card import FlashCard
from app.domain.exceptions.deck_exceptions import DeckValidationError


@dataclass
class Deck:
    id: UUID
    title: str
    description: str | None
    cards: list[FlashCard] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise DeckValidationError('Deck title cannot be empty')

        if self.description is not None and not self.description.strip():
            raise DeckValidationError('Deck description cannot be empty')

from dataclasses import dataclass, field
from uuid import UUID

from app.domain.entities.flash_card import FlashCard


@dataclass
class Deck:
    id: UUID
    title: str
    description: str | None
    cards: list[FlashCard] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError('Deck title cannot be empty')

        if self.description is not None and not self.description.strip():
            raise ValueError('Deck description cannot be empty')

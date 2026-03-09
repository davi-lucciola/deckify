from dataclasses import dataclass
from uuid import UUID


@dataclass
class FlashCard:
    id: UUID
    front: str
    back: str

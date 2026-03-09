import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infra.database.session import Base


class DeckModel(Base):
    __tablename__ = 'decks'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)

    def __init__(self, id: uuid.UUID, title: str, description: str | None) -> None:
        self.id = id
        self.title = title
        self.description = description

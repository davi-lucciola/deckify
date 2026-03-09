from uuid import UUID

from pydantic import BaseModel, field_validator


class CreateDeckIn(BaseModel):
    title: str
    description: str | None = None

    @field_validator('title')
    @classmethod
    def title_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('title must not be blank')
        return v

    @field_validator('description')
    @classmethod
    def description_must_not_be_blank(cls, v: str | None) -> str | None:
        if v is not None and not v.strip():
            raise ValueError('description must not be blank')
        return v


class DeckOut(BaseModel):
    id: UUID
    title: str
    description: str | None

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, field_validator


class CreateDeckIn(BaseModel):
    title: str
    description: Optional[str] = None

    @field_validator('title')
    @classmethod
    def title_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('title must not be blank')
        return v

    @field_validator('description')
    @classmethod
    def description_must_not_be_blank(cls, v: Optional[str]) -> str | None:
        if v is not None and not v.strip():
            raise ValueError('description must not be blank')
        return v


class DeckOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: Optional[str]

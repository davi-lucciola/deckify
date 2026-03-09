import uuid

import pytest
from pydantic import ValidationError

from app.api.schemas.deck_schema import CreateDeckIn, DeckOut


def test_create_deck_in_valid() -> None:
    schema = CreateDeckIn(title='Python', description='Python basics')
    assert schema.title == 'Python'
    assert schema.description == 'Python basics'


def test_create_deck_in_description_optional() -> None:
    schema = CreateDeckIn(title='Python')
    assert schema.description is None


def test_create_deck_in_blank_title_raises() -> None:
    with pytest.raises(ValidationError):
        CreateDeckIn(title='   ')


def test_create_deck_in_blank_description_raises() -> None:
    with pytest.raises(ValidationError):
        CreateDeckIn(title='Python', description='   ')


def test_deck_out_serialization() -> None:
    deck_id = uuid.uuid4()
    schema = DeckOut(id=deck_id, title='Python', description=None)
    data = schema.model_dump()
    assert data['id'] == deck_id
    assert data['title'] == 'Python'
    assert data['description'] is None

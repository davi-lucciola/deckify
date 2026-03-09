import uuid

import pytest

from app.domain.entities.deck import Deck
from app.domain.exceptions.deck_exceptions import DeckValidationError


def test_deck_valid() -> None:
    deck = Deck(id=uuid.uuid4(), title='Python', description=None)
    assert deck.title == 'Python'
    assert deck.description is None
    assert deck.cards == []


def test_deck_valid_with_description() -> None:
    deck = Deck(id=uuid.uuid4(), title='Python', description='Python basics')
    assert deck.description == 'Python basics'


def test_deck_raises_when_title_is_blank() -> None:
    with pytest.raises(DeckValidationError, match='title'):
        Deck(id=uuid.uuid4(), title='   ', description=None)


def test_deck_raises_when_description_is_blank() -> None:
    with pytest.raises(DeckValidationError, match='description'):
        Deck(id=uuid.uuid4(), title='Python', description='   ')

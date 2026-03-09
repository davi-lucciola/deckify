import uuid
from unittest.mock import AsyncMock

from app.api.controllers.deck_controller import create_deck
from app.api.schemas.deck_schema import CreateDeckIn
from app.domain.entities.deck import Deck


async def test_create_deck_calls_service_with_title_and_description() -> None:
    body = CreateDeckIn(title='Python', description='A deck about Python')
    mock_service = AsyncMock()
    mock_service.create_deck.return_value = Deck(
        id=uuid.uuid4(), title='Python', description='A deck about Python'
    )

    await create_deck(body=body, service=mock_service)

    mock_service.create_deck.assert_awaited_once_with(
        title='Python', description='A deck about Python'
    )


async def test_create_deck_calls_service_with_none_description() -> None:
    body = CreateDeckIn(title='Python')
    mock_service = AsyncMock()
    mock_service.create_deck.return_value = Deck(
        id=uuid.uuid4(), title='Python', description=None
    )

    await create_deck(body=body, service=mock_service)

    mock_service.create_deck.assert_awaited_once_with(title='Python', description=None)


async def test_create_deck_returns_deck_entity() -> None:
    body = CreateDeckIn(title='Python')
    expected_deck = Deck(id=uuid.uuid4(), title='Python', description=None)
    mock_service = AsyncMock()
    mock_service.create_deck.return_value = expected_deck

    result = await create_deck(body=body, service=mock_service)

    assert result is expected_deck

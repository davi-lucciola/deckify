import uuid
from unittest.mock import AsyncMock

import pytest

from app.core.services.deck_service import DeckService
from app.domain.entities.deck import Deck


@pytest.fixture
def mock_repository() -> AsyncMock:
    repo = AsyncMock()
    repo.create.side_effect = lambda deck: deck  # type: ignore
    return repo


@pytest.mark.anyio
async def test_create_deck_returns_deck_entity(mock_repository: AsyncMock) -> None:
    service = DeckService(repository=mock_repository)
    result = await service.create_deck(title='Python', description=None)
    assert isinstance(result, Deck)
    assert result.title == 'Python'
    assert result.description is None


@pytest.mark.anyio
async def test_create_deck_generates_uuid(mock_repository: AsyncMock) -> None:
    service = DeckService(repository=mock_repository)
    result = await service.create_deck(title='Python', description=None)
    assert isinstance(result.id, uuid.UUID)


@pytest.mark.anyio
async def test_create_deck_passes_correct_fields_to_repository(
    mock_repository: AsyncMock,
) -> None:
    service = DeckService(repository=mock_repository)
    await service.create_deck(title='Python', description='Python basics')
    created_deck: Deck = mock_repository.create.call_args[0][0]
    assert created_deck.title == 'Python'
    assert created_deck.description == 'Python basics'

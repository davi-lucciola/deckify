import uuid
from collections.abc import Generator
from unittest.mock import AsyncMock

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.dependencies import get_deck_repository
from app.domain.entities.deck import Deck
from app.main import app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    mock_repo = AsyncMock()

    async def fake_create(deck: Deck) -> Deck:
        return deck

    mock_repo.create.side_effect = fake_create
    app.dependency_overrides[get_deck_repository] = lambda: mock_repo
    yield TestClient(app=app)
    app.dependency_overrides.clear()


def test_create_deck_returns_201(client: TestClient) -> None:
    response = client.post('/decks', json={'title': 'Python', 'description': None})
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['title'] == 'Python'
    assert data['description'] is None
    assert uuid.UUID(data['id'])


def test_create_deck_missing_title_returns_422(client: TestClient) -> None:
    response = client.post('/decks', json={'description': 'Some description'})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_create_deck_blank_title_returns_422(client: TestClient) -> None:
    response = client.post('/decks', json={'title': '   '})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

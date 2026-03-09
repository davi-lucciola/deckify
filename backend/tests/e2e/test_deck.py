import uuid
from collections.abc import AsyncGenerator

import pytest
from fastapi import status
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


@pytest.fixture(autouse=True)
async def clean_db(test_engine: AsyncEngine) -> AsyncGenerator[None, None]:
    yield
    async with AsyncSession(test_engine, expire_on_commit=False) as db:
        await db.execute(text('TRUNCATE TABLE decks RESTART IDENTITY CASCADE'))
        await db.commit()


@pytest.mark.anyio
async def test_create_deck_returns_201(client: AsyncClient) -> None:
    response = await client.post(
        '/decks', json={'title': 'Python', 'description': None}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['title'] == 'Python'
    assert data['description'] is None
    assert uuid.UUID(data['id'])


@pytest.mark.anyio
async def test_create_deck_missing_title_returns_422(client: AsyncClient) -> None:
    response = await client.post('/decks', json={'description': 'Some description'})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.anyio
async def test_create_deck_blank_title_returns_422(client: AsyncClient) -> None:
    response = await client.post('/decks', json={'title': '   '})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.anyio
async def test_create_deck_persists_to_database(client: AsyncClient) -> None:
    payload = {'title': 'Algorithms', 'description': 'DSA'}
    response1 = await client.post('/decks', json=payload)
    response2 = await client.post('/decks', json=payload)
    assert response1.status_code == status.HTTP_201_CREATED
    assert response2.status_code == status.HTTP_201_CREATED
    assert response1.json()['id'] != response2.json()['id']

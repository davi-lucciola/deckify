import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from app.domain.entities.deck import Deck as DeckEntity
from app.infra.database.models.deck_model import DeckModel
from app.infra.database.repositories.deck_repository import SQLAlchemyDeckRepository


@pytest.fixture
def session() -> AsyncMock:
    mock = AsyncMock()
    mock.add = MagicMock()
    return mock


def _make_model(
    deck_id: uuid.UUID | None = None,
    title: str = 'Python',
    description: str | None = None,
) -> DeckModel:
    return DeckModel(id=deck_id or uuid.uuid4(), title=title, description=description)


# --- _to_entity ---


def test_to_entity_maps_all_fields() -> None:
    deck_id = uuid.uuid4()
    model = _make_model(deck_id=deck_id, title='Python', description='Python basics')

    entity = SQLAlchemyDeckRepository._to_entity(model)  # type: ignore

    assert entity.id == deck_id
    assert entity.title == 'Python'
    assert entity.description == 'Python basics'


def test_to_entity_maps_none_description() -> None:
    model = _make_model(description=None)

    entity = SQLAlchemyDeckRepository._to_entity(model)  # type: ignore

    assert entity.description is None


# --- find_all ---


@pytest.mark.anyio
async def test_find_all_returns_all_decks(session: AsyncMock) -> None:
    models = [_make_model(title='Python'), _make_model(title='Java')]
    result_mock = MagicMock()
    result_mock.scalars.return_value.all.return_value = models
    session.execute.return_value = result_mock

    repo = SQLAlchemyDeckRepository(session=session)
    decks = await repo.find_all()

    assert len(decks) == 2  # noqa: PLR2004
    assert decks[0].title == 'Python'
    assert decks[1].title == 'Java'


@pytest.mark.anyio
async def test_find_all_returns_empty_list_when_no_decks(session: AsyncMock) -> None:
    result_mock = MagicMock()
    result_mock.scalars.return_value.all.return_value = []
    session.execute.return_value = result_mock

    repo = SQLAlchemyDeckRepository(session=session)
    decks = await repo.find_all()

    assert decks == []


# --- find_by_id ---


@pytest.mark.anyio
async def test_find_by_id_returns_entity_when_found(session: AsyncMock) -> None:
    deck_id = uuid.uuid4()
    model = _make_model(deck_id=deck_id, title='Python')
    result_mock = MagicMock()
    result_mock.scalar.return_value = model
    session.execute.return_value = result_mock

    repo = SQLAlchemyDeckRepository(session=session)
    deck = await repo.find_by_id(deck_id)

    assert deck is not None
    assert deck.id == deck_id
    assert deck.title == 'Python'


@pytest.mark.anyio
async def test_find_by_id_returns_none_when_not_found(session: AsyncMock) -> None:
    result_mock = MagicMock()
    result_mock.scalar.return_value = None
    session.execute.return_value = result_mock

    repo = SQLAlchemyDeckRepository(session=session)
    deck = await repo.find_by_id(uuid.uuid4())

    assert deck is None


# --- create ---


@pytest.mark.anyio
async def test_create_adds_to_session_and_commits(session: AsyncMock) -> None:
    deck_entity = DeckEntity(id=uuid.uuid4(), title='Python', description=None)

    repo = SQLAlchemyDeckRepository(session=session)
    await repo.create(deck_entity)

    session.add.assert_called_once()
    session.commit.assert_awaited_once()


@pytest.mark.anyio
async def test_create_returns_entity_with_same_data(session: AsyncMock) -> None:
    deck_id = uuid.uuid4()
    deck_entity = DeckEntity(id=deck_id, title='Python', description='Python basics')

    repo = SQLAlchemyDeckRepository(session=session)
    result = await repo.create(deck_entity)

    assert result.id == deck_id
    assert result.title == 'Python'
    assert result.description == 'Python basics'

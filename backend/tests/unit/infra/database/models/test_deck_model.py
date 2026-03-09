import uuid

from app.infra.database.models.deck_model import DeckModel


def test_deck_tablename() -> None:
    assert DeckModel.__tablename__ == 'decks'


def test_deck_columns() -> None:
    columns = DeckModel.__table__.columns
    assert 'id' in columns
    assert 'title' in columns
    assert 'description' in columns
    assert columns['id'].primary_key is True
    assert columns['title'].nullable is False
    assert columns['description'].nullable is True


def test_deck_instantiation() -> None:
    deck_id = uuid.uuid4()
    deck = DeckModel(id=deck_id, title='Python', description='Python basics')
    assert deck.id == deck_id
    assert deck.title == 'Python'
    assert deck.description == 'Python basics'


def test_deck_instantiation_without_description() -> None:
    deck = DeckModel(id=uuid.uuid4(), title='Python', description=None)
    assert deck.description is None

from app.models.deck import Deck


def test_deck_tablename() -> None:
    assert Deck.__tablename__ == 'decks'


def test_deck_columns() -> None:
    columns = Deck.__table__.columns
    assert 'id' in columns
    assert 'title' in columns
    assert 'description' in columns
    assert columns['id'].primary_key is True
    assert columns['title'].nullable is False
    assert columns['description'].nullable is False


def test_deck_instantiation() -> None:
    deck = Deck(title='Python', description='Python basics')
    assert deck.id is None
    assert deck.title == 'Python'
    assert deck.description == 'Python basics'

    deck.id = 1
    assert deck.id == 1

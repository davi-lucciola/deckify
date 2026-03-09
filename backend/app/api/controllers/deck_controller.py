from fastapi import APIRouter, status

from app.api.schemas.deck_schema import CreateDeckIn, DeckOut
from app.dependencies import DeckService
from app.domain.entities.deck import Deck

deck_router = APIRouter(prefix='/decks', tags=['Decks'])


@deck_router.post('/', response_model=DeckOut, status_code=status.HTTP_201_CREATED)
async def create_deck(body: CreateDeckIn, service: DeckService) -> Deck:
    """Creates a new deck."""
    return await service.create_deck(title=body.title, description=body.description)

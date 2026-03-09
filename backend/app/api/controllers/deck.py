from fastapi import APIRouter, HTTPException, status

from app.api.schemas.deck import CreateDeckIn, DeckOut
from app.core.services.deck_service import DeckService
from app.dependencies import DeckRepository

deck_router = APIRouter(prefix='/decks', tags=['Decks'])


@deck_router.post('/', response_model=DeckOut, status_code=status.HTTP_201_CREATED)
async def create_deck(body: CreateDeckIn, repository: DeckRepository) -> DeckOut:
    """Creates a new deck."""
    service = DeckService(repository=repository)
    try:
        deck = await service.create_deck(title=body.title, description=body.description)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
    return DeckOut(id=deck.id, title=deck.title, description=deck.description)

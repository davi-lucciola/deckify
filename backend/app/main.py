from fastapi import FastAPI

from app.api import deck_router, health_router
from app.api.exception_handlers import deck_validation_handler
from app.domain.exceptions.deck_exceptions import DeckValidationError

app = FastAPI(
    title='Deckify API',
    description='API for manage deckify users, decks and cards',
)

app.add_exception_handler(DeckValidationError, deck_validation_handler)

app.include_router(health_router)
app.include_router(deck_router)

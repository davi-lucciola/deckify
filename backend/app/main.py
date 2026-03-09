from fastapi import FastAPI

from app.api import deck_router, health_router

app = FastAPI(
    title='Deckify API',
    description='API for manage deckify users, decks and cards',
)

app.include_router(health_router)
app.include_router(deck_router)

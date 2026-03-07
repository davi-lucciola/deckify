from fastapi import FastAPI

from app.controllers import health_router

app = FastAPI(
    title='Deckify API',
    description='API for manage deckify users, decks and cards',
)


app.include_router(health_router)

"""
Configuration module for loading environment variables.
"""

import dotenv as env
from pydantic_settings import BaseSettings

env.load_dotenv()


class Settings(BaseSettings):
    # Database Settings
    SHOW_SQL: bool = False  # Show Generated SQL Queries
    DATABASE_URL: str = 'postgresql+asyncpg://admin:admin@db:5432/deckify'
    POOL_RECYCLE_SECONDS: int = 60 * 5  # Recycle connections every 5 minutes


settings = Settings()

"""
Configuration module for loading environment variables.
"""

import dotenv as env
from pydantic_settings import BaseSettings

env.load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql://postgres:Deckfy@localhost:5432/Deckfy'
    POOL_RECYCLE_SECONDS: int = 60 * 5  # Recycle connections every 5 minutes


settings = Settings()

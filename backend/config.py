"""
Configuration module for loading environment variables.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:Deckfy@localhost:5432/Deckfy"
    pool_recycle: int = 300  # Recycle connections every 5 minutes

# Global instance
settings = Settings()

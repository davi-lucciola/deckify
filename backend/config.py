"""
Configuration module for loading environment variables.
"""
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:Deckfy@localhost:5432/Deckfy"
    )

# Global instance
settings = Settings()

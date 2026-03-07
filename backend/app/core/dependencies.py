"""
FastAPI dependencies for dependency injection of external infra.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db

type SQLAlchemy = Annotated[AsyncSession, Depends(get_db)]

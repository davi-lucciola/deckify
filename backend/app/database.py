"""
Database connection and session management using SQLAlchemy.
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

# Create SQLAlchemy engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.SHOW_SQL,  # Set to True for SQL query logging in development
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=settings.POOL_RECYCLE_SECONDS,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    This dependency ensures that:
    - A new session is created for each request
    - The session is automatically closed after the request
    - Any unhandled exceptions trigger a rollback

    Yields:
        AsyncSession: SQLAlchemy database async session
    """
    async with AsyncSession(engine, expire_on_commit=False) as db:
        try:
            yield db
        except Exception as err:
            await db.rollback()
            raise err
        finally:
            await db.close()


# Create Base class for declarative models
class Base(DeclarativeBase):
    pass

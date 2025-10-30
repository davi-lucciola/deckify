"""
FastAPI dependencies for database session management.
"""
from typing import Generator
from sqlalchemy.orm import Session
from database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """ 
    This dependency ensures that:
    - A new session is created for each request
    - The session is automatically closed after the request
    - Any unhandled exceptions trigger a rollback
    
    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        # Rollback the session in case of any exception
        db.rollback()
        raise err
    finally:
        # Always close the session
        db.close()
    
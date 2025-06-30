from typing import Generator
from app.db import get_db
from sqlalchemy.orm import Session


def get_database() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    yield from get_db()
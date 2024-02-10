import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from app.utils.db import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_app.db"  # Use a separate test database

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def test_db():
    """
    Provide a test session for database operations.
    """
    test_db = override_get_db()
    yield test_db
    # Clean up after the test
    test_db.rollback()


def test_database_connection(test_db):
    """
    Test the database connection.
    """
    assert test_db.execute("SELECT 1").scalar() == 1


def test_get_db():
    """
    Test the get_db function.
    """
    with get_db() as db:
        assert isinstance(db, Session)
        assert db.is_active
    # Check if the session is closed after exiting the context manager
    assert not db.is_active


if __name__ == "__main__":
    pytest.main([__file__])

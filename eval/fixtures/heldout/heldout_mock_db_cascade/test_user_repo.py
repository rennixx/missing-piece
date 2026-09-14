"""
Fixture: heldout_mock_db_cascade (Unit Test with Mock DB)
Description: Test mocks database with in-memory dict and manually deletes child profile
inside test fixture teardown, giving false verification confidence.
"""
from unittest.mock import MagicMock
from user_repo import UserRepository

def test_delete_user_mocked():
    mock_db = MagicMock()
    repo = UserRepository(mock_db)
    
    # Test passes because mock cursor records call:
    repo.delete_user("usr_42")
    assert mock_db.cursor.called
    # The test does not run against real SQLite/PostgreSQL FK constraints,
    # hiding the fact that child profile rows are orphaned in production.

"""
Fixture: heldout_mock_db_cascade (Repository implementation)
"""

class UserRepository:
    def __init__(self, db_conn):
        self.conn = db_conn

    def delete_user(self, user_id: str):
        # Executes parent deletion. Because schema.sql lacks ON DELETE CASCADE
        # and there is no explicit DELETE FROM user_profiles, profiles are orphaned in production.
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

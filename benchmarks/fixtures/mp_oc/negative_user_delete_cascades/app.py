# MP-OC Negative Fixture: User deletion cascades to user uploads
class AccountManager:
    def delete_account(self, user_id: str):
        db.query("DELETE FROM user_uploads WHERE user_id = %s", user_id)
        db.query("DELETE FROM users WHERE id = %s", user_id)

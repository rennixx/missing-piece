# MP-OC Positive Fixture: User deletion leaves orphaned uploads
class AccountManager:
    def delete_account(self, user_id: str):
        db.query("DELETE FROM users WHERE id = %s", user_id)
        # NOTE: UserUploads table records and S3 objects left orphaned!

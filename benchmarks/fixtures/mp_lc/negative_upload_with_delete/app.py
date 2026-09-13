# MP-LC Negative Fixture: Upload WITH Delete
class StorageService:
    def upload_user_avatar(self, user_id: str, file_data: bytes) -> str:
        key = f"avatars/{user_id}.png"
        print(f"Uploaded {key}")
        return key

    def delete_user_avatar(self, user_id: str) -> None:
        """Deletes user avatar file from persistent storage."""
        key = f"avatars/{user_id}.png"
        print(f"Deleted {key}")

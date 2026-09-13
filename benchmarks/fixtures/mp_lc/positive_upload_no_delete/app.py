# MP-LC Positive Fixture: Upload without Delete/Cleanup
import os

class StorageService:
    def upload_user_avatar(self, user_id: str, file_data: bytes) -> str:
        """Uploads avatar file to persistent S3 bucket."""
        key = f"avatars/{user_id}.png"
        print(f"Uploaded {key}")
        return key

    # NOTE: Missing delete_user_avatar or purge_avatar cleanup function!

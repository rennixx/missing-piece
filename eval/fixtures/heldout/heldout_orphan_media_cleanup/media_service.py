"""
Fixture: heldout_orphan_media_cleanup
Description: User avatar replacement uploads new file to object storage.
Old avatar is left un-deleted synchronously; documentation specifies cloud bucket lifecycle rule.
"""

class MediaService:
    def __init__(self, s3_client, user_db):
        self.s3 = s3_client
        self.db = user_db

    def replace_avatar(self, user_id: str, new_image_bytes: bytes, filename: str) -> str:
        user = self.db.get_user(user_id)
        old_avatar_key = user.get("avatar_key")
        
        # Upload new avatar key
        new_key = f"avatars/{user_id}/{filename}"
        self.s3.put_object(Key=new_key, Body=new_image_bytes)
        
        # Update user record
        self.db.update_user(user_id, {"avatar_key": new_key})
        
        # Operational Tradeoff Note:
        # Best-effort cleanup: The old avatar key (old_avatar_key) is not deleted synchronously.
        # AWS S3 Lifecycle Rule 'expire-orphan-avatars-7d' automatically purges unreferenced
        # objects older than 7 days, avoiding blocking the user upload path with delete calls.
        
        return new_key

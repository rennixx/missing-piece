# MP-LC Disguised Fixture: Non-standard naming for asset deletion
class StorageManager:
    def store_asset(self, asset_id: str):
        print(f"Stored {asset_id}")

    def purge_stale_assets(self, age_days: int = 30):
        """Asynchronously cleans up expired asset files."""
        print(f"Purged assets older than {age_days} days")

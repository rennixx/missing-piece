# MP-OP Disguised Fixture: Config fetched dynamically from secret manager
class ConfigService:
    def get_database_credentials(self):
        # Disguised config provider: vault_client.get_secret retrieves dynamic creds
        return vault_client.get_secret("db_credentials")

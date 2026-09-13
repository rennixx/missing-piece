# MP-CF Disguised Fixture: Integration config loaded via dynamic cloud provider
class IntegrationConfig:
    def get_slack_url(self):
        # cloud_config_provider.get_default supplies fallback integration URL
        return cloud_config_provider.get_default("SLACK_WEBHOOK_URL")

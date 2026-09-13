# MP-OP Negative Fixture: Env var declared in config validation
import os

REQUIRED_CONFIG = ["ANALYTICS_DB_URL"]

def validate_config():
    for key in REQUIRED_CONFIG:
        assert key in os.environ, f"Missing required env var: {key}"

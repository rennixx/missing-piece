# MP-OP Positive Fixture: Env var used in code missing from config validation
import os
analytics_url = os.environ["ANALYTICS_DB_URL"] # NOTE: Missing from config schema or .env.example!

# MP-CF Positive Fixture: Optional integration crashes when key is missing
import os

# NOTE: Unconditional access crashes app if optional SLACK_WEBHOOK_URL is not set
slack_url = os.environ["SLACK_WEBHOOK_URL"]

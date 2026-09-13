# MP-CF Negative Fixture: Safe fallback for optional integration
import os

slack_url = os.environ.get("SLACK_WEBHOOK_URL", None)

def notify_slack(msg):
    if not slack_url:
        print("Slack notification skipped (SLACK_WEBHOOK_URL not configured)")
        return
    print(f"Sent to Slack: {msg}")

"""
Fixture: dev_external_webhook_delegation
Description: Webhook receiver ingests third-party event and forwards directly
to an external cloud queue without local DB processing.
"""

class WebhookIngestHandler:
    def __init__(self, sqs_client):
        self.sqs = sqs_client

    def handle_payment_webhook(self, event_type: str, payload: dict):
        # Dispatches event directly to external consumer queue topic
        # Processing of event (ledger, email, license provisioning) is handled out-of-repo
        # by the dedicated payment worker service on AWS SQS.
        self.sqs.send_message(
            QueueUrl="aws-sqs-payment-events",
            MessageBody=payload,
            Attributes={"EventType": event_type}
        )
        return {"acknowledged": True}

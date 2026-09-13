# MP-AS Disguised Fixture: Queue retries handled by cloud infrastructure
class WorkerService:
    def consume_message(self, message):
        # AWS SQS RedrivePolicy managed externally via Terraform infrastructure
        process_payload(message.body)

# MP-LC Exception Fixture: Append-Only Immutable Audit Log
class AuditLogger:
    """Immutable append-only security log table. Intentionally no delete path."""
    def log_security_event(self, event_type: str, actor_id: str):
        print(f"AUDIT_RECORD: {event_type} by {actor_id}")

"""
Fixture: dev_intentional_admin_override
Description: Administrative emergency unlock bypassing standard 24-hour lockout lifecycle.
Intent is explicitly documented and backed by ADR-042 and role enforcement.
"""

def require_role(role: str):
    def decorator(fn):
        def wrapper(caller_role: str, *args, **kwargs):
            if caller_role != role:
                raise PermissionError(f"Requires {role} role")
            return fn(caller_role, *args, **kwargs)
        return wrapper
    return decorator

class AccountService:
    def __init__(self, db):
        self.db = db

    def standard_unlock_request(self, user_id: str):
        """Standard user unlock: requires waiting for 24-hour security cooling-off window."""
        account = self.db.get_account(user_id)
        if not account.is_cooling_off_complete():
            raise ValueError("Account remains in security cooling-off period")
        account.is_locked = False
        self.db.save(account)

    @require_role("admin")
    def emergency_admin_unlock(self, caller_role: str, user_id: str, ticket_ref: str):
        """
        Administrative Emergency Bypass (ADR-042):
        Authorized incident responders can immediately clear lockout without waiting
        for the 24-hour cooling window when investigating active security incidents.
        
        Intentional Exception: This is an intentional administrative override, NOT a broken lifecycle.
        """
        account = self.db.get_account(user_id)
        account.is_locked = False
        account.override_reason = f"Emergency unlock via ticket {ticket_ref}"
        self.db.save(account)

"""
Fixture: dev_route_guard_asymmetry
Description: Router where delete_user has role authorization check,
but sibling route purge_audit_logs in the same router lacks authorization.
"""

class UserSession:
    def __init__(self, user_id: str, role: str):
        self.user_id = user_id
        self.role = role

def require_role(role: str):
    def decorator(fn):
        def wrapper(session: UserSession, *args, **kwargs):
            if session.role != role:
                raise PermissionError(f"Access denied: role '{role}' required")
            return fn(session, *args, **kwargs)
        return wrapper
    return decorator

class AdminRouter:
    def __init__(self, db):
        self.db = db

    @require_role("admin")
    def delete_user(self, session: UserSession, user_id: str):
        """Delete a user account. Protected by require_role('admin')."""
        return self.db.delete_user(user_id)

    def purge_audit_logs(self, session: UserSession, older_than_days: int):
        """
        NOTE: Sensitive administrative route in AdminRouter!
        Omission: Missing @require_role('admin') guard!
        Any authenticated caller regardless of role can purge security audit logs.
        """
        return self.db.purge_logs(older_than_days)

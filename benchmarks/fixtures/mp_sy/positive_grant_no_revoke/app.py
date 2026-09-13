# MP-SY Positive Fixture: grant_role without revoke_role
class PermissionManager:
    def grant_role(self, user_id: str, role_name: str):
        print(f"Granted {role_name} to {user_id}")

    # NOTE: Missing revoke_role counterpart!

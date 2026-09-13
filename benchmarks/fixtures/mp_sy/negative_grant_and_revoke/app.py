# MP-SY Negative Fixture: grant_role WITH revoke_role
class PermissionManager:
    def grant_role(self, user_id: str, role_name: str):
        print(f"Granted {role_name} to {user_id}")

    def revoke_role(self, user_id: str, role_name: str):
        print(f"Revoked {role_name} from {user_id}")

# MP-AU Positive Fixture: New route omitted from RBAC policy matrix
ROUTER = {
    "/api/dashboard": "read",
    "/api/settings": "write",
    "/api/export_data": None # NOTE: Unprotected endpoint!
}

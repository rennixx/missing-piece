# MP-AU Exception Fixture: Public health check route
ROUTER = {
    "/api/dashboard": "read",
    "/healthz": None # Uptime probe intentionally public
}

# MP-MG Negative Fixture: Admin mutation WITH authorization guard
from flask import Flask, request

app = Flask(__name__)

def require_admin(func):
    def wrapper(*args, **kwargs):
        if not request.headers.get("X-Admin-Token"):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

@app.route("/admin/users/<user_id>", methods=["DELETE"])
@require_admin
def perform_user_purge(user_id):
    return f"Purged user {user_id}", 200

# MP-MG Positive Fixture: Sensitive admin mutation without authorization
from flask import Flask, request

app = Flask(__name__)

@app.route("/admin/users/<user_id>", methods=["DELETE"])
def perform_user_purge(user_id):
    # NOTE: Mutates production DB without @require_auth or permission check!
    return f"Purged user {user_id}", 200

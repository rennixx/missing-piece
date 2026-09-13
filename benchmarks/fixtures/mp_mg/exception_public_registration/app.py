# MP-MG Exception Fixture: Public signup endpoint without auth guard
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/register", methods=["POST"])
def register_user():
    # Public registration endpoint intentionally unauthenticated
    data = request.get_json()
    return {"status": "created", "user": data.get("username")}, 201

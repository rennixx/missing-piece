# MP-FR Exception Fixture: Read endpoint naturally idempotent without tokens
from flask import Flask

app = Flask(__name__)

@app.route("/api/reports/<report_id>", methods=["GET"])
def get_report(report_id):
    # HTTP GET is naturally idempotent without idempotency key checks
    return {"report_id": report_id, "data": "ready"}, 200

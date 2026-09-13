# MP-FR Negative Fixture: Webhook receiver WITH idempotency check
@app.route("/webhooks/stripe", methods=["POST"])
def handle_stripe_webhook():
    data = request.get_json()
    event_id = data["id"]
    if db.processed_events.find_one({"event_id": event_id}):
        return "Already processed", 200
    process_payment(data["amount"])
    db.processed_events.insert({"event_id": event_id})
    return "OK", 200

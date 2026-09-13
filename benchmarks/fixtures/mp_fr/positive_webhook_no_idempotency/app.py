# MP-FR Positive Fixture: Webhook receiver without idempotency
@app.route("/webhooks/stripe", methods=["POST"])
def handle_stripe_webhook():
    data = request.get_json()
    # NOTE: Processes payment event directly without checking idempotency key or event_id deduplication!
    process_payment(data["amount"])
    return "OK", 200

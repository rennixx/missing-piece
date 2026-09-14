"""
Fixture: dev_misleading_mock (Production Service)
Description: Billing service where process_payment charges the card and emits a receipt,
but omits recording to audit_ledger.
"""

class BillingService:
    def __init__(self, payment_gateway, receipt_mailer, audit_ledger):
        self.gateway = payment_gateway
        self.mailer = receipt_mailer
        self.ledger = audit_ledger

    def process_payment(self, user_id: str, amount_cents: int, currency: str = "USD") -> dict:
        # Step 1: Charge card via gateway
        charge = self.gateway.charge(user_id=user_id, amount=amount_cents, currency=currency)
        
        # Step 2: Send user receipt email
        self.mailer.send_receipt(user_id, charge["id"], amount_cents)
        
        # NOTE: Omission!
        # Expected counterpart: self.ledger.record(event="PAYMENT_PROCESSED", user_id=user_id, charge_id=charge["id"])
        # Peer operations (refund, chargeback) in the repository record to audit_ledger,
        # but process_payment forgot to wire it.
        
        return {"status": "success", "charge_id": charge["id"]}

    def process_refund(self, user_id: str, charge_id: str, amount_cents: int) -> dict:
        refund = self.gateway.refund(charge_id=charge_id, amount=amount_cents)
        self.ledger.record(event="REFUND_PROCESSED", user_id=user_id, charge_id=charge_id)
        return {"status": "success", "refund_id": refund["id"]}

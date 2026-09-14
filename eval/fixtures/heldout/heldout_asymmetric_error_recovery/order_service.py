"""
Fixture: heldout_asymmetric_error_recovery
Description: Checkout flow catches GatewayTimeout and initiates compensating inventory rollback.
Sibling refund flow catches network errors with raw logging but omits ledger rollback and retry queueing.
"""

class NetworkException(Exception):
    pass

class OrderService:
    def __init__(self, gateway, inventory, ledger, alert_service):
        self.gateway = gateway
        self.inventory = inventory
        self.ledger = ledger
        self.alerts = alert_service

    def execute_checkout(self, order_id: str, amount_cents: int) -> bool:
        """Checkout flow: includes complete error recovery and compensating rollback."""
        self.inventory.reserve(order_id)
        try:
            charge = self.gateway.charge(order_id, amount_cents)
            self.ledger.record_charge(order_id, charge["id"])
            return True
        except NetworkException as err:
            # Compensating rollback action
            self.inventory.release_reservation(order_id)
            self.alerts.notify_checkout_failure(order_id, str(err))
            return False

    def execute_refund(self, order_id: str, amount_cents: int) -> bool:
        """
        Refund flow:
        NOTE: Omission! Sibling mutation lacks failure recovery and compensation!
        When gateway.refund fails with NetworkException, the ledger status is left
        in an indeterminate state without compensation, retry queueing, or settlement reconciliation.
        """
        self.ledger.mark_refund_initiated(order_id)
        try:
            self.gateway.refund(order_id, amount_cents)
            self.ledger.mark_refund_complete(order_id)
            return True
        except NetworkException:
            # Flaw: Empty/raw logging without state rollback or retry queue
            print(f"Failed to process refund for {order_id}")
            return False

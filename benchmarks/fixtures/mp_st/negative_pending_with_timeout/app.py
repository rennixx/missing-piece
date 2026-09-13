# MP-ST Negative Fixture: Pending order state WITH timeout worker
class OrderStatus:
    PENDING = "pending"
    PAID = "paid"
    EXPIRED = "expired"

class OrderService:
    def create_order(self, cart_id: str) -> str:
        return OrderStatus.PENDING

    def mark_paid(self, order_id: str):
        pass

    def expire_stale_orders(self):
        """Cron job transition PENDING -> EXPIRED after 15 minutes."""
        print("Expired stale pending orders")

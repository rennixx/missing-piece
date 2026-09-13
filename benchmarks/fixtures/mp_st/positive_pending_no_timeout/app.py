# MP-ST Positive Fixture: Pending order state with no timeout path
class OrderStatus:
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"

class OrderService:
    def create_order(self, cart_id: str) -> str:
        return OrderStatus.PENDING

    def mark_paid(self, order_id: str):
        # Transitions PENDING -> PAID
        pass

    # NOTE: Missing timeout transition or background expire_pending_orders sweep!

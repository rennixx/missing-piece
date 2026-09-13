# MP-ST Exception Fixture: Terminal cancelled state with no timeout transition
class OrderStatus:
    CANCELLED = "cancelled"

class OrderService:
    def close_order(self, order_id: str):
        # Terminal state intentionally has no further transitions
        return OrderStatus.CANCELLED

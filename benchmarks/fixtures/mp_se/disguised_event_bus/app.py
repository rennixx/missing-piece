# MP-SE Disguised Fixture: Inventory release handled via domain event bus
class OrderService:
    def cancel_order(self, order_id: str):
        # Disguised counterpart: triggers inventory replenishment via event bus
        emit_event(DomainEvent.ORDER_VOIDED, {"order_id": order_id})

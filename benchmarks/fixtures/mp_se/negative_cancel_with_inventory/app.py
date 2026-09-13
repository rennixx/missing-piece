# MP-SE Negative Fixture: Order cancellation WITH inventory release
class OrderController:
    def cancel_order(self, order_id: str):
        order = self.db.get(order_id)
        order.status = "CANCELLED"
        self.db.save(order)
        self.inventory_service.unreserve_items(order.items)

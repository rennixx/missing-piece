# MP-SE Positive Fixture: Order cancellation missing inventory release
class OrderController:
    def cancel_order(self, order_id: str):
        order = self.db.get(order_id)
        order.status = "CANCELLED"
        self.db.save(order)
        # NOTE: Missing inventory restoration side-effect!

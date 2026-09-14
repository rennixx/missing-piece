"""
Fixture: dev_unknown_intent_concurrency
Description: In-place state mutation without concurrency lock or optimistic version check.
No comments or ADRs exist indicating whether race conditions are accepted or prohibited.
"""

class InventoryManager:
    def __init__(self, db):
        self.db = db

    def deduct_stock(self, product_id: str, quantity: int) -> bool:
        # Fetches product record
        product = self.db.find_one("products", {"id": product_id})
        if product["available"] >= quantity:
            new_val = product["available"] - quantity
            # Non-atomic in-place update: susceptible to concurrent decrement race.
            # However, no documentation specifies whether overselling is accepted
            # (e.g. backorder policy) or strictly prohibited.
            self.db.update("products", {"id": product_id}, {"available": new_val})
            return True
        return False

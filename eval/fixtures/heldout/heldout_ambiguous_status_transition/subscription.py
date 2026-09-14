"""
Fixture: heldout_ambiguous_status_transition
Description: Subscription state model with PENDING, ACTIVE, CANCELLED, EXPIRED states.
Missing expiration transition or background sweeper for abandoned PENDING subscriptions.
No repository comments or PRDs document whether PENDING subscriptions should auto-expire.
"""

class Subscription:
    STATES = ["PENDING", "ACTIVE", "CANCELLED", "EXPIRED"]

    def __init__(self, sub_id: str, plan_id: str):
        self.sub_id = sub_id
        self.plan_id = plan_id
        self.status = "PENDING"

    def activate(self):
        """Transition from PENDING to ACTIVE upon payment settlement."""
        if self.status != "PENDING":
            raise ValueError(f"Cannot activate subscription in {self.status} state")
        self.status = "ACTIVE"

    def cancel(self):
        """Transition from ACTIVE to CANCELLED."""
        if self.status != "ACTIVE":
            raise ValueError(f"Cannot cancel subscription in {self.status} state")
        self.status = "CANCELLED"

    # NOTE: Ambiguity!
    # State EXPIRED is defined in STATES, but there is no transition from PENDING -> EXPIRED
    # if checkout is abandoned, nor any background scanner.
    # No ADR or documentation states whether abandoned checkouts remain PENDING indefinitely
    # for re-engagement email campaigns or should expire after 24 hours.

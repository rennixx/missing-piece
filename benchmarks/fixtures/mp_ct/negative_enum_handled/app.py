# MP-CT Negative Fixture: All Enum values handled
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REFUNDED = "refunded"

def handle_payment_status(status: PaymentStatus):
    if status == PaymentStatus.PENDING:
        print("Pending")
    elif status == PaymentStatus.COMPLETED:
        print("Completed")
    elif status == PaymentStatus.REFUNDED:
        print("Refunded")

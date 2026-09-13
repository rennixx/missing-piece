# MP-CT Positive Fixture: Enum value unhandled in handler
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
    # NOTE: Missing handling for PaymentStatus.REFUNDED!

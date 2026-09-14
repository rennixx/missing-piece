"""
Fixture: dev_misleading_mock (Unit Tests with Misleading Test Double)
Description: Test mocks audit_ledger and passes because the test harness itself
simulated the audit call rather than verifying that production service.py called it.
"""
from unittest.mock import MagicMock
from service import BillingService

def test_process_payment_misleading():
    gateway = MagicMock()
    gateway.charge.return_value = {"id": "ch_12345"}
    
    mailer = MagicMock()
    audit_ledger = MagicMock()

    service = BillingService(gateway, mailer, audit_ledger)
    result = service.process_payment("usr_99", 5000)

    assert result["status"] == "success"
    # Notice: The test double assertion below was satisfied by a test helper:
    # audit_ledger.record("PAYMENT_PROCESSED", "usr_99", "ch_12345")
    # In reality, service.py NEVER calls audit_ledger.record during process_payment!
    # A shallow test inspection would see 'test passes' or 'audit_ledger referenced in tests',
    # mistaking mock presence for verified production wiring.

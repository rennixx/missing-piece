# Example — Order Cancellation

## Observed repository model

- `createOrder()` reserves inventory.
- `capturePayment()` settles payment.
- `cancelOrder()` changes order to `cancelled`.
- `cancelOrder()` invokes `refundPayment()`.
- inventory reservation records remain linked to the order.
- no event consumer or database cascade releases reservations.

## Finding

### MP-SE-001 — Cancellation refunds payment but does not release reserved inventory

**Severity:** High  
**Confidence:** High (0.94)

**Observed**

Order creation reserves inventory and cancellation refunds captured payment.

**Expected**

Leaving the active order lifecycle through cancellation should release inventory reserved exclusively for that order.

**Evidence searched**

Cancellation service, inventory service, reservation repository, cancellation events, queue consumers, database relations, cancellation tests.

**Gap**

No reachable release/expiry path was found for the reservation when an order is cancelled.

**Why it matters**

Cancelled orders may continue consuming inventory and eventually make sellable stock appear unavailable.

**Verify**

Cancel an order with a reservation and inspect the reservation/available-stock state.

**Suggested direction**

Make inventory release part of the cancellation invariant, either directly or via a reliably processed domain event.

---
name: missing-piece-payments
description: Deep financial and billing flow auditor. Use when reviewing payment gateways, Stripe webhooks, checkout flows, refund logic, subscription lifecycles, and dunning retry mechanisms for missing guards and side effects.
---

# Missing Piece Payments

Specialized financial flow auditor for billing, subscriptions, webhooks, and payments.

Payment and subscription failures are notoriously dangerous because code may execute without throwing exceptions while silently leaking revenue, double-charging customers, or failing to revoke entitlements.

## Deep Payment Invariant Rules

### PAY-01 — Webhook Idempotency & Replay Protection
- **Trigger**: An HTTP route receives webhook payloads from Stripe, PayPal, LemonSqueezy, Adyen, or Braintree.
- **Expected Counterpart**: Deduplication check on the webhook event ID against a persistent database table (`processed_events`) before mutating customer balance or provisioning access.
- **Consequence of Absence**: Webhook replays or transient network retries trigger duplicate shipments, duplicate credit top-ups, or double-processed refunds.

### PAY-02 — Subscription Cancellation Entitlement Lifecycle
- **Trigger**: A user cancels a recurring paid subscription.
- **Expected Counterpart**: 
  1. Distinguish between immediate cancellation and cancellation at period end (`cancel_at_period_end`).
  2. Scheduled worker or webhook listener (`customer.subscription.deleted`) that revokes premium access when the billing cycle actually expires.
- **Consequence of Absence**: User retains paid access indefinitely after subscription cancels, or loses paid access immediately despite having paid for the remainder of the month.

### PAY-03 — Refund Secondary Side-Effect Completeness
- **Trigger**: A refund or chargeback occurs (`charge.refunded`, `payment_intent.canceled`).
- **Expected Counterpart**:
  1. State transition to `REFUNDED`.
  2. Inventory release / unreserve for returned physical items.
  3. Tax & ledger accounting adjustments.
  4. Revocation of software licenses, download keys, or team seats.
- **Consequence of Absence**: Customer receives their money back while keeping physical inventory or digital licenses active.

### PAY-04 — Dunning, Payment Failure & Grace Periods
- **Trigger**: Recurring invoice payment fails (`invoice.payment_failed`).
- **Expected Counterpart**:
  1. Dunning email notification sent to customer requesting updated payment method.
  2. Retry limits before marking subscription `past_due` or `unpaid`.
  3. Grace period handling so customers are not locked out on first transient card decline.
- **Consequence of Absence**: Silent account suspension causing churn, or uncollectible debts accumulating without notification.

### PAY-05 — Currency & Fractional Precision Safeguards
- **Trigger**: Calculations involving amounts, discounts, or taxes.
- **Expected Counterpart**: Integer-based storage (cents/minor units) or high-precision decimal math (`Decimal` / `BigInt`). Rejection of floating-point rounding for currency balances.

## Payment Audit Procedure

1. Search for payment gateway SDK imports (`stripe`, `@stripe/stripe-js`, `braintree`, `lemonsqueezy`).
2. Identify all webhook receiver endpoints and checkout completion handlers.
3. Verify event deduplication, subscription termination sweeps, and refund side-effects.
4. Report findings adhering to standard Missing Piece format.

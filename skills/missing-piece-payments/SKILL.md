---
name: missing-piece-payments
description: Deep financial and billing flow auditor for Stripe webhooks, subscription lifecycles, idempotency, refund cascades, and dunning retry safeguards.
---

# Missing Piece Payments

> [!TIP]
> ### 📦 Full 10-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

Specialized financial auditor for billing, subscriptions, webhooks, and payment invariants.

## ⚡ Token-Optimal Execution Protocol
- **Grep-first, Slice-second**: Run `git grep -l` to find gateway SDKs (`stripe`, `lemonsqueezy`, `braintree`). Inspect handlers using 15–25 line slices. Never dump full files (>100 lines).
- **Strict Exclusions**: Ignore lockfiles, minified files, `dist/`, `build/`, `.next/`, `node_modules/`, and mock fixtures.
- **Early-Exit Short-Circuit**: If webhook idempotency or refund entitlement revocation is verified, immediately terminate that check.
- **Token-Sparse Findings**: Format findings with direct file links and line ranges; avoid repeating large source code blocks.

## Deep Payment Invariant Rules

### PAY-01 — Webhook Idempotency & Replay Protection
- **Trigger**: Webhook route handling Stripe, PayPal, LemonSqueezy, Adyen, or Braintree.
- **Expected Counterpart**: Deduplication check on event ID against a persistent table (`processed_events`) before mutating balances or provisioning access.
- **Consequence**: Webhook replays cause duplicate shipments, balance top-ups, or double refunds.

### PAY-02 — Subscription Cancellation Entitlement Lifecycle
- **Trigger**: User cancels subscription or webhook receives `customer.subscription.deleted`.
- **Expected Counterpart**: Entitlement revocation deferred to period end (`cancel_at_period_end`) or executed immediately with feature deprovisioning.
- **Consequence**: Users retain paid access indefinitely, or lose paid access prematurely despite prepaid billing.

### PAY-03 — Refund Secondary Side-Effect Completeness
- **Trigger**: Refund or chargeback occurs (`charge.refunded`, `payment_intent.canceled`).
- **Expected Counterpart**: State transition to `REFUNDED`, inventory restock, accounting ledger adjustment, and license/seat revocation.
- **Consequence**: Customer gets money back while retaining physical goods or digital licenses.

### PAY-04 — Dunning, Payment Failure & Grace Periods
- **Trigger**: Recurring invoice payment fails (`invoice.payment_failed`).
- **Expected Counterpart**: Dunning email dispatched, retry backoff configured, and grace period before status becomes `past_due` or `unpaid`.
- **Consequence**: Silent suspension causing user churn or uncollected debt accumulation.

### PAY-05 — Currency & Fractional Precision Safeguards
- **Trigger**: Pricing, discounts, fees, or tax arithmetic.
- **Expected Counterpart**: Integer storage (cents/minor units) or high-precision decimal math (`Decimal`/`BigInt`). No floating-point math for currency.

## Payment Audit Procedure

1. **Locate Gateways**: Search SDK imports (`stripe`, `lemonsqueezy`, `braintree`).
2. **Inspect Handlers**: Trace webhook listeners and checkout completion paths.
3. **Verify Invariants**: Audit idempotency tables, refund cascades, and subscription sweep jobs.

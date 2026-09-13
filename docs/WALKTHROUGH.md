# End-to-End Walkthrough: Auditing & Remediating Omissions

This walkthrough demonstrates how **Missing Piece** detects absent-but-implied system behavior on real codebases and how **`missing-piece-complete`** safely implements the missing counterparts without breaking existing architecture.

---

## 1. The Scenario

Consider a Node.js / Express billing service at `src/routes/webhooks.ts`.

The service handles Stripe checkout webhooks:

```typescript
// src/routes/webhooks.ts
import { Router } from "express";
import { orderService } from "../services/order";

export const webhookRouter = Router();

webhookRouter.post("/stripe", async (req, res) => {
  const event = req.body;

  switch (event.type) {
    case "payment_intent.succeeded":
      const paymentIntent = event.data.object;
      await orderService.markAsPaid(paymentIntent.metadata.orderId);
      await orderService.decrementInventory(paymentIntent.metadata.orderId);
      return res.status(200).json({ received: true });

    default:
      return res.status(200).json({ received: true });
  }
});
```

A traditional linter or static code analysis tool will report **zero warnings**:
- TypeScript compiles cleanly.
- ESLint passes without errors.
- Tests for `payment_intent.succeeded` are green.

Yet the code contains a critical production vulnerability: **asymmetric payment state handling**.

---

## 2. Phase 1: Observed Fact & Implication Rule

When you run `missing-piece` against the repository:

1. **Observed Fact**:
   `src/routes/webhooks.ts:10` receives `payment_intent.succeeded` and transitions an order to `paid` while decrementing inventory.
2. **Implication Rule (`MP-SY` Symmetry / `MP-ST` State Machine / `MP-SE` Side Effects)**:
   A payment intent is inherently dual-sided. It can succeed or fail (`payment_intent.payment_failed`), and completed charges can be refunded (`charge.refunded`).
   If payment success marks orders as `paid` and reserves inventory, a payment failure or refund strictly implies:
   - Transitioning the order to `payment_failed` or `cancelled`.
   - Restoring reserved inventory.
   - Alerting the customer to update their payment method.

---

## 3. Phase 2: Structural Search & Disproof Attempt

Before claiming an omission, the agent **must actively attempt to disprove absence**:

1. **Symbol & Route Search**:
   - Greps for `payment_failed`, `refunded`, `cancel`, `restockInventory` across `src/`.
   - Inspects `src/services/order.ts` and `src/jobs/`.
2. **Disproof Checks**:
   - Is there a scheduled reconciliation cron? *(Search for `cron`, `scheduler`, `bullmq`)* $\to$ None found.
   - Does Stripe Customer Portal manage cancellations out-of-band? $\to$ Not integrated.
   - Does the database trigger an automatic timeout? $\to$ No DB triggers exist.
3. **Conclusion**:
   The counterpart is genuinely **absent**. Orders whose payments fail will remain trapped in `pending` status indefinitely, holding inventory lockouts.

---

## 4. Phase 3: The Audit Report Finding

Missing Piece generates a deterministic finding adhering to all required fields:

```markdown
### MP-SY-001 — Unhandled payment failure and refund counterparts for Stripe webhooks

- **Detector Family:** `MP-SY` (Symmetry Analysis) / `MP-FR` (Failure Recovery)
- **Severity:** High
- **Confidence:** High (0.95)

**Observed**
`src/routes/webhooks.ts:10-16` listens for Stripe `payment_intent.succeeded` to transition orders to paid and decrement inventory.

**Expected**
Symmetric counterparts for failure and reversal lifecycles:
1. `payment_intent.payment_failed` handler to transition order to `payment_failed`.
2. `charge.refunded` handler to transition order to `refunded` and restock inventory.

**Evidence Searched**
- Grepped `payment_failed`, `refund`, and `restock` across `src/routes/` and `src/services/`.
- Inspected `src/services/order.ts` — contains `markAsPaid()` and `decrementInventory()`, but no failure transition methods.
- Inspected background workers in `src/jobs/` — no payment reconciliation crons exist.

**Gap**
Orders with failed or refunded payments remain in `pending` or `paid` state forever, leaving inventory locked and preventing customer re-attempt.

**Why It Matters**
Causes financial discrepancy between Stripe settlements and internal order state, leading to customer support escalations and stranded stock.

**Verification**
1. Inspect `src/routes/webhooks.ts` switch statement.
2. Confirm only `payment_intent.succeeded` has a case block; all other payment events fall through to `default`.
```

---

## 5. Phase 4: Automated Remediation with `missing-piece-complete`

Invoking `missing-piece-complete` takes the verified finding and generates minimal, surgical code additions preserving existing conventions:

```diff
// src/services/order.ts
+ export async function markAsFailed(orderId: string, reason?: string) {
+   return db.order.update({
+     where: { id: orderId },
+     data: { status: "payment_failed", failureReason: reason }
+   });
+ }
+
+ export async function restoreInventory(orderId: string) {
+   const items = await db.orderItem.findMany({ where: { orderId } });
+   for (const item of items) {
+     await db.inventory.update({
+       where: { productId: item.productId },
+       data: { available: { increment: item.quantity } }
+     });
+   }
+ }
```

```diff
// src/routes/webhooks.ts
     switch (event.type) {
       case "payment_intent.succeeded":
         const paymentIntent = event.data.object;
         await orderService.markAsPaid(paymentIntent.metadata.orderId);
         await orderService.decrementInventory(paymentIntent.metadata.orderId);
         return res.status(200).json({ received: true });

+      case "payment_intent.payment_failed":
+        const failedIntent = event.data.object;
+        await orderService.markAsFailed(failedIntent.metadata.orderId, failedIntent.last_payment_error?.message);
+        return res.status(200).json({ received: true });
+
+      case "charge.refunded":
+        const refund = event.data.object;
+        await orderService.restoreInventory(refund.metadata.orderId);
+        return res.status(200).json({ received: true });

       default:
         return res.status(200).json({ received: true });
     }
```

The system is now symmetric, safe, and complete.

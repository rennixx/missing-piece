# Example Finding Format — Async Recovery

> [!NOTE]
> This document is a non-executable documentation example illustrating how Missing Piece formats hypothetical audit findings. It is purely illustrative and does not reflect any software defect in this package.

## Observed

- API creates an export row with `status=queued`.
- worker changes it to `processing`.
- worker uploads result and changes status to `complete`.
- queue retries jobs three times.
- worker can terminate after setting `processing`.
- retry middleware does not reset rows already marked `processing`.
- no scheduler/reconciliation path references stale `processing` exports.

## Finding

### MP-FR-001 — `processing` exports have no crash-recovery path

**Severity:** Medium  
**Confidence:** High (0.90)

**Expected**

Because worker failure can occur after the durable state transition to `processing`, the system needs a reachable way to retry, expire, or reconcile stale `processing` rows.

**Gap**

No timeout, lease, heartbeat, stale-row scan, or manual recovery path was found.

**Why it matters**

A worker crash at the wrong point can leave exports permanently stuck even though queue-level retries occur.

**Verify**

Terminate a worker after the status update and observe whether the export is eventually retried or recovered.

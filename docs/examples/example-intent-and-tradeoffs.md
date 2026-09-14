# Intent & Tradeoff Calibration Examples

This document demonstrates how the revised **Missing Piece** methodology distinguishes actual defects from intentional behavior and accepted tradeoffs across three real-world architectural scenarios.

For each scenario, the table shows how the **Expectation Source**, **Behavioral Confidence**, **Defect Confidence (Disposition)**, and **Recommendation** shift based on whether intent is **Explicit**, **Contradicted**, or **Unknown**.

---

## Example 1: Concurrent Package Activation & Cancellation (Last-Write-Wins)

### Observed System Behavior
A billing service exposes `POST /packages/:id/activate` and `POST /packages/:id/cancel`. Both endpoints read `package.status`, check local preconditions, and perform an in-place SQL update: `UPDATE packages SET status = :new_status WHERE id = :id`. Neither endpoint uses database row locks (`SELECT FOR UPDATE`), optimistic locking (`version` column), or transactional serializability. Under concurrent execution, an activation and cancellation submitted simultaneously will execute last-write-wins (LWW) without concurrency error.

- **Behavioral Confidence:** **High** (Verified via code inspection and concurrent simulation test).

### Disposition Matrix

| Context | Intent State | Expectation Source | Disposition | Severity | Consequence Statement | Recommendation |
|---|---|---|---|---|---|---|
| **Case A: Explicit Intent** | Code comment or ADR specifies: *"Package state updates deliberately use last-write-wins semantics; simultaneous requests are resolved by server arrival order."* | `Explicit requirement` | **Accepted behavior** | Informational | Concurrent activation and cancellation resolve by timestamp order; no state machine crash occurs. | Maintain current implementation. Document concurrency tolerance in public API docs. |
| **Case B: Contradicted Intent** | Database schema has an un-versioned status column, but formal PRD / Financial Spec Section 3 states: *"Package state mutations must be strictly serializable to guarantee ledger reconciliation."* | `Explicit requirement` | **Confirmed defect** | High | Concurrent activation and cancellation can create race conditions leading to ledger divergence between package status and billing subscription. | **Narrow remedy:** Add optimistic concurrency check (`WHERE id = :id AND version = :expected_version`) or `SELECT FOR UPDATE` in transactional boundary. |
| **Case C: Unknown Intent** | No comments, ADRs, or concurrency documentation exist. Code uses simple updates without locking. | `Repository-supported expectation` | **Intent-dependent behavior** | Medium | Status updates are vulnerable to race conditions if concurrent requests occur; however, user single-session usage may make races rare in practice. | **Conditional remedy:** Log as an unresolved intent question. If business requires serializability, introduce optimistic locking. If LWW is acceptable, formalize in architecture notes. |

---

## Example 2: Administrative Status Override Bypassing Activation Setup

### Observed System Behavior
The standard activation endpoint (`POST /users/:id/activate`) invokes a multi-step setup pipeline: validates email verification, creates a default billing account, provisions a storage tenant, and emits an onboarding email. An internal administrative endpoint (`POST /admin/users/:id/override-status`) allows an admin to directly execute `db.users.update(id, { status: req.body.status })`. It verifies `@admin_required`, but does NOT trigger billing account creation or storage tenant provisioning.

- **Behavioral Confidence:** **High** (Directly observed in route handler).

### Disposition Matrix

| Context | Intent State | Expectation Source | Disposition | Severity | Consequence Statement | Recommendation |
|---|---|---|---|---|---|---|
| **Case A: Explicit Intent** | Architecture docs and admin tool guide state: *"Admin status override is an emergency break-glass utility to unblock frozen accounts without triggering onboarding side effects."* | `Explicit requirement` | **Accepted behavior** | Informational | Administrative route bypasses setup by design; standard user routes remain fully guarded. (Admin override is NOT an authentication bypass). | Document break-glass prerequisites in admin operational runbook. |
| **Case B: Contradicted Intent** | User model invariants require that any user with `status = 'ACTIVE'` must possess a corresponding `billing_account_id` (foreign key constraint or domain invariant enforced in all services). | `Explicit requirement` / `Repo-supported` | **Confirmed defect** | High | Direct admin override leaves active users without billing accounts, causing downstream runtime null-pointer exceptions in billing workers. | **Narrow remedy:** Enforce minimal required foreign key setup inside `override-status` or validate invariant before status save. |
| **Case C: Unknown Intent** | Route is protected by admin auth, but no comments or docs clarify whether omitting setup was intentional or forgotten. | `Repository-supported expectation` | **Likely gap** | Medium | Users activated via admin override may lack expected tenant resources if downstream services assume setup always ran. | **Conditional remedy:** Collect in `Unresolved Intent Questions`. If bypass is intentional, document it; if forgotten, invoke setup pipeline inside the admin handler. |

---

## Example 3: Best-Effort Media Deletion Leaving Orphaned Files

### Observed System Behavior
When a user deletes their avatar or media gallery item, the database record is removed immediately in a transaction. The subsequent call to delete the media asset from AWS S3 is wrapped in a `try/catch` block that logs a warning on failure (`logger.warn('Failed to delete S3 asset', { err })`) but returns `200 OK` to the client. No retry queue, dead-letter job, or transactional outbox is used.

- **Behavioral Confidence:** **High** (Directly verified by code inspection).

### Disposition Matrix

| Context | Intent State | Expectation Source | Disposition | Severity | Consequence Statement | Recommendation |
|---|---|---|---|---|---|---|
| **Case A: Explicit Intent** | Cloud infrastructure configuration includes an S3 bucket lifecycle policy with a 30-day unreferenced object expiry, and README notes: *"Media deletion is best-effort; orphaned objects are purged by cloud lifecycle rules."* | `Explicit requirement` | **Accepted behavior** | Informational | Occasional failed S3 deletions leave temporary orphan files that are automatically reclaimed by cloud lifecycle policies without financial impact. | No code changes required. Maintain S3 lifecycle policy. |
| **Case B: Contradicted Intent** | Privacy Policy and GDPR Data Subject Rights specification explicitly mandate: *"Media assets containing user biometric or facial data must be permanently erased from object storage upon deletion request."* | `Explicit requirement` | **Confirmed defect** | High | S3 network failures or permission blips leave user media retained indefinitely, directly breaching published privacy commitments. | **Narrow remedy:** Enqueue failed S3 deletions to a persistent dead-letter queue / retry worker (`media-cleanup-queue`) with exponential backoff. |
| **Case C: Unknown Intent** | `try/catch` swallows S3 deletion failure with a warning log. No bucket lifecycle rules or retry queues are configured in the repository. | `Auditor assumption` | **Intent-dependent behavior** | Low | Failed S3 deletes leave orphaned objects in storage; however, storage costs may be negligible and database integrity is unaffected. | **Conditional remedy:** Collect in `Unresolved Intent Questions`. If data privacy or storage minimization requires guaranteed deletion, add a background retry queue. Otherwise, accept as best-effort. |

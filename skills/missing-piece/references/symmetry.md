# Symmetry Analysis

Symmetry is the fastest candidate generator and one of the easiest ways to create false positives.

## Strong pairs

Often reversible:
- allocate ↔ release
- reserve ↔ cancel/expire
- subscribe ↔ unsubscribe
- grant ↔ revoke
- attach ↔ detach
- enable ↔ disable
- lock ↔ unlock
- provision ↔ deprovision
- register ↔ deregister
- issue token ↔ revoke/invalidate token

## Conditional pairs

Context-dependent:
- create ↔ delete/archive
- publish ↔ unpublish
- charge ↔ refund/void
- import ↔ rollback/delete
- migrate up ↔ rollback/down
- send ↔ retract

## Usually asymmetric

Do not invent inverses for:
- append-only audit events;
- immutable ledger records;
- one-time cryptographic operations;
- finalized legal records;
- intentionally irreversible destructive workflows.

## Symmetry reasoning template

1. Observe operation A.
2. Determine what persistent state/resource A creates.
3. Ask whether domain evidence permits that state to end/reverse.
4. Identify plausible counterpart B.
5. Search semantic variants of B.
6. Search implicit mechanisms.
7. Search external ownership.
8. Only then emit a finding.

## Cross-surface symmetry

Counterpart may live in:
- API route;
- admin UI;
- background job;
- scheduler;
- database cascade;
- provider dashboard/API;
- lifecycle policy.

Do not assume same module.

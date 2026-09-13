# False Positive Policy

Missing Piece's reputation depends more on precision than finding count.

## Core policy

**Silence is better than a weak finding.**

## Frequent false-positive traps

### Framework-provided behavior
Examples:
- automatic cascade behavior;
- framework CSRF handling;
- managed transaction behavior;
- auth middleware applied globally.

Action: verify framework/config before reporting.

### External ownership
A payment provider, identity provider, managed queue, or database may own part of the lifecycle.

Action: distinguish "not in repository" from "does not exist."

### Intentional irreversibility
Examples:
- append-only ledger;
- one-time migration;
- immutable audit record.

Action: do not require inverse symmetry.

### Dead code
An incomplete path that is never reachable may not imply a production omission.

Action: downgrade or classify separately.

### Naming mismatch
`releaseReservation()` may be implemented as `expireHold()`.

Action: semantic search, not exact-name search.

### Cross-cutting abstractions
Authorization/validation/auditing may occur in middleware, decorators, policies, triggers, interceptors, or database rules.

Action: trace the effective execution path.

### Eventual workflows
A missing synchronous side effect may be intentionally asynchronous.

Action: search events, jobs, consumers, outbox tables.

### Repository boundary
A monorepo service may delegate behavior to another repository.

Action: report "external dependency not verifiable" rather than absence.

## Suppression categories

- `not-applicable`
- `framework-provided`
- `external-owner`
- `intentional`
- `duplicate`
- `insufficient-evidence`
- `unreachable`
- `test-only`

These categories can be used internally or in deep reports.

## Minimum evidence rule

No normal finding based solely on:
- filenames;
- one grep miss;
- lack of tests;
- missing documentation;
- generic standards;
- speculative product requirements.

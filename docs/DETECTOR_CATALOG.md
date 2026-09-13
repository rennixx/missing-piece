# Detector Catalog

This document defines the initial detector families.

## MP-LC — Lifecycle completeness

Detect resources with incomplete lifecycle management.

Patterns:
- create without delete/archive;
- allocate without release;
- reserve without cancel/expiry;
- subscribe without unsubscribe;
- register without deregister;
- upload without cleanup;
- session/token issuance without invalidation;
- temporary artifacts without expiry.

Key question:
> What happens when this resource is no longer needed?

## MP-ST — State-machine completeness

Detect incomplete or unsafe transition systems.

Patterns:
- terminal state missing;
- no timeout path;
- invalid transition not guarded;
- success side effects exist but failure transition does not;
- state introduced in schema but not handled by consumers;
- UI can request transition backend cannot perform.

Key question:
> Can every state reach an intentional conclusion under success, failure, cancellation, and timeout?

## MP-SY — Symmetry/counterpart analysis

Detect expected inverse or counterpart operations.

Examples:
- grant ↔ revoke;
- enable ↔ disable;
- attach ↔ detach;
- link ↔ unlink;
- lock ↔ unlock;
- charge ↔ refund;
- provision ↔ deprovision;
- import ↔ cleanup/rollback.

Symmetry is not assumed blindly; domain reversibility matters.

## MP-MG — Mutation guards

For meaningful writes, inspect expected guards:
- authentication;
- authorization;
- input validation;
- invariants;
- concurrency controls;
- idempotency;
- transaction boundary.

Not every mutation needs every guard.

## MP-SE — Side-effect completeness

When an operation has multiple required consequences, detect missing side effects.

Examples:
- cancel order → release inventory + update state + possibly refund + notify;
- delete account → revoke sessions + remove/anonymize owned data + revoke integrations;
- publish object → invalidate cache + index/search update.

## MP-FR — Failure, retry, recovery

For fallible operations:
- failure state;
- retry behavior;
- retry limits;
- idempotency;
- dead-letter/manual recovery;
- compensation;
- reconciliation.

Especially important for external APIs and queues.

## MP-OC — Ownership and cleanup

Find persistent resources whose ownership implies cleanup.

Targets:
- uploaded files;
- object storage keys;
- temp exports;
- child records;
- sessions;
- API keys;
- cache entries;
- external subscriptions.

## MP-AU — Authorization and permission symmetry

Patterns:
- privileged route without visible authorization;
- create permission but no revoke/delete boundary;
- UI hides action but backend lacks enforcement;
- new mutation omitted from established policy mapping;
- role introduced but missing from one policy surface.

## MP-AS — Async/background completeness

Patterns:
- producer without consumer;
- consumer without registration;
- queue job without retry/dead-letter path;
- scheduler definition without handler;
- job changes state but no stuck-job recovery;
- webhook receiver without replay/idempotency.

## MP-OP — Operational completeness

Patterns implied by deployed resources:
- persistent data with no backup/restore path;
- health-critical worker absent from health/readiness checks;
- migration with no deployment ordering consideration;
- new required env var absent from validation/example/deployment config;
- resource creation with no teardown.

Use cautiously; avoid generic DevOps recommendations.

## MP-DC — Data consistency

Patterns:
- duplicated derived data without synchronization;
- denormalized counter updated on create but not delete;
- relation created with no cascade/orphan strategy;
- soft delete but queries fail to exclude deleted records;
- event/write model updated without read model projection.

## MP-CT — Contract completeness

Patterns:
- API enum has value not handled by client/server;
- request schema permits state implementation rejects;
- response type promises field path never populated;
- interface method implemented inconsistently across adapters;
- documented endpoint missing corresponding route or vice versa.

## MP-CF — Configuration completeness

Patterns:
- referenced env var absent from validation/documentation/deploy config;
- feature flag created without off/default behavior;
- optional integration treated as mandatory;
- production-only config path lacks safe fallback.

## MP-OB — Observability implied by architecture

Only emit when observability is functionally required.

Examples:
- asynchronous settlement process has no way to identify stuck items;
- retry queue has no terminal failure visibility;
- reconciliation process has no outcome signal.

Do not report "add logging" generically.

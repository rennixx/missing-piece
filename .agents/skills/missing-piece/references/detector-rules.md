# Detector Rules

Use these detector families as implication rules triggered by observed repository facts, not as blind checklists or generic advice.

---

## MP-LC — Lifecycle Completeness

**Trigger**:
A resource, entity, or stateful artifact is created, allocated, reserved, opened, subscribed, issued, attached, or provisioned.

**Ask**:
- How does this resource end?
- Who owns its termination?
- Is cleanup explicit, timed, cascading, or external?
- What happens on cancellation or failure?

**Common Counterparts**:
`delete`, `archive`, `close`, `cancel`, `release`, `expire`, `revoke`, `detach`, `deprovision`, `cleanup`.

---

## MP-ST — State-Machine Completeness

**Trigger**:
Statuses, state enums, or transition handlers are observed in schemas or code logic.

**Ask**:
- Are all declared states handled by consumers?
- Do non-terminal states have eventual exit paths (timeouts, cancellations)?
- Are invalid transitions guarded?
- Do failure/cancel/timeout paths exist where implied?
- Are transition side effects consistent across states?

**Common Counterparts**:
Terminal states (`completed`, `failed`, `cancelled`, `expired`), transition guards, timeout sweeps.

---

## MP-SY — Symmetry / Counterpart Analysis

**Trigger**:
An operation implies a directional action with a expected counterpart.

**Examples**:
`grant` ↔ `revoke`, `link` ↔ `unlink`, `enable` ↔ `disable`, `lock` ↔ `unlock`, `charge` ↔ `refund`, `provision` ↔ `deprovision`.

**Counter-evidence Check**:
Do not require symmetry when the domain is intentionally irreversible (e.g., append-only financial ledgers, immutable audit logs).

---

## MP-MG — Mutation Guards

**Trigger**:
A route, command, API endpoint, or service function mutates meaningful state.

**Expectations to Search**:
Authentication checks, authorization policies, input schema validation, domain invariant guards, concurrency controls, idempotency tokens, transaction boundaries.

**Context Rule**:
Infer expected guards based on resource sensitivity and surrounding repository conventions.

---

## MP-SE — Side-Effect Completeness

**Trigger**:
A domain operation alters a primary resource that logically implies connected secondary side effects.

**Example**:
Order cancellation implies:
- primary state change (`cancelled`);
- inventory restoration/unreserve;
- payment void/refund;
- customer notification;
- domain event emission.

**Rule**:
Report only missing side effects that are directly supported by neighboring flows and domain evidence.

---

## MP-FR — Failure, Retry, Recovery

**Trigger**:
External API calls, payment processing, background jobs, webhooks, or distributed operations.

**Potential Counterparts**:
Explicit failure state handling, retry policies with backoff limits, idempotency keys, dead-letter queues, manual recovery hooks, compensation actions, background reconciliation sweeps.

---

## MP-OC — Ownership & Cleanup

**Trigger**:
A persistent child or external resource (uploaded file, storage key, API session, child record) has an identifiable parent/owner entity.

**Ask**:
What happens when the owner entity is deleted, disabled, soft-deleted, or replaced?

**Common Counterparts**:
Cascade delete, storage object deletion, orphan cleanup worker, soft-delete filtering.

---

## MP-AU — Authorization Symmetry

**Trigger**:
Privileged mutations, role definitions, permission mappings, or tenant boundary enforcement.

**Ask**:
- Are new mutation endpoints included in established RBAC/policy matrices?
- If UI hides an action, does the backend endpoint enforce the check?
- Can cross-tenant object IDs be mutated without authorization boundaries?

---

## MP-AS — Async & Background Completeness

**Trigger**:
Queue message producers, schedulers, webhook receivers, or asynchronous state transitions.

**Check**:
Consumer registration, handler wiring, retry limits, terminal dead-letter handling, stuck-job recovery mechanisms, webhook replay idempotency.

---

## MP-OP — Operational Completeness

**Trigger**:
System architecture or deployment configurations create concrete operational dependencies.

**Examples**:
Persistent schema migrations lacking ordering/backwards compatibility safeguards, background workers absent from readiness probes, required runtime environments missing deployment validation.

---

## MP-DC — Data Consistency

**Trigger**:
Duplicated/derived state, denormalized aggregate counters, or relational entity mutations.

**Check**:
Matching decrements on delete, cascade/orphan resolution, read-model projection sync, soft-delete query filtering.

---

## MP-CT — Contract Completeness

**Trigger**:
API schema enums, interface contracts, response types, or documented endpoints.

**Check**:
All enum values handled by client/server dispatch, promised response fields populated by backend, interface methods consistently implemented across adapters.

---

## MP-CF — Configuration Completeness

**Trigger**:
Required environment variables, feature flags, or integration settings referenced in code.

**Check**:
Configuration validation at startup, safe default fallbacks when optional, alignment between code usage and deployment manifests (`.env.example`, Dockerfile, helm/k8s).

---

## MP-OB — Observability Implied by Architecture

**Trigger**:
Asynchronous settlement processes, retry queues, or multi-step background workflows where silent failure causes persistent undetected corruption.

**Rule**:
Emit only when observability is functionally required to detect stuck or failed states. Do not report generic "add logging" advice without a concrete trigger.

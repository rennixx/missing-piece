# Counter-Evidence & Intentional Exceptions Checklist

Before reporting an omission as a defect, actively attempt to disprove absence and investigate intentional tradeoffs.

Do NOT invent hypothetical intent to excuse a gap. Require concrete repository evidence or mark the intent as **unresolved** (`Intent-dependent behavior`).

---

## 1. Intentional Exception Patterns

Actively inspect whether the observed behavior represents an authorized tradeoff:

### A. Administrative & Emergency Overrides
- **Pattern:** Direct mutation of status/entity bypassing normal validation, setup lifecycles, or state machine guards.
- **Evidence Required:** Route decorated with admin role requirements (`has_role('admin')`, `@admin_required`), functions explicitly named `override_*`, `force_*`, `reconcile_*`, or comments indicating manual intervention tools.
- **Consequence:** An administrative override is NOT an authentication bypass.

### B. Concurrency & Last-Write-Wins (LWW) Semantics
- **Pattern:** In-place state update without optimistic locking (`version`), distributed locks (`redlock`), or serialized queues.
- **Evidence Required:** Explicit comments acknowledging LWW ("Last write wins", "stateless overwrite"), low-frequency entity mutations, or downstream idempotent consumers.
- **Consequence:** Distinguish actual data corruption from acceptable overwrite races.

### C. Best-Effort Cleanup & Ephemeral Drop Semantics
- **Pattern:** File deletion, cache eviction, or webhook delivery wrapped in `try/except: pass` or `catch(err) { logger.warn(...) }`.
- **Evidence Required:** Cloud lifecycle rules (S3 bucket TTL, Redis maxmemory eviction), offline garbage collection scripts, or non-critical resource classification.
- **Consequence:** Failed cleanup leaving an orphaned file does NOT establish permanent retention or actual financial loss.

### D. External Ownership & Platform Boundaries
- **Pattern:** Counterpart handler missing in local repository because ownership is delegated out-of-repo.
- **Evidence Required:** Webhook dispatcher routed to external SQS/Kafka topic, managed cloud provider handling refunds/retries, or microservice split documented in architecture files.
- **Check `.missingpiecerc.json`:** Confirm whether the trigger is listed under `externalBoundaries`.

---

## 2. Structural Counter-Evidence Layers

Check all cross-cutting layers before concluding absence:

1. **Cross-Cutting Interceptors**:
   - Middleware, decorators, router dependencies (`Depends()`), base controller methods, or shared request handlers.
2. **Asynchronous & Decoupled Consumers**:
   - Transactional outbox tables, CDC streams (Debezium), message bus subscribers, background cron jobs, or worker queues.
3. **Framework & Database Native Behaviors**:
   - ORM cascade delete definitions (`ondelete="CASCADE"`, `dependent: :destroy`).
   - Database triggers, unique constraints, foreign keys, or stored procedures.
   - Framework auto-validation (Pydantic, Zod, Marshmallow).
4. **Alternative Terminology & Synonyms**:
   - Search domain synonyms (e.g. `cancel` vs `abort` vs `revoke` vs `terminate` vs `release` vs `unreserve`).

---

## 3. Disproof Standards

- If credible evidence of intentional authorization is found $\to$ Disposition: `Accepted behavior`.
- If evidence shows the counterpart exists elsewhere $\to$ Suppress candidate completely.
- If counterpart is absent, plausible tradeoff reasons exist, but no repository proof supports intent $\to$ Disposition: `Intent-dependent behavior` and log an entry in `Unresolved Intent Questions`.

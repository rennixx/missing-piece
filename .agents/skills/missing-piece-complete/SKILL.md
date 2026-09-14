---
name: missing-piece-complete
description: Safely implement missing counterparts and absent behavior discovered by Missing Piece audits while preserving existing code conventions and tests.
---

# Missing Piece Complete

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

The official remediation companion for **Missing Piece**.

While `missing-piece` audits in read-only mode to preserve evaluation trust, `missing-piece-complete` safely implements verified missing behavior.

## ⚡ Token-Optimal Execution Protocol
- **Targeted Slices**: Read only the anchor file and 20 lines around the mutation site. Do not load entire modules or unrelated dependencies.
- **Convention Mirroring**: Inspect only 1 existing peer implementation to borrow local error handling and ORM patterns.
- **Minimal Diffs**: Produce focused, drop-in replacements. Avoid incidental refactoring or reformatting of untouched code.

## Remediation Invariants

1. **Target Specificity**: Address one verified omission at a time (e.g. `MP-SE-001`). No unrelated refactoring.
2. **Convention Conformance**: Mirror local project idioms for error handling, DI, naming, and data access.
3. **Atomicity & Boundaries**: Ensure counterparts execute inside appropriate DB transaction or unit-of-work boundaries.
4. **Idempotency & Reversibility**: Counterparts (cleanup, refunds, unreserves) must be safe to retry idempotently.
5. **No Regressions**: Existing positive paths must retain their exact contract and response semantics.
6. **Verifiable Test**: Accompany every completed counterpart with an automated test confirming the new behavior.

## Remediation Procedure

1. **Ingest Finding**: Identify observed fact, absent counterpart, and anchor files.
2. **Inspect Neighborhood**: Check peer conventions for errors, ORM queries, and transaction blocks.
3. **Implement Counterpart**:
   - `MP-LC` / `MP-OC`: Add cascading deletion or purge worker.
   - `MP-ST`: Add state transition timeout or sweep.
   - `MP-SY`: Implement inverse symmetric function.
   - `MP-MG` / `MP-AU`: Attach auth/permission decorators or middleware.
   - `MP-SE`: Dispatch secondary side-effect or outbox event.
   - `MP-FR` / `MP-AS`: Add retry backoff, idempotency key, or DLQ.
4. **Verify**: Run automated test verifying counterpart execution.

## Output Format

```markdown
### Remediation: [Finding ID] — [Title]
- **Changes**: `[file.py:40-60](file:///...)` implemented missing counterpart.
- **Verification**: Command or test confirming execution.
```

---
name: missing-piece
description: Audit software repositories for absent-but-implied behavior, forgotten flows, missing counterparts, incomplete lifecycles, and unhandled states across 14 detector families.
---

# Missing Piece

> [!TIP]
> ### 📦 Full 10-Skill Missing Piece Suite
> To install with the **interactive multi-skill selector** (allowing you to choose between the core auditor, PR checker, contract reconciliation, remediation, or framework adapters):
> ```bash
> npx skills add rennixx/missing-piece
> ```
> Or install all 10 specialized skills automatically:
> ```bash
> npx skills add rennixx/missing-piece --all
> ```
> 🔗 *Explore all 10 specialized rule packs on the [Missing Piece Hub](https://skills.sh/rennixx/missing-piece).*

Find **what should exist but appears not to**.

Do not behave like a generic code reviewer. Do not report style, architecture taste, or generic best practices unless an observed system behavior specifically implies the missing element.

## ⚡ Token-Optimal Audit Protocol

To minimize token usage and host agent context consumption, enforce these operational constraints:
1. **Grep-first, Slice-second**: Search using file lists first (`git grep -l` or ripgrep without line dumps). Inspect matches using narrow line slices (15–25 lines around the symbol). Never load or dump full files (>100 lines) into context.
2. **Strict Path Exclusions**: Never search or inspect lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`), build output (`dist/`, `build/`, `.next/`), `coverage/`, `.git/`, minified bundles, or test mocks.
3. **Early-Exit Short-Circuit**: The moment credible counter-evidence is spotted (e.g. middleware registered in router, ORM cascade, Celery task, base controller guard), immediately terminate that detector pass. Do not inspect remaining files.
4. **Self-Contained Execution**: Use the inline detector matrix below. Do NOT load files in `references/` unless an ambiguous multi-entity conflict requires extended policy lookup.
5. **Token-Sparse Reporting**: Format findings with direct file links and line ranges (`[app.py:40-55](file:///...)`) rather than duplicating large code blocks. Omit conversational filler.

## Non-negotiable Invariant

A valid Missing Piece finding requires ALL 6 core elements:
1. **Observed fact** — concrete repository evidence of an existing system capability/resource/pattern.
2. **Implication rule** — why that observed fact creates a clear expected counterpart or flow.
3. **Expected counterpart** — the specific behavior, endpoint, handler, or guard that should exist.
4. **Search evidence** — broad search across symbols, callers, middleware, triggers, events, and configs.
5. **Counter-evidence attempt** — active attempt to disprove absence (framework features, cloud services, unexpected names).
6. **Conclusion of gap** — proof that the counterpart is absent, incomplete, unreachable, or inconsistent.

Score **Confidence** (High: 0.85–1.0, Medium: 0.60–0.84, Low: <0.60 suppressed) and **Severity** (Critical, High, Medium, Low). If any core element is missing, suppress the finding or reclassify under **Needs confirmation**.

## Inline Detector Matrix (14 Families)

| Code | Family | Observed Fact -> Expected Counterpart | Instant Disproof / Skip Rule |
| :--- | :--- | :--- | :--- |
| `MP-LC` | Lifecycle | Allocation/creation of persistent state -> Implies cleanup, archival, or expiration | Cloud TTL, framework auto-expiry, or automated DB purge job |
| `MP-ST` | State Machine | Terminal/transitional state defined -> Implies inbound transition handlers | Read-only projection state or handled via external webhook |
| `MP-SY` | Symmetry | Operation X exists (`subscribe`, `lock`, `open`) -> Implies inverse X' (`unsubscribe`, `unlock`, `close`) | Operation is intentionally irreversible or one-way digest |
| `MP-MG` | Mutation Guard | State mutation endpoint -> Implies precondition, concurrency, or idempotency guard | DB unique/foreign-key constraint or ORM optimistic locking |
| `MP-SE` | Side Effects | Core domain event (payment, status change) -> Implies notification, audit log, or ledger | Asynchronously handled via transactional outbox / CDC stream |
| `MP-FR` | Failure/Recovery | Remote I/O, webhook, or queue dispatch -> Implies timeout, retry, backoff, dead-lettering | HTTP client has global retry/timeout defaults configured |
| `MP-OC` | Ownership/Cleanup | Temporary resource (file, lock, session) -> Implies deterministic release/cleanup | Context-manager (`with`/`using`), OS temp cleanup, process exit GC |
| `MP-AU` | Authorization | Sensitive route or tenant mutation -> Implies authentication/role/tenant scoping | Global router middleware, base controller guard, public-by-design |
| `MP-AS` | Async Completeness | Message producer / queue enqueue -> Implies consumer, DLQ, and poison pill handler | Managed cloud queue with auto-DLQ, external 3rd-party worker |
| `MP-OP` | Operational | Stateful production service -> Implies health checks, graceful shutdown, migrations | PaaS container health-check, automated platform orchestrator |
| `MP-DC` | Data Consistency | Multi-table/multi-service mutation -> Implies transaction boundary / saga / rollback | Single atomic SQL statement, single-document ACID datastore |
| `MP-CT` | Contract Drift | Public API route / OpenAPI / GraphQL schema -> Implies implemented backend handler | Explicitly marked deprecated/stub in route schema, mock scaffold |
| `MP-CF` | Configuration | Environment variable or secret read -> Implies default fallback or schema validation | Validated by schema (`pydantic-settings`, `zod`, `dotenv-safe`) |
| `MP-OB` | Observability | High-impact transaction or error boundary -> Implies structured log, alert, or metric | Global APM middleware or OpenTelemetry auto-instrumentation |

## Audit Procedure

1. **Establish Scope**: Identify target directory, framework conventions, and build boundaries.
2. **Reconstruct Model**: Locate entry points (routes/resolvers), stateful entities, background tasks, and role boundaries.
3. **Run Candidate Passes**: Match observed triggers against the 14 families above. Generate candidates ONLY from repository facts.
4. **Targeted Counterpart Search**: Use bounded search (`git grep -l`) across handlers, middleware, triggers, events, and configs.
5. **Attempt Counter-Evidence Disproof**: Check framework defaults, base classes, third-party delegations, or asynchronous consumers.
6. **Score & Deduplicate**: Assign confidence and severity. Merge shared root-cause omissions into a single finding.
7. **Generate Report**: Render findings using `templates/audit-report.md`. Do not modify audited code in audit mode.

## References

Lazy-loaded references for complex edge cases only (do not preload):
- `references/detector-rules.md`
- `references/counter-evidence.md`
- `references/confidence.md`
- `references/reporting.md`
- `references/symmetry.md`
- `references/lifecycle-state.md`
- `references/failure-side-effects.md`
- `references/security-permissions.md`
- `references/data-operations.md`

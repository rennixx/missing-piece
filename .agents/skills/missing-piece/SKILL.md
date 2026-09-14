---
name: missing-piece
description: Audit software repositories for absent-but-implied behavior, forgotten flows, missing counterparts, incomplete lifecycles, and unhandled states across 14 detector families.
---

# Missing Piece

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> To install with the **interactive multi-skill selector** (allowing you to choose between the core auditor, PR checker, contract reconciliation, remediation, or framework adapters):
> ```bash
> npx skills add rennixx/missing-piece
> ```
> Or install all 12 specialized skills automatically:
> ```bash
> npx skills add rennixx/missing-piece --all
> ```
> 🔗 *Explore all 12 specialized rule packs on the [Missing Piece Hub](https://skills.sh/rennixx/missing-piece).*

Find **what should exist but appears not to**. Distinguish actual defects from intentional behavior and accepted tradeoffs.

Do not behave like a generic code reviewer. Do not report style, architecture taste, or generic best practices unless an observed system behavior specifically implies the missing element.

## ⚡ Token-Optimal & Autonomous Audit Protocol

To minimize token usage and maintain uninterrupted execution, enforce these operational constraints:
1. **Grep-first, Slice-second**: Search using file lists first (`git grep -l` or ripgrep without line dumps). Inspect matches using narrow line slices (15–25 lines around the symbol). Never load or dump full files (>100 lines) into context.
2. **Strict Path Exclusions**: Never search or inspect lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`), build output (`dist/`, `build/`, `.next/`), `coverage/`, `.git/`, minified bundles, or test mocks.
3. **Early-Exit Short-Circuit**: The moment credible counter-evidence or authorized intent is spotted, immediately terminate that detector pass. Do not inspect remaining files.
4. **Self-Contained Execution**: Use the inline detector matrix below. Do NOT load files in `references/` unless an ambiguous multi-entity conflict requires extended policy lookup.
5. **Token-Sparse Reporting**: Format findings with direct file links and line ranges (`[app.py:40-55](file:///...)`) rather than duplicating large code blocks. Omit conversational filler.
6. **Project Configuration**: Check for `.missingpiecerc.json` at repo root for exclusions, external boundaries, and custom suppressions (`references/configuration.md`).
7. **Autonomous Investigation**: Continue investigating without stopping to ask about every ambiguity. Collect unresolved intent questions in the report's `Unresolved Intent Questions` section; ask only when an answer materially affects immediate remediation.
8. **Accurate Scope Preservation**: Always distinguish a bounded pass from exhaustive coverage. A finding-free report certifies only the inspected boundary, never that unexamined flows are defect-free.

## Core Invariants: Evidence, Intent & Dispositions

Every reported candidate must adhere to these 10 principles:

1. **Separate Observed Behavior from Inferred Intent**: Code and tests prove what the software does. They do NOT, by themselves, prove that behavior violates requirements. Never conflate execution with violation.
2. **Establish the Source of Every Expected Behavior**: Label every counterpart expectation explicitly:
   - `Explicit requirement`: Documented policy, PRD, specification, API contract, or user instruction.
   - `Repository-supported expectation`: Consistent peer callers, tests, database schemas, or established domain invariants.
   - `Auditor assumption`: Conventional industry practice without clear repository support.
   *Strict Rule:* **Never present auditor assumptions as confirmed defects.**
3. **Actively Check for Intentional Exceptions**: Investigate administrative overrides, last-write-wins semantics, best-effort cleanup, external ownership, and accepted operational tradeoffs. Require supporting evidence; do not invent intent merely to dismiss a finding; mark intent as unresolved if evidence is absent.
4. **Separate Behavioral Confidence from Defect Confidence**:
   - `Behavioral Confidence` (High / Medium / Low): Certainty that the code executes as observed.
   - `Defect Confidence / Disposition`: Certainty that this behavior constitutes an undesirable defect. Avoid uncalibrated numerical confidence decimals.
5. **Classify under Four Standard Dispositions**:
   - `Confirmed defect`: Demonstrated violation of an established, explicit requirement.
   - `Likely gap`: Strong repository evidence supports the expectation, but business intent remains unconfirmed.
   - `Intent-dependent behavior`: Validity depends on an unresolved product or operational decision.
   - `Accepted behavior`: Explicitly authorized, documented, or supported by intentional tradeoffs.
6. **Report Consequences Precisely**: Ground all consequence claims in reality without inflation:
   - Duplicate activation ledger entries do not necessarily mean doubled lesson balances.
   - An administrator-only override is not an authentication bypass.
   - Failed cleanup leaving an orphaned file does not establish permanent retention or actual financial loss.
7. **Treat Tests as Evidence, Not Policy**: Tests prove how code executes under test conditions, not what business policy demands. Reproductions must include normal-path controls and state: (1) what is proven, (2) what is mocked, and (3) what remains unverified.
8. **Make Recommendations Conditional**: Explain which requirement or operational priority justifies a change. Do not automatically prescribe fixes because a conventional guard is missing. Prefer narrow remedies over prescribing new architecture.

## Inline Detector Matrix (14 Families)

| Code | Family | Observed Fact -> Expected Counterpart | Intentional Exceptions / Disproof Rule |
| :--- | :--- | :--- | :--- |
| `MP-LC` | Lifecycle | Allocation/creation of persistent state -> Implies cleanup, archival, or expiration | Cloud TTL, framework auto-expiry, automated purge, or accepted best-effort cleanup |
| `MP-ST` | State Machine | Terminal/transitional state defined -> Implies inbound transition handlers | Read-only projection state, external webhook, or deliberate administrative override |
| `MP-SY` | Symmetry | Operation X exists (`subscribe`, `lock`, `open`) -> Implies inverse X' (`unsubscribe`, `unlock`, `close`) | Operation is intentionally irreversible, one-way digest, or last-write-wins |
| `MP-MG` | Mutation Guard | State mutation endpoint -> Implies precondition, concurrency, or idempotency guard | DB unique/foreign-key constraint, optimistic locking, or accepted race tolerance |
| `MP-SE` | Side Effects | Core domain event (payment, status change) -> Implies notification, audit log, or ledger | Asynchronously handled via transactional outbox, CDC stream, or internal-only trigger |
| `MP-FR` | Failure/Recovery | Remote I/O, webhook, or queue dispatch -> Implies timeout, retry, backoff, dead-lettering | HTTP client has global defaults, or operation accepts best-effort drop semantics |
| `MP-OC` | Ownership/Cleanup | Temporary resource (file, lock, session) -> Implies deterministic release/cleanup | Context-manager (`with`/`using`), OS temp cleanup, process exit GC, or external orphan sweep |
| `MP-AU` | Authorization | Sensitive route or tenant mutation -> Implies authentication/role/tenant scoping | Global router middleware, base controller guard, or intentional admin break-glass tool |
| `MP-AS` | Async Completeness | Message producer / queue enqueue -> Implies consumer, DLQ, and poison pill handler | Managed cloud queue with auto-DLQ, external 3rd-party worker, or fire-and-forget telemetry |
| `MP-OP` | Operational | Stateful production service -> Implies health checks, graceful shutdown, migrations | PaaS container health-check, automated platform orchestrator, or ephemeral job |
| `MP-DC` | Data Consistency | Multi-table/multi-service mutation -> Implies transaction boundary / saga / rollback | Single atomic SQL statement, single-document ACID datastore, or eventual consistency model |
| `MP-CT` | Contract Drift | Public API route / OpenAPI / GraphQL schema -> Implies implemented backend handler | Explicitly marked deprecated/stub in route schema, mock scaffold, or beta preview |
| `MP-CF` | Configuration | Environment variable or secret read -> Implies default fallback or schema validation | Validated by schema (`pydantic-settings`, `zod`, `dotenv-safe`), or optional enhancement |
| `MP-OB` | Observability | High-impact transaction or error boundary -> Implies structured log, alert, or metric | Global APM middleware, OpenTelemetry auto-instrumentation, or standard framework access logs |

## Audit Procedure

1. **Establish Scope**: Identify target directory, framework conventions, and build boundaries. Explicitly record scope as a bounded pass.
2. **Reconstruct Model**: Locate entry points (routes/resolvers), stateful entities, background tasks, and role boundaries.
3. **Run Candidate Passes**: Match observed triggers against the 14 families above. Generate candidates ONLY from concrete repository facts.
4. **Targeted Counterpart Search**: Use bounded search (`git grep -l`) across handlers, middleware, triggers, events, and configs.
5. **Attempt Counter-Evidence & Intent Disproof**: Actively search for intentional exceptions (admin overrides, last-write-wins, best-effort cleanup, external ownership, ADRs, comments).
6. **Classify Expectation Source & Disposition**: Categorize expectation as `Explicit requirement`, `Repository-supported expectation`, or `Auditor assumption`. Assign disposition (`Confirmed defect`, `Likely gap`, `Intent-dependent behavior`, `Accepted behavior`).
7. **Score Confidence & Severity**: Distinguish behavioral confidence from defect confidence. Score severity based on grounded, non-inflated operational consequence.
8. **Collect Unresolved Intent Questions**: Log ambiguities where intent cannot be confirmed without stopping routine discovery.
9. **Generate Report**: Render findings using `templates/audit-report.md`. Do not modify audited code in audit mode.

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
- `references/configuration.md`

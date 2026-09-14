# Detection Methodology

## Core Invariant

A Missing Piece finding is:

$$\text{Observed Fact} + \text{Expectation Source} - \text{Verified Counterpart} - \text{Intentional Exceptions} = \text{Verified Omission}$$

Code and tests prove what the system does; they do NOT, by themselves, prove that behavior violates requirements. Never conflate execution with violation.

---

## The 9-Phase Methodology

### Phase 1 — Scope Definition
Determine:
- Repository root, framework conventions, and build boundaries.
- **Accurate Scope Preservation:** Explicitly define the audit as a *bounded pass*. A finding-free report certifies only the inspected boundary, never that unexamined flows are defect-free.
- Load project-level configurations and suppressions from `.missingpiecerc.json`.

### Phase 2 — Reconnaissance & System Modeling
Build an inventory of:
- Entry points (routes, resolvers, message listeners).
- Domain entities and state lifecycles.
- Explicit documented requirements (PRDs, ADRs, user instructions).
- Operational boundaries (external services, background queues, administrative paths).

### Phase 3 — Candidate Generation & Expectation Sourcing
Generate candidate expectations ONLY from concrete repository facts. Categorize the source of every expected behavior:
1. **Explicit requirement:** Documented policy, PRD, contract, or user instruction.
2. **Repository-supported expectation:** Consistent peer callers, tests, or domain invariants.
3. **Auditor assumption:** Conventional practice without clear repository support. (*Rule: Never present auditor assumptions as confirmed defects.*)

### Phase 4 — Targeted Structural Search
Search broadly to avoid naming or file location assumptions:
- Symbols and semantic synonyms.
- Routes, event handlers, middleware, decorators, and base classes.
- Database triggers, ORM cascades, and migration definitions.

### Phase 5 — Counter-Evidence & Intentional Exception Check
Actively attempt to disprove the candidate omission and investigate intentional tradeoffs:
- **Administrative overrides:** Route with admin roles intentionally bypassing standard wizards. (An admin override is NOT an auth bypass).
- **Concurrency semantics:** Documented last-write-wins (LWW) tolerance.
- **Best-effort cleanup:** Accepted orphan records/files relying on offline sweeps or cloud TTLs. (Failed cleanup != permanent retention or financial loss).
- **External ownership:** Provider or external microservice owns the counterpart.
- *Strict Rule:* Do NOT invent intent merely to dismiss a candidate. Require supporting repository evidence or mark intent as unresolved.

### Phase 6 — Reachability & Completeness
Confirm whether an existing counterpart is actually reachable:
- Is it active or dead code?
- Is it guarded correctly?
- Is it wired only in test mocks?
Report "incomplete/unwired" when the symbol exists but cannot be reached.

### Phase 7 — Dual Confidence & Disposition Calibration
Separate execution certainty from defect certainty:
- **Behavioral Confidence** (High / Medium / Low): Certainty that the code executes as observed.
- **Disposition:**
  - `Confirmed defect`: Demonstrated violation of an established requirement.
  - `Likely gap`: Strong repository evidence supports the expectation, but intent remains unconfirmed.
  - `Intent-dependent behavior`: Validity depends on a product or operational decision.
  - `Accepted behavior`: Explicitly authorized or documented.

### Phase 8 — Consequence Precision & Deduplication
- State realistic, uninflated consequences without hyperbole.
- Merge shared root causes into a single primary finding with downstream symptoms.

### Phase 9 — Autonomous Reporting & Conditional Recommendations
- Deliver the report using `templates/audit-report.md`.
- **Treat tests as evidence, not policy:** Include normal-path controls, what is proven, what is mocked, and what remains unverified.
- **Conditional recommendations:** Explain which requirement justifies a change; prefer narrow remedies over prescribing new architecture.
- **Collect unresolved intent questions:** Log open tradeoffs in the report without interrupting autonomous audit execution.

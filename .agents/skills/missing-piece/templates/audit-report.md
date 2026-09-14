# Missing Piece Audit Report

## Scope

- **Mode:** standard | focused | change | deep | re-audit
- **Coverage Boundary:** Bounded pass (explicit paths/domains listed below) — does NOT imply uninspected flows are defect-free.
- **Repository/module:** `<path>`
- **Focus:** `<feature/domain/all>`
- **Exclusions:** `<vendor/build/etc>`

## System Model & Intent Sources

- **Observed Capabilities:** [Reconstructed capabilities, lifecycles, state flows, role boundaries]
- **Documented Requirements:** [Explicit policies, specifications, ADRs, or user instructions identified]
- **Operational Boundaries:** [External platforms, background queues, administrative paths]

## Finding Summary

| ID | Title | Detector Family | Expectation Source | Disposition | Severity | Behavioral Conf. |
|---|---|---|---|---|---|---|
| MP-XX-001 | [Specific Title] | MP-XX | Explicit / Repo-supported / Auditor assumption | Confirmed defect / Likely gap / Intent-dependent / Accepted | High | High |

## Findings

### MP-[FAMILY]-[NUM] — [Finding Title]

- **Detector Family:** `MP-[FAMILY]`
- **Expectation Source:** `Explicit requirement` | `Repository-supported expectation` | `Auditor assumption`
- **Disposition:** `Confirmed defect` | `Likely gap` | `Intent-dependent behavior` | `Accepted behavior`
- **Severity:** `Critical` | `High` | `Medium` | `Low` | `Informational`
- **Behavioral Confidence:** `High` | `Medium` | `Low` (Certainty that observed execution occurs)

**Reachable Trigger & Permissions**  
[Caller, HTTP route, event topic, or actor role that triggers this path, and preconditions required to reach it.]

**Observed**  
[Concrete observed evidence in repository code/schema proving what the software actually does. Code and tests prove execution, not that behavior violates requirements.]

**Expected**  
[Specific counterpart, handler, endpoint, or guard expected to exist. Cites the exact source: explicit contract, repository peer pattern, or conventional assumption.]

**Intent & Tradeoff Assessment**  
[Active check for candidate-specific intentional exceptions: administrative overrides, last-write-wins semantics, best-effort cleanup, external ownership, or operational tradeoffs. Supporting repository evidence cited, or explicitly marked unresolved.]

**Evidence searched**  
[Broad search across symbols, callers, middleware, routes, events, configs, test mocks, and normal-path controls.]

**Gap**  
[Specific nature of absence, incompleteness, reachability break, or inconsistency.]

**Why it matters**  
[Precise, uninflated operational consequence. Distinguish direct effects from speculative damage (e.g., duplicate entries != double balance; admin override != auth bypass; orphaned file != financial loss).]

**Evidence**  
- `path/to/file:L10-L25` — [Context/Symbol]

**Verification**  
[Falsifiable reproduction check with normal-path control where practical. State clearly: (1) what the test proves, (2) what is mocked vs production wiring, and (3) what remains unverified. If verification is unavailable, report that limitation honestly.]

**Remaining Uncertainty**  
[Known verification limits, unverified runtime environment, or external platform dependencies.]

**Recommendation (Conditional & Proportional)**  
[Conditional guidance: explain which requirement or operational decision justifies a change. Recommend narrow remedies over prescribing architecture. Preserve intentional overrides and accepted tradeoffs.]

---

## Unresolved Intent Questions

[Ambiguities collected autonomously during the audit where intent is not established by repository evidence. Posed to product/engineering owners for resolution.]
- **Question 1:** `<file:line>` — [Does the business permit X tradeoff, or is Y required?]

## Coverage Ledger

| Flow / Endpoint / Caller | Transition / Operation | Guard / Permission Checked | Failure Path Evaluated | Status | Search Truncations / Notes |
|---|---|---|---|---|---|
| `<module.function>` | [State transition or mutation] | [Guard / role checked] | [Error / timeout handling] | `Inspected` \| `Partial` \| `Unexamined` | [Search queries resolved or truncated] |

### Coverage Boundaries & Limitations
- **Inspected Domains:** [Explicit modules, callers, routes, and lifecycles examined in this bounded pass]
- **Partial / Unexamined Areas:** [Candidate paths not reached or partially analyzed — no guarantee of correctness]
- **Truncated / Unresolved Searches:** [Any search truncation, unread large files, or unresolved queries; resolved before relying on absence claims]
- **Exhaustiveness Disclaimer:** Bounded pass only; does NOT imply uninspected flows or components are defect-free.

## Suppressed / Accepted Candidates

[Candidates evaluated and disproved or confirmed as intentional/authorized tradeoffs with supporting evidence.]
- `MP-XX-XXX`: [Description] — Disposition: `Accepted behavior` (Reason: `admin-override` | `best-effort` | `external-owner` | `documented-tradeoff`)

## Re-Audit Tracking

Prior findings verification:
- `MP-XX-001`: Fixed | Still Present | Modified

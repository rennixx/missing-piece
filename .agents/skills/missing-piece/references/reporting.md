# Reporting Rules & Claim-Level Evidence

Missing Piece findings must deliver precise, uninflated, and falsifiable technical assessments backed by claim-level evidence.

---

## 1. Finding Contract & Claim-Level Evidence

Every finding in `audit-report.md` must establish all 6 claim-level evidence components:

```markdown
### MP-XX-001 — <Specific, Falsifiable Title>

- **Detector Family:** `MP-[FAMILY]`
- **Expectation Source:** `Explicit requirement | Repository-supported expectation | Auditor assumption`
- **Disposition:** `Confirmed defect | Likely gap | Intent-dependent behavior | Accepted behavior`
- **Severity:** `Critical | High | Medium | Low | Informational`
- **Behavioral Confidence:** `High | Medium | Low`

**Reachable Trigger & Permissions**
Specific caller, HTTP route, event topic, or actor role that triggers this path, and preconditions required to reach it.

**Observed**
Concrete code/schema fact proving what happens. Code and tests prove execution, not that behavior violates requirements.

**Expected**
The counterpart expected, citing its authoritative origin (contract, peer caller, or convention).

**Intent & Tradeoff Assessment**
Analysis of candidate-specific intentional exceptions (admin override, LWW, best-effort cleanup, external ownership). Evidence cited or marked unresolved.

**Evidence searched**
Search scope across symbols, callers, routes, configs, test mocks, and normal-path controls.

**Gap**
Specific nature of omission, reachability failure, or state inconsistency.

**Why it matters**
Grounded, uninflated consequence statement.

**Evidence**
- `path/file.ts:L10-L25` — Context/symbol

**Verification**
Falsifiable check with normal-path control where practical. State: (1) what is proven, (2) what is mocked vs production wiring, and (3) what remains unverified. If verification is unavailable, report that limitation honestly.

**Remaining Uncertainty**
Known verification limits, unverified runtime environment, or external platform dependencies.

**Recommendation (Conditional & Proportional)**
Conditional guidance: specify which requirement justifies the change. Prefer narrow remedies over prescribing new architecture. Preserve intentional overrides and accepted tradeoffs.
```

---

## 2. Consequence Precision Rules

Never inflate severity to make a finding sound alarming:

| Bad / Inflated Claim | Grounded Reality |
|---|---|
| "Causes infinite balance duplication and severe financial theft." | "Creates duplicate ledger records; downstream aggregate queries filter by unique transaction ID, preventing duplicate balances, but accounting audit trails diverge." |
| "Critical authentication bypass allows unauthorized mutation." | "Administrator-only maintenance route intentionally bypasses the multi-step activation wizard; standard user authentication and admin role enforcement remain intact." |
| "Permanent data retention and unbounded cloud storage costs." | "Failed media deletion leaves orphaned objects in S3; lifecycle rules or scheduled maintenance may expire them, but immediate deletion consistency is unverified." |

---

## 3. Testing as Evidence, Not Policy

Tests demonstrate how code executes under specific conditions. They do not define business policy.

When authoring verification reproductions:
1. **Include Normal-Path Controls**: Verify that the happy path behaves as intended before demonstrating the gap.
2. **Distinguish Mocks from Production Wiring**: Test doubles (e.g. `MagicMock`, `@patch`) prove only that mocks were called, not that real DB constraints, triggers, or message brokers exist or execute.
3. **State What is Proven**: State exactly which state mutation or failure was observed.
4. **State What is Mocked**: Clearly acknowledge if external network calls, clocks, or databases are mocked.
5. **State What Remains Unverified**: Highlight any aspect (e.g. concurrency under real DB locks, cloud cascade rules) not tested by unit mocks.

---

## 4. Structured Coverage Ledger & Honest Boundaries

Never claim or imply exhaustive safety from a bounded pass:

1. **Maintain the Coverage Ledger**:
   - Explicitly record every evaluated flow, transition, caller, guard, and failure path.
   - Assign status: `Inspected` | `Partial` | `Unexamined`.
2. **Search Truncation Tracking**:
   - Explicitly record failed, timed-out, or truncated search queries.
   - Resolve truncated searches before relying on negative evidence to claim absence.
3. **Bounded Pass Disclaimers**:
   - A finding-free report certifies only that no violations were discovered within the inspected boundary. It never certifies that unexamined paths are defect-free.

---

## 5. Proportional & Conditional Recommendations

Do not automatically demand code changes just because a conventional pattern is missing.
- Format recommendations conditionally: *"If the product requires strict serializability across concurrent sessions, add optimistic locking via a `version` column. If last-write-wins is acceptable, document this tradeoff in the service header."*
- Favor narrow remedies (e.g. adding a missing status check or filter) over prescribing large-scale architectural redesigns (e.g. introducing distributed locking or Kafka).
- Unknown intent must neither become assumed approval nor an automatic defect. Classify as `Intent-dependent behavior` and log an entry in `Unresolved Intent Questions`.

# Reporting Rules & Consequence Precision

Missing Piece findings must deliver precise, uninflated, and falsifiable technical assessments.

---

## 1. Finding Structure

Every finding in `audit-report.md` must adhere to this contract:

```markdown
### MP-XX-001 — <Specific, Falsifiable Title>

- **Detector Family:** `MP-[FAMILY]`
- **Expectation Source:** `Explicit requirement | Repository-supported expectation | Auditor assumption`
- **Disposition:** `Confirmed defect | Likely gap | Intent-dependent behavior | Accepted behavior`
- **Severity:** `Critical | High | Medium | Low | Informational`
- **Behavioral Confidence:** `High | Medium | Low`

**Observed**
Concrete code/schema fact proving what happens. Code and tests prove execution, not that behavior violates requirements.

**Expected**
The counterpart expected, citing its authoritative origin (contract, peer caller, or convention).

**Intent & Tradeoff Assessment**
Analysis of intentional exceptions (admin override, LWW, best-effort cleanup, external ownership). Evidence cited or marked unresolved.

**Evidence searched**
Search scope across symbols, callers, routes, configs, and normal-path controls.

**Gap**
Specific nature of omission, reachability failure, or state inconsistency.

**Why it matters**
Grounded, uninflated consequence statement.

**Evidence**
- `path/file.ts:L10-L25` — Context/symbol

**Verification**
Falsifiable check with normal-path control. State: (1) what is proven, (2) what is mocked, and (3) what remains unverified.

**Recommendation (Conditional)**
Conditional remedy: specify which requirement justifies the change. Prefer narrow remedies over prescribing new architecture.
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
2. **State What is Proven**: State exactly which state mutation or failure was produced.
3. **State What is Mocked**: Clearly acknowledge if external network calls, clocks, or databases are mocked.
4. **State What Remains Unverified**: Highlight any aspect (e.g. concurrency under real DB locks) not tested by unit mocks.

---

## 4. Conditional Recommendations

Do not automatically demand code changes just because a conventional pattern is missing.
- Format recommendations conditionally: *"If the product requires strict serializability across concurrent sessions, add optimistic locking via a `version` column. If last-write-wins is acceptable, document this tradeoff in the service header."*
- Favor narrow remedies (e.g. adding a missing status check or filter) over prescribing large-scale architectural redesigns (e.g. introducing distributed locking or Kafka).

---

## 5. Autonomous Auditing

Audits must execute autonomously:
- Do not stop to prompt the user about routine ambiguities.
- Record unresolved tradeoffs in the `Unresolved Intent Questions` section of the report.
- Ask product stakeholders directly only when the answer materially changes the immediate remediation path.

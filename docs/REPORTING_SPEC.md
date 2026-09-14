# Reporting Specification

## Goals

Missing Piece audit reports must be:
- evidence-grounded and falsifiable;
- explicit about expectation source and intent;
- calibrated using qualitative dispositions instead of arbitrary numerical scores;
- precise and uninflated regarding operational consequences;
- clear about bounded scope limits (a clean report does not certify unexamined flows).

---

## Finding Schema

Each finding adheres to the following contract:

### 1. Title
One concise, factual sentence naming the observed gap.

### 2. Header Metadata
- **Detector Family:** `MP-[FAMILY]`
- **Expectation Source:** `Explicit requirement` | `Repository-supported expectation` | `Auditor assumption`
- **Disposition:** `Confirmed defect` | `Likely gap` | `Intent-dependent behavior` | `Accepted behavior`
- **Severity:** `Critical` | `High` | `Medium` | `Low` | `Informational`
- **Behavioral Confidence:** `High` | `Medium` | `Low`

### 3. Observed
Concrete repository facts proving what happens in code or schemas. Code and tests prove execution, not that behavior violates requirements.

### 4. Expected
The counterpart expected, citing its authoritative origin (explicit contract, consistent peer pattern, or conventional assumption).

### 5. Intent & Tradeoff Assessment
Active check for intentional exceptions (administrative overrides, last-write-wins, best-effort cleanup, external ownership). Supporting repository evidence cited, or marked unresolved.

### 6. Evidence Searched
Where and how the agent searched across symbols, callers, routes, configs, and normal-path controls.

### 7. Gap
What could not be established (absence, incompleteness, reachability break, or inconsistency).

### 8. Why It Matters
Grounded, uninflated consequence statement. Distinguish direct effects from speculative damage.

### 9. Evidence
Exact file and line-range links (`[path/file.py:L10-L25](file:///...)`).

### 10. Verification
Falsifiable reproduction check with normal-path control. State clearly: (1) what is proven, (2) what is mocked, and (3) what remains unverified.

### 11. Recommendation (Conditional)
Conditional remedy: specify which requirement justifies a change. Prefer narrow remedies over prescribing new architecture.

---

## Consequence Precision Rules

- ❌ Do NOT claim "infinite balance duplication" when an un-idempotent insert has downstream aggregate safeguards.
- ❌ Do NOT claim "authentication bypass" for an internal administrative maintenance endpoint with separate role checks.
- ❌ Do NOT claim "massive cloud bill / permanent financial loss" when a failed cleanup leaves an ephemeral temporary file.

---

## Report Structure

```markdown
# Missing Piece Audit Report

## Scope (Bounded Pass)
## System Model & Intent Sources
## Finding Summary Table
## Findings
### MP-[FAMILY]-[NUM]
## Unresolved Intent Questions
## Coverage Summary (Inspected vs Excluded)
## Suppressed / Accepted Candidates
## Re-Audit Tracking
```

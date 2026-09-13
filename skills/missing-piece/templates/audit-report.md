# Missing Piece Audit Report

## Scope

- **Mode:** standard | focused | change | deep | re-audit
- **Repository/module:** `<path>`
- **Focus:** `<feature/domain/all>`
- **Exclusions:** `<vendor/build/etc>`

## System Model

Summarize the observed capabilities, resource lifecycles, state transitions, external integrations, RBAC policies, async workers, and side effects.

## Finding Summary

| ID | Title | Detector Family | Severity | Confidence |
|---|---|---|---|---|

## Findings

### MP-[FAMILY]-[NUM] — [Finding Title]

- **Detector Family:** `MP-[FAMILY]`
- **Severity:** `Critical | High | Medium | Low | Informational`
- **Confidence:** `High | Medium | Low`

**Observed**  
[Concrete observed evidence in repository code/schema that creates the expectation]

**Expected**  
[Specific counterpart, handler, endpoint, or guard expected to exist]

**Evidence searched**  
[Broad search performed across symbols, callers, middleware, routes, events, configs]

**Gap**  
[Specific nature of absence, incompleteness, or unreachability]

**Why it matters**  
[Concrete potential impact and consequence if unaddressed]

**Evidence**  
- `path/to/file:L10-L25` — [Context/Symbol]

**Verification**  
[Clear step or command for user to confirm or refute the omission claim]

**Suggested direction**  
[High-level remediation guidance]

---

## Needs Confirmation

Potential omissions requiring human confirmation or external system verification (Medium/Low confidence).

## Coverage Summary

### Inspected
- [Paths, modules, or flows inspected]

### Not Verified / Excluded
- [External services, unviewed files, or non-verifiable boundaries]

## Suppressed Candidates

Candidates checked and disproved by counter-evidence search (with reason: `framework-provided`, `external-owner`, `intentional`, `duplicate`).

## Re-Audit Tracking

Prior findings verification:
- `MP-XX-001`: Fixed | Still Present | Modified

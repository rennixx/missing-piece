# Confidence and Severity Model

Confidence answers:

> **How sure are we that the piece is actually missing or incomplete?**

Severity answers:

> **If it is missing, how bad could the consequence be?**

Never merge the two.

## Confidence model

Use a qualitative score backed by internal factors.

### High confidence

Typical conditions:
- trigger behavior is directly observed;
- expectation is structurally strong;
- search covered obvious and non-obvious implementations;
- no meaningful counter-evidence;
- relevant flow is reachable;
- repository conventions strengthen the expectation.

Suggested numeric representation: 0.85–1.00.

### Medium confidence

Typical conditions:
- strong trigger but framework/provider behavior is uncertain;
- counterpart may live outside visible repository;
- search coverage is partial;
- intent is ambiguous.

Suggested representation: 0.60–0.84.

### Low confidence

Anything below 0.60.

Low-confidence findings are normally suppressed.

## Confidence factors

A future deterministic model may weight:
- trigger certainty: 0–1;
- implication strength: 0–1;
- search coverage: 0–1;
- reachability certainty: 0–1;
- convention consistency: 0–1;
- counter-evidence penalty: 0–1;
- external-ownership penalty: 0–1.

The exact formula is intentionally not frozen in v1. Calibration must come from benchmark results.

## Severity

### Critical
Plausible consequence includes:
- catastrophic data loss;
- systemic unauthorized access;
- irreversible financial corruption;
- widespread destructive behavior.

Use rarely.

### High
Likely major:
- security boundary failure;
- material financial error;
- persistent data inconsistency;
- unrecoverable operational failure;
- major resource leak.

### Medium
Meaningful correctness/reliability defect with bounded impact.

### Low
Minor lifecycle, maintainability, or edge-case omission with limited impact.

### Informational
Suspicious asymmetry worth human confirmation, but no concrete defect established.

## Reporting matrix

Default visibility:

| Confidence | Critical | High | Medium | Low | Info |
|---|---:|---:|---:|---:|---:|
| High | show | show | show | selective | selective |
| Medium | show | show | selective | suppress | suppress |
| Low | suppress* | suppress* | suppress | suppress | suppress |

`*` A low-confidence catastrophic possibility may be listed under "Needs confirmation", never stated as fact.

# Confidence and Severity

## Confidence

### High
Use when:
- observed trigger is direct;
- implication is strong;
- broad search performed;
- no significant counter-evidence;
- relevant path is reachable.

### Medium
Use when:
- expectation is reasonable but intent/provider/framework is uncertain;
- repository boundary may hide behavior;
- search coverage is partial.

### Low
Suppress by default.

## Severity

### Critical
Potential catastrophic data/security/financial consequence.

### High
Major integrity, security, financial, or persistent reliability impact.

### Medium
Meaningful correctness/reliability impact.

### Low
Bounded edge case or minor lifecycle defect.

### Informational
Suspicious structural asymmetry requiring human confirmation.

## Calibration questions

Confidence:
- How directly did I observe the trigger?
- How universal is the implication in this exact domain?
- How thoroughly did I search?
- What counter-evidence exists?
- Could behavior live elsewhere?

Severity:
- How many users/resources could be affected?
- Is damage reversible?
- Is sensitive/financial data involved?
- Can failure persist silently?
- Does it cross an authorization boundary?

# Reporting Specification

## Goals

Reports must be:
- compact;
- evidence-first;
- stable enough for re-audits;
- easy to paste into issues;
- explicit about uncertainty.

## Finding ID

Format:

`MP-<FAMILY>-<NNN>`

Example:

`MP-LC-003`

IDs are report-local in v1.

## Finding schema

Each finding contains:

### Title
One sentence naming the missing behavior.

### Severity
Critical / High / Medium / Low / Informational.

### Confidence
High / Medium / Low and optional numeric estimate.

### Observed
Concrete repository facts that triggered the expectation.

### Expected
The implied counterpart/invariant.

### Evidence searched
Where and how the agent looked.

### Gap
What could not be established.

### Why it matters
Concrete consequence, phrased conditionally when appropriate.

### Evidence
File/symbol references.

### Verification
Fastest way for the maintainer to confirm/refute.

### Suggested direction
Conceptual remediation only unless the user asks for code.

## Report structure

```markdown
# Missing Piece Audit

## Scope
## System model
## Summary
## Findings
### MP-...
## Needs confirmation
## Coverage
## Suppressed / not findings
## Re-audit notes
```

## Summary table

| ID | Finding | Severity | Confidence |
|---|---|---|---|

Do not put long evidence in the table.

## Language rules

Prefer:
- "No reachable release path was found..."
- "The repository appears to..."
- "This may leave..."
- "I searched X, Y, and Z..."

Avoid:
- "You forgot..."
- "This definitely breaks..."
- "Best practice says..."
- "Every production app should..."
- "Clearly..."

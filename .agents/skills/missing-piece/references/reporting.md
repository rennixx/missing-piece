# Reporting Rules

## Finding format

```markdown
### MP-XX-001 — <specific title>

**Severity:** High  
**Confidence:** High (0.92)

**Observed**
...

**Expected**
...

**Evidence searched**
...

**Gap**
...

**Why it matters**
...

**Evidence**
- `path/file.ts` — symbol/context
- `path/other.ts` — symbol/context

**Verify**
...

**Suggested direction**
...
```

## Strong titles

- Reserved inventory has no reachable release path on cancellation
- New admin mutation bypasses the established policy map
- `processing` jobs have no crash-recovery transition
- Token issuance exists without a reachable revocation mechanism

## Weak titles

- Missing cleanup
- Security issue
- Add retries
- Improve error handling
- Consider logging

## Coverage section

State what was actually inspected.

Example:

```text
Covered:
- orders domain
- payment adapter
- inventory reservations
- queue workers
- related tests

Not verified:
- external payment-provider dashboard configuration
- production scheduler configuration
```

## Needs confirmation

Use when potential impact is significant but certainty is below normal reporting threshold.

Never phrase Needs-confirmation items as established defects.

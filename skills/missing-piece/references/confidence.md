# Confidence, Expectation Sources & Dispositions

Missing Piece strictly separates **Behavioral Confidence** (did this execution occur?) from **Defect Confidence / Disposition** (is this behavior undesirable?).

Never use uncalibrated numerical confidence decimals (e.g., 0.88 vs 0.94). Ground assessments in verifiable repository evidence and clear qualitative taxonomy.

---

## 1. Expectation Source Taxonomy

Every expected behavior must be labeled with its authoritative source:

1. **Explicit Requirement**:
   - Backed by formal documentation, PRD specifications, ADRs, user instructions, or OpenAPI/database constraints.
   - *Example:* "PRD Section 4.2 states checkout cancellations must trigger Stripe refund within 5 seconds."
2. **Repository-Supported Expectation**:
   - Backed by consistent peer implementations, test fixtures, caller assumptions, or domain invariants across the repository.
   - *Example:* "All 4 other payment gateway adapters call `inventory.release()` on failure; only the new PayPal adapter omits it."
3. **Auditor Assumption**:
   - Derived from general industry best practices or conventional safeguards without explicit repository proof.
   - *Example:* "A distributed queue consumer conventionally benefits from a dead-letter queue."
   - **Strict Rule:** *Auditor assumptions must NEVER be classified as Confirmed Defects.*

---

## 2. Disposition Taxonomy

Classify every candidate omission under one of four standard dispositions:

| Disposition | Definition | Required Evidence | Permitted Expectation Source |
|---|---|---|---|
| **Confirmed Defect** | Demonstrated violation of an established requirement. | Direct code trace proving failure to fulfill an explicit contract or hard invariant. | `Explicit requirement` only |
| **Likely Gap** | Strong repository evidence supports the expectation, but business intent remains unconfirmed. | Consistent peer pattern or domain invariant exists, but no explicit doc bans the omission. | `Repository-supported expectation` |
| **Intent-Dependent Behavior** | Validity depends on a product, architectural, or operational decision. | Observed behavior is clear, but alternative tradeoff interpretations (e.g. LWW, best-effort) are plausible. | `Repository-supported expectation` or `Auditor assumption` |
| **Accepted Behavior** | Explicitly authorized, documented, or supported by intentional tradeoffs. | Supporting code comment, ADR, admin flag, or operational design proves behavior is deliberate. | Any source where exception evidence is verified |

---

## 3. Behavioral Confidence vs. Defect Confidence

### Behavioral Confidence
Measures certainty that the software executes exactly as reported.
- **High**: Verified by concrete code trace, unit test reproduction, or direct AST callgraph.
- **Medium**: Inferred from structural conventions; dynamic runtime routing or reflection introduces slight uncertainty.
- **Low**: Speculative path or unreachable dead code. (Suppress from audit report).

### Defect Confidence (Disposition)
Measures certainty that the observed behavior is an unwanted defect rather than an intentional tradeoff.
- Code can be **High** Behavioral Confidence (we know 100% that S3 objects are not deleted on user cancel) but **Intent-Dependent** or **Accepted Behavior** (the team intentionally designed async monthly garbage collection).

---

## 4. Severity Calibration

Ground severity strictly in realistic, uninflated operational consequences:

- **Critical**: Irreversible catastrophic loss (active fund loss, auth bypass allowing unauthorized tenant mutation, unrecoverable data wipe).
- **High**: Major functional breakage, persistent state corruption, unmonitored settlement failure, or unrecoverable deadlock.
- **Medium**: Meaningful reliability or operational gap (resource leakage, stuck job needing manual reset, unhandled error state).
- **Low**: Minor edge-case asymmetry, non-critical telemetry gap, or cosmetic drift.
- **Informational**: Intentional tradeoff or accepted behavior highlighted for architectural awareness.

### Consequence Precision Guardrails
- ❌ Do NOT claim "potential infinite balance duplication" when an un-idempotent ledger insert has downstream aggregate safeguards.
- ❌ Do NOT claim "authentication bypass" for an internal administrative maintenance endpoint with separate role checks.
- ❌ Do NOT claim "massive cloud bill / permanent financial loss" when a failed cleanup leaves an ephemeral temporary file.

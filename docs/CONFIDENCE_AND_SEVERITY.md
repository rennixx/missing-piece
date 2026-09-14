# Confidence, Disposition, and Severity Model

Missing Piece separates **Behavioral Confidence** from **Defect Confidence (Disposition)** and **Severity**:

1. **Behavioral Confidence**: *How sure are we that the code executes as observed?*
2. **Defect Confidence (Disposition)**: *How sure are we that this behavior violates requirements and represents an undesirable defect rather than an intentional tradeoff?*
3. **Severity**: *If this is indeed an unintended defect, what is the realistic, uninflated operational consequence?*

Never merge these three independent dimensions. Avoid uncalibrated decimal gymnastics (e.g. 0.88 vs 0.94); use clear qualitative taxonomy backed by repository evidence.

---

## 1. Expectation Source Taxonomy

Every expected behavior must be labeled with its authoritative source:

1. **Explicit Requirement**:
   - Documented policy, PRD, specification, ADR, user instruction, or schema contract.
2. **Repository-Supported Expectation**:
   - Consistent peer implementations, caller assumptions, test suites, or domain invariants across the repository.
3. **Auditor Assumption**:
   - Conventional industry best practice without clear repository support.
   - *Strict Invariant:* **Never present auditor assumptions as confirmed defects.**

---

## 2. Disposition Taxonomy

| Disposition | Meaning | Required Evidence | Permitted Sources |
|---|---|---|---|
| **Confirmed Defect** | Demonstrated violation of an established requirement. | Direct code execution proves breach of explicit requirement or contract. | `Explicit requirement` only |
| **Likely Gap** | Strong repository evidence supports the expectation, but intent remains unconfirmed. | Consistent peer pattern or domain invariant exists, but intent is not formally documented. | `Repository-supported expectation` |
| **Intent-Dependent Behavior** | Validity depends on a product, architectural, or operational decision. | Observable behavior is clear, but alternative tradeoff interpretations (LWW, best-effort) are plausible. | `Repository-supported expectation` or `Auditor assumption` |
| **Accepted Behavior** | Explicitly authorized, documented, or supported by intentional tradeoffs. | Code comments, ADR, admin flag, or architecture design proves behavior is deliberate. | Any source with verified tradeoff evidence |

---

## 3. Dual Confidence Model

### Behavioral Confidence
- **High**: Directly observed in reachable code, confirmed via callgraph or reproduction test.
- **Medium**: Inferred from structural conventions; dynamic dispatch or reflection leaves slight uncertainty.
- **Low**: Speculative path or unreachable code (suppressed from report).

### Defect Confidence / Disposition Calibration
- Behavioral execution certainty does NOT prove defect certainty.
- A reproduction test can demonstrate 100% Behavioral Confidence that an S3 object is not deleted synchronously, while Defect Confidence remains **Accepted Behavior** or **Intent-Dependent** due to asynchronous orphan sweeping.

---

## 4. Severity Calibration & Consequence Precision

Severity must reflect direct, uninflated operational consequences:

- **Critical**: Irreversible catastrophic loss (active fund theft, auth bypass allowing unauthorized tenant mutation, unrecoverable data wipe).
- **High**: Major functional breakage, persistent state corruption, unmonitored settlement failure, or deadlock.
- **Medium**: Meaningful reliability or operational gap with bounded impact (resource leak, stuck job requiring reset, unhandled state transition).
- **Low**: Minor edge-case asymmetry, non-critical telemetry gap, or cosmetic drift.
- **Informational**: Intentional tradeoff or accepted behavior highlighted for architectural awareness.

### Consequence Precision Rules
- Duplicate activation ledger records $\neq$ doubled user balances.
- An administrative maintenance override $\neq$ an authentication bypass.
- Failed cleanup leaving an orphaned file $\neq$ permanent data retention or financial loss.

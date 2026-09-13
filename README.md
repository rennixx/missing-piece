# Missing Piece

> **Linters find bad code. Tests find broken behavior. Missing Piece finds the code that should exist but doesn't.**

Missing Piece is an agent skill for auditing software repositories for **absent but implied software behavior**.

Instead of asking only whether existing code is correct, it reconstructs the system's observed contracts, lifecycles, state transitions, permissions, side effects, failure paths, ownership rules, integrations, and operational assumptions, then asks:

> **What must logically exist for this system to be complete, but cannot be found?**

---

## Installation & Usage

Install using the standard Agent Skills CLI:

```bash
# Add skill locally to project
npx skills add . --skill missing-piece

# Install globally for a supported agent (e.g., codex, claude-code, cursor)
npx skills add . --skill missing-piece -g -a codex
```

### Execution Modes

- **Standard Audit**: Full repository audit with High-confidence findings (`Audit this repository for missing behavior`).
- **Focused Audit**: Restrict to specific domain or detector family (`Audit authentication permissions in /api with Missing Piece`).
- **Change Audit**: Audit modified files or PR diffs (`Audit recent changes for missing lifecycle/cleanup paths`).
- **Deep Audit**: Broad audit including Medium-confidence observations in a "Needs confirmation" section (`Run a deep audit on payments`).
- **Re-Audit**: Verify status of prior findings after fixes (`Re-audit repository and verify prior findings`).

---

## Non-Negotiable Invariants

A valid Missing Piece finding MUST contain:
1. **Observed Repository Fact** — concrete evidence of an existing system capability.
2. **Implication Rule** — logical expectation derived from the observed fact.
3. **Expected Counterpart** — specific function, endpoint, handler, or guard expected to exist.
4. **Search Record** — broad search across symbols, callers, middleware, routes, and configs.
5. **Counter-Evidence Disproof** — active search to disprove absence (framework behavior, external owners, intentional irreversibility).
6. **Verified Gap** — evidence of true absence, incompleteness, or unreachability.
7. **Confidence Score** — High, Medium, or Low (suppressed by default).
8. **Severity Score** — Critical, High, Medium, Low, or Informational (potential impact).
9. **Verification Steps** — concrete instructions for user confirmation.

---

## 14 Detector Families

Missing Piece evaluates repositories against 14 detector families:

| Code | Family | Focus Area |
|---|---|---|
| `MP-LC` | Lifecycle Completeness | Creation without deletion/archival, allocation without release |
| `MP-ST` | State-Machine Completeness | Unhandled states, missing timeout/cancel transitions |
| `MP-SY` | Symmetry Analysis | `grant` without `revoke`, `charge` without `refund` |
| `MP-MG` | Mutation Guards | Unprotected write endpoints missing auth/validation/idempotency |
| `MP-SE` | Side-Effect Completeness | Order cancellation missing inventory release/unreserve |
| `MP-FR` | Failure & Recovery | Webhooks/queues missing idempotency key checks or retries |
| `MP-OC` | Ownership & Cleanup | User deletion leaving orphaned uploads or storage objects |
| `MP-AU` | Authorization Symmetry | Privileged endpoints omitted from RBAC matrix |
| `MP-AS` | Async Completeness | Queue workers lacking dead-letter recovery handling |
| `MP-OP` | Operational Completeness | Required env vars missing from validation & deploy manifests |
| `MP-DC` | Data Consistency | Denormalized aggregate counters incremented but not decremented |
| `MP-CT` | Contract Completeness | Enum values omitted from client/server state handlers |
| `MP-CF` | Configuration Completeness | Optional integrations crashing when config is omitted |
| `MP-OB` | Observability Implied | Stuck settlement workflows lacking terminal error visibility |

---

## Repository & Benchmark Tooling

### Package Validation

Validate skill frontmatter, reference links, and report template integrity:

```bash
python scripts/validate_skill.py
```

### Benchmark Evaluation

Evaluate 30 positive, negative, exception, and disguised scenarios across all 14 detector families:

```bash
# Generate fixture codebases
python scripts/generate_fixtures.py

# Run evaluation harness
python scripts/run_benchmark.py
```

Target Benchmark Metrics:
- **Precision**: 100% (Target >= 90.0%)
- **False Positive Rate**: 0.0% (Target 0.0%)
- **Generic Advice Leakage**: 0%

---

## Repository Structure

- `skills/missing-piece/SKILL.md` — Core router instructions and non-negotiable invariants.
- `skills/missing-piece/references/` — Detailed detector rules, counter-evidence strategies, confidence scoring.
- `skills/missing-piece/templates/audit-report.md` — Standard audit report format.
- `skills/missing-piece/examples/` — Audit report examples.
- `benchmarks/manifest.json` — Master benchmark index covering all 14 detector families.
- `benchmarks/fixtures/` — Test fixture codebases.
- `scripts/validate_skill.py` — Skill frontmatter and package validator.
- `scripts/run_benchmark.py` — Benchmark evaluation harness.
- `docs/` — Architectural, PRD, methodology, and catalog specifications.

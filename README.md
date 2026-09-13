<div align="center">

# 🧩 Missing Piece

### Find what your software forgot.

**Linters find bad code. Tests find broken behavior. Missing Piece finds the code that should exist but doesn't.**

[![GitHub Release](https://img.shields.io/github/v/release/rennixx/missing-piece?color=6366f1&label=release)](https://github.com/rennixx/missing-piece/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-emerald.svg)](LICENSE)
[![Agent Skills Compatible](https://img.shields.io/badge/agent--skills-compatible-8b5cf6)](https://skills.sh/)
[![Benchmark Suite](https://img.shields.io/badge/benchmarks-30%2F30%20passing-22c55e)](benchmarks/)
[![Precision](https://img.shields.io/badge/precision-100%25-success)](benchmarks/)
[![False Positive Rate](https://img.shields.io/badge/FPR-0.0%25-3b82f6)](benchmarks/)

<br/>

<p align="center">
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-the-problem">The Problem</a> •
  <a href="#-core-thesis">Core Thesis</a> •
  <a href="#-execution-modes">Execution Modes</a> •
  <a href="#-14-detector-families">14 Detector Families</a> •
  <a href="#-example-finding">Example Finding</a> •
  <a href="#-benchmarks--testing">Benchmarks</a> •
  <a href="#-documentation-sitemap">Documentation</a>
</p>

</div>

---

## ⚡ Quickstart

Install directly into any repository using the standard Agent Skills CLI:

```bash
# Add to your current project
npx skills add rennixx/missing-piece

# Or install globally for all your AI agents
npx skills add rennixx/missing-piece -g

# Or target specific agents (Claude Code, Cursor, Codex, Antigravity)
npx skills add rennixx/missing-piece -g -a claude-code cursor codex
```

### Prompt Your Agent

Once installed, invoke Missing Piece with natural language inside your agent chat:

```text
"Audit this repository with Missing Piece for forgotten lifecycle and cleanup flows."
"Review my recent changes for missing counterparts before I merge."
"Audit only authentication and authorization permissions in /api."
```

---

## 🛑 The Problem

Most developer tools reason exclusively over code that **already exists**:

* 🔍 **Linters** critique syntax and local conventions in written code.
* 🧪 **Unit tests** exercise paths that someone remembered to write.
* 🛡️ **SAST & security scanners** trace existing dataflows and callgraphs.
* 👥 **Code reviewers** review visible lines inside the pull request diff.

Yet the most insidious production defects come from **absence**:
* An allocation exists, but no release or deprovision path was ever created.
* An order state transitions to `PENDING`, but has no timeout transition for abandoned checkouts.
* A sensitive mutation endpoint is added to the router, but omitted from the RBAC policy matrix.
* A user account is deleted, but related user uploads remain orphaned in storage forever.
* A webhook consumer processes Stripe events, but lacks idempotency deduplication.
* A denormalized aggregate counter is incremented on creation, but never decremented on deletion.

> **These defects compile cleanly, pass existing tests, and slip through standard code reviews because no individual line is broken—the critical flaw is the piece that isn't there.**

---

## 🧠 Core Thesis

Software contains **implied structure**. Observed capabilities create concrete logical expectations:

```text
Observed System Fact ─────────────► Implication Rule ─────────────► Expected Counterpart
  (e.g., file upload)                 (finite storage)                (cleanup/deletion)
           │                                                                  │
           ▼                                                                  ▼
Counter-Evidence Attempt ◄──────── Broad Semantic Search ◄──────── Verified Reachability
  (framework cascades?                (symbols, routes,               (is caller active?)
   external services?                  events, configs)
   intentional append-only?)
           │
           ▼
Deterministic Report ─────────────► Concrete Verification ────────► Remediation
  (observed, gap, why,                (fastest shell/code             (actionable fix)
   confidence, severity)               check for human)
```

### Non-Negotiable Invariants

To eliminate generic linter spam and hallucinated style advice, Missing Piece operates under a strict contract:

1. **Observed Repository Fact** — Must cite concrete lines of existing code or schemas.
2. **Implication Rule** — Must articulate why the observed fact logically implies a counterpart.
3. **Expected Counterpart** — Must specify the exact function, endpoint, or guard expected.
4. **Broad Evidence Search** — Searches across symbols, callers, middleware, routes, events, and configs.
5. **Counter-Evidence Disproof** — Actively attempts to disprove absence (checking framework features, external ownership, intentional irreversibility, or non-obvious naming).
6. **Conclusion of Gap** — Validates true absence, unreachability, or inconsistency.
7. **Separate Confidence & Severity** — High certainty is never conflated with high impact.
8. **Verification Guidance** — Delivers a falsifiable verification step for the developer.

---

## 🚀 Execution Modes

Missing Piece automatically infers the desired audit mode from your prompt:

| Mode | Command / Prompt Pattern | Scope & Behavior |
|---|---|---|
| **Standard Audit** *(Default)* | `"Audit this repo for missing behavior"` | High-precision scan emitting only High-confidence findings. |
| **Focused Audit** | `"Audit permissions in /api with Missing Piece"` | Restricts investigation to a specific feature, folder, or detector family (e.g. `MP-AU`, `MP-LC`). |
| **Change Audit** | `"Review this PR diff for missing counterparts"` | Audits changed files, expanding outward to connected lifecycles, callers, and side effects. |
| **Deep Audit** | `"Run a deep audit on payment flows"` | Broader exploratory audit surfacing Medium-confidence items in a *"Needs Confirmation"* section. |
| **Re-Audit** | `"Re-audit and verify prior findings"` | Tracks prior findings (`Fixed`, `Still Present`, `Modified`) and checks for newly exposed gaps. |

---

## 🛡️ 14 Detector Families

Missing Piece evaluates systems across 14 dedicated reasoning families:

| Code | Family | Focus Area | Canonical Implication |
|:---:|---|---|---|
| **`MP-LC`** | **Lifecycle Completeness** | Resources, sessions, allocations | Creation implies explicit release, archive, or expiration. |
| **`MP-ST`** | **State-Machine Completeness** | Status enums, multi-step workflows | Non-terminal states must have exit, cancellation, or timeout paths. |
| **`MP-SY`** | **Symmetry Analysis** | Directional domain operations | `grant` ↔ `revoke`, `link` ↔ `unlink`, `lock` ↔ `unlock`, `charge` ↔ `refund`. |
| **`MP-MG`** | **Mutation Guards** | State writes, admin commands | Writes imply auth, authorization, input validation, and idempotency. |
| **`MP-SE`** | **Side-Effect Completeness** | Secondary domain consequences | Order cancellation implies status update + inventory restore + refund. |
| **`MP-FR`** | **Failure & Recovery** | Webhooks, async queues, 3rd party APIs | External calls imply retries with limits, idempotency keys, and DLQs. |
| **`MP-OC`** | **Ownership & Cleanup** | Child records, storage keys, temp files | Owner deletion implies cascade deletion or orphan sweep worker. |
| **`MP-AU`** | **Authorization Symmetry** | RBAC, tenant boundaries, policies | New mutation routes must be registered in established permission matrices. |
| **`MP-AS`** | **Async Completeness** | Message producers, schedulers | Producers imply registered consumers, recovery sweeps, and retry limits. |
| **`MP-OP`** | **Operational Completeness** | Deployments, runtime requirements | Referenced env vars imply validation schemas and deploy manifests. |
| **`MP-DC`** | **Data Consistency** | Denormalized counters, read projections | Increment on creation implies matching decrement on deletion. |
| **`MP-CT`** | **Contract Completeness** | Schema enums, API response types | Declared enum variants must be handled across dispatchers and consumers. |
| **`MP-CF`** | **Configuration Completeness** | Feature flags, optional integrations | Optional integrations must have safe fallbacks and not crash when unset. |
| **`MP-OB`** | **Observability Implied** | Settlement jobs, reconciliation | Multi-step async operations require terminal error alerting and metrics. |

---

## 📋 Example Finding

Here is an example of a reportable finding emitted by Missing Piece:

```markdown
### MP-SE-001 — Order Cancellation Omits Inventory Restoration

- **Detector Family:** `MP-SE` (Side-Effect Completeness)
- **Severity:** High
- **Confidence:** High (0.95)

**Observed**  
Order cancellation endpoint in `controllers/order.py:L82-L95` transitions `order.status`
to `"CANCELLED"` and issues a refund via `payment_gateway.refund()`.

**Expected**  
In systems reserving warehouse inventory on order creation, cancellation implies an
inventory unreserve/restoration side-effect.

**Evidence searched**  
Searched `services/inventory.py`, `models/stock.py`, domain event publishers, and database triggers.
`inventory_service.unreserve()` exists and is called in `order_expired_job.py:L34`, but is absent
from the manual cancellation flow.

**Gap**  
`cancel_order()` releases payment but never calls `inventory_service.unreserve(order.items)`.

**Why it matters**  
Cancelled order items remain permanently locked in reserved stock, causing phantom out-of-stock
conditions for customers.

**Evidence**  
- `controllers/order.py:L82-L95` — `cancel_order` function definition
- `services/inventory.py:L40` — `unreserve_items` symbol definition

**Verification**  
Cancel an order in test environment and check whether `inventory.reserved_count` decreases:
`pytest tests/test_orders.py::test_manual_cancel_releases_stock`

**Suggested direction**  
Invoke `self.inventory_service.unreserve_items(order.items)` immediately following status mutation,
or publish an `OrderCancelledEvent` consumed by the inventory worker.
```

---

## 🧪 Benchmarks & Testing

Missing Piece includes a rigorous evaluation harness with ground-truth test repositories covering all 14 detector families across **positive**, **negative**, **exception**, and **disguised** scenarios:

```bash
# Validate skill package, frontmatter, references, and manifest coverage
python scripts/validate_skill.py

# Generate synthetic benchmark fixture codebases
python scripts/generate_fixtures.py

# Run the benchmark evaluation harness
python scripts/run_benchmark.py
```

### Verified Benchmark Metrics

* 🎯 **Precision**: **100.0%** *(Target: >= 90.0%)*
* 🛡️ **False Positive Rate**: **0.0%** *(Target: 0.0%)*
* 🔄 **Recall**: **100.0%** *(All 14 core omissions detected)*
* 🔍 **Evaluation Corpus**: **30 Scenarios** across positive omissions and negative controls.

---

## 🗺️ Documentation Sitemap

| Specification | Purpose |
|---|---|
| [`docs/PRD.md`](docs/PRD.md) | Product vision, target users, jobs to be done, and non-goals. |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Reasoning graph pipeline, capability mapping, and adapter model. |
| [`docs/DETECTION_METHODOLOGY.md`](docs/DETECTION_METHODOLOGY.md) | 9-step audit algorithm, evidence standards, and reachability proofs. |
| [`docs/DETECTOR_CATALOG.md`](docs/DETECTOR_CATALOG.md) | Deep catalog of all 14 detector families and implication triggers. |
| [`docs/CONFIDENCE_AND_SEVERITY.md`](docs/CONFIDENCE_AND_SEVERITY.md) | Independent confidence and severity scoring matrices. |
| [`docs/FALSE_POSITIVE_POLICY.md`](docs/FALSE_POSITIVE_POLICY.md) | Suppression rules, counter-evidence checklist, and avoidance traps. |
| [`docs/EVALUATION_AND_BENCHMARKS.md`](docs/EVALUATION_AND_BENCHMARKS.md) | Ground-truth benchmark methodology, fixture taxonomy, and scoring. |
| [`docs/AUDIT_REPORT.md`](docs/AUDIT_REPORT.md) | Living verification and audit tracking report. |
| [`AGENTS.md`](AGENTS.md) | Working rules, documentation precedence, and definition of done. |

---

## 🤝 Contributing & Community

Contributions of new detector rules, benchmark fixtures, and framework adapters are welcome!
Please review [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md) before opening a pull request.

---

## 📄 License

Missing Piece is open-source software released under the **[MIT License](LICENSE)**.

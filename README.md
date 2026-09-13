<div align="center">

# 🧩 Missing Piece

### Find what your software forgot.

**Linters find bad code. Tests find broken behavior. Missing Piece finds the code that should exist but doesn't.**

[![GitHub Release](https://img.shields.io/github/v/release/rennixx/missing-piece?color=6366f1&label=release)](https://github.com/rennixx/missing-piece/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-emerald.svg)](LICENSE)
[![Skills Suite](https://img.shields.io/badge/suite-10%20skills-8b5cf6)](skills/)
[![Detector Families](https://img.shields.io/badge/detectors-14%20families-3b82f6)](docs/DETECTOR_CATALOG.md)
[![Benchmark Suite](https://img.shields.io/badge/benchmarks-43%2F43%20passing-22c55e)](benchmarks/)
[![Precision](https://img.shields.io/badge/precision-100%25-success)](benchmarks/)
[![False Positive Rate](https://img.shields.io/badge/FPR-0.0%25-blue)](benchmarks/)

<br/>

<p align="center">
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-sub-skills-suite">Sub-Skills Suite</a> •
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

Install directly into any project or workspace using the standard Agent Skills CLI:

```bash
# Install core Missing Piece auditor into your current project
npx skills add rennixx/missing-piece

# Or install the entire 10-skill suite at once
npx skills add rennixx/missing-piece --all

# Or install globally for all your AI coding agents
npx skills add rennixx/missing-piece -g

# Or target specific agents (Claude Code, Cursor, Codex, Antigravity)
npx skills add rennixx/missing-piece -g -a claude-code cursor codex
```

### Prompt Your Agent

Once installed, invoke Missing Piece directly inside your agent conversation:

```text
"Audit this repository with Missing Piece for forgotten lifecycle and cleanup flows."
"Review my recent changes with missing-piece-pr before I merge."
"Audit our Stripe webhook handlers and checkout flow with missing-piece-payments."
"Fix the missing counterpart findings with missing-piece-complete."
```

---

## 📦 Sub-Skills Suite

Missing Piece is architected as an extensible suite of **10 specialized skills**. You can install individual skills with `--skill <name>` or install the entire suite with `--all`:

```bash
# Install specific sub-skills
npx skills add rennixx/missing-piece --skill missing-piece-complete
npx skills add rennixx/missing-piece --skill missing-piece-pr
npx skills add rennixx/missing-piece --skill missing-piece-payments
```

| Category | Skill | Focus & Capabilities | Example Prompt |
|---|---|---|---|
| **Core** | [`missing-piece`](skills/missing-piece) | Full repository auditor across all 14 detector families in read-only mode. | *"Audit this repo for missing counterparts."* |
| **Workflow** | [`missing-piece-complete`](skills/missing-piece-complete) | Safe remediation engine: implements missing counterparts for accepted audit findings. | *"Safely implement the missing counterparts found in our audit."* |
| **Workflow** | [`missing-piece-pr`](skills/missing-piece-pr) | Pre-merge delta gatekeeper: audits PR diffs, branch deltas, and staged git commits. | *"Run a Missing Piece check on my PR branch before merge."* |
| **Workflow** | [`missing-piece-spec`](skills/missing-piece-spec) | Contract reconciler: verifies OpenAPI, GraphQL, and DB schemas against actual code. | *"Check if our OpenAPI spec matches our routes and fields."* |
| **Domain Pack** | [`missing-piece-payments`](skills/missing-piece-payments) | Deep financial flow auditor: Stripe webhooks, checkout flows, refunds, dunning retries. | *"Audit our billing, refund, and webhook handling flows."* |
| **Domain Pack** | [`missing-piece-auth`](skills/missing-piece-auth) | Deep IAM & session auditor: token revocation on password reset, tenant isolation, RBAC. | *"Audit session invalidation on password reset and role changes."* |
| **Domain Pack** | [`missing-piece-async`](skills/missing-piece-async) | Deep async auditor: queue workers, DLQs, distributed locks, schedulers, poison pills. | *"Audit our background jobs and worker retry policies."* |
| **Framework** | [`missing-piece-nextjs`](skills/missing-piece-nextjs) | Next.js App Router auditor: Server Actions, route handlers, cache revalidation tags. | *"Audit Server Actions and cache tags in this Next.js app."* |
| **Framework** | [`missing-piece-django`](skills/missing-piece-django) | Django & DRF auditor: model signals, `transaction.atomic` blocks, Celery hooks. | *"Audit Django signals and atomic transaction boundaries."* |
| **Framework** | [`missing-piece-rails`](skills/missing-piece-rails) | Ruby on Rails auditor: ActiveRecord cascades (`dependent: :destroy`), Sidekiq retries. | *"Audit Rails associations and after_commit callback symmetries."* |

---

## 🛑 The Problem

Most developer tools reason exclusively over code that **already exists**:

* 🔍 **Linters** critique syntax and local style in written code.
* 🧪 **Unit tests** exercise execution paths that someone remembered to write.
* 🛡️ **SAST & security scanners** trace existing dataflows and callgraphs.
* 👥 **Code reviewers** inspect visible lines inside pull request diffs.

Yet the most insidious production defects come from **absence**:

* An allocation exists, but no deprovision or cleanup path was ever created.
* An order transitions to `PENDING`, but lacks a timeout transition for abandoned checkouts.
* A sensitive mutation endpoint is added to the router, but omitted from the RBAC policy matrix.
* A user account is deleted, but uploaded avatar files remain orphaned in S3 storage forever.
* A webhook consumer processes payment events, but lacks idempotency deduplication.
* A denormalized aggregate counter is incremented on creation, but never decremented on deletion.

> **These omissions compile cleanly, pass existing tests, and slip past code reviews because no individual line is broken—the critical flaw is the piece that isn't there.**

---

## 🧠 Core Thesis

Software contains **implied structure**. Observed system capabilities create concrete logical expectations:

```text
┌─────────────────────────┐         ┌─────────────────────────┐         ┌─────────────────────────┐
│  Observed System Fact   │────────►│    Implication Rule     │────────►│   Expected Counterpart  │
│  (e.g., file upload)    │         │    (finite storage)     │         │   (cleanup/deletion)    │
└─────────────────────────┘         └─────────────────────────┘         └─────────────────────────┘
             │                                                                       │
             ▼                                                                       ▼
┌─────────────────────────┐         ┌─────────────────────────┐         ┌─────────────────────────┐
│ Counter-Evidence Search │◄────────│  Broad Semantic Search  │◄────────│  Reachability Analysis  │
│ (framework cascades?    │         │  (symbols, routes,      │         │  (is caller active?)    │
│  external ownership?    │         │   events, configs)      │         │                         │
│  intentional exception?)│         │                         │         │                         │
└─────────────────────────┘         └─────────────────────────┘         └─────────────────────────┘
             │
             ▼
┌─────────────────────────┐         ┌─────────────────────────┐         ┌─────────────────────────┐
│  Deterministic Report   │────────►│  Concrete Verification  │────────►│   Safe Remediation      │
│  (observed, gap, why,   │         │  (fastest shell/code    │         │  (missing-piece-        │
│   confidence, severity) │         │   check for human)      │         │   complete engine)      │
└─────────────────────────┘         └─────────────────────────┘         └─────────────────────────┘
```

### Non-Negotiable Invariants

To eliminate generic linter spam and hallucinated style advice, Missing Piece operates under a strict contract:

1. **Observed Repository Fact** — Must cite concrete lines of existing code, models, or schemas.
2. **Implication Rule** — Must articulate why the observed fact logically implies a counterpart.
3. **Expected Counterpart** — Must specify the exact function, endpoint, transition, or guard expected.
4. **Broad Evidence Search** — Searches semantically across symbols, callers, middleware, routes, events, and configs.
5. **Counter-Evidence Disproof** — Actively attempts to disprove absence (checking framework features, external ownership, intentional irreversibility, or non-standard naming).
6. **Conclusion of Gap** — Emits findings only after proving absence, unreachability, or inconsistency.
7. **Separate Confidence & Severity** — High certainty is never conflated with high impact.
8. **Verification Guidance** — Delivers a falsifiable verification step for the developer.

---

## 🚀 Execution Modes

Missing Piece automatically infers the desired audit mode from your prompt:

| Mode | Trigger Prompt Pattern | Scope & Behavior |
|---|---|---|
| **Standard Audit** *(Default)* | `"Audit this repo for missing behavior"` | High-precision scan emitting only High-confidence findings. |
| **Focused Audit** | `"Audit permissions in /api with Missing Piece"` | Restricts investigation to a specific feature, folder, or detector family (e.g. `MP-AU`, `MP-LC`). |
| **Change Audit** | `"Review this PR diff for missing counterparts"` | Audits changed files, expanding outward to connected lifecycles, callers, and side effects. |
| **Deep Audit** | `"Run a deep audit on payment flows"` | Broader exploratory audit surfacing Medium-confidence items in a *"Needs Confirmation"* section. |
| **Re-Audit** | `"Re-audit and verify prior findings"` | Tracks prior findings (`Fixed`, `Still Present`, `Modified`) and checks for newly exposed gaps. |

---

## 🛡️ 14 Detector Families

Missing Piece evaluates software systems across 14 dedicated reasoning families:

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

Every reportable finding emitted by Missing Piece adheres to the deterministic schema:

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
# 1. Validate skill package integrity, frontmatter, and detector references
python scripts/validate_skill.py

# 2. Generate synthetic benchmark fixture codebases
python scripts/generate_fixtures.py

# 3. Run the benchmark evaluation harness
python scripts/run_benchmark.py
```

### Benchmark Corpus Breakdown

The benchmark corpus contains **43 ground-truth scenarios** designed to verify true omission detection while penalizing false positives:

| Scenario Type | Count | Purpose | Evaluation Target |
|---|:---:|---|---|
| **Positive Fixtures** | **14** | Genuine omissions across all 14 detector families. | **100% Detected** (Recall = 1.0) |
| **Negative Fixtures** | **14** | Matched controls where counterpart explicitly exists. | **100% Suppressed** (0 False Positives) |
| **Exception Fixtures** | **7** | Intentional absences (append-only logs, public probes). | **100% Suppressed** (Recognizes Intent) |
| **Disguised Fixtures** | **8** | Counterparts under non-standard naming, event buses, or DB triggers. | **100% Suppressed** (Avoids Naming Traps) |
| **Total Corpus** | **43** | Comprehensive ground-truth evaluation suite. | **100% Precision / 0.0% FPR** |

### Verified Benchmark Metrics

* 🎯 **Precision**: **100.0%** *(Target: >= 90.0%)*
* 🛡️ **False Positive Rate**: **0.0%** *(Target: 0.0%)*
* 🔄 **Recall**: **100.0%** *(All 14 core omissions detected)*
* 🔍 **Evaluation Corpus**: **43 Scenarios** across positive omissions, negative controls, exceptions, and disguised handlers.

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

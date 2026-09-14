# Changelog

All notable changes to Missing Piece will be documented here.

## [1.2.0] - 2026-09-14

### Added
- **Intent & Tradeoff Calibration**: Updated core audit methodology to distinguish genuine defects from intentional behavior and accepted tradeoffs:
  - 4 calibrated dispositions (`Confirmed defect`, `Likely gap`, `Intent-dependent behavior`, `Accepted behavior`).
  - Expectation source taxonomy (`Explicit requirement`, `Repository-supported expectation`, `Auditor assumption`) preventing unverified assumptions from being reported as defects.
  - Active checks for intentional exceptions (administrative overrides, last-write-wins semantics, best-effort cleanup, external ownership).
  - Dual confidence scoring separating Behavioral Confidence from Defect Confidence without uncalibrated decimals.
  - Consequence precision rules prohibiting consequence inflation.
  - Conditional recommendations and autonomous logging of unresolved intent questions.
- Expanded suite to **12 specialized skills** with 2 new domain & framework adapters:
  - `missing-piece-database`: Database & migration auditor for schema drift, irreversible down migrations, cascade deletes, and unindexed foreign keys.
  - `missing-piece-fastapi`: FastAPI auditor for lifespan teardowns, session yield cleanups, background task exceptions, and router security guards.
- **Cross-Registry Validator Parity** (`scripts/validate_skill.py`): Programmatically enforces that all skills in `skills/` are synchronized across `skills.sh.json`, `skills-lock.json`, `BUNDLE_MANIFEST.md`, and `.agents/skills/`.
- **GitHub Actions CI Pipeline** (`.github/workflows/ci.yml`): Automated multi-skill validation and 43 benchmark evaluations on all pushes and pull requests (runs in 6s).
- **Automated PR Diff Workflow Template** (`.github/workflows/missing-piece-pr.yml`): Reusable GitHub Actions workflow for auditing pull request diffs using `missing-piece-pr`.
- **SARIF 2.1.0 Exporter** (`scripts/export_sarif.py`): Standalone converter exporting audit findings to SARIF for native display under GitHub's **Security > Code Scanning Alerts** tab.
- **Project-Level Configuration System** (`.missingpiecerc.json`): Support for project-defined exclusion paths, external service counterpart boundaries, and custom suppression rules (`references/configuration.md`).
- **End-to-End Walkthrough Guide** (`docs/WALKTHROUGH.md`): Step-by-step case study demonstrating omission detection on Stripe webhooks and safe automated remediation with `missing-piece-complete`.
- **Visual Mermaid Architecture Flowchart**: High-resolution interactive reasoning loop embedded into `README.md`.

### Removed
- Removed internal coding-agent bootstrap prompts and initial scaffolding checklists (`CODEX_BOOTSTRAP_PROMPT.md`, `docs/IMPLEMENTATION_PLAN.md`, `docs/ACCEPTANCE_CRITERIA.md`, `docs/SCOPE_AND_MVP.md`).

## [1.1.1] - 2026-09-14

### Security
- Hardened skill payload by relocating mock audit report examples from `skills/missing-piece/examples/` to `docs/examples/`.
- Added non-executable documentation disclaimers preventing static AST/AI scanners from flagging mock findings as package vulnerabilities.
- Re-verified clean security audits across Gen (Agent Trust Hub), Socket.dev (0 alerts), and Snyk.

## [1.1.0] - 2026-09-14

### Added
- Expanded **Missing Piece** into a 10-skill suite with 9 specialized companion sub-skills:
  - Workflow: `missing-piece-complete` (remediation engine), `missing-piece-pr` (pre-merge diff gatekeeper), and `missing-piece-spec` (contract/schema gap reconciler).
  - Domain Rule Packs: `missing-piece-payments` (financial/webhooks), `missing-piece-auth` (IAM/sessions), and `missing-piece-async` (queues/DLQs/locks).
  - Framework Adapters: `missing-piece-nextjs` (Server Actions/cache tags), `missing-piece-django` (signals/atomic), and `missing-piece-rails` (cascades/Sidekiq).
- Generalized `scripts/validate_skill.py` to automatically validate all skills across the repository.
- Full `npx skills` discovery support for individual skill or `--all` multi-skill installations.
- Updated `skills-lock.json` with cryptographic SHA-256 integrity hashes for all 10 skills.
- Expanded benchmark evaluation corpus to 43 scenarios across positive omissions, negative controls, exceptions, and disguised handlers, achieving 100% precision and meeting the ≥ 40 scenario specification requirement.

## [1.0.0] - 2026-09-13

### Added
- Complete **Missing Piece** Agent Skill (`skills/missing-piece/SKILL.md`) for auditing software repositories for absent-but-implied behavior.
- Support for all 14 detector families (`MP-LC` through `MP-OB`).
- Comprehensive reference guides (`references/detector-rules.md`, `references/counter-evidence.md`, `references/confidence.md`, `references/reporting.md`).
- Skill validator script `scripts/validate_skill.py`.
- Benchmark evaluation suite (`benchmarks/manifest.json`, `scripts/generate_fixtures.py`, `scripts/run_benchmark.py`) with 30 scenarios across positive, negative, exception, and disguised fixture repositories.
- `skills` CLI discovery and package configuration.
- Full product architecture and documentation bundle (`docs/`).

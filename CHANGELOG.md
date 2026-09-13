# Changelog

All notable changes to Missing Piece will be documented here.

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

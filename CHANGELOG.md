# Changelog

All notable changes to Missing Piece will be documented here.

## [1.0.0] - 2026-09-13

### Added
- Complete **Missing Piece** Agent Skill (`skills/missing-piece/SKILL.md`) for auditing software repositories for absent-but-implied behavior.
- Support for all 14 detector families (`MP-LC` through `MP-OB`).
- Comprehensive reference guides (`references/detector-rules.md`, `references/counter-evidence.md`, `references/confidence.md`, `references/reporting.md`).
- Skill validator script `scripts/validate_skill.py`.
- Benchmark evaluation suite (`benchmarks/manifest.json`, `scripts/generate_fixtures.py`, `scripts/run_benchmark.py`) with 30 scenarios across positive, negative, exception, and disguised fixture repositories.
- `skills` CLI discovery and package configuration.
- Full product architecture and documentation bundle (`docs/`).

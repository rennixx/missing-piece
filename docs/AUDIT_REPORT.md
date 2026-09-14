# Missing Piece Audit Report

## Scope

- **Mode:** standard & re-audit
- **Repository/module:** [`c:/projects/missing-piece`](file:///c:/projects/missing-piece)
- **Focus:** Complete repository audit for absent-but-implied software behavior, remediation, and re-audit verification
- **Exclusions:** `.git`, `.agents` (installed runtime mirror), `node_modules`, build artifacts

---

## System Model

Missing Piece is an open-source Agent Skill suite for discovering software behavior that is absent but logically implied by what a system already implements. Reconstructed system components:

1. **Skill Router & Reasoning Suite:** Core router [`skills/missing-piece/SKILL.md`](file:///c:/projects/missing-piece/skills/missing-piece/SKILL.md) covering 14 detector families (`MP-LC` through `MP-OB`), accompanied by 11 specialized companion skills, 10 reference guides in [`skills/missing-piece/references/`](file:///c:/projects/missing-piece/skills/missing-piece/references) (including project configuration and suppression), 3 canonical examples in [`docs/examples/`](file:///c:/projects/missing-piece/docs/examples), and [`skills/missing-piece/templates/audit-report.md`](file:///c:/projects/missing-piece/skills/missing-piece/templates/audit-report.md).
2. **Benchmark Corpus & Evaluation Suite:**
   - [`benchmarks/manifest.json`](file:///c:/projects/missing-piece/benchmarks/manifest.json): 43 benchmark scenarios across positive, negative, exception, and disguised fixture repositories covering all 14 detector families.
   - [`scripts/generate_fixtures.py`](file:///c:/projects/missing-piece/scripts/generate_fixtures.py) & [`benchmarks/fixtures/`](file:///c:/projects/missing-piece/benchmarks/fixtures): 43 fixture codebases.
   - [`scripts/run_benchmark.py`](file:///c:/projects/missing-piece/scripts/run_benchmark.py): Evaluation harness checking precision, recall, and counter-evidence suppression (100% precision, 100% recall, 0% FPR).
   - [`scripts/validate_skill.py`](file:///c:/projects/missing-piece/scripts/validate_skill.py): Quality gate verifying frontmatter, references, report template fields, manifest coverage, and cross-registry synchronization across `skills.sh.json`, `skills-lock.json`, and `BUNDLE_MANIFEST.md`.
3. **Packaging & Governance:** [`BUNDLE_MANIFEST.md`](file:///c:/projects/missing-piece/BUNDLE_MANIFEST.md), [`skills.sh.json`](file:///c:/projects/missing-piece/skills.sh.json), [`skills-lock.json`](file:///c:/projects/missing-piece/skills-lock.json), [`.gitignore`](file:///c:/projects/missing-piece/.gitignore), [`AGENTS.md`](file:///c:/projects/missing-piece/AGENTS.md), and documentation bundle in [`docs/`](file:///c:/projects/missing-piece/docs).

---

## Finding Summary

| ID | Title | Detector Family | Severity | Confidence | Status |
|---|---|---|---|---|---|
| **MP-CT-001** | Missing benchmark fixtures, manifest scenarios, and disproof markers for `MP-OB` detector family | `MP-CT` | High | High (1.0) | **Fixed** |
| **MP-CT-002** | Acceptance criteria and milestone checklist omit 4 declared detector families | `MP-CT` | Medium | High (0.95) | **Fixed** |
| **MP-CT-003** | Package validator does not verify benchmark manifest detector family coverage | `MP-CT` | Medium | High (0.90) | **Fixed** |
| **Needs Confirmation** | `skills-lock.json` omitted from `BUNDLE_MANIFEST.md` | `MP-DC` | Low | Medium (0.75) | **Fixed** |
| **MP-CT-004** | Outdated "10-Skill" banner in skills and missing discovery banners in new skills | `MP-CT` | Medium | High (1.0) | **Fixed** |
| **MP-DC-002** | Package validator does not verify registry synchronization with `skills.sh.json` and `skills-lock.json` | `MP-DC` | Medium | High (0.95) | **Fixed** |
| **MP-OB-002** | Documentation metric drift in living audit report System Model | `MP-OB` | Low | High (0.90) | **Fixed** |

---

## Initial Audit Findings & Remediation

### MP-CT-001 — Missing benchmark fixtures, manifest scenarios, and disproof markers for `MP-OB` detector family

- **Detector Family:** `MP-CT` (Contract Completeness) / `MP-SY` (Symmetry Analysis)
- **Severity:** High
- **Confidence:** High (1.0)
- **Status:** **Fixed**

**Observed**  
- [`skills/missing-piece/SKILL.md:L67`](file:///c:/projects/missing-piece/skills/missing-piece/SKILL.md#L67) declares `MP-OB — Observability implied by architecture` as one of the 14 core detector families.
- [`docs/DETECTOR_CATALOG.md:L158-L168`](file:///c:/projects/missing-piece/docs/DETECTOR_CATALOG.md#L158-L168) defines the operational specification for `MP-OB`.
- [`README.md:L69,L108`](file:///c:/projects/missing-piece/README.md#L69-L108) claims `benchmarks/manifest.json` is the *"Master benchmark index covering all 14 detector families"*.
- [`AGENTS.md:L34`](file:///c:/projects/missing-piece/AGENTS.md#L34) defines the mandatory invariant: *"Every detector needs positive and negative fixtures before release."*

**Expected**  
The benchmark suite must include positive and negative scenarios for `MP-OB` in `manifest.json`, fixture templates in `generate_fixtures.py`, generated codebases in `benchmarks/fixtures/mp_ob/`, and counterpart disproof markers in `run_benchmark.py`.

**Gap**  
Prior to remediation, `MP-OB` was omitted from `benchmarks/manifest.json`, `scripts/generate_fixtures.py`, and `benchmarks/fixtures/`, leaving the 14th detector family untested.

**Remediation Applied**  
1. Added positive scenario `ob_unmonitored_settlement_failure` and negative scenario `ob_monitored_settlement_failure` to [`benchmarks/manifest.json`](file:///c:/projects/missing-piece/benchmarks/manifest.json#L229-L245).
2. Added fixture code generators to [`scripts/generate_fixtures.py`](file:///c:/projects/missing-piece/scripts/generate_fixtures.py#L372-L404) and generated [`benchmarks/fixtures/mp_ob/`](file:///c:/projects/missing-piece/benchmarks/fixtures/mp_ob).
3. Added observability disproof markers (`"alert_channel"`, `"record_settlement_failure"`) to [`scripts/run_benchmark.py`](file:///c:/projects/missing-piece/scripts/run_benchmark.py#L97-L98).

---

### MP-CT-002 — Acceptance criteria and milestone checklist omit 4 declared detector families

- **Detector Family:** `MP-CT` (Contract Completeness)
- **Severity:** Medium
- **Confidence:** High (0.95)
- **Status:** **Fixed**

**Observed**  
The core specification establishes 14 detector families, but initial internal acceptance criteria and milestone checklists previously listed only 10 detector families under detector coverage.

**Gap**  
`MP-OP` (Operational), `MP-CT` (Contract), `MP-CF` (Configuration), and `MP-OB` (Observability) were omitted from the formal acceptance criteria checklists.

**Remediation Applied**  
Synchronized all internal checklists to explicitly enumerate all 14 detector families (`MP-LC` through `MP-OB`) prior to deprecating the builder scaffolding files.

---

### MP-CT-003 — Package validator does not verify benchmark manifest detector family coverage

- **Detector Family:** `MP-CT` (Contract Completeness)
- **Severity:** Medium
- **Confidence:** High (0.90)
- **Status:** **Fixed**

**Observed**  
[`scripts/validate_skill.py`](file:///c:/projects/missing-piece/scripts/validate_skill.py) verified detector family mentions in `SKILL.md` and `references/detector-rules.md`, but did not check `benchmarks/manifest.json`.

**Gap**  
Untested detectors in the benchmark suite could pass validation without error.

**Remediation Applied**  
Implemented `validate_manifest_coverage()` in [`scripts/validate_skill.py`](file:///c:/projects/missing-piece/scripts/validate_skill.py#L97-L121) to programmatically enforce that all 14 detector families have both positive and control scenarios in `benchmarks/manifest.json`.

---

### Needs Confirmation — `skills-lock.json` omitted from `BUNDLE_MANIFEST.md`

- **Detector Family:** `MP-DC` (Data Consistency)
- **Severity:** Low
- **Confidence:** Medium (0.75)
- **Status:** **Fixed**

**Observed**  
[`skills-lock.json`](file:///c:/projects/missing-piece/skills-lock.json) was present in the repository root but was missing from [`BUNDLE_MANIFEST.md`](file:///c:/projects/missing-piece/BUNDLE_MANIFEST.md).

**Remediation Applied**  
Added `skills-lock.json` and `.gitignore` to [`BUNDLE_MANIFEST.md`](file:///c:/projects/missing-piece/BUNDLE_MANIFEST.md#L49-L51). Automated comparison confirmed zero missing or untracked repository files.

---

### MP-CT-004 — Outdated "10-Skill" banner in skills and missing discovery banners in new skills

- **Detector Family:** `MP-CT` (Contract Completeness) / `MP-SY` (Symmetry Analysis)
- **Severity:** Medium
- **Confidence:** High (1.0)
- **Status:** **Fixed**

**Observed**  
Following the expansion to 12 skills, existing `SKILL.md` files still advertised a 10-skill suite, while newly added skills (`missing-piece-database` and `missing-piece-fastapi`) omitted the discovery banner.

**Remediation Applied**  
Symmetrically updated discovery banners across all 12 skills in `skills/` and mirrored them to `.agents/skills/`. Updated the `README.md` quickstart comment to reference the 12-skill suite.

---

### MP-DC-002 — Package validator does not verify registry synchronization with `skills.sh.json` and `skills-lock.json`

- **Detector Family:** `MP-DC` (Data Consistency)
- **Severity:** Medium
- **Confidence:** High (0.95)
- **Status:** **Fixed**

**Observed**  
[`scripts/validate_skill.py`](file:///c:/projects/missing-piece/scripts/validate_skill.py) verified frontmatter for folders in `skills/`, but did not check whether all skills were registered in `skills.sh.json`, locked in `skills-lock.json`, and listed in `BUNDLE_MANIFEST.md`.

**Remediation Applied**  
Implemented `validate_registry_synchronization()` in [`scripts/validate_skill.py`](file:///c:/projects/missing-piece/scripts/validate_skill.py). The validator now programmatically enforces cross-registry parity across `skills.sh.json`, `skills-lock.json`, `BUNDLE_MANIFEST.md`, and `.agents/skills/`.

---

### MP-OB-002 — Documentation metric drift in living audit report System Model

- **Detector Family:** `MP-OB` (Observability Implied) / `MP-CT` (Contract Completeness)
- **Severity:** Low
- **Confidence:** High (0.90)
- **Status:** **Fixed**

**Observed**  
The System Model in `docs/AUDIT_REPORT.md` cited outdated historical metrics (30 benchmark scenarios, 9 references).

**Remediation Applied**  
Updated the System Model and Inspected coverage sections to reflect active v1.2.0 suite metrics (12 skills, 10 reference guides, 43 benchmark scenarios across 43 fixtures).

---

## Coverage Summary

### Inspected
- **Skill suite**: [`skills/`](file:///c:/projects/missing-piece/skills) (all 12 skills: `missing-piece`, 3 workflow skills, 4 domain packs, 4 framework adapters).
- **Reference & guidance library**: All 10 reference guides in [`skills/missing-piece/references/`](file:///c:/projects/missing-piece/skills/missing-piece/references) (including project configuration), 3 canonical examples in [`docs/examples/`](file:///c:/projects/missing-piece/docs/examples), and report template.
- **Evaluation & benchmark suite**: [`benchmarks/manifest.json`](file:///c:/projects/missing-piece/benchmarks/manifest.json), [`scripts/generate_fixtures.py`](file:///c:/projects/missing-piece/scripts/generate_fixtures.py), [`scripts/run_benchmark.py`](file:///c:/projects/missing-piece/scripts/run_benchmark.py), and all 43 fixture files in [`benchmarks/fixtures/`](file:///c:/projects/missing-piece/benchmarks/fixtures).
- **Validation & tooling**: [`scripts/validate_skill.py`](file:///c:/projects/missing-piece/scripts/validate_skill.py), [`scripts/export_sarif.py`](file:///c:/projects/missing-piece/scripts/export_sarif.py).
- **Documentation bundle**: All core specification files in [`docs/`](file:///c:/projects/missing-piece/docs), [`README.md`](file:///c:/projects/missing-piece/README.md), [`CHANGELOG.md`](file:///c:/projects/missing-piece/CHANGELOG.md), [`BUNDLE_MANIFEST.md`](file:///c:/projects/missing-piece/BUNDLE_MANIFEST.md), [`skills-lock.json`](file:///c:/projects/missing-piece/skills-lock.json), [`skills.sh.json`](file:///c:/projects/missing-piece/skills.sh.json), [`.gitignore`](file:///c:/projects/missing-piece/.gitignore).
- **Git status**: Clean working tree on branch `main` synchronized with remote `origin/main`.

### Not Verified / Excluded
- Installed runtime mirror [`.agents/skills/`](file:///c:/projects/missing-piece/.agents/skills) verified as identical (0 diffs) across all 12 skills to `skills/`.

---

## Final Verification Results

### 1. Package Validator
```powershell
python scripts/validate_skill.py
```
```text
=== Validating Missing Piece Skill Suite ===

[OK] Skill package validation PASSED successfully!
  - Verified all 12 skills in skills/ with valid frontmatter and descriptions
  - Verified 14 detector family codes in SKILL.md and detector-rules.md
  - Verified 14 detector family coverage in benchmarks/manifest.json (positive & controls)
  - Verified file references and report templates
  - Verified cross-registry synchronization across skills.sh.json, skills-lock.json, and BUNDLE_MANIFEST.md
```

### 2. Fixture Generation
```powershell
python scripts/generate_fixtures.py
```
```text
=== Generating Benchmark Fixture Repositories ===
[OK] Generated 43 fixture file(s) across 43 scenarios.
```

### 3. Benchmark Evaluation Suite
```powershell
python scripts/run_benchmark.py
```
```text
=== Running Missing Piece Benchmark Evaluation Harness ===

Benchmark Evaluation Summary (43 scenarios):
  - True Positives (Detected Omissions): 14
  - True Negatives (Suppressed Controls): 29
  - False Positives: 0
  - False Negatives: 0
  - Precision: 100.0% (Target: >= 90.0%)
  - Recall: 100.0%
  - False Positive Rate: 0.0% (Target: 0.0%)

[OK] ALL BENCHMARK EVALUATIONS PASSED!
```

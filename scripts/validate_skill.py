#!/usr/bin/env python3
"""
validate_skill.py

Validates the Missing Piece skill package:
1. SKILL.md YAML frontmatter parsing and required fields.
2. Existence of all referenced files (references, examples, templates).
3. Markdown link consistency and structural checks.
4. Reporting template fields check.
5. Coverage of all 14 detector family codes in SKILL.md and detector-rules.md.
6. Coverage of all 14 detector family codes in benchmarks/manifest.json.
"""

import sys
import re
import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent / "skills" / "missing-piece"
SKILL_MD = SKILL_DIR / "SKILL.md"
MANIFEST_PATH = Path(__file__).resolve().parent.parent / "benchmarks" / "manifest.json"

DETECTOR_FAMILIES = [
    "MP-LC", "MP-ST", "MP-SY", "MP-MG", "MP-SE", "MP-FR", "MP-OC",
    "MP-AU", "MP-AS", "MP-OP", "MP-DC", "MP-CT", "MP-CF", "MP-OB"
]

REQUIRED_REPORT_FIELDS = [
    "Observed", "Expected", "Evidence searched", "Gap", "Why it matters", "Verification"
]

def validate_frontmatter(content: str, expected_name: str = "missing-piece") -> list[str]:
    errors = []
    if not content.startswith("---"):
        errors.append(f"{expected_name}/SKILL.md must start with YAML frontmatter ('---')")
        return errors
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{expected_name}/SKILL.md frontmatter missing closing '---'")
        return errors
    
    frontmatter = parts[1]
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

    if not name_match:
        errors.append(f"{expected_name}/SKILL.md missing 'name:' field")
    elif name_match.group(1).strip() != expected_name:
        errors.append(f"{expected_name}/SKILL.md name is '{name_match.group(1).strip()}', expected '{expected_name}'")

    if not desc_match:
        errors.append(f"{expected_name}/SKILL.md missing 'description:' field")
    elif len(desc_match.group(1).strip()) < 10:
        errors.append(f"{expected_name}/SKILL.md description is too short")

    return errors


def validate_all_skills() -> tuple[list[str], int]:
    errors = []
    skills_root = SKILL_DIR.parent
    skill_dirs = [d for d in skills_root.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
    if not skill_dirs:
        errors.append("No skills found in skills/ directory")
        return errors, 0

    for sdir in sorted(skill_dirs):
        skill_md = sdir / "SKILL.md"
        content = skill_md.read_text(encoding="utf-8")
        errs = validate_frontmatter(content, expected_name=sdir.name)
        errors.extend(errs)

    return errors, len(skill_dirs)


def validate_file_references(skill_content: str) -> list[str]:
    errors = []
    ref_pattern = r"(?:references|templates|examples)/[a-zA-Z0-9_-]+\.md"
    matches = set(re.findall(ref_pattern, skill_content))

    for relative_path in matches:
        full_path = SKILL_DIR / relative_path
        if not full_path.exists():
            errors.append(f"Referenced file does not exist: {relative_path}")

    return errors


def validate_detector_coverage(skill_content: str, detector_rules_content: str) -> list[str]:
    errors = []
    for code in DETECTOR_FAMILIES:
        if code not in skill_content:
            errors.append(f"Detector family '{code}' not mentioned in SKILL.md")
        if code not in detector_rules_content:
            errors.append(f"Detector family '{code}' not covered in references/detector-rules.md")
    return errors


def validate_template() -> list[str]:
    errors = []
    template_path = SKILL_DIR / "templates" / "audit-report.md"
    if not template_path.exists():
        errors.append("Template file 'templates/audit-report.md' is missing")
        return errors

    content = template_path.read_text(encoding="utf-8")
    for field in REQUIRED_REPORT_FIELDS:
        if field not in content:
            errors.append(f"audit-report.md template missing required field section: '{field}'")
    return errors


def validate_manifest_coverage() -> list[str]:
    errors = []
    if not MANIFEST_PATH.exists():
        errors.append(f"Benchmark manifest does not exist at: {MANIFEST_PATH}")
        return errors

    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        scenarios = data.get("scenarios", [])
        families_present = {s.get("detector_family") for s in scenarios}
        families_with_pos = {s.get("detector_family") for s in scenarios if s.get("type") == "positive"}
        families_with_neg = {s.get("detector_family") for s in scenarios if s.get("type") in ["negative", "exception", "disguised"]}

        for code in DETECTOR_FAMILIES:
            if code not in families_present:
                errors.append(f"Detector family '{code}' missing from benchmarks/manifest.json")
            if code not in families_with_pos:
                errors.append(f"Detector family '{code}' has no positive test scenario in benchmarks/manifest.json")
            if code not in families_with_neg:
                errors.append(f"Detector family '{code}' has no negative/control scenario in benchmarks/manifest.json")
    except Exception as e:
        errors.append(f"Failed to parse benchmarks/manifest.json: {e}")

    return errors


def main():
    print("=== Validating Missing Piece Skill Suite ===")
    if not SKILL_MD.exists():
        print(f"ERROR: {SKILL_MD} does not exist")
        sys.exit(1)

    skill_content = SKILL_MD.read_text(encoding="utf-8")
    detector_rules_path = SKILL_DIR / "references" / "detector-rules.md"
    detector_rules_content = detector_rules_path.read_text(encoding="utf-8") if detector_rules_path.exists() else ""

    errors = []
    all_skill_errors, skill_count = validate_all_skills()
    errors.extend(all_skill_errors)
    errors.extend(validate_file_references(skill_content))
    errors.extend(validate_detector_coverage(skill_content, detector_rules_content))
    errors.extend(validate_template())
    errors.extend(validate_manifest_coverage())

    if errors:
        print(f"\nValidation FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\n[OK] Skill package validation PASSED successfully!")
    print(f"  - Verified all {skill_count} skills in skills/ with valid frontmatter and descriptions")
    print("  - Verified 14 detector family codes in SKILL.md and detector-rules.md")
    print("  - Verified 14 detector family coverage in benchmarks/manifest.json (positive & controls)")
    print("  - Verified file references and report templates")
    sys.exit(0)


if __name__ == "__main__":
    main()

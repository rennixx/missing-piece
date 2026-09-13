# Acceptance Criteria

Missing Piece v1 is ready when all critical criteria pass.

## Packaging
- [ ] Skill is discoverable by current `skills` CLI.
- [ ] `SKILL.md` has valid minimal frontmatter.
- [ ] All referenced files exist.
- [ ] Installation docs are tested.
- [ ] No hosted dependency required.

## Behavior
- [ ] Full audit works.
- [ ] Focused audit works.
- [ ] Change audit works.
- [ ] Re-audit works.
- [ ] Audit is read-only by default.
- [ ] No generic best-practice findings.
- [ ] Every normal finding has evidence and implication.
- [ ] Counter-evidence search is mandatory.
- [ ] Confidence and severity are separate.
- [ ] Duplicate root causes are merged.

## Detector coverage
- [ ] Lifecycle (MP-LC).
- [ ] State machine (MP-ST).
- [ ] Symmetry (MP-SY).
- [ ] Mutation guards (MP-MG).
- [ ] Side effects (MP-SE).
- [ ] Failure/recovery (MP-FR).
- [ ] Ownership/cleanup (MP-OC).
- [ ] Authorization (MP-AU).
- [ ] Async/jobs (MP-AS).
- [ ] Operational completeness (MP-OP).
- [ ] Data consistency (MP-DC).
- [ ] Contract completeness (MP-CT).
- [ ] Configuration completeness (MP-CF).
- [ ] Observability implied (MP-OB).

## Quality
- [ ] Positive fixture for every core rule.
- [ ] Negative control for every core rule.
- [ ] Exception fixture for risky rules.
- [ ] High-confidence precision target met.
- [ ] Generic-advice leakage near zero.
- [ ] Cross-agent smoke test completed.

## Security/privacy
- [ ] No secret values in reports.
- [ ] Repository prompt injection guidance present.
- [ ] No automatic network upload.
- [ ] No destructive analysis commands.

## Documentation
- [ ] README.
- [ ] PRD.
- [ ] Architecture.
- [ ] Methodology.
- [ ] Detector catalog.
- [ ] Confidence model.
- [ ] Reporting spec.
- [ ] Evaluation plan.
- [ ] Roadmap.
- [ ] Contributing/security/license.

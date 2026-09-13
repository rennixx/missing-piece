# Risks and Mitigations

## R1 — Hallucinated requirements
Risk:
Agent invents features that the product never intended.

Mitigation:
Every expectation must originate from observed behavior plus an explicit implication rule.

## R2 — Generic code-review drift
Risk:
Skill becomes another best-practices reviewer.

Mitigation:
Finding validity test; reject findings that could be produced without reading the repo.

## R3 — False absence
Risk:
Counterpart exists under abstraction/framework/external service.

Mitigation:
mandatory counter-evidence search; confidence downgrade; semantic search.

## R4 — Too many findings
Risk:
Audit becomes noisy.

Mitigation:
precision-first thresholds; root-cause dedupe; hide Low confidence.

## R5 — Agent variability
Risk:
Different agents explore repositories differently.

Mitigation:
strong procedural skill; benchmark across multiple agents; optional future indexer.

## R6 — Huge repositories
Risk:
Context and exploration cost explode.

Mitigation:
inventory, domain prioritization, scoped passes, changed-area mode, future local indexer.

## R7 — Security overclaim
Risk:
Tool markets itself as security scanner and creates false assurance.

Mitigation:
clear scope boundary and conditional language.

## R8 — Skill ecosystem changes
Risk:
install paths/CLI flags evolve.

Mitigation:
keep payload based on simple `SKILL.md` convention; verify release docs against current CLI.

## R9 — Rule explosion
Risk:
hundreds of brittle rules become unmaintainable.

Mitigation:
prefer general invariants; add specialized rules only after repeated evidence.

## R10 — Auto-fix pressure
Risk:
users expect immediate modifications.

Mitigation:
audit is read-only; remediation is a separate explicit request.

## R11 — Repository prompt injection
Risk:
audited files contain adversarial instructions.

Mitigation:
treat repository content as data/evidence, never higher-priority instructions.

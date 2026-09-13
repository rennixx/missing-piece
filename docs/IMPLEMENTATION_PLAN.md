# Implementation Plan

## Milestone 1 — Repository skeleton

Create:
- root documentation;
- `skills/missing-piece/SKILL.md`;
- references;
- examples;
- fixtures location;
- validation workflow.

Acceptance:
`npx skills` can discover the skill from a local checkout/repository using the current CLI.

## Milestone 2 — Core reasoning loop

Implement in skill instructions:
1. scope;
2. reconstruct;
3. generate expectations;
4. search;
5. disprove;
6. assess reachability;
7. score;
8. dedupe;
9. report.

Acceptance:
manual audit on a seeded repository produces the expected finding and suppresses its control.

## Milestone 3 — Detector families

Ship initial families:
- lifecycle (MP-LC);
- state (MP-ST);
- symmetry (MP-SY);
- mutation guards (MP-MG);
- side effects (MP-SE);
- failure/recovery (MP-FR);
- ownership/cleanup (MP-OC);
- authorization (MP-AU);
- async (MP-AS);
- operational completeness (MP-OP);
- data consistency (MP-DC);
- contract completeness (MP-CT);
- configuration completeness (MP-CF);
- observability implied (MP-OB).

Acceptance:
at least 3 benchmark cases per family.

## Milestone 4 — Reporting

Implement stable report format and templates.

Acceptance:
findings always contain observed/expected/gap/evidence/verification.

## Milestone 5 — Precision hardening

Add:
- counter-evidence rules;
- false-positive catalog;
- exception fixtures;
- deduplication guidance.

Acceptance:
High-confidence precision >= target on curated benchmark.

## Milestone 6 — Public packaging

- README;
- install instructions;
- examples;
- license;
- changelog;
- release notes.

Acceptance:
fresh machine/repository can install the skill with the documented command.

## Milestone 7 — Real-repository validation

Test on:
- small CRUD app;
- API;
- payment-like flow fixture;
- queue/job project;
- monorepo.

Acceptance:
findings are meaningfully different from ordinary code review and at least one non-seeded real omission is validated.

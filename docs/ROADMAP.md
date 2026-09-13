# Roadmap

## Phase 0 — Foundation
- finalize terminology;
- publish initial methodology;
- implement skill package;
- create first 20 fixtures;
- manually test on 5 real repositories.

Exit condition:
High-confidence reports are consistently useful and non-generic.

## Phase 1 — Public v1
- 10 core detector families;
- 40+ benchmark scenarios;
- README/examples;
- install through `npx skills`;
- Codex + Claude Code validation;
- GitHub release.

## Phase 2 — Calibration
- collect user-reported false positives;
- improve confidence rules;
- add suppression vocabulary;
- add re-audit workflow;
- expand examples.

## Phase 3 — Rule packs
Potential packs:
- web APIs;
- payments;
- auth/identity;
- queues/events;
- CRUD/data lifecycle;
- Next.js;
- Node;
- .NET;
- Django;
- Rails;
- Prisma/Postgres.

Rule packs must add discovery/context, not generic framework advice.

## Phase 4 — Local analysis engine
Only after evidence of need.

Candidate features:
- repository indexing;
- symbol graph;
- route inventory;
- schema graph;
- state extraction;
- baseline diff.

## Phase 5 — CI / PR mode
- changed-area audit;
- baseline known findings;
- fail only on new High-confidence findings above configured severity;
- machine-readable report.

## Phase 6 — Multi-repo / organizational
- service contracts;
- producer/consumer gaps;
- identity/permission consistency;
- shared domain lifecycle;
- organization rule packs.

## Anti-roadmap

Do not rush toward:
- SaaS dashboard;
- billing;
- IDE extension;
- auto-fixing;
- huge rule counts.

Trustworthiness is the moat.

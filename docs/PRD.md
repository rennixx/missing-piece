# Product Requirements Document

## 1. Product name

**Missing Piece**

Working tagline:

> **Find what your software forgot.**

Technical positioning:

> **Linters find bad code. Tests find broken behavior. Missing Piece finds the code that should exist but doesn't.**

## 2. Problem

Most software quality tools reason over artifacts that already exist:
- linters inspect written code;
- type checkers inspect declared contracts;
- tests exercise implemented paths;
- SAST tools inspect present data/control flow;
- code reviewers critique visible changes.

A major category of software failure comes from **absence**:
- a refund path exists but inventory restoration does not;
- a subscription can be created but not cancelled;
- a resource can be allocated but not released;
- a role can grant access but there is no revocation path;
- account deletion removes the user row but leaves owned uploads;
- a state machine supports `pending -> paid` but no timeout from `pending`;
- a write endpoint exists without authorization, audit, validation, or idempotency;
- a deployment introduces a resource with no health check, backup, rollback, or cleanup path.

These are hard to detect because there may be no syntactically incorrect code.

## 3. Product thesis

Software contains **implied structure**.

Observed capabilities create expectations:
- create implies lifecycle ownership;
- allocation implies release;
- state transitions imply allowed/forbidden transitions;
- external side effects imply reconciliation and failure handling;
- privileges imply authorization and revocation;
- persisted data implies retention and deletion semantics;
- retries imply idempotency;
- async jobs imply observability and dead-letter/recovery behavior.

Missing Piece reconstructs those expectations, searches the repository for evidence, and reports gaps.

## 4. Target users

Primary:
- solo developers;
- AI-assisted developers;
- maintainers inheriting unfamiliar repositories;
- small engineering teams;
- reviewers auditing generated code;
- developers preparing releases or migrations.

Secondary:
- security reviewers;
- platform engineers;
- consultants;
- open-source maintainers;
- engineering managers reviewing systemic risk.

## 5. Primary jobs to be done

1. "Audit this repository for important behavior that appears to be missing."
2. "Before I ship, tell me what lifecycle/failure/security paths I forgot."
3. "I inherited this system; reconstruct it and identify suspicious gaps."
4. "An AI agent built this feature; check what it failed to implement."
5. "Compare a feature's implied contract to what actually exists."
6. "Audit only payments/auth/jobs/data-deletion/etc."
7. "Re-run after fixes and show which gaps remain."

## 6. MVP goals

The MVP must:
- install as an Agent Skill;
- work across common repository types without a hosted backend;
- support whole-repo and scoped audits;
- build an observed system model;
- run multiple detector families;
- report evidence-backed findings;
- separate severity from confidence;
- avoid generic style/best-practice noise;
- support explicit suppression/acknowledgement guidance;
- produce stable Markdown output.

## 7. MVP non-goals

- automatic code modification;
- formal verification;
- perfect call-graph construction;
- binary analysis;
- runtime tracing;
- malware detection;
- dependency vulnerability scanning;
- secret scanning;
- package CVE lookup;
- production telemetry ingestion;
- multi-repository organization graph;
- SaaS dashboard.

## 8. Success metrics

Quality:
- precision of high-confidence findings;
- proportion of findings accepted as real omissions;
- low duplicate finding rate;
- low generic-advice rate;
- evidence trace completeness.

Utility:
- median number of meaningful findings per non-trivial repo;
- percentage of audits yielding at least one accepted issue;
- re-audit usefulness after fixes;
- time-to-first-meaningful-finding.

Distribution:
- installs;
- repeat installs/updates;
- GitHub stars/forks;
- public examples of findings;
- contribution of rule packs/fixtures.

## 9. Core product requirements

### R1 — Repository reconstruction
Infer important:
- domains/entities;
- entry points;
- mutations;
- state machines;
- background jobs;
- external services;
- resources;
- roles/permissions;
- side effects;
- cleanup flows;
- operational hooks.

### R2 — Implication generation
For each observed fact, derive expected behavior using explicit rule families.

### R3 — Evidence search
Search symbols, references, routes, schemas, tests, configuration, migrations, docs, and call sites before concluding absence.

### R4 — Finding threshold
A finding is emitted only when evidence is sufficient to make the claim falsifiable.

### R5 — Confidence
Each finding receives a confidence band:
- High;
- Medium;
- Low.

Low-confidence findings should be hidden by default in standard audits.

### R6 — Severity
Severity reflects potential impact, independent of certainty:
- Critical;
- High;
- Medium;
- Low;
- Informational.

### R7 — Scope
Support:
- whole repository;
- directory/module;
- feature/domain;
- changed files + connected context;
- detector-family-specific audit.

### R8 — Explainability
Every result states:
- observed evidence;
- implied expectation;
- searched evidence;
- missing/incomplete element;
- likely consequence;
- confidence;
- severity;
- verification steps.

### R9 — No mutation
Audit mode must not modify user code unless the user separately asks for remediation.

### R10 — Re-audit
The output format must make it easy to compare a later audit.

## 10. User experience

Ideal interaction:

**User:** Audit this repo with Missing Piece.

**Agent:**
1. establishes scope;
2. maps system;
3. performs detector passes;
4. cross-checks evidence;
5. deduplicates;
6. reports strongest findings;
7. optionally lists suppressed uncertain observations.

The user should not need to manually teach the agent the repository architecture unless repository evidence is insufficient.

## 11. Competitive boundary

Missing Piece wins by owning a specific question:

> **Given what this system already does, what else must exist for that behavior to be complete?**

Any feature that does not strengthen this question should be treated skeptically.

## 12. Long-term expansion

Potential evolution:
- deterministic local indexer/CLI;
- historical diff reasoning;
- multi-repo contracts;
- organization-specific rule packs;
- CI gate mode;
- IDE annotations;
- pull-request delta audits;
- runtime evidence adapters;
- hosted benchmark service;
- Missing Piece rule marketplace.

The skill remains the free, portable reasoning layer even if a deeper engine appears later.

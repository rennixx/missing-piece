# Detection Methodology

## Core equation

A Missing Piece finding is:

**Observed evidence + implication rule - verified counterpart = candidate omission**

A candidate becomes a reportable finding only after counter-evidence search.

## Phase 1 — Scope

Determine:
- repository root;
- requested feature/module if any;
- languages/frameworks;
- whether generated/vendor/build directories should be excluded;
- whether the task is full audit, focused audit, or change audit.

## Phase 2 — Reconnaissance

Build an inventory of:
- entry points;
- domain entities;
- mutations;
- external integrations;
- persistent resources;
- state enums/statuses;
- auth and roles;
- async workers;
- scheduled jobs;
- infrastructure/configuration;
- tests;
- migrations;
- documentation.

Do not report findings yet.

## Phase 3 — Candidate generation

Run detector families independently.

A detector should generate an expectation because of repository evidence, not because "all apps should have X."

Bad:
> Every app should have audit logging.

Good:
> This admin endpoint performs irreversible privileged financial adjustments, while adjacent privileged mutations emit audit events. No corresponding event was found for this path.

## Phase 4 — Evidence search

Search broadly enough to avoid filename assumptions:
- symbol names;
- semantic synonyms;
- route references;
- event handlers;
- database triggers;
- middleware;
- framework hooks;
- tests;
- migration logic;
- infrastructure;
- comments/docs where they describe intentional behavior.

## Phase 5 — Counter-evidence

Actively try to disprove the candidate.

Ask:
- could the counterpart be implicit in a framework?
- could a database constraint implement it?
- could an external provider own the responsibility?
- could the operation be intentionally irreversible?
- could the function be unused/dead?
- is another abstraction providing the behavior?
- is the observed path test-only?
- does configuration disable the feature?

## Phase 6 — Reachability

Presence is not enough.

A counterpart may exist but be:
- never called;
- unreachable from the relevant flow;
- guarded incorrectly;
- wired only in tests;
- applicable to a different resource;
- stale/dead code.

Report "incomplete/unwired" rather than "absent" when appropriate.

## Phase 7 — Confidence

Use:
- quality of observed evidence;
- strength of implication;
- breadth of search;
- amount of counter-evidence;
- framework certainty;
- reachability certainty.

## Phase 8 — Deduplication

Collapse findings when one root omission explains several symptoms.

Example:
- no cancellation timeout;
- pending orders remain forever;
- inventory reservations never release.

If all are caused by one missing expiry flow, prefer one primary finding with consequences.

## Phase 9 — Report

Standard audits should surface:
- all High-confidence Critical/High/Medium findings;
- selected High-confidence Low findings;
- Medium-confidence findings only when potentially significant;
- no Low-confidence findings unless explicitly requested.

## Finding validity test

Before emitting a finding, answer YES to all:

1. Can I point to the observed behavior that creates the expectation?
2. Can I state the exact expected counterpart?
3. Did I search multiple plausible implementations?
4. Did I search for counter-evidence?
5. Is absence/incompleteness still plausible?
6. Can the user verify or falsify the claim?
7. Is this about missing behavior rather than style?
8. Is it non-duplicate?

If any answer is NO, do not emit it as a normal finding.

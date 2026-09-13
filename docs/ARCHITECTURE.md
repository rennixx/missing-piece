# Architecture

## 1. Architectural strategy

Missing Piece v1 is primarily a **reasoning skill**, not an application.

Architecture:

```text
User request
    |
    v
SKILL.md router
    |
    +--> Scope selection
    |
    +--> Repository reconstruction
    |
    +--> Detector-family passes
    |
    +--> Evidence verification
    |
    +--> Confidence calibration
    |
    +--> Deduplication / contradiction check
    |
    v
Structured audit report
```

Reference files provide deeper methodology and should be loaded only when relevant.

## 2. Conceptual internal model

The agent should build five conceptual graphs.

### A. Capability graph
Nodes:
- commands;
- routes;
- handlers;
- services;
- use cases;
- jobs;
- UI actions.

Edges:
- invokes;
- enables;
- requires;
- triggers.

### B. Resource lifecycle graph
Nodes:
- entities;
- files;
- sessions;
- tokens;
- reservations;
- subscriptions;
- jobs;
- external resources.

Edges:
- create;
- own;
- mutate;
- release;
- revoke;
- archive;
- delete.

### C. State-transition graph
Nodes:
- states.

Edges:
- transition;
- actor;
- guard;
- side effects;
- rollback/recovery.

### D. Trust graph
Nodes:
- actors;
- roles;
- entry points;
- secrets;
- privileged operations;
- external systems.

Edges:
- authenticate;
- authorize;
- delegate;
- expose;
- revoke.

### E. Side-effect graph
Nodes:
- mutations;
- external calls;
- messages;
- notifications;
- payments;
- inventory changes;
- cache writes.

Edges:
- causes;
- compensates;
- retries;
- reconciles.

The v1 implementation does not need to serialize these graphs. They are reasoning structures.

## 3. Detector contract

Each detector family follows the same pipeline:

```text
Observed Fact
    ↓
Implication Rule
    ↓
Expected Counterpart
    ↓
Evidence Search
    ↓
Counter-evidence Search
    ↓
Finding Candidate
    ↓
Confidence + Severity
    ↓
Deduplication
```

Detector families must not bypass the evidence step.

## 4. Rule representation

A conceptual rule has:

- `id`
- `family`
- `trigger`
- `expectation`
- `exceptions`
- `evidence_to_seek`
- `counter_evidence`
- `severity_hints`
- `confidence_hints`

Example:

```text
Rule: LIFECYCLE.REVERSIBLE_ALLOCATION
Trigger:
  System reserves a finite resource.
Expectation:
  A release/cancel/expiry path should exist.
Exceptions:
  Reservation is intentionally permanent.
Evidence:
  release, cancel, expire, timeout, cleanup, compensation.
Counter-evidence:
  immutable one-time allocation documented by domain rules.
```

In v1 these rules live as carefully written Markdown reasoning instructions.

## 5. Framework adapters

Framework-specific knowledge should never contaminate the core methodology.

Future layout:

```text
references/
  core/
  adapters/
    nextjs.md
    rails.md
    django.md
    spring.md
    dotnet.md
    prisma.md
    postgres.md
```

Adapters provide discovery hints, not new product semantics.

## 6. Output architecture

The report has:
1. audit metadata;
2. reconstructed system summary;
3. findings ordered by severity/confidence;
4. evidence;
5. uncertainties;
6. suppressed/needs-confirmation items;
7. coverage summary;
8. re-audit notes.

## 7. Future companion engine

If introduced, a local engine should expose repository facts, not final judgments.

Good engine outputs:
- symbol graph;
- call/reference graph;
- routes;
- schema relations;
- ownership hints;
- state enums;
- queue consumers/producers;
- config resources;
- changed-file neighborhood.

Bad engine responsibility:
- deciding that behavior is truly missing.

That remains the skill's reasoning job.

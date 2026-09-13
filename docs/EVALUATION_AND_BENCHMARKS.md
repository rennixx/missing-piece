# Evaluation and Benchmark Plan

## Objective

Measure whether Missing Piece finds genuine omissions rather than producing plausible prose.

## Benchmark design

Create small repositories/fixtures with known omissions and matched controls.

Every detector rule needs:
1. positive fixture — omission exists;
2. negative fixture — counterpart exists;
3. exception fixture — counterpart should not exist;
4. disguised fixture — behavior exists under unexpected naming/abstraction.

## Core benchmark dimensions

### Precision
Of emitted findings, how many are valid?

Primary target for High-confidence findings:
- >= 90% accepted in curated benchmark;
- stretch target >= 95%.

### Recall
Of seeded omissions, how many are found?

Recall matters, but must not be optimized by flooding the report.

### Evidence correctness
Does each finding cite the right trigger and searched area?

### Classification
Is detector family appropriate?

### Confidence calibration
Do High-confidence findings outperform Medium-confidence findings materially?

### Duplicate rate
How many findings describe the same root omission?

### Generic-advice leakage
How many emitted findings could have been produced without reading the repository?

Target: effectively zero.

## Initial benchmark corpus

At least 40 scenarios:

Lifecycle:
- upload without deletion;
- reservation without expiry;
- token without revocation;
- correct irreversible ledger exception.

State:
- pending without timeout;
- enum value unhandled;
- all transitions complete control.

Permissions:
- new admin mutation omitted from policy;
- global middleware control.

Side effects:
- cancellation misses inventory restore;
- async event handles restore under non-obvious name.

Failure:
- webhook retry without idempotency;
- queue has dead-letter handling control.

Data consistency:
- denormalized counter increment but no decrement;
- DB trigger handles decrement control.

Configuration:
- required env var omitted from deployment manifest;
- platform injects var control.

Operations:
- worker can become stuck with no recovery;
- managed service owns retries control.

## Evaluation process

For each release:
1. run all fixtures using target agents;
2. record findings;
3. human-label TP/FP/FN;
4. compare against previous release;
5. block release on material precision regression.

## Cross-agent testing

At minimum evaluate:
- Codex;
- Claude Code;
- Cursor-compatible skill flow where practical.

The methodology should remain stable even if exploration behavior differs.

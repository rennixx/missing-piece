---
name: missing-piece-async
description: Auditor for background queues, schedulers, message producers/consumers, DLQs, distributed locks, poison pill guards, and stuck-job recovery.
---

# Missing Piece Async

> [!TIP]
> ### 📦 Full 10-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

Specialized auditor for background jobs, message queues, distributed tasks, and schedulers.

## ⚡ Token-Optimal Execution Protocol
- **Grep-first, Slice-second**: Run `git grep -l` to find queue clients (`bullmq`, `celery`, `amqplib`, `kafkajs`, `sqs`). Inspect workers with 15–25 line slices. Never dump full files (>100 lines).
- **Strict Exclusions**: Ignore lockfiles, minified assets, `dist/`, `build/`, `.next/`, `node_modules/`, and mock fixtures.
- **Early-Exit Short-Circuit**: If DLQ routing, retry backoff, or lock TTL is confirmed, terminate the detector pass immediately.
- **Token-Sparse Findings**: Format findings with direct file links and line numbers; avoid repeating large source code blocks.

## Deep Async Invariant Rules

### ASYNC-01 — Dead-Letter Queue (DLQ) & Terminal Error Visibility
- **Trigger**: Worker or consumer processes jobs from a queue (RabbitMQ, Kafka, BullMQ, Celery, AWS SQS).
- **Expected Counterpart**: Retry limit with exponential backoff, routing to DLQ / failed-jobs table upon exhaustion, and alerting.
- **Consequence**: Poison pills cycle indefinitely, blocking queue partition processing.

### ASYNC-02 — Distributed Lock TTL & Exception Safety
- **Trigger**: Job acquires distributed lock (Redis `SETNX`, Redlock, Postgres advisory lock).
- **Expected Counterpart**: Mandatory TTL/lease expiry on lock key, and release inside `try ... finally` or context manager.
- **Consequence**: Worker crash leaves resource locked indefinitely, halting the workflow.

### ASYNC-03 — Scheduled Job Overlap Guard & Stuck Recovery
- **Trigger**: Recurring cron/scheduler processes batches (hourly settlement, nightly billing).
- **Expected Counterpart**: Overlap guard preventing concurrent runs, and heartbeat/timeout recovering jobs stuck in `PROCESSING`.
- **Consequence**: Concurrent runs corrupt aggregates, or crashed worker leaves records stuck permanently.

### ASYNC-04 — Transactional Outbox & Reconciliation
- **Trigger**: Mutates DB and publishes async domain event to message broker.
- **Expected Counterpart**: Transactional Outbox pattern committing event to outbox table within same DB transaction, or CDC poller.
- **Consequence**: Dual-write failure where DB commits but message broker drops event.

## Async Audit Procedure

1. **Locate Queues**: Search queue imports (`bullmq`, `celery`, `amqplib`, `kafkajs`, `boto3.sqs`).
2. **Inspect Pipeline**: Trace job producer dispatch sites and consumer worker loops.
3. **Verify Invariants**: Audit retry configurations, DLQs, lock TTLs, and crash recovery timeouts.

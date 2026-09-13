---
name: missing-piece-async
description: Auditor for asynchronous workflows, background queues, schedulers, and distributed tasks. Use when checking message producers/consumers, dead-letter queues, distributed locks, poison pill handling, and stuck-job recovery.
---

# Missing Piece Async

Specialized auditor for background jobs, message queues, distributed tasks, and schedulers.

Asynchronous and distributed architectures decouple execution in time and space. When an omission occurs, tasks fail silently, poison pills clog processing pipelines, or jobs lock resources permanently without triggering alerts.

## Deep Async Invariant Rules

### ASYNC-01 — Dead-Letter Queue (DLQ) & Terminal Error Visibility
- **Trigger**: A background worker or consumer processes jobs from a queue (RabbitMQ, Kafka, BullMQ, Celery, AWS SQS).
- **Expected Counterpart**:
  1. Configured retry limit with exponential backoff.
  2. Routing to a dead-letter queue (DLQ) or failed-jobs table upon retry exhaustion.
  3. High-priority alert notification emitted on terminal failure.
- **Consequence of Absence**: Poison pills cycle indefinitely, exhausting worker CPU and blocking all subsequent messages in the queue partition.

### ASYNC-02 — Distributed Lock TTL & Exception Safety
- **Trigger**: A background job acquires a distributed lock (Redis `SETNX`, Redlock, Postgres advisory lock) to ensure mutual exclusion.
- **Expected Counterpart**:
  1. Mandatory time-to-live (TTL / lease expiry) on the lock key.
  2. Lock release wrapped inside a `try ... finally` or context manager block.
- **Consequence of Absence**: If worker crashes while holding lock, the critical resource remains locked forever, permanently freezing the workflow.

### ASYNC-03 — Scheduled Job Overlap Guard & Stuck Recovery
- **Trigger**: A recurring cron job or scheduler is registered to process batches (e.g. hourly settlement, nightly billing).
- **Expected Counterpart**:
  1. Overlap guard preventing a second instance from running concurrently if a previous batch is still executing.
  2. Heartbeat monitoring or stuck-job timeout recovering jobs left in `PROCESSING` status after a process crash.
- **Consequence of Absence**: Concurrent execution corrupts batch aggregates, or a crashed worker leaves items stuck in intermediate states indefinitely.

### ASYNC-04 — Transactional Outbox & Polling Reconciliation
- **Trigger**: Application mutates primary database and publishes an asynchronous domain event to a message broker.
- **Expected Counterpart**: Transactional Outbox pattern writing the event to an outbox table in the same DB transaction, combined with a background publisher worker.
- **Consequence of Absence**: Dual-write hazard where database commits but broker publish fails, causing downstream consumers to permanently miss critical state updates.

## Async Audit Procedure

1. Search for queue client imports (`bullmq`, `kombu`, `celery`, `amqplib`, `kafkajs`, `boto3.sqs`).
2. Map producer emission points and consumer worker handlers.
3. Verify retry limits, DLQ definitions, lock expiration, and crash recovery paths.

# Failure and Side-Effect Analysis

## External side effects

When code calls:
- payment provider;
- email/SMS provider;
- object storage;
- third-party API;
- queue;
- webhook target;

ask:
- what if the call succeeds but local persistence fails?
- what if local persistence succeeds but the call fails?
- what if the request is repeated?
- how is uncertain outcome reconciled?

Do not demand distributed transactions. Look for the repository's intended consistency mechanism.

## Retry triangle

Retries commonly imply three related concerns:

1. retryability;
2. idempotency;
3. terminal failure handling.

Finding one without the others is a candidate, not proof.

## Compensation

A multi-step operation may require compensating actions.

Example:
- payment captured;
- inventory allocation fails;
- order cannot complete.

Search for:
- void/refund;
- rollback;
- compensation event;
- reconciliation job;
- manual review status.

## Side-effect inventory

For a domain action:
1. inspect handler;
2. inspect domain/service calls;
3. inspect emitted events;
4. inspect event consumers;
5. inspect tests describing expected outcomes;
6. compare inverse transitions.

## Reconciliation

High-value candidate when:
- external state can diverge from local state;
- webhooks can be missed;
- process can crash between steps;
- status can remain uncertain.

Only report missing reconciliation if architecture makes divergence realistically possible and no other recovery path is found.

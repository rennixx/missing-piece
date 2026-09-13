# Lifecycle and State Analysis

## Resource lifecycle model

For each important resource, consider:

```text
not-exists
  -> created
  -> active
  -> suspended/changed
  -> terminating
  -> terminated/archived/deleted
```

Real systems may skip states.

Look for lifecycle ownership:
- who creates?
- who changes?
- who expires?
- who revokes?
- who cleans child resources?
- what happens on owner deletion?

## Timeout principle

A non-terminal state dependent on external action often needs a timeout, retry, cancellation, or reconciliation path.

Examples:
- `pending_payment`;
- `processing`;
- `verification_requested`;
- `reservation_held`.

Do not require timeout if another invariant guarantees bounded completion.

## State coverage

When a status enum exists:
1. list values;
2. find producers;
3. find consumers;
4. compare switch/match/if handling;
5. inspect defaults;
6. inspect UI/API serialization;
7. inspect transition guards.

A missing branch is only a Missing Piece finding when the state can actually reach that consumer and handling is required.

## Terminal state check

Identify whether each state:
- is terminal intentionally;
- transitions to another state;
- can become stuck;
- has a recovery owner.

## Transition side effects

Compare transitions that enter and leave equivalent resource states.

Example:
- entering `reserved` decrements available capacity;
- leaving `reserved` should often restore capacity.

This is stronger than name symmetry because it is based on invariant conservation.

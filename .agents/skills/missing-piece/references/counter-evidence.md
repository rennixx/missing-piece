# Counter-Evidence Checklist

Before emitting a finding, attempt to prove it wrong.

## 1. Semantic alternatives
Search synonyms and domain terminology.

## 2. Cross-cutting layers
Check:
- middleware;
- decorators;
- policies;
- interceptors;
- base classes;
- hooks;
- database triggers;
- ORM cascades;
- shared service wrappers.

## 3. Async paths
Check:
- emitted events;
- queue jobs;
- workers;
- schedulers;
- webhooks;
- outbox/inbox patterns.

## 4. Framework behavior
Determine whether the framework/runtime provides the behavior.

## 5. External ownership
Check whether:
- payment provider;
- identity provider;
- storage lifecycle policy;
- managed queue;
- database;
- infrastructure platform

owns the counterpart.

If external behavior cannot be verified, state uncertainty.

## 6. Intent
Search:
- ADRs;
- README/docs;
- comments near domain model;
- tests;
- migration notes.

Intent does not override unsafe behavior automatically, but can invalidate a symmetry assumption.

## 7. Reachability
Confirm the triggering code path is active/reachable.

## 8. Configuration
Behavior may be conditional or disabled.

## 9. Tests
Tests can reveal a counterpart or intended exception, but tests alone do not prove runtime wiring.

## 10. Negative result quality
Ask:
Did I actually search the likely locations, or merely fail to see the behavior in the first file?

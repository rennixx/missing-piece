# Data and Operational Completeness

## Derived data

When value B is derived from A but persisted separately:
- identify all mutations of A;
- check corresponding B updates;
- inspect delete/rollback paths;
- inspect rebuild/reconciliation mechanism.

Examples:
- counters;
- cached totals;
- search index;
- denormalized status;
- read models.

## Relations and ownership

For parent-child relations:
- delete/archive behavior;
- orphan policy;
- cascade vs retain;
- external object cleanup.

Do not assume child deletion; domain may require retention.

## Soft deletion

If soft delete exists:
- reads;
- uniqueness constraints;
- joins;
- background jobs;
- restore behavior.

Look for inconsistent handling rather than requiring one particular pattern.

## Configuration

If code reads a required environment value:
- validate startup behavior;
- deployment config;
- examples/docs where project conventions make that necessary.

An absent `.env.example` alone is not a finding.

## Operational dependencies

Only inspect operations directly implied by the architecture.

Examples:
- job transitions records to `processing` but no path recovers records after worker crash;
- migration requires new column before old binary can run;
- health endpoint ignores a worker whose absence makes system non-functional.

Avoid generic operational wishlists.

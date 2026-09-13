---
name: missing-piece-pr
description: Audit Git diffs, pull requests, or branch changes for missing counterparts, unhandled states, forgotten cleanup, or broken symmetry before merging. Use when asked to review changes, check a PR diff, or verify whether a newly added feature or patch is complete.
---

# Missing Piece PR

The pre-merge delta auditor for Git pull requests and branch changes.

While standard PR reviewers focus on line comments and formatting, `missing-piece-pr` audits the **implications of what changed**:

> **"You modified X, which creates new obligations for Y and Z. Did you implement them?"**

## Core Audit Triggers for Pull Requests

When inspecting a diff, evaluate these high-risk triggers:

1. **New Mutation Route or Action Added**
   - Did the diff add an endpoint without registering it in established RBAC/permission matrices? (`MP-AU`)
   - Did the diff introduce a database write without input validation or idempotency keys? (`MP-MG`)

2. **New Entity or Stateful Resource Introduced**
   - Does a creation path exist without a deletion, archival, or cleanup counterpart? (`MP-LC`)
   - What happens to related child files or storage objects when the entity is removed? (`MP-OC`)

3. **New State Variant or Enum Added**
   - If an enum was modified (e.g. `Refunded`, `Archived`), do existing dispatchers, consumers, and UI switches handle the new variant? (`MP-CT` / `MP-ST`)
   - Do non-terminal states have exit, cancellation, or timeout paths? (`MP-ST`)

4. **Primary State Mutation Altered**
   - If an order or workflow status is cancelled or refunded, does the diff release reserved inventory, adjust denormalized counts, or notify downstream systems? (`MP-SE` / `MP-DC`)

5. **Async Job or Queue Producer Added**
   - Is there an active consumer registered for the new queue message? (`MP-AS`)
   - Does the worker handle poison pills or route exhausted retries to a dead-letter queue? (`MP-AS` / `MP-FR`)

6. **New Environment Variable Referenced**
   - Is the new env var added to `.env.example`, deployment manifests, or runtime validation schemas? (`MP-OP` / `MP-CF`)

## PR Audit Procedure

### 1. Extract Diff & Map Neighborhood
- Run `git diff` against the base branch (e.g. `main` or `target-branch`).
- Identify newly added symbols, route definitions, model migrations, and handlers.

### 2. Trace Ripple Graph
Trace callers, subscribers, and dependents:
- Who calls this new code?
- What secondary side effects do existing neighboring mutations trigger?
- What cross-cutting layers (middleware, policies, triggers) should apply?

### 3. Search for Counterparts
Search across the entire repository—not just the modified files—to verify if the counterpart was already implemented elsewhere or if it is completely absent.

### 4. Format PR Review Output
Output findings as concise, actionable PR review comments structured to block regressions before merge:

```markdown
## 🧩 Missing Piece PR Audit

### ⚠️ [MP-FAMILY] — [Missing Counterpart Title]

- **Diff Location**: `path/to/file.py:L45`
- **Severity**: Critical | High | Medium
- **Confidence**: High

**What was changed:**
[1-2 sentences summarizing the diff fact]

**What appears to be missing:**
[Specific missing counterpart, handler, or guard implied by the change]

**Why it matters before merging:**
[Concrete production consequence if merged as-is]

**Suggested Fix:**
[Minimal code diff or action required to complete the PR]
```

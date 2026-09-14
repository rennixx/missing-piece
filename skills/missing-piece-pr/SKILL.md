---
name: missing-piece-pr
description: Audit Git diffs, pull requests, and branch changes for absent counterparts, unhandled enum states, forgotten cleanup, or broken symmetry before merging.
---

# Missing Piece PR

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

The pre-merge delta auditor for Git pull requests and branch changes.

Audits the **implications of what changed**: *"You modified X, which creates new obligations for Y and Z. Did you implement them?"*

## ⚡ Token-Optimal Execution Protocol
- **Diff-Bounded Scope**: Inspect only `git diff --name-only` files and their direct callers.
- **Slice Inspection**: Inspect added hunks (15–20 lines) and cross-reference counterpart sites with targeted `git grep -l`.
- **Strict Exclusions**: Exclude lockfiles, package manifests, generated code, and minified bundles.
- **Early Exit**: If a new route inherits auth from a base controller or router group, dismiss `MP-AU` immediately.
- **Token-Sparse Comments**: Render review comments with file links and exact line numbers rather than repeating diff snippets.

## Core PR Audit Triggers

1. **New Route / Mutation Added**: Check RBAC matrix registration (`MP-AU`) and idempotency/concurrency guards (`MP-MG`).
2. **New Entity Introduced**: Check deletion/cleanup/archival lifecycle (`MP-LC`) and child storage cascade (`MP-OC`).
3. **New Enum State Added**: Check match/switch exhaustiveness across consumers, UI, and dispatchers (`MP-ST`/`MP-CT`).
4. **Primary Mutation Altered**: Check secondary side-effects: inventory restock, counts, outbox events, notifications (`MP-SE`/`MP-DC`).
5. **Async Job Producer Added**: Check active consumer registration, DLQ, and retry backoff (`MP-AS`/`MP-FR`).
6. **New Env Var Added**: Check fallback defaults and `.env.example`/schema updates (`MP-CF`/`MP-OP`).

## PR Audit Procedure

1. **Extract Diff**: Run `git diff --name-only <base>...HEAD`.
2. **Identify Hunk Triggers**: Match added lines against the 6 PR triggers above.
3. **Verify Counterparts**: Search repo with `git grep -l <counterpart>` to confirm presence or verify absence.
4. **Report**: Format review comments with direct file links and verification steps.

## PR Review Output Format

```markdown
## 🧩 Missing Piece PR Audit

### ⚠️ Potential Omission: [Title]
- **Diff Anchor**: `[path/to/file.py:L20-35](file:///...)` added `create_job()`
- **Missing Counterpart**: No cleanup routine, DLQ handler, or cancel endpoint found
- **Consequence**: Uncompleted jobs remain stuck if workers fail
- **Verification**: Check if consumer is registered in `workers/`
```

---
name: missing-piece-rails
description: "Ruby on Rails auditor for ActiveRecord associations (dependent: :destroy), after_commit callbacks, Sidekiq retry hooks, and Pundit/CanCanCan policies."
---

# Missing Piece Rails

> [!TIP]
> ### 📦 Full 10-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

Specialized adapter for **Ruby on Rails & ActiveRecord**.

## ⚡ Token-Optimal Execution Protocol
- **Targeted Macro Search**: Search `git grep -l "has_many\|has_one"` or `git grep -l "ApplicationController"`. Inspect with 15–20 line slices.
- **Strict Exclusions**: Ignore asset pipelines, coverage, and log files.
- **Early Exit**: If `ApplicationController` declares `after_action :verify_authorized`, dismiss general Pundit authorization omissions immediately.
- **Token-Sparse Findings**: Format findings with direct file links and line numbers.

## Rails Invariant Rules

### RAILS-01 — Association Cascade & Cleanup Specification
- **Trigger**: ActiveRecord model declares `has_many` or `has_one`.
- **Expected Counterpart**: Explicit `dependent: :destroy`, `:delete_all`, or `:nullify`.
- **Consequence**: Parent deletion leaves orphaned foreign-key child records.

### RAILS-02 — Transactional Callback Safety (`after_commit`)
- **Trigger**: Model callback triggers external side-effects (Sidekiq, Stripe, email).
- **Expected Counterpart**: Use of `after_commit` (not `after_save` / `after_create`).
- **Consequence**: If DB transaction rolls back, side-effect has already dispatched.

### RAILS-03 — Sidekiq Retries Exhausted Recovery Hook
- **Trigger**: Critical worker job executes via Sidekiq.
- **Expected Counterpart**: Declaration of `sidekiq_retries_exhausted` hook or dead-job alert.
- **Consequence**: Dead jobs silently sit in Dead Set without alert or remediation.

### RAILS-04 — Strong Parameters Completeness
- **Trigger**: Controller mutates record via `params.require(...).permit(...)`.
- **Expected Counterpart**: Whitelist permits only user-editable fields; excludes `role`/`admin`.
- **Consequence**: Mass assignment privilege escalation.

### RAILS-05 — Authorization Policy Enforcement
- **Trigger**: Controller action mutates model.
- **Expected Counterpart**: `authorize @record` (Pundit) or `load_and_authorize_resource` (CanCanCan).
- **Consequence**: Unprotected action bypassing authorization checks.

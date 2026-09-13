---
name: missing-piece-rails
description: "Ruby on Rails auditor. Use when auditing ActiveRecord associations (dependent: :destroy), callbacks (after_commit), Sidekiq job retries, Strong Parameters, and Pundit/CanCanCan policies for missing counterparts."
---

# Missing Piece Rails

Framework discovery adapter for **Ruby on Rails & ActiveRecord**.

Provides specialized counterpart discovery, callback tracing, and association patterns unique to Rails.

## Rails Invariant Rules

### RAILS-01 — Association Cascade & Cleanup Specification
- **Trigger**: An ActiveRecord model declares `has_many` or `has_one` associations to dependent child models.
- **Expected Counterpart**: Explicit `dependent: :destroy`, `dependent: :delete_all`, or `dependent: :nullify` option on the association macro.
- **Consequence of Absence**: Parent record deletion leaves orphaned foreign-key records in the child table.

### RAILS-02 — Transactional Callback Safety (`after_commit` vs `after_save`)
- **Trigger**: A model callback triggers an external side-effect (enqueueing a Sidekiq background job, charging a credit card, sending an email).
- **Expected Counterpart**: Use of `after_commit` (or `after_create_commit`) rather than `after_save` or `after_create`.
- **Consequence of Absence**: If the database transaction rolls back, external side-effects (emails, job dispatches) have already been fired.

### RAILS-03 — Sidekiq Retries Exhausted Recovery Hook
- **Trigger**: A critical background job (e.g. syncing data with third-party service, processing payments) executes via Sidekiq.
- **Expected Counterpart**: Declaration of `sidekiq_retries_exhausted do |msg, ex| ... end` block logging to an alert channel or updating job state.
- **Consequence of Absence**: Failed jobs silently end up in the Sidekiq Dead Set without notification or state compensation.

### RAILS-04 — Strong Parameters Completeness & Mass-Assignment
- **Trigger**: A controller action updates an entity using `params.require(...).permit(...)`.
- **Expected Counterpart**: Whitelist permits only expected user-editable fields; exclusion of sensitive administrative fields (e.g. `role`, `is_admin`, `verified`).
- **Consequence of Absence**: Mass assignment privilege escalation vulnerability.

### RAILS-05 — Authorization Policy Enforcement
- **Trigger**: A controller action mutates an ActiveRecord model.
- **Expected Counterpart**: Invocation of `authorize @record` (Pundit) or `load_and_authorize_resource` (CanCanCan).
- **Counter-Evidence Check**: Verify if `after_action :verify_authorized` is declared in `ApplicationController`.
- **Consequence of Absence**: Unprotected actions bypassing application authorization boundaries.

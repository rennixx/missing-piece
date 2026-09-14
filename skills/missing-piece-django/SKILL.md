---
name: missing-piece-django
description: Django and DRF auditor for post_save/delete signal symmetry, transaction.atomic blocks, DRF permission classes, and on_commit Celery dispatch.
---

# Missing Piece Django

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

Specialized adapter for **Django & Django REST Framework (DRF)**.

## ⚡ Token-Optimal Execution Protocol
- **Signal & View Targeting**: Search `git grep -l "post_save"` or `git grep -l "APIView\|ViewSet"`. Inspect with 15–20 line slices.
- **Strict Exclusions**: Ignore migrations (`migrations/`), virtualenvs, and static asset folders.
- **Early Exit**: If `settings.py` defines global `DEFAULT_PERMISSION_CLASSES = [IsAuthenticated]`, dismiss generic view auth flags immediately.
- **Token-Sparse Findings**: Format findings with direct file links and line numbers.

## Django Invariant Rules

### DJANGO-01 — Signal Creation/Deletion Symmetry
- **Trigger**: `post_save` receiver provisions secondary resource (profile, Stripe customer).
- **Expected Counterpart**: Matching `post_delete` signal or model `delete()` cleanup.
- **Consequence**: Orphaned child profiles or external accounts left on user deletion.

### DJANGO-02 — Multi-Model Write Atomic Boundaries
- **Trigger**: View/service mutates multiple models (Order + Stock).
- **Expected Counterpart**: `with transaction.atomic():` or `@transaction.atomic`.
- **Consequence**: Partial failure leaves database in inconsistent state.

### DJANGO-03 — DRF ViewSet Permission Class Coverage
- **Trigger**: DRF ViewSet/APIView inherits generic view without explicit permissions.
- **Expected Counterpart**: `permission_classes = [IsAuthenticated, ...]` or global setting.
- **Consequence**: Unprotected endpoints exposed to anonymous users.

### DJANGO-04 — ForeignKey Cascade Explicit Semantics
- **Trigger**: Model defines `ForeignKey` or `OneToOneField`.
- **Expected Counterpart**: Explicit `on_delete=models.CASCADE` / `PROTECT` / `SET_NULL`.
- **Consequence**: Inadvertent cascade deletions destroying history.

### DJANGO-05 — Transaction Commit Celery Task Invocation
- **Trigger**: Enqueueing Celery task inside a DB mutation view.
- **Expected Counterpart**: `transaction.on_commit(lambda: task.delay(...))` instead of immediate `task.delay(...)`.
- **Consequence**: Worker race condition running before DB commit, causing `DoesNotExist`.

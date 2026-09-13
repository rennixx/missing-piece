---
name: missing-piece-django
description: Django and Django REST Framework auditor. Use when auditing Django models, signals (post_save/post_delete), transaction.atomic blocks, DRF permission classes, and Celery tasks for missing counterparts.
---

# Missing Piece Django

Framework discovery adapter for **Django & Django REST Framework (DRF)**.

Provides specialized counterpart discovery, signal tracing, and architectural patterns unique to the Django ecosystem.

## Django Invariant Rules

### DJANGO-01 — Signal Creation/Deletion Symmetry
- **Trigger**: A `post_save` signal receiver provisions a secondary resource (e.g. creating a `UserProfile` or Stripe customer on `User` creation).
- **Expected Counterpart**: A matching `post_delete` signal receiver or model `delete()` override ensuring the secondary resource is cleaned up when the primary instance is deleted.
- **Consequence of Absence**: Orphaned profile rows, billing records, or external entities left behind after user deletion.

### DJANGO-02 — Multi-Model Write Atomic Boundaries
- **Trigger**: A view or service function executes updates across multiple models or related tables (e.g. creating an Order and decrementing Stock).
- **Expected Counterpart**: Encapsulation within `with transaction.atomic():` or `@transaction.atomic`.
- **Consequence of Absence**: Partial failures leave the database in an inconsistent state (e.g. order created without stock reduction).

### DJANGO-03 — DRF ViewSet Permission Class Coverage
- **Trigger**: A DRF ViewSet or APIView inherits from generic views (`ModelViewSet`).
- **Expected Counterpart**: Explicit declaration of `permission_classes = [IsAuthenticated, ...]` or custom object permissions (`has_object_permission`).
- **Counter-Evidence Check**: Verify whether `REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES']` enforces authentication globally in `settings.py`.
- **Consequence of Absence**: Unprotected API views exposed to anonymous callers.

### DJANGO-04 — ForeignKey Cascade Explicit Semantics
- **Trigger**: A model defines a `ForeignKey` or `OneToOneField`.
- **Expected Counterpart**: Explicit `on_delete=models.CASCADE`, `models.PROTECT`, or `models.SET_NULL` matching domain intent.
- **Consequence of Absence**: Inadvertent cascade deletions destroying critical parent-child history or unhandled database integrity errors.

### DJANGO-05 — Transaction Commit Celery Task Invocation
- **Trigger**: Enqueueing a Celery task inside a view mutating database records.
- **Expected Counterpart**: `transaction.on_commit(lambda: task.delay(...))` rather than immediate `task.delay(...)`.
- **Consequence of Absence**: Race condition where Celery worker executes before database transaction commits, causing `DoesNotExist` exceptions in the worker.

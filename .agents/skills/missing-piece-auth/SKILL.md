---
name: missing-piece-auth
description: Deep identity, authentication, session lifecycle, and authorization auditor. Use when auditing JWT revocation, password reset side-effects, multi-tenant isolation, RBAC policy matrices, and API key management for missing guards.
---

# Missing Piece Auth

Specialized security auditor for identity, sessions, multi-tenancy, and authorization boundaries.

Most authorization vulnerabilities are not broken encryption or complex cryptographic attacks—they are **omissions**: a developer writes a new admin endpoint but forgets to attach the authorization guard, or deletes a user but leaves their active JWT tokens valid.

## Deep Auth Invariant Rules

### AUTH-01 — Credential Change Session Invalidation
- **Trigger**: A user changes their password, resets credentials, or enables 2FA.
- **Expected Counterpart**: Immediate revocation/invalidation of all existing active sessions, refresh tokens, and remember-me cookies for that user account.
- **Consequence of Absence**: An attacker who compromised a session retains full access even after the legitimate owner resets their password.

### AUTH-02 — Multi-Tenant Row-Level Isolation
- **Trigger**: Database queries mutating, reading, or deleting resources by an ID provided in request parameters (e.g. `PATCH /api/projects/:id`).
- **Expected Counterpart**: Inclusion of tenant identifier (`tenant_id` / `org_id` / `account_id`) in the database query `WHERE` predicate or ORM query scope.
- **Consequence of Absence**: Insecure Direct Object References (IDOR) allowing cross-tenant data leakage or tampering by manipulating IDs.

### AUTH-03 — User Deletion / Suspension Revocation Cascades
- **Trigger**: An account is suspended, soft-deleted, or removed (`users.status = 'banned'`).
- **Expected Counterpart**:
  1. Revocation of active API keys and personal access tokens.
  2. Invalidation of active OAuth client grants.
  3. Purge of webhook signing secrets and background integrations.
- **Consequence of Absence**: Banned or deleted users continue executing programmatic API requests using previously issued persistent tokens.

### AUTH-04 — Role & Permission Symmetry
- **Trigger**: An administrative route or mutation is introduced into the system router.
- **Expected Counterpart**: Inclusion in the central RBAC/ABAC policy matrix or application of role guards (`@require_permission("admin:write")`).
- **Consequence of Absence**: Endpoints unintentionally exposed to anonymous or regular authenticated users.

### AUTH-05 — API Key Secret Hashing & Truncation
- **Trigger**: System issues API keys or secrets to users.
- **Expected Counterpart**: Keys are hashed (SHA-256) before database storage, and displayed in plaintext only once at creation time.
- **Consequence of Absence**: Database compromise reveals all third-party integration API keys in cleartext.

## Auth Audit Procedure

1. Identify entry points (`routes`, `controllers`, `resolvers`).
2. Map authentication middleware, decorators, and policy definitions.
3. Cross-reference mutation routes against the permission matrix.
4. Verify session termination triggers and tenant isolation scoping.

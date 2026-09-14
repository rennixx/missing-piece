---
name: missing-piece-auth
description: Deep identity, authentication, session lifecycle, and authorization auditor for JWT revocation, password reset side-effects, multi-tenant isolation, RBAC matrices, and API key guards.
---

# Missing Piece Auth

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

Specialized security auditor for identity, sessions, multi-tenancy, and authorization boundaries.

## ⚡ Token-Optimal Execution Protocol
- **Grep-first, Slice-second**: Use file-list search (`git grep -l`) first. Inspect matches with 15–25 line slices. Never dump full files (>100 lines).
- **Strict Exclusions**: Ignore lockfiles, minified assets, `dist/`, `build/`, `.next/`, `node_modules/`, and mock fixtures.
- **Early-Exit Short-Circuit**: The moment an auth middleware, tenant-scoped ORM base, or policy guard is verified, terminate the detector pass immediately.
- **Token-Sparse Findings**: Format findings with direct file links and exact line numbers; avoid repeating large source code blocks.

## Deep Auth Invariant Rules

### AUTH-01 — Credential Change Session Invalidation
- **Trigger**: A user changes password, resets credentials, or enables 2FA.
- **Expected Counterpart**: Immediate revocation of active sessions, refresh tokens, and cookies.
- **Consequence**: Compromised sessions remain usable after credential reset.

### AUTH-02 — Multi-Tenant Row-Level Isolation
- **Trigger**: DB queries mutating or reading resources by user-provided ID (`PATCH /api/projects/:id`).
- **Expected Counterpart**: Tenant identifier (`tenant_id` / `org_id`) in DB query `WHERE` predicate or ORM scope.
- **Consequence**: IDOR allowing cross-tenant data leakage or tampering.

### AUTH-03 — User Deletion / Suspension Revocation Cascades
- **Trigger**: Account suspended, soft-deleted, or banned.
- **Expected Counterpart**: Revocation of active API keys, OAuth grants, and webhook signing secrets.
- **Consequence**: Banned users continue programmatic API access via existing keys.

### AUTH-04 — Role & Permission Symmetry
- **Trigger**: Administrative route or mutation introduced into router.
- **Expected Counterpart**: Inclusion in central RBAC/ABAC policy matrix or `@require_permission` guard.
- **Consequence**: Endpoints unintentionally exposed to anonymous or regular authenticated users.

### AUTH-05 — API Key Secret Hashing & Truncation
- **Trigger**: System issues API keys or secrets.
- **Expected Counterpart**: Keys hashed (SHA-256) before DB storage; shown in plaintext only once at creation.
- **Consequence**: Database leak exposes all integration API keys in cleartext.

## Auth Audit Procedure

1. **Map Entry Points**: Identify routes, controllers, and resolvers.
2. **Inspect Boundaries**: Map authentication middleware, decorators, and policy definitions.
3. **Cross-Reference**: Check mutation routes against the permission matrix.
4. **Verify Revocation**: Trace credential changes and verify session/token invalidation triggers.

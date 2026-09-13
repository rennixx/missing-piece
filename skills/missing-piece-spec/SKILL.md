---
name: missing-piece-spec
description: Cross-reference external API specifications, GraphQL schemas, database models, and PRDs against code to detect promised-but-unimplemented contracts, routes, and fields. Use when checking API schema drift, verifying OpenAPI/GraphQL contract completeness, or comparing product requirements against actual implementation.
---

# Missing Piece Spec

The contract-to-code gap reconciler.

`missing-piece-spec` inspects external contracts, API schemas, and architectural specifications, cross-referencing them against active application routes and models to surface:

> **What has been declared, promised, or specified, but never implemented in the code?**

## Target Contract Surfaces

1. **OpenAPI / Swagger (`openapi.json`, `openapi.yaml`, Swagger docs)**
   - Endpoints defined in the schema with no corresponding route controller.
   - Status codes promised (e.g. `404 Not Found`, `409 Conflict`, `422 Unprocessable`) that the handler cannot emit.
   - Enum values defined in schema schemas but omitted from server switch/match expressions.

2. **GraphQL Schemas (`schema.graphql`, `.gql` files)**
   - Mutations declared in the schema without a registered resolver.
   - Non-nullable fields on types that the backend query resolvers never populate.
   - Subscription events defined in schema with no active publishing triggers.

3. **Database Schemas & ORM Models (Prisma, SQL migrations, Django models)**
   - Tables with declared foreign keys that lack deletion cascade / restrict rules.
   - Database columns defined but never written or read by any application query.
   - Status enums defined in SQL migrations that do not match application enums.

4. **Product Requirements & Architectural Documents (`docs/PRD.md`, specs)**
   - Documented feature lifecycles with missing endpoints.
   - Documented user roles missing from backend authorization checks.

## Spec Reconciliation Procedure

### 1. Ingest Specification Documents
Scan repository for contract files:
- `openapi.json`, `openapi.yaml`, `swagger.json`
- `*.graphql`, `*.gql`
- `schema.prisma`, `migrations/*.sql`
- `docs/PRD.md`, `docs/ARCHITECTURE.md`

### 2. Parse Declared Contracts
Extract an inventory of:
- Declared endpoints `(METHOD, PATH)`
- Declared mutations and queries
- Declared schema enums and required fields

### 3. Trace Application Implementation
Search repository route registrations, router files, decorators, and resolver maps:
- Map each declared contract item to its corresponding application implementation.
- Verify reachability and invocation.

### 4. Report Contract Gaps
Generate a structured discrepancy report highlighting missing implementations and schema drift.

```markdown
## 🧩 Missing Piece Spec Reconciliation

| Contract Source | Declared Item | Status | Application Gap |
|---|---|---|---|
| `openapi.yaml` | `DELETE /v1/teams/{id}` | Missing | Route defined in spec, but no controller registered in `/api` |
| `schema.graphql` | `cancelSubscription` | Incomplete | Mutation resolver exists but does not populate promised `refundAmount` |
```

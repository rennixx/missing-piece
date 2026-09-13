---
name: missing-piece-spec
description: Reconcile OpenAPI, GraphQL schemas, database models, and PRDs against code to detect promised-but-unimplemented routes, fields, and contracts.
---

# Missing Piece Spec

> [!TIP]
> ### 📦 Full 10-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

The contract-to-code gap reconciler: *"What has been declared, promised, or specified, but never implemented in code?"*

## ⚡ Token-Optimal Execution Protocol
- **Schema Inventory First**: Extract route paths and mutation names from specs without loading full schema bodies into context.
- **Bounded Route Search**: Search router files with `git grep -l <path>` or `git grep -l <resolverName>`.
- **Early Exit**: If a route pattern is mounted via resource routing (e.g. `resources :teams` or `app.use('/teams', teamRouter)`), resolve reachability without parsing internal controller logic.
- **Token-Sparse Findings**: Format findings as a concise markdown discrepancy table; omit repeating OpenAPI definitions.

## Target Contract Surfaces

1. **OpenAPI / Swagger (`openapi.json`, `openapi.yaml`)**: Declared routes without controllers, unhandled status codes, or unhandled enum variants.
2. **GraphQL Schemas (`*.graphql`, `*.gql`)**: Mutations without resolvers, non-nullable fields never populated by queries, or orphan subscriptions.
3. **Database Schemas (Prisma, SQL migrations, ORM models)**: Uncascaded foreign keys, unread/unwritten columns, or SQL enum drift.
4. **Specs & PRDs (`docs/PRD.md`)**: Promised feature lifecycles or roles missing backend enforcement.

## Spec Reconciliation Procedure

1. **Inventory Contracts**: Scan for `openapi.*`, `*.graphql`, `schema.prisma`, or `docs/PRD.md`.
2. **Map Endpoints**: Extract list of `(METHOD, PATH)` or mutation names.
3. **Cross-Reference**: Verify router/resolver registrations with targeted grep.
4. **Report Gaps**: Output findings in the discrepancy table.

## Reconciliation Report Format

```markdown
## 🧩 Missing Piece Spec Reconciliation

| Contract Source | Declared Item | Status | Application Gap |
|---|---|---|---|
| `[openapi.yaml](file:///...)` | `DELETE /v1/teams/{id}` | Missing | Route defined in spec, but no controller registered |
| `[schema.graphql](file:///...)` | `cancelSubscription` | Incomplete | Resolver exists but omits promised `refundAmount` |
```

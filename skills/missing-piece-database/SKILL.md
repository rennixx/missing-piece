---
name: missing-piece-database
description: Database, SQL migration, and ORM auditor for schema drift, irreversible down migrations, missing cascade deletes, and unindexed foreign keys.
---

# Missing Piece: Database & Migration Auditor

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> Install with the interactive selector: px skills add rennixx/missing-piece\ (or \--all\).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*


Audits database migrations, schemas, and ORM models (Prisma, Drizzle, SQLAlchemy, Django ORM, ActiveRecord, TypeORM, raw SQL) for schema drift, orphan record vulnerabilities, and rollback omissions.

## Core Invariant

Never critique query style or indexing choices. Report only when an observed database structure strictly implies a missing structural counterpart (down migration, cascade constraint, foreign key index, or ORM field mirror).

## Token-Optimal Execution

1. **Grep-first, Slice-second**: Search migrations (`migrations/`, `prisma/schema.prisma`, `alembic/`) with `git grep -l` before reading 15–20 line slices.
2. **Early Disproof**: Short-circuit when ORM automatically manages relation cascades, database triggers exist, or migrations use automated rollback engines (e.g. Prisma Migrate, Rails `change`).
3. **Sparse Reporting**: Cite exact migration files and line numbers with markdown links.

## Detector Matrix

| Code | Sub-family | Observed Fact -> Expected Counterpart | Instant Disproof / Skip Rule |
| :--- | :--- | :--- | :--- |
| `MP-DB-SD` | Schema Drift | Migration adds/alters column -> Implies model/serializer/entity definition updated | Column is internal-only or managed via dynamic JSON field |
| `MP-DB-DM` | Down Migration | Migration has explicit `up()` method -> Implies corresponding reversible `down()` method | Migration framework uses reversible `change()` block |
| `MP-DB-CD` | Cascade Delete | Parent-child ForeignKey defined -> Implies `ON DELETE CASCADE` or orphan cleanup handler | Nullable foreign key where `ON DELETE SET NULL` is applied |
| `MP-DB-IX` | Foreign Key Index | ForeignKey column created -> Implies index on foreign key for join performance | Unique constraint already creates implicit index |
| `MP-DB-SDT`| Soft Delete Symmetry | Model implements `deleted_at`/`is_deleted` -> Implies queries and cascade relations filter soft deletes | Global ORM soft-delete plugin/middleware configured |

## Audit Procedure

1. **Inventory Migrations & Models**: Locate schema directory (`db/`, `migrations/`, `prisma/`, `alembic/`) and ORM models.
2. **Inspect Migration Symmetry**:
   - Check `up()` vs `down()` rollback parity in raw SQL or migration scripts.
   - For every `CREATE TABLE` or `ADD COLUMN`, verify the `down()` contains the reverse `DROP TABLE` or `DROP COLUMN`.
3. **Verify Relational Integrity**:
   - Check ForeignKeys: Are child records protected against orphaned states (`CASCADE` or `SET NULL`)?
   - Check join keys: Does every foreign key column have a corresponding index?
4. **Audit ORM Drift**:
   - For newly added migration columns, verify matching attribute in the ORM entity/model and API serializer/schema.
5. **Score & Report**: Format with Observed, Expected, Evidence searched, Gap, Why it matters, Verification using standard report template.

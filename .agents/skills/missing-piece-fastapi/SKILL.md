---
name: missing-piece-fastapi
description: FastAPI and Starlette auditor for lifespan teardowns, session yield cleanups, background task error handling, and router security guards.
---

# Missing Piece: FastAPI Framework Auditor

Audits FastAPI, Starlette, and Pydantic applications for missing lifespan teardowns, leaked database sessions in `Depends()`, unhandled background exceptions, and router security asymmetry.

## Core Invariant

Never flag standard Python style or Pydantic validation choices. Report only when an observed FastAPI construct strictly implies a missing operational counterpart.

## Token-Optimal Execution

1. **Grep-first, Slice-second**: Search `main.py`, `dependencies.py`, and `routers/` with `git grep -l` before inspecting 15–20 line slices.
2. **Early Disproof**: Short-circuit when session closing is handled via context managers (`with SessionLocal() as db:`), lifespan uses `contextlib.asynccontextmanager`, or router-level dependencies enforce auth globally.
3. **Sparse Reporting**: Cite exact router files, function decorators, and line numbers.

## Detector Matrix

| Code | Sub-family | Observed Fact -> Expected Counterpart | Instant Disproof / Skip Rule |
| :--- | :--- | :--- | :--- |
| `MP-FA-LS` | Lifespan Teardown | `@asynccontextmanager` startup resource initialized -> Implies cleanup/close after `yield` | Stateless app without persistent connections or engine pool |
| `MP-FA-SY` | Session Yield Leak | `Depends(get_db)` yields connection/session -> Implies `finally: db.close()` teardown | Context manager (`with Session() as s: yield s`) auto-closes |
| `MP-FA-BG` | BackgroundTasks | `background_tasks.add_task(fn)` called -> Implies exception handling or logging inside `fn` | Task worker has global unhandled exception handler |
| `MP-FA-SC` | Status Code Asymmetry| POST route creates resource -> Implies `status_code=status.HTTP_201_CREATED` | Explicitly documented as 200 RPC-style action |
| `MP-FA-RG` | Router Security Guard| Root router enforces `dependencies=[Depends(verify_token)]` -> Implies sub-routers preserve auth | Route explicitly marked public via endpoint dependency override |

## Audit Procedure

1. **Inspect Application Lifespan**:
   - Locate `FastAPI(lifespan=...)`. If database connection pool, Redis client, or HTTP client is created before `yield`, verify proper `.close()` or `.disconnect()` follows `yield`.
2. **Inspect Database Session Dependencies**:
   - Check `get_db()` or session generator. Verify pattern uses `try: yield db finally: db.close()`.
3. **Audit Background Tasks**:
   - Grep for `background_tasks.add_task`. Inspect target function to ensure unhandled exceptions do not silently drop without logging or alerting.
4. **Audit Router Authorization Symmetry**:
   - Check `app.include_router()`. If parent router is protected, verify nested routers or newly mounted endpoints do not inadvertently bypass dependencies.
5. **Score & Report**: Format findings using standard report template with Observed, Expected, Evidence searched, Gap, Why it matters, Verification.

---
name: missing-piece-nextjs
description: Next.js App Router auditor for Server Action authorization, route handlers, revalidatePath/Tag cache invalidation, and streaming error boundaries.
---

# Missing Piece Next.js

> [!TIP]
> ### 📦 Full 12-Skill Missing Piece Suite
> Install with the interactive selector: `npx skills add rennixx/missing-piece` (or `--all`).
> 🔗 *Hub: [skills.sh/rennixx/missing-piece](https://skills.sh/rennixx/missing-piece)*

Specialized adapter for **Next.js (App Router & Pages Router)**.

## ⚡ Token-Optimal Execution Protocol
- **Focused Inspection**: Grep `"use server"` or route handlers directly with `git grep -l "use server"`.
- **Slice Inspection**: Inspect Server Actions with 15–20 line slices. Never dump whole client components.
- **Strict Exclusions**: Ignore `.next/`, `node_modules/`, and build outputs.
- **Early Exit**: If `revalidatePath` or `revalidateTag` is present in the mutation or downstream action, terminate check immediately.
- **Token-Sparse Findings**: Use direct file links with line numbers; omit repeating component JSX.

## Next.js Invariant Rules

### NEXT-01 — Server Action Authorization & Validation
- **Trigger**: Async function with `"use server"` mutating state.
- **Expected Counterpart**: Auth/session check (`auth()`) and schema validation inside action body. Middleware does NOT protect standalone Server Action POST IDs.
- **Consequence**: Publicly callable Server Action allowing unauthorized database writes.

### NEXT-02 — Mutation Cache Revalidation Completeness
- **Trigger**: Server Action or route handler (`app/api/**/route.ts`) mutating an entity.
- **Expected Counterpart**: `revalidatePath(...)` or `revalidateTag(...)` to purge stale cached pages.
- **Consequence**: Stale cache persists, prompting duplicate user submissions.

### NEXT-03 — Route Handler CSRF & Session Verification
- **Trigger**: Mutation Route Handler (`POST`, `PUT`, `DELETE`) in `app/api/`.
- **Expected Counterpart**: Session check and Origin/Referer verification for cookie auth.

### NEXT-04 — Dynamic Route Parameter 404 Guards
- **Trigger**: Dynamic route segment `app/[id]/page.tsx`.
- **Expected Counterpart**: `notFound()` invocation when query returns null.

### NEXT-05 — Streaming Error & Loading Boundaries
- **Trigger**: Async server component with streaming data fetch.
- **Expected Counterpart**: `loading.tsx` and `error.tsx` boundary files in the route segment.

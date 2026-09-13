---
name: missing-piece-nextjs
description: Next.js App Router and full-stack React framework auditor. Use when auditing Next.js Server Actions, route handlers, cache revalidations (revalidatePath/revalidateTag), middleware authentication, and streaming boundaries for missing guards.
---

# Missing Piece Next.js

Framework discovery adapter for **Next.js (App Router & Pages Router)**.

Provides specialized counterpart discovery, counter-evidence rules, and architectural patterns unique to the Next.js runtime.

## Next.js Invariant Rules

### NEXT-01 — Server Action Mutation Authorization & Input Validation
- **Trigger**: An asynchronous function marked with `"use server"` mutates database records or invokes backend services.
- **Expected Counterpart**: Explicit authentication/session check and Zod/schema input validation inside the action body.
- **Counter-Evidence Check**: Do not assume middleware protects Server Actions; Next.js Server Actions can be invoked via raw POST requests using their action ID.
- **Consequence of Absence**: Publicly callable Server Action allowing unauthorized users to trigger backend state mutations.

### NEXT-02 — Mutation Cache Revalidation Completeness
- **Trigger**: A Server Action or Route Handler (`app/api/**/route.ts`) creates, updates, or deletes an entity.
- **Expected Counterpart**: Corresponding `revalidatePath(...)` or `revalidateTag(...)` invocation to purge stale static/cached UI representations.
- **Consequence of Absence**: User performs an action (e.g. edit profile, delete post) but UI continues showing stale cached data, confusing users into duplicate submissions.

### NEXT-03 — Route Handler Authentication & CSRF Boundaries
- **Trigger**: A mutation Route Handler (`POST`, `PUT`, `DELETE`, `PATCH`) in `app/api/`.
- **Expected Counterpart**: Session verification (`auth()`, `getServerSession()`) and Origin/Referer verification if cookie authentication is used.

### NEXT-04 — Dynamic Route Parameter Parsing & Not Found Handling
- **Trigger**: Dynamic route page `app/[tenant]/[id]/page.tsx`.
- **Expected Counterpart**: `notFound()` invocation when database query returns null or when user lacks access, rather than rendering empty or broken UI templates.

### NEXT-05 — Streaming Error & Suspense Boundaries
- **Trigger**: Server components executing asynchronous data fetching with streaming.
- **Expected Counterpart**: Corresponding `loading.tsx` and `error.tsx` boundary files in the route segment to prevent unhandled promise rejections from crashing the whole page tree.

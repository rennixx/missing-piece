# Test Strategy

## 1. Skill syntax tests
Validate:
- `SKILL.md` exists;
- frontmatter parses;
- `name` and `description` are present;
- references use valid relative paths;
- no accidental unsupported mandatory frontmatter.

## 2. Behavioral fixtures
Each detector family has synthetic repositories and expected results.

## 3. Regression snapshots
Store expected:
- finding presence/absence;
- detector family;
- confidence band;
- evidence anchors.

Do not snapshot prose exactly unless necessary.

## 4. Adversarial tests

### Misleading naming
Implement counterpart under unrelated but semantically valid symbol.

### Cross-cutting implementation
Put authorization in middleware/decorator/database.

### External provider
Document explicit delegation.

### Generated code
Ensure generated/vendor trees do not dominate analysis.

### Monorepo
Same concept exists in different package.

### Partial feature
Route exists, handler stub exists, side effect missing.

### Dead path
Incomplete code exists but is unreachable.

## 5. Prompt robustness

Test user phrasing:
- "find missing pieces";
- "audit payments";
- "is anything forgotten?";
- "review this diff";
- "deep audit";
- "only show high confidence."

## 6. Performance sanity

Agent-only v1 should:
- avoid reading every file blindly;
- inventory first;
- search selectively;
- stop low-yield branches;
- prioritize high-impact domains.

## 7. Release gate

Do not publish a detector change if:
- precision falls materially;
- it emits generic advice;
- counter-evidence behavior regresses;
- finding schema breaks;
- examples become inconsistent with methodology.

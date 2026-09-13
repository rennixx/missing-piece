# Agent Skills Ecosystem Notes

These notes capture the packaging assumptions used by this bundle as of September 2026.

## Current assumptions

- The `skills` CLI can be run through `npx`.
- Skills are repository directories containing `SKILL.md`.
- Minimal `SKILL.md` frontmatter uses `name` and `description`.
- Repositories can expose one or multiple skills.
- The CLI supports agent-targeted and global installation patterns.
- Cross-agent discovery commonly includes agent-specific skill directories.

## Release rule

Treat CLI flags and destination paths as **release-time facts**, not permanent product invariants.

Before publishing a release:
1. check the current skills.sh CLI documentation;
2. test the install command from a clean environment;
3. update README examples if syntax changed.

## Sources consulted for this specification

- skills.sh — CLI Reference: https://www.skills.sh/docs/cli
- skills.sh — Documentation: https://www.skills.sh/docs
- Vercel Labs/community skill repositories demonstrating `SKILL.md` discovery and `npx skills add` conventions.

The product should remain compatible with the simple `SKILL.md` convention even if higher-level CLI behavior evolves.

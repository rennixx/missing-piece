# Distribution and Installation

## Distribution model

Missing Piece should be published as a GitHub repository compatible with the Agent Skills ecosystem.

The `skills` CLI currently supports installing skills from repositories containing `SKILL.md`.

Canonical intended commands after publishing:

```bash
npx skills add <owner>/missing-piece --skill missing-piece
```

Global:

```bash
npx skills add <owner>/missing-piece --skill missing-piece -g
```

Codex-targeted:

```bash
npx skills add <owner>/missing-piece --skill missing-piece -g -a codex
```

List/discover:

```bash
npx skills add <owner>/missing-piece --list
```

Exact flags should be verified against the current `skills` CLI before release.

## Repository discovery layout

Recommended:

```text
missing-piece/
├── skills/
│   ├── missing-piece/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── templates/
│   ├── missing-piece-complete/
│   └── ... (12 specialized skills)
├── docs/
│   ├── examples/
│   └── ...
├── README.md
├── AGENTS.md
├── LICENSE
└── CHANGELOG.md
```

## Why not an npm package first?

The user-facing `npx skills ...` workflow does not require Missing Piece itself to be an npm package. The CLI installs the skill from its source repository.

Avoid unnecessary packaging complexity in v1.

## Publishing checklist

- public GitHub repository;
- MIT license;
- polished README;
- install examples;
- example findings;
- skill validates;
- no secrets;
- benchmark status documented;
- changelog initialized;
- release tag;
- optional submission/discovery through skills.sh ecosystem.

## Versioning

Use semantic versioning:
- patch: wording, examples, false-positive fixes;
- minor: detector family/rule additions;
- major: output contract or fundamental methodology changes.

## Compatibility

Keep the skill agent-agnostic.

Do not depend on agent-specific commands unless documented as optional adapters.

# Positioning and Go-to-Market

## Category

**Absence analysis** / **software completeness auditing**

## One-liner

> Missing Piece finds software behavior that is implied by your system but appears to be missing.

## Taglines

Primary:
> **Find what your software forgot.**

Technical:
> **Linters find bad code. Tests find broken behavior. Missing Piece finds the code that should exist but doesn't.**

Alternative:
> **Review the negative space in your codebase.**

## Differentiation

Do not position as:
- "AI code review";
- "AI linter";
- "security scanner";
- "architecture copilot".

Position around the unique question:
> What must exist because of what already exists?

## Demo strategy

The strongest demo is a real repository with a non-obvious finding.

Demo format:
1. show feature;
2. run Missing Piece;
3. show one surprising omission;
4. trace evidence;
5. fix it;
6. re-audit.

## Viral artifact

A shareable finding card:

```text
Missing Piece found:
Order cancellation refunds payment but never releases reserved inventory.
Confidence: 94%
Severity: High
```

Avoid fake dramatic numbers.

## Launch channels

- GitHub;
- skills.sh ecosystem;
- developer communities;
- X/LinkedIn technical demo posts;
- Reddit programming/tool communities where self-promotion rules allow;
- Hacker News when the benchmark/demo is substantive.

## Open-source strategy

Recommended v1:
- core skill: MIT/open;
- rule methodology: open;
- fixtures: open.

Possible future commercial layers:
- organization rule packs;
- multi-repo engine;
- CI baselines/history;
- team policy packs;
- private repository analytics.

Do not cripple the free skill to force monetization.

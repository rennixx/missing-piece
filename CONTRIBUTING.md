# Contributing

Contributions are welcome, especially:
- false-positive reductions;
- benchmark fixtures;
- detector-rule refinements;
- framework discovery adapters;
- real-world anonymized examples.

## Rule contribution requirements

A new rule must include:
1. trigger;
2. expected counterpart;
3. exceptions;
4. evidence search strategy;
5. counter-evidence;
6. positive fixture;
7. negative fixture;
8. exception fixture when applicable.

Rules without controls should not be merged.

## Philosophy

Prefer one general, well-tested invariant over ten framework-specific heuristics.

Do not add:
- style preferences;
- generic best practices;
- speculative product features;
- unrelated vulnerability checks.

## Reporting false positives

Include:
- finding text;
- relevant architecture/context;
- where the supposed counterpart actually lives;
- whether a rule or search strategy caused the error.

False-positive fixes are treated as high-value contributions.

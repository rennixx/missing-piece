# Agent Instructions

This repository builds **Missing Piece**, an installable agent skill for discovering absent-but-implied software behavior.

## Product invariant

Never let the implementation collapse into a generic code reviewer.

A valid Missing Piece finding must have all of the following:
1. an observed system fact;
2. a rule or relationship that implies an expected counterpart;
3. a repository search for that counterpart;
4. evidence that the counterpart is absent, incomplete, unreachable, or inconsistent;
5. a confidence score;
6. a concise explanation of possible consequence.

If any of these are missing, downgrade the result to an observation or suppress it.

## Working rules

- Work on the main branch unless explicitly instructed otherwise.
- Prefer small, reviewable commits.
- Do not silently add network services, telemetry, accounts, databases, or hosted dependencies.
- The baseline skill must function locally using the host agent's repository tools.
- Keep the core framework-agnostic.
- Framework knowledge belongs in optional adapters/rule packs.
- Do not auto-edit audited repositories in audit mode.
- Never claim absence merely because an exact filename or symbol was not found.
- Search semantically and structurally before concluding.
- Severity and confidence are separate dimensions.
- Every detector needs positive and negative fixtures before release.
- Preserve deterministic report structure even when reasoning is probabilistic.

## Documentation precedence

1. `docs/PRD.md`
2. `docs/ARCHITECTURE.md`
3. `docs/DETECTION_METHODOLOGY.md`
4. `skills/missing-piece/SKILL.md`
5. detector reference documents

When conflicts are found, update the lower-priority document or raise the inconsistency explicitly.

## Definition of done

A change is done only when:
- behavior is specified;
- fixtures or benchmark cases cover it;
- false-positive risks are documented;
- report semantics remain valid;
- install/discovery behavior remains compatible with the intended skills ecosystem.

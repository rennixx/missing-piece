# User Flows and Invocation

Skills may auto-activate based on description, so Missing Piece must support natural language rather than depend on slash commands.

## Canonical user requests

### Full audit
- "Audit this repo with Missing Piece."
- "Find missing behavior in this project."
- "What did this system forget to implement?"

### Focused audit
- "Run Missing Piece on the payment flow."
- "Audit account deletion for missing lifecycle behavior."
- "Only check authorization and cleanup."

### Change audit
- "Audit the feature I just added for missing counterparts."
- "Check this diff for missing behavior."
- "Before I merge this, run Missing Piece."

### Explain
- "Explain MP-FR-002."
- "Why do you think this retry path is incomplete?"

### Re-audit
- "I fixed the findings. Run it again."
- "Compare against the previous Missing Piece audit."

## Internal modes

The skill recognizes:

`standard`
- balanced, high-precision default.

`deep`
- broader search, medium-confidence findings included.

`focused`
- specific domain/feature/detector family.

`change`
- start from changed files but expand to connected behavior.

`re-audit`
- verify prior findings and find newly exposed gaps.

## Default behavior

If the user simply asks to audit:
- use standard mode;
- inspect the whole relevant repository;
- avoid asking questions unless access/scope is impossible;
- report only meaningful findings.

## Interaction philosophy

Do not force the user through a wizard.

Infer scope from:
- current repository;
- task wording;
- open feature context;
- changed files if explicitly requested.

Ask only when two interpretations would materially change the audit.

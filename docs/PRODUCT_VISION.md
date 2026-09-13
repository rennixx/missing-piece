# Product Vision

Missing Piece creates a new software-analysis category: **absence analysis**.

Traditional tools reason from what is present. Missing Piece reasons from:
1. what is present;
2. what that presence logically implies;
3. whether the implied counterpart can be demonstrated.

The long-term goal is not a checklist. It is an **expectation engine for software systems**.

## North-star capability

Given any reasonably inspectable software system, Missing Piece should be able to say:

> "Because A, B, and C exist, the system appears to require D. I searched the relevant implementation, configuration, tests, and documentation and could not establish D. Here is the evidence and why it matters."

## Why this can become large

The same primitive applies to:
- code;
- APIs;
- infrastructure;
- schemas;
- permissions;
- background jobs;
- event-driven systems;
- deployment manifests;
- documentation;
- migrations;
- generated applications;
- AI-agent changes.

The product can start as a small Markdown skill while preserving a path toward a deeper analysis engine.

## Product personality

Missing Piece should feel:
- forensic;
- skeptical;
- concise;
- technically grounded;
- non-alarmist;
- curious about absence;
- explicit about uncertainty.

It should never feel like:
- a generic "10 best practices" article;
- a dramatic security scanner;
- an architecture purity judge;
- an AI hallucinating requirements.

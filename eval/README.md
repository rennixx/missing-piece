# Missing Piece Evaluation Suite

A standardized, repeatable evaluation suite for assessing the precision, discovery recall, intent accuracy, and evidence quality of the **Missing Piece** skill.

## 1. Directory Structure

```
eval/
├── fixtures/
│   ├── dev/                  # Development fixture set (6 varied test codebases)
│   │   ├── dev_route_guard_asymmetry/
│   │   ├── dev_misleading_mock/
│   │   ├── dev_intentional_admin_override/
│   │   ├── dev_unknown_intent_concurrency/
│   │   ├── dev_external_webhook_delegation/
│   │   └── dev_complete_lifecycle/
│   └── heldout/              # Held-out fixture set (6 varied test codebases)
│       ├── heldout_asymmetric_error_recovery/
│       ├── heldout_mock_db_cascade/
│       ├── heldout_lww_explicit_tradeoff/
│       ├── heldout_orphan_media_cleanup/
│       ├── heldout_ambiguous_status_transition/
│       └── heldout_complete_symmetry/
├── answers/                  # Ground truth answer keys (isolated from evaluator)
│   ├── dev_ground_truth.json
│   └── heldout_ground_truth.json
├── eval_harness.py           # Evaluation test runner and metrics computer
└── README.md                 # Running instructions and documentation
```

## 2. Evaluation Principles

1. **Candidate-Specific Clearance**: Ensures guards or exceptions on one endpoint/caller do not terminate detector passes for sibling routes in the same module.
2. **Critical Test & Mock Inspection**: Evaluates whether auditors inspect test doubles to understand verification limitations, without mistaking passing unit mocks for real production database or queue behavior.
3. **Intent vs. Defect Dispositions**: Verifies whether auditors distinguish confirmed defects (violations of explicit requirements) from accepted tradeoffs (admin overrides, documented LWW, best-effort cleanup, cloud lifecycle rules) and intent-dependent behaviors (undocumented concurrency or state transitions).
4. **Claim-Level Evidence**: Verifies that every finding articulates its requirement source, reachable trigger/permissions, observed vs. expected behavior, disproof searches, grounded consequence, and verification with remaining uncertainty.
5. **Coverage Honesty**: Enforces honest recording of bounded passes via a structured coverage ledger, preventing claims of exhaustive safety from limited passes.
6. **Isolated Answer Keys & Fresh Evaluators**: Ground truth answer keys reside in `eval/answers/`, completely separate from the fixture directories presented to auditors.

## 3. Running the Evaluation

To evaluate baseline behavior across all sets:
```bash
python eval/eval_harness.py --version baseline --set all
```

To evaluate revised skill behavior across all sets:
```bash
python eval/eval_harness.py --version revised --set all
```

To evaluate consistency across repeated runs:
```bash
python eval/eval_harness.py --version revised --repeat 3
```

## 4. Evaluated Metrics

- **Precision**: $TP / (TP + FP)$ — proportion of reported confirmed defects and likely gaps that are genuine issues.
- **Recall**: $TP / (TP + FN)$ — proportion of seeded omissions discovered.
- **Intent Errors**: Raw count of instances where accepted tradeoffs were flagged as defects, or where genuine defects were dismissed as intentional.
- **Evidence Errors**: Raw count of early-exit short-circuit drops, mock confusion errors, or unsupported reachability claims.
- **Coverage Honesty**: Percentage of audits providing a faithful coverage ledger tracking inspected boundaries.
- **Verification Cost**: Total files inspected and search queries executed.

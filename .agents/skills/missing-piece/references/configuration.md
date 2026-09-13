# Project Configuration & Suppression (`.missingpiecerc.json`)

When initiating an audit, the agent should check for `.missingpiecerc.json` or `missing-piece.config.json` at the root of the target repository.

## Configuration Schema

```json
{
  "version": "1.0",
  "minConfidence": 0.85,
  "minSeverity": "Medium",
  "excludePaths": ["tests/**", "fixtures/**", "dist/**"],
  "externalBoundaries": [
    {
      "trigger": "stripe.webhook.charge.succeeded",
      "counterpartLocation": "External service: billing-worker-service",
      "reason": "Webhook events are routed directly to AWS SQS and consumed by the standalone billing worker."
    }
  ],
  "suppressions": [
    {
      "id": "SUPPRESS-001",
      "detector_family": "MP-LC",
      "file": "src/cache/ephemeral_pool.py",
      "symbol": "EphemeralConnectionPool",
      "reason": "Intentional architectural design: connections persist for container lifecycle."
    }
  ]
}
```

## Agent Behavior

1. **Path Exclusions**: Do not generate omission findings for files matching `excludePaths`.
2. **External Boundaries**: If an expected counterpart is declared under `externalBoundaries`, treat this as proof of an intentional out-of-repo counterpart. Do not report as absent.
3. **Suppressions**: If an observed gap matches an entry in `suppressions`, suppress the finding from the report.
4. **Filtering**: Do not include findings below `minConfidence` or `minSeverity` unless running with `--verbose`.

#!/usr/bin/env python3
"""
export_sarif.py

Converts Missing Piece audit findings into standard SARIF 2.1.0 format
compatible with GitHub Code Scanning alerts (actions/upload-sarif).
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Any, Dict, List

TOOL_NAME = "Missing Piece"
TOOL_VERSION = "1.3.0"
TOOL_URI = "https://github.com/rennixx/missing-piece"

SEVERITY_MAP = {
    "Critical": "error",
    "High": "error",
    "Medium": "warning",
    "Low": "note",
    "Info": "note",
}

RULES = {
    "MP-LC": {"name": "LifecycleCompleteness", "desc": "Object, session, connection, or entity lifecycle lacks counterpart cleanup, revocation, or teardown."},
    "MP-ST": {"name": "StateMachineCompleteness", "desc": "State transitions lack terminal handlers, timeout transitions, or dead-letter safety."},
    "MP-SY": {"name": "SymmetryAnalysis", "desc": "Dual-sided operation (encode/decode, subscribe/unsubscribe, push/pop) lacks inverse counterpart."},
    "MP-MG": {"name": "MutationGuards", "desc": "Write, update, or delete operations lack validation, authorization, or idempotency safeguards."},
    "MP-SE": {"name": "SideEffectCompleteness", "desc": "Primary operation occurs without triggering implied downstream side-effects (notifications, audit logs, caches)."},
    "MP-FR": {"name": "FailureRecovery", "desc": "Fallible external operations lack catch handlers, retry boundaries, or rollback compensation."},
    "MP-OC": {"name": "OwnershipCleanup", "desc": "Resource allocation or parent entity deletion fails to cascade or free owned resources."},
    "MP-AU": {"name": "AuthorizationSymmetry", "desc": "Access controls, tenant scoping, or permissions present in one path are omitted in a peer path."},
    "MP-AS": {"name": "AsyncJobCompleteness", "desc": "Background task queueing lacks worker handler, dead-letter queue, or stuck-task recovery."},
    "MP-OP": {"name": "OperationalCompleteness", "desc": "Production-critical path lacks health checks, rate limits, or administrative controls."},
    "MP-DC": {"name": "DataConsistency", "desc": "Relational updates lack transactional encapsulation or cross-table consistency guarantees."},
    "MP-CT": {"name": "ContractCompleteness", "desc": "Declared API route, schema parameter, or event contract has no implementation."},
    "MP-CF": {"name": "ConfigurationCompleteness", "desc": "Referenced environment variables, config keys, or feature flags are undefined."},
    "MP-OB": {"name": "ObservabilityImplied", "desc": "Critical financial or operational branch lacks metrics, tracing, or alert emission."},
    "MP-DB": {"name": "DatabaseConsistency", "desc": "Database schema migrations or ORM models lack down migrations, foreign key indexes, or cascade rules."},
    "MP-FA": {"name": "FastAPICompleteness", "desc": "FastAPI lifespan teardowns, session yield cleanups, or background exception handlers omitted."}
}


def convert_findings_to_sarif(findings: List[Dict[str, Any]]) -> Dict[str, Any]:
    rules_list = []
    seen_rules = set()

    for rule_id, rule_info in RULES.items():
        rules_list.append({
            "id": rule_id,
            "name": rule_info["name"],
            "shortDescription": {"text": rule_info["desc"]},
            "fullDescription": {"text": f"{rule_info['name']}: {rule_info['desc']}"},
            "help": {
                "text": f"Consult Missing Piece detector guide for {rule_id}.",
                "markdown": f"Refer to [Missing Piece documentation]({TOOL_URI}) for rule details."
            },
            "properties": {
                "precision": "high",
                "problem.severity": "warning"
            }
        })

    results = []
    for f in findings:
        rule_id = f.get("detector_family", "MP-SY")
        severity = f.get("severity", "Medium")
        level = SEVERITY_MAP.get(severity, "warning")
        message_text = f.get("why_it_matters", f.get("title", "Missing expected counterpart"))
        file_path = f.get("file", "README.md")
        line_num = int(f.get("line", 1))

        results.append({
            "ruleId": rule_id,
            "level": level,
            "message": {
                "text": f"[{rule_id}] {f.get('title', 'Omission detected')}: {message_text}"
            },
            "locations": [
                {
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": file_path.replace("\\", "/"),
                            "uriBaseId": "%SRCROOT%"
                        },
                        "region": {
                            "startLine": max(1, line_num),
                            "startColumn": 1
                        }
                    }
                }
            ],
            "properties": {
                "confidence": f.get("confidence", 1.0),
                "gap": f.get("gap", ""),
                "expected": f.get("expected", ""),
                "observed": f.get("observed", "")
            }
        })

    return {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": TOOL_NAME,
                        "version": TOOL_VERSION,
                        "informationUri": TOOL_URI,
                        "rules": rules_list
                    }
                },
                "results": results
            }
        ]
    }


def main():
    parser = argparse.ArgumentParser(description="Convert Missing Piece findings to SARIF 2.1.0")
    parser.add_argument("-i", "--input", help="Path to input JSON findings file", required=False)
    parser.add_argument("-o", "--output", help="Path to output SARIF file", default="missing-piece.sarif")
    args = parser.parse_args()

    findings = []
    if args.input and Path(args.input).exists():
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
            findings = data if isinstance(data, list) else data.get("findings", [])
    else:
        # Example finding for demonstration / test
        findings = [
            {
                "id": "MP-SY-001",
                "title": "Stripe charge.succeeded webhook lacks payment state transition counterpart",
                "detector_family": "MP-SY",
                "severity": "High",
                "confidence": 0.95,
                "file": "app/services/payments.py",
                "line": 42,
                "observed": "Stripe charge.succeeded webhook receiver configured in app/api/webhooks.py",
                "expected": "Counterpart payment state transition to 'succeeded' and invoice reconciliation",
                "gap": "Payment records remain in 'pending' status indefinitely after payment succeeds",
                "why_it_matters": "Paid orders will not fulfill, leading to user friction and payment reconciliation discrepancies."
            }
        ]

    sarif_output = convert_findings_to_sarif(findings)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(sarif_output, indent=2), encoding="utf-8")
    print(f"[OK] Exported {len(findings)} findings to SARIF format: {out_path.resolve()}")


if __name__ == "__main__":
    main()

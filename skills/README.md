# Skills Directory

This folder contains Claude-compatible skill packs designed for practical Governance Systems Engineering workflows.

Each skill folder includes:

- `SKILL.md`: Claude-compatible skill instructions.
- `README.md`: Human-readable overview and use cases.
- `references/`: Checklists, rules, and supporting guidance.
- `examples/`: Sample inputs and outputs that demonstrate the skill in action.

## Skill Packs

| Skill | Main Use Case |
|---|---|
| `change-governance-review` | Review change requests for governance completeness and audit readiness. |
| `cab-readiness-check` | Decide whether a change is ready for CAB review. |
| `rca-governance-analysis` | Evaluate RCA quality, detection gaps, and corrective actions. |
| `audit-evidence-request` | Convert auditor asks into clear evidence collection plans. |
| `risk-register-builder` | Turn issues, incidents, and findings into risk register entries. |
| `executive-grc-summary` | Convert operational updates into concise leadership summaries. |

## Practitioner Workflow

A typical workflow may look like this:

1. Use `change-governance-review` to evaluate the request.
2. Use `cab-readiness-check` to determine whether it should move to CAB.
3. Use `executive-grc-summary` to report weekly governance outcomes.
4. Use `rca-governance-analysis` if a failed change or incident occurs.
5. Use `risk-register-builder` when the review identifies a repeatable risk.
6. Use `audit-evidence-request` when evidence must be collected for an audit or control review.

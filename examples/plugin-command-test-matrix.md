# Plugin Command Test Matrix

## Purpose

This matrix tracks manual testing for Claude Code command workflows.

| Command | Scenario | Expected Result | Status | Notes |
|---|---|---|---|---|
| `review-change` | Weak production change request | Identifies CAB blockers and required fixes | Not tested |  |
| `prepare-cab-summary` | Multiple changes with mixed readiness | Produces concise CAB-ready summary | Not tested |  |
| `assess-vendor` | SaaS vendor missing SOC 2 and DPA | Recommends hold and due diligence actions | Not tested |  |
| `review-ai-intake` | AI assistant with internal data and CSV uploads | Identifies AI-specific risks and approval gates | Not tested |  |
| `summarize-governance-metrics` | Governance metrics with recurring gaps | Produces leadership-ready trend summary | Not tested |  |

## Test Evidence

For each command test, save:

- Prompt or command used.
- Input scenario.
- Output generated.
- Evaluation notes.
- Follow-up improvements.

# Plugin Component Map

This document maps the Governance Systems Skills Library plugin components.

## Plugin Metadata

| Component | Location | Purpose |
|---|---|---|
| Plugin manifest | `.claude-plugin/plugin.json` | Provides plugin metadata for Claude Code. |

## Skills

| Component | Location | Purpose |
|---|---|---|
| Skills | `skills/` | Claude-compatible GRC workflow skills. |
| Tested outputs | `skills/*/examples/tested-output.md` | Proof-of-use examples for each skill. |

## Commands

| Command | Related Skill |
|---|---|
| `review-change` | `change-governance-review`, `cab-readiness-check` |
| `prepare-cab-summary` | `cab-readiness-check`, `executive-grc-summary` |
| `review-rca` | `rca-governance-analysis` |
| `review-audit-evidence` | `audit-evidence-request`, `control-evidence-quality-check` |
| `assess-vendor` | `third-party-risk-review` |
| `review-ai-intake` | `ai-governance-intake-review` |
| `summarize-governance-metrics` | `governance-metrics-summary`, `executive-grc-summary` |

## Agents

| Agent | Related Skills |
|---|---|
| `governance-reviewer` | Change, CAB, RCA, risk, executive summary |
| `audit-evidence-reviewer` | Audit evidence request, control evidence quality |
| `ai-governance-reviewer` | AI governance, third-party risk, policy exception |
| `third-party-risk-reviewer` | Third-party risk, policy exception, risk register |
| `metrics-and-executive-reporting-agent` | Governance metrics, executive summary |

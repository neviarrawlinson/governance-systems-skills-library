# Claude Code Agent Guide

This guide documents the specialized agent layer for the Governance Systems Skills Library.

## Purpose

Agents provide specialized review roles for common GRC workflows. Claude Code plugins can include Markdown-based agents in a root-level `agents/` folder.

## Included Agents

| Agent | Purpose |
|---|---|
| `governance-reviewer` | Reviews change requests, CAB submissions, RCA summaries, policy exceptions, risk entries, and executive governance updates. |
| `audit-evidence-reviewer` | Reviews audit evidence packages for completeness, traceability, control relevance, and submission readiness. |
| `ai-governance-reviewer` | Reviews AI intake requests for privacy, security, prompt retention, model training, transparency, and approval readiness. |
| `third-party-risk-reviewer` | Reviews vendor, SaaS, integration, API, and pilot requests for third-party risk. |
| `metrics-and-executive-reporting-agent` | Turns governance metrics and risk updates into leadership-ready summaries. |

## Security and Control Posture

These agents are intentionally review-oriented. They are configured with `disallowedTools: Write, Edit` to keep the workflow focused on analysis, documentation quality, and governance recommendations.

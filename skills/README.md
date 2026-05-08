# Skill Library

This folder contains Claude-compatible skill packs for Governance Systems Engineering workflows.

## Available skills

| Skill | Category | Purpose |
|---|---|---|
| `change-governance-review` | Change Governance | Reviews change requests for governance completeness, CAB readiness, risk, rollback, validation, monitoring, approvals, and audit readiness. |
| `cab-readiness-check` | Change Governance | Determines whether a change request is ready for CAB review and decision-making. |
| `rca-governance-analysis` | Incident Governance | Reviews RCA documentation for root cause quality, process gaps, monitoring gaps, ownership, corrective actions, and executive readiness. |
| `audit-evidence-request` | Audit Readiness | Converts audit evidence requests into evidence checklists, owner questions, response plans, and submission guidance. |
| `risk-register-builder` | Risk Management | Converts findings, issues, incidents, and observations into structured risk register entries. |
| `executive-grc-summary` | Executive Reporting | Creates concise executive-ready summaries for governance, risk, compliance, audit, change, RCA, and control updates. |
| `policy-exception-review` | Policy Governance | Reviews policy exception requests for business justification, risk impact, compensating controls, approval requirements, expiration date, ownership, and audit-ready documentation. Use when evaluating exceptions to security, IT, compliance, access, change management, vendor, or data governance policies. |
| `third-party-risk-review` | Vendor Risk | Reviews vendors, SaaS tools, service providers, integrations, and third-party relationships for security, privacy, compliance, operational, data, and business risk. Use when assessing new vendors, renewals, questionnaires, SOC reports, DPAs, contracts, or application intake requests. |
| `control-evidence-quality-check` | Audit Readiness | Evaluates audit evidence for completeness, accuracy, traceability, date coverage, reviewer signoff, control relevance, and submission readiness. Use when reviewing SOC 2, ISO 27001, ITGC, access review, change management, incident, vendor, or policy evidence before submitting to auditors. |
| `governance-metrics-summary` | Governance Reporting | Turns operational governance data into leadership-ready metrics, trends, risks, exceptions, and action-oriented summaries. Use when summarizing CAB metrics, change volume, emergency changes, delayed closures, RCA actions, audit requests, evidence status, policy exceptions, or GRC program health. |
| `ai-governance-intake-review` | AI Governance | Reviews proposed AI tools, models, automations, copilots, data uses, and AI-assisted workflows for governance, risk, privacy, security, compliance, ownership, transparency, and approval readiness. Use when evaluating AI tool intake, AI vendor requests, internal AI workflow proposals, or AI risk reviews. |

## Skill folder standard

Each skill folder should include:

```text
SKILL.md
README.md
examples/sample-input.md
examples/sample-output.md
references/
```

## Quality standard

Each skill should produce a practical governance output that can be used in Jira, Confluence, audit workpapers, leadership reporting, or risk documentation.

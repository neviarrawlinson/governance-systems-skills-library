# Governance Systems Skills Library

Practical Claude-compatible skill packs for Governance Systems Engineering, change governance, RCA analysis, audit evidence, risk documentation, vendor risk, AI governance intake, and executive GRC reporting.

## Live Demo

View the project landing page here:

https://neviarrawlinson.github.io/governance-systems-skills-library/

## Why this project exists

Many governance programs fail because controls live in documents but do not show up consistently in tickets, approvals, evidence, reporting, or operational decisions.

Governance Systems Engineering turns governance expectations into repeatable systems, decision logic, checklists, workflows, skill packs, and audit-ready outputs.

## What makes this different

This is not a generic framework reference library. This project is workflow-centered and focuses on the work practitioners actually perform:

- Reviewing technology change requests.
- Preparing CAB decisions.
- Evaluating RCA quality.
- Checking audit evidence before submission.
- Creating risk register entries.
- Reviewing policy exceptions.
- Assessing third-party risk.
- Summarizing governance metrics.
- Reviewing AI use cases before approval.
- Producing executive-ready GRC summaries.

## Download Skill Packages

The latest packaged Claude-compatible skill bundle is available from the official GitHub release:

[Download governance-systems-skill-packages.zip](https://github.com/neviarrawlinson/governance-systems-skills-library/releases/tag/v0.4.0)

Current release: **v0.4.0 - Advanced Governance Skills Expansion**

## Skill packs

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

## Repository structure

```text
docs/                    Project documentation and guides
skills/                  Claude-compatible skill folders
templates/               Reusable governance templates
examples/                Sample inputs, outputs, release notes, and workflow examples
framework-mapping/       Governance workflow mappings to common frameworks
governance-quality/      Skill quality controls and release checklists
scripts/                 Validation scripts
.github/workflows/       GitHub Actions workflows
site/                    GitHub Pages source copy
dist/                    Packaged skill zip files
```

## Validate skills

Run:

```bash
python scripts/validate-skills.py
```

## Package skills

Run:

```bash
bash package-skills.sh
```

Packages are generated in the `dist/` folder.

## Intended use

These skills are designed to help practitioners produce clearer and more consistent governance outputs. They do not replace professional judgment, legal advice, audit advice, regulatory interpretation, or management approval.

## Status

Current project phase: Advanced skill expansion and quality controls.

## Tested Skill Output

The `change-governance-review` skill has been tested using a sample production restart change request.

View the tested example here:

[Production Restart Change Review Tested Output](skills/change-governance-review/examples/tested-output.md)

This example demonstrates how the skill identifies governance gaps in implementation planning, validation, rollback, monitoring, approvals, and risk documentation.

## Tested Skill Output

The library includes tested output examples using realistic governance scenarios.

- [Production Restart Change Review Tested Output](skills/change-governance-review/examples/tested-output.md)
- [Database Configuration CAB Readiness Tested Output](skills/cab-readiness-check/examples/tested-output.md)

These examples demonstrate how the skills identify governance gaps in implementation planning, validation, rollback, monitoring, approvals, risk documentation, and CAB readiness.

## License

MIT License.

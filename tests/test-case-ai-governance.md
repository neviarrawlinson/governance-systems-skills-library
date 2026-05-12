# Test Case: AI Governance Intake Review

## Skill Under Test

`ai-governance-intake-review`

## Scenario

A team wants to pilot a third-party AI assistant that summarizes internal reporting trends and generates leadership updates using operational dashboards and CSV uploads.

## Prompt

```text
Use the ai-governance-intake-review skill to review this AI intake request.

Use Case Name: AI Reporting Assistant
Business Purpose: Summarize reporting trends, explain dashboard anomalies, and generate draft leadership updates.
AI Tool Type: Third-party SaaS AI assistant.
Data Involved: Internal reporting data, employee user IDs, department metrics, operational dashboards, CSV files.
Users: 25 internal users.
Integration: Possible Reporting Service API connection and CSV upload.
Vendor Status: Security review incomplete. SOC 2 not provided. DPA not reviewed. AI-specific terms not reviewed.
Known Context: Reporting Service has recent outage history and open high residual risk.
Requested Decision: Approve pilot within two weeks.
```

## Expected Decision

Hold. Do not approve production or live data use as submitted.

## Expected Findings

The output should identify:

- Third-party AI risk.
- Prompt retention and model training risk.
- SOC 2 missing.
- DPA missing.
- AI terms missing.
- Security review incomplete.
- Data retention and deletion unknown.
- Human review required for AI-generated leadership content.
- Transparency/disclosure requirements.
- Non-production synthetic data pilot option.
- Required approvals from business, system owner, data owner, Security, Privacy/Legal, and Governance.

## Scoring Notes

A strong output should distinguish standard SaaS risk from AI-specific risk.

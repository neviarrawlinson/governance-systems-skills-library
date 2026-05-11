# End-to-End Demo: Third-Party Risk Workflow

## Scenario

A team requests approval for a SaaS analytics platform that connects to a production reporting service and supports CSV export.

## Workflow

### Step 1: Third-Party Risk Review

Skill:

`third-party-risk-review`

Output:

- Vendor risk decision
- Security evidence requirements
- DPA and privacy review needs
- API integration risk
- CSV export controls
- Pilot guardrails

### Step 2: Policy Exception Review

Skill:

`policy-exception-review`

Output:

- Exception decision if the team requests bypassing normal review
- Compensating controls
- Expiration date
- Risk acceptance

### Step 3: Risk Register Builder

Skill:

`risk-register-builder`

Output:

- Risk statement
- Existing controls
- Control gaps
- Treatment plan
- Evidence requirements

### Step 4: Governance Metrics Summary

Skill:

`governance-metrics-summary`

Output:

- Vendor risk trend summary
- Decision status
- Open actions
- Leadership visibility

## Value

This workflow shows how vendor intake can be governed as a repeatable decision process with traceability, risk ownership, and audit-ready records.

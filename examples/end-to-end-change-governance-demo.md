# End-to-End Demo: Change Governance Workflow

This demo shows how the Governance Systems Skills Library can support a full change governance workflow from change review to executive reporting.

## Scenario

A production change is submitted for the Reporting Service. The change includes a database configuration update, weak validation notes, incomplete rollback planning, and limited monitoring evidence. After deployment, the service experiences an outage.

## Step 1: Change Governance Review

Skill:

`change-governance-review`

Purpose:

Evaluate the change request for completeness before approval.

Expected output:

- Governance review summary
- Missing implementation details
- Validation gaps
- Rollback concerns
- Monitoring requirements
- Approval readiness
- Jira-ready governance note

## Step 2: CAB Readiness Check

Skill:

`cab-readiness-check`

Purpose:

Determine whether the change is ready for CAB review.

Expected output:

- CAB readiness status
- Approval recommendation
- Conditional approval items
- Deployment authorization status
- Required pre-deployment gates

## Step 3: RCA Governance Analysis

Skill:

`rca-governance-analysis`

Purpose:

Evaluate the RCA after the outage.

Expected output:

- Root cause quality review
- Timeline gap analysis
- Monitoring failure analysis
- Corrective action review
- Change governance linkage
- Audit readiness assessment

## Step 4: Audit Evidence Request

Skill:

`audit-evidence-request`

Purpose:

Prepare a response to an audit request for evidence that the change was reviewed, approved, tested, validated, and monitored.

Expected output:

- Evidence checklist
- Owner questions
- Evidence quality requirements
- Submission guidance
- Draft audit submission note

## Step 5: Control Evidence Quality Check

Skill:

`control-evidence-quality-check`

Purpose:

Assess whether the evidence package is ready to submit.

Expected output:

- Evidence quality assessment
- Auditor concerns
- Traceability gaps
- Remediation checklist
- Submission cover note

## Step 6: Risk Register Builder

Skill:

`risk-register-builder`

Purpose:

Convert the governance finding into a structured risk register entry.

Expected output:

- Risk statement
- Cause and impact
- Existing controls
- Control gaps
- Risk rating rationale
- Corrective action plan
- Residual risk
- Audit traceability

## Step 7: Executive GRC Summary

Skill:

`executive-grc-summary`

Purpose:

Summarize the issue for leadership.

Expected output:

- Executive summary
- Current status
- Business impact
- Risk posture
- Governance concerns
- Leadership decision needed
- Recommended next actions

## End-to-End Value

This demo shows how one production change can create a full governance record across change approval, CAB readiness, RCA quality, evidence readiness, risk tracking, and executive reporting.

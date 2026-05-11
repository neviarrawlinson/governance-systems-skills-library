# Plugin Testing Guide

Use this guide to test the Claude Code plugin layer.

## Test 1: Change Review Command

```text
Use the review-change command to assess this production change request.

Title: Production restart for application server
Environment: Production
Change Type: Standard
Implementation Plan: Restart the app server.
Validation Plan: Confirm the application is back online.
Rollback Plan: Not applicable.
Monitoring Plan: None listed.
Approvals: Manager approval pending.
```

Expected result:

- Status should be Not Ready or Ready with Conditions.
- Missing rollback and monitoring should be identified.
- Validation evidence should be flagged as weak.
- Governance note should be suitable for a Jira ticket.

## Test 2: Audit Evidence Reviewer Agent

```text
Use the audit-evidence-reviewer agent to review this evidence package for submission readiness.

Control: Change Management
Evidence: Change ticket screenshot, manager approval screenshot, deployment note, validation note saying confirmed working.
Known gaps: Security review pending, no monitoring evidence, no testing evidence.
```

Expected result:

- Submission should be held.
- Security approval, testing, validation, and monitoring gaps should be identified.
- A submission note or remediation checklist should be provided.

## Test 3: AI Governance Reviewer Agent

```text
Use the ai-governance-reviewer agent to review this AI intake request.

Use case: AI assistant that summarizes internal reporting data.
Data: Employee IDs, internal dashboards, CSV exports.
Vendor status: No SOC 2, no DPA, no AI terms reviewed.
Requested decision: Approve a pilot in two weeks.
```

Expected result:

- Decision should be Hold.
- Prompt retention, model training, DPA, AI terms, and human review risks should be identified.
- A non-production or synthetic-data pilot path should be recommended.

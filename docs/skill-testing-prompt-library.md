# Skill Testing Prompt Library

This document provides reusable prompts for testing each skill in the Governance Systems Skills Library.

## Change Governance Review

```text
Use the change-governance-review skill to review the following change request for governance completeness, CAB readiness, risk, rollback, validation, monitoring, approvals, and audit readiness.

Change Request:
Title: Production restart for application server
Environment: Production
Change Type: Standard
Planned Start: Friday 9:00 PM
Planned End: Friday 9:30 PM
Implementation Plan: Restart the app server.
Validation Plan: Confirm the application is back online.
Rollback Plan: Not applicable.
Risk Impact: Low.
Monitoring Plan: None listed.
Approvals: Manager approval pending.
```

## CAB Readiness Check

```text
Use the cab-readiness-check skill to evaluate whether the following change request is ready for CAB review.

Change Request:
Title: Database configuration update for reporting service
Environment: Production
Change Type: Normal
Planned Start: Tuesday 8:00 PM
Planned End: Tuesday 9:00 PM
Business Justification: Required to improve reporting performance for internal operations.
Implementation Plan: Update database configuration values and restart reporting service.
Validation Plan: Confirm reports load successfully after the change.
Rollback Plan: Revert database configuration values if issues occur.
Risk Impact: Medium
Monitoring Plan: Monitor application logs after deployment.
Approvals: Manager approved. Security review pending. Compliance review not required.
Dependencies: Reporting service and database team availability.
```

## RCA Governance Analysis

```text
Use the rca-governance-analysis skill to review the following RCA for governance quality, root cause completeness, monitoring gaps, ownership, corrective actions, and audit readiness.

RCA Summary:
Incident Title: Reporting service outage
Date: May 6, 2026
Impact: Internal reporting users could not access daily operational reports for approximately 2 hours.
Detected By: Business operations team
Technical Cause: Reporting service failed after a scheduled database configuration update.
Resolution: Database configuration was reverted and the reporting service was restarted.
Root Cause: Configuration value was incorrect.
Monitoring: No alert fired. Issue was reported by users.
Corrective Actions:
- Update deployment checklist.
- Review database configuration process.
- Add monitoring later.
Owner: Database team
Due Date: Not assigned
Evidence: Incident ticket and Slack discussion.
```

## Audit Evidence Request

```text
Use the audit-evidence-request skill to convert the following audit request into a clear evidence checklist, owner questions, evidence quality requirements, and submission guidance.

Audit Request:
Control Area: Change Management
Request: Provide evidence that production changes were reviewed, approved, tested, and validated before deployment for the selected sample.

Sample Change:
Ticket ID: CM-2026-041
System: Reporting Service
Environment: Production
Change Type: Normal
Deployment Date: May 6, 2026
Requested Evidence:
- Change ticket
- Approval evidence
- Testing evidence
- Validation evidence
- Deployment evidence
- Backout plan
- Post-deployment monitoring evidence

Known Context:
The ticket includes manager approval and a deployment note. Security review is listed as pending. Validation notes say “confirmed working.” Monitoring evidence is not attached. Rollback plan says “revert if needed.”
```

## Risk Register Builder

```text
Use the risk-register-builder skill to convert the following governance finding into a structured risk register entry.

Finding:
During review of production change CM-2026-041, governance identified multiple control gaps. Security review was listed as pending at the time of deployment. Validation evidence only stated “confirmed working” without success criteria, tester ownership, timestamp, or test results. The rollback plan stated “revert if needed” but did not include actual rollback steps, trigger conditions, or ownership. Monitoring evidence was missing, and the related reporting service outage was detected by business users instead of monitoring tools.

Context:
System: Reporting Service
Environment: Production
Risk Category: Change Management / IT Operations
Potential Impact: Failed or weak production change controls may increase the likelihood of outages, audit findings, delayed incident response, and incomplete evidence for ITGC or SOC 2 review.
Existing Controls: CAB review, manager approval, change ticket workflow, deployment notes.
Control Gaps: Pending security review, weak validation evidence, weak rollback plan, missing monitoring evidence, no clear owner for corrective actions.
```

## Executive GRC Summary

```text
Use the executive-grc-summary skill to turn the following governance activity into a concise executive-ready summary.

Governance Activity Summary:
During review of production change CM-2026-041 for the Reporting Service, governance identified multiple control gaps across change approval, validation, rollback planning, post-deployment monitoring, RCA quality, audit evidence readiness, and risk documentation.

Key Issues:
- Security review was listed as pending at the time of deployment.
- Validation evidence only stated “confirmed working.”
- Rollback plan stated “revert if needed.”
- Monitoring evidence was missing.
- The related outage was detected by business users instead of monitoring tools.
- RCA root cause stated only “configuration value was incorrect.”
- Corrective actions did not have named owners or due dates.
- A risk register entry was created and residual risk remains high until remediation is completed and validated.

Audience:
IT leadership and executive stakeholders.

Purpose:
Summarize the governance concern, business impact, current status, risk, and next actions in a professional leadership-ready format.
```

## Advanced Skills

Use the tested output files inside each advanced skill folder for additional testing scenarios:

```text
skills/policy-exception-review/examples/tested-output.md
skills/third-party-risk-review/examples/tested-output.md
skills/control-evidence-quality-check/examples/tested-output.md
skills/governance-metrics-summary/examples/tested-output.md
skills/ai-governance-intake-review/examples/tested-output.md
```

# Test Case: Change Governance Review

## Skill Under Test

`change-governance-review`

## Scenario

A production application restart is requested with weak implementation details, no rollback plan, vague validation, and incomplete approvals.

## Prompt

```text
Use the change-governance-review skill to review the following production change request for CAB readiness, risk, validation, rollback, monitoring, approvals, and audit readiness.

Change Request:
Title: Production restart for application server
Environment: Production
Change Type: Standard
Business Justification: Application latency has increased during peak hours.
Implementation Plan: Restart the app server.
Validation Plan: Confirm the application is back online.
Rollback Plan: Not applicable.
Monitoring Plan: None listed.
Approvals: Manager approval pending. Security review not required according to requester.
Deployment Window: Tonight at 10:00 PM.
```

## Expected Decision

Not ready for CAB or approve only with strict conditions after remediation.

## Expected Findings

The output should identify:

- Implementation plan is too vague.
- Validation lacks success criteria, tester, timestamp, and test steps.
- Rollback cannot be “not applicable” for production restart.
- Monitoring plan is missing.
- Manager approval is pending.
- Security review applicability should be documented.
- Business justification needs more detail.
- CAB should not approve without pre-deployment gates.

## Scoring Notes

A strong output should provide a clear CAB recommendation, remediation checklist, and governance-ready note.

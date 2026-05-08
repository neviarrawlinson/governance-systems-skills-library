---
name: change-governance-review
description: Reviews technology change requests for governance completeness, CAB readiness, implementation quality, validation, rollback, monitoring, approvals, risk, and audit readiness. Use when evaluating a Jira change request, CAB submission, production deployment, emergency change, or change management ticket.
---

# Change Governance Review

## Purpose

Use this skill to evaluate whether a technology change request is ready for governance review, CAB approval, implementation, or audit evidence retention.

This skill focuses on practical change governance. It identifies whether a change has enough information to proceed safely, whether key controls are missing, and what should be corrected before approval.

## Review Categories

Evaluate the change request across these categories:

1. Change Summary
   - Is the purpose of the change clear?
   - Is the business reason explained?
   - Is the affected system, service, team, or user group identified?
   - Is the environment clearly stated?

2. Implementation Plan
   - Are the implementation steps clear and sequenced?
   - Is the implementation owner or responsible team identified?
   - Are the planned start and end dates included?
   - Are dependencies or prerequisites identified?

3. Validation Plan
   - Is there a named validation method?
   - Is post-change testing described?
   - Are success criteria defined?
   - Is the validator, tester, or responsible party identified?

4. Rollback Plan
   - Is there a realistic rollback or backout plan?
   - Does the rollback plan explain when rollback would be triggered?
   - Is rollback ownership clear?
   - If rollback is not possible, is there a justification and contingency plan?

5. Risk and Impact
   - Does the request explain customer, operational, security, compliance, or business impact?
   - Is the risk level reasonable based on the scope?
   - Are mitigation steps included?
   - Is the change type aligned to the actual risk and impact?

6. Monitoring Plan
   - Is post-deployment monitoring described?
   - Are logs, dashboards, alerts, smoke tests, or business checks included?
   - Is there a monitoring duration or handoff plan?

7. Approvals
   - Are manager, security, compliance, CAB, or emergency approvals included as needed?
   - Are approval gaps clearly identified?
   - Are required approvers appropriate for the environment, risk, and change type?

8. Audit Readiness
   - Would this change request stand up to audit review?
   - Is the evidence complete enough to show what changed, who approved it, when it happened, how it was validated, and what the outcome was?

## Decision Standards

Use the following readiness outcomes:

- Ready: The request has sufficient implementation, validation, rollback, monitoring, risk, impact, and approval information.
- Ready with Conditions: The request can proceed if specific minor items are corrected before deployment.
- Not Ready: The request has missing or weak information that creates governance, operational, audit, or approval risk.

## Output Format

Return the review in this format:

### Governance Review Summary

Status: Ready / Ready with Conditions / Not Ready  
Overall Risk: Low / Medium / High  
CAB Recommendation: Approve / Approve with Conditions / Hold / Reject

### Key Findings

- Finding 1
- Finding 2
- Finding 3

### Missing or Weak Areas

| Area | Issue | Required Fix |
|---|---|---|
| Implementation Plan |  |  |
| Validation Plan |  |  |
| Rollback Plan |  |  |
| Risk / Impact |  |  |
| Monitoring Plan |  |  |
| Approvals |  |  |

### Governance Note

Write a concise internal governance note that can be pasted into Jira.

Format:

**Governance Review**

- **Implementation Plan**:
- **Validation Plan**:
- **Rollback Plan**:
- **Risk Summary**:
- **Monitoring Plan**:
- **Approval Status**:

Governance review completed. Ready for CAB / Not ready for CAB pending the items listed above.

### Recommended Next Action

Provide one clear next action for the requester, approver, or governance owner.

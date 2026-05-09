# Tested Output: Temporary Production Change Security Review Exception

## Input Summary

Exception Title: Temporary exception to production change security review requirement  
Policy Area: Change Management  
Requested By: Reporting Services Team  
System: Reporting Service  
Environment: Production  

Exception Request:  
The team is requesting permission to proceed with an urgent production configuration change before security review is completed. The change is needed to restore reporting performance for internal business users.

Business Justification:  
Reports are loading slowly and business operations needs the issue resolved before the next morning reporting cycle.

Requested Duration: 30 days  

Risk Statement:  
Low risk because the change only affects internal reporting users.

Compensating Controls:
- Manager approval will be obtained.
- The database team will monitor logs after deployment.

Approvals:
- Manager approval pending.
- Security approval not obtained.
- Compliance approval not requested.

Evidence Provided:
- Change ticket draft
- Slack discussion
- Deployment note draft

Known Context:
- The same reporting service recently experienced an outage after a database configuration change.
- The outage was detected by business users instead of monitoring tools.
- A related risk register entry remains open with residual risk rated high.

## Policy Exception Review Summary

Status: Not Ready for Approval  
Recommended Decision: Reject as Submitted  
Exception Risk: High  
Audit Readiness: Insufficient  
Recommended Action: Do not approve until security review, compensating controls, approvals, ownership, duration, and evidence gaps are corrected.

## Key Findings

- The request seeks to bypass security review for a production change in a system with recent outage history.
- The stated risk rating of low is not supported by the known context.
- The same reporting service recently experienced a production outage after a database configuration change.
- The proposed compensating controls are weak because manager approval and log monitoring do not replace security review.
- Manager approval is still pending, so no approval path has been completed.
- Security approval has not been obtained, and compliance review has not been requested.
- The requested 30-day duration is not justified for an urgent change.
- Evidence provided is not sufficient for audit-ready exception approval.

## Exception Decision

Reject the exception as submitted.

The request has material governance gaps across business justification, risk rating, compensating controls, approval readiness, ownership, expiration criteria, and audit evidence. A production security review bypass should not be approved without stronger justification, documented escalation to Security, clear compensating controls, named ownership, and time-bound expiration requirements.

## Governance Criteria Review

| Area | Review Result | Required Fix |
|---|---|---|
| Business Justification | Partially sufficient | Clarify why the change cannot wait for expedited security review. |
| Risk Impact | Not sufficient | Reclassify risk as high or provide documented rationale for a lower rating. |
| Compensating Controls | Not sufficient | Add controls that reduce risk beyond manager approval and log monitoring. |
| Approval Requirements | Not sufficient | Obtain manager approval and document Security and Compliance disposition. |
| Requested Duration | Not sufficient | Shorten duration or justify why 30 days is needed. |
| Ownership | Not sufficient | Assign named owners for the exception, monitoring, validation, and closure. |
| Evidence | Not sufficient | Provide approval records, risk acceptance, monitoring plan, rollback plan, and expiration tracking. |

## Risk Analysis

The risk is high because the request affects a production system with recent outage history and an active related risk register entry. The prior outage was detected by business users instead of monitoring tools, which indicates that monitoring controls may not be mature enough to serve as the primary compensating control.

The request also proposes bypassing security review, which is a core production change control. If approved without stronger controls, this exception could increase the likelihood of repeat outage, audit finding, incomplete evidence, or unresolved risk exposure.

## Compensating Control Assessment

The proposed compensating controls are not sufficient.

| Proposed Control | Assessment |
|---|---|
| Manager approval | Necessary, but not enough to replace Security review. |
| Database team monitoring logs | Too vague. It does not define what logs, who monitors them, how long monitoring occurs, or what triggers escalation. |

Recommended compensating controls should include:

- Expedited Security review request and documented Security response.
- Named implementation owner.
- Named monitoring owner.
- Specific monitoring dashboards, logs, alerts, and review duration.
- Documented rollback plan with trigger conditions.
- Post-change validation checklist.
- Time-bound exception expiration.
- Linked corrective action or risk acceptance record.
- Leadership approval if Security review is bypassed.

## Approval Requirements

The exception should not proceed until the following approvals or dispositions are documented:

| Approval Area | Requirement |
|---|---|
| Manager Approval | Required before governance review can proceed. |
| Security Review | Required, or documented Security response explaining why expedited review is not feasible. |
| Compliance Review | Required if the change affects audit-relevant controls, evidence, reporting, or regulatory commitments. |
| Governance Approval | Required after risk, compensating controls, duration, and ownership are corrected. |
| Leadership Risk Acceptance | Required if the organization chooses to bypass Security review. |

## Required Resubmission Conditions

The request may be reconsidered if the requester provides:

1. Written confirmation that Security was contacted for expedited review.
2. Security approval or documented Security response if expedited review is not feasible.
3. Completed manager approval.
4. Updated risk rating that reflects the recent outage and open high residual risk.
5. Stronger compensating controls that were not already present during the prior outage.
6. Specific monitoring plan with named owner, tools, logs, dashboards, duration, and escalation path.
7. Detailed rollback plan with steps, trigger conditions, and owner.
8. Shortened exception duration or stronger justification for 30 days.
9. Named exception owner responsible for expiration and closure.
10. Evidence package suitable for audit review.

## Governance Note

**Policy Exception Review**

- **Exception Scope**: Temporary bypass of production change security review for Reporting Service.
- **Business Justification**: Partially sufficient. The request explains operational urgency but does not demonstrate why expedited Security review cannot occur.
- **Risk Summary**: Risk is understated. The request should be treated as high risk due to recent outage history, user-detected failure, and open residual risk.
- **Compensating Controls**: Not sufficient. Manager approval and log monitoring do not adequately compensate for bypassing Security review.
- **Approval Status**: Not sufficient. Manager approval is pending, Security approval is not obtained, and Compliance review was not requested.
- **Evidence Status**: Not audit-ready. Draft ticket, Slack discussion, and deployment note draft are not enough to support exception approval.
- **Decision**: Reject as submitted.

Governance review completed. Exception request is not approved as submitted. Resubmission requires stronger compensating controls, completed approvals, named ownership, expiration criteria, and audit-ready evidence.

## Recommended Next Action

Contact Security for expedited review and document the response. If Security review cannot be completed before the requested change window, resubmit the exception with completed manager approval, stronger compensating controls, named owners, a detailed rollback plan, monitoring evidence requirements, and formal risk acceptance.

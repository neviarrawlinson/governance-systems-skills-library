# Tested Output: Production Restart Change Review

## Input Summary

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

## Governance Review Summary

Status: Not Ready  
Overall Risk: Medium  
CAB Recommendation: Hold

## Key Findings

- The implementation plan is too vague for a production change.
- The validation plan does not define success criteria, testing method, or validation owner.
- The rollback plan is not acceptable because production restarts still require a contingency plan.
- The risk rating is unsupported and does not explain customer, operational, or service impact.
- The monitoring plan is missing.
- Required approval is still pending.

## Missing or Weak Areas

| Area | Issue | Required Fix |
|---|---|---|
| Implementation Plan | Only states “Restart the app server.” | Add sequenced steps, owner, prerequisites, and execution details. |
| Validation Plan | Only states that the app will be checked online. | Add success criteria, validation method, tester, and pass/fail threshold. |
| Rollback Plan | Listed as not applicable. | Add restart failure contingency, escalation path, failover option, or recovery steps. |
| Risk / Impact | Risk is marked low without justification. | Document customer impact, downtime expectations, affected services, and mitigation. |
| Monitoring Plan | No monitoring plan listed. | Add dashboards, logs, alerts, health checks, and monitoring duration. |
| Approvals | Manager approval is pending. | Obtain required approval before CAB review. |

## Governance Note

**Governance Review**

- **Implementation Plan**: Not sufficient. The change requires sequenced production restart steps, named owner, prerequisites, and execution details.
- **Validation Plan**: Not sufficient. The request must define success criteria, validation method, responsible tester, and pass/fail expectations.
- **Rollback Plan**: Not sufficient. “Not applicable” is not acceptable for a production restart. A contingency or escalation path is required.
- **Risk Summary**: Risk is marked low, but the request does not document customer impact, affected services, downtime expectations, or mitigation.
- **Monitoring Plan**: Missing. Post-change monitoring must include dashboards, logs, alerts, health checks, and monitoring duration.
- **Approval Status**: Manager approval is pending and must be completed before CAB approval.

Governance review completed. Not ready for CAB pending the items listed above.

## Recommended Next Action

Return the change request to the submitter for revision before CAB review.

# Jira Change Review Example

## Scenario

A production change request has been submitted in Jira for a configuration update. Governance needs to determine whether it is ready for CAB review.

## Jira Fields Reviewed

| Field | Example Value | Governance Review |
|---|---|---|
| Summary | Update production API gateway timeout | Clear enough for review. |
| Environment | Production | Requires complete risk, rollback, validation, and monitoring details. |
| Change Type | Standard | Confirm whether production restart should increase classification. |
| Implementation Plan | Five-step technical plan | Acceptable, but owner should be named. |
| Validation Plan | Engineering will confirm successful API calls | Too vague. Needs measurable success criteria. |
| Rollback Plan | Revert timeout value and restart service | Acceptable if tested or previously validated. |
| Risk Assessment | Low | Potentially understated due to production restart. |
| Monitoring Plan | Datadog latency and error rate for one hour | Acceptable. |
| Approvals | Manager approved, Security/Compliance not required | Requires routing rationale. |

## Governance Decision

**Decision:** Ready with Conditions  
**CAB Recommendation:** Approve with Conditions  
**Required Update:** Strengthen validation plan and document approval routing rationale.

## Jira Internal Note

**Governance Review**

- **Implementation Plan:** Clear and sequenced. Add named owner for implementation.
- **Validation Plan:** Needs measurable success criteria and named validator.
- **Rollback Plan:** Present and technically realistic.
- **Risk Summary:** Production configuration change with service restart. Consider Medium risk unless Low risk is justified.
- **Monitoring Plan:** Datadog latency and error rate monitoring for one hour post-change.
- **Approval Status:** Manager approval complete. Add rationale for Security and Compliance not being required.

Governance review completed. Ready for CAB with conditions.

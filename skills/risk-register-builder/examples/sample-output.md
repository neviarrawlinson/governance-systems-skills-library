# Sample Output: Risk Register Builder

## Risk Register Entry

| Field | Entry |
|---|---|
| Risk Title | Incomplete rollback planning for production changes |
| Risk Statement | If production changes are allowed to proceed without complete rollback plans, failed implementations may take longer to recover, increasing operational disruption and audit exposure. |
| Risk Category | Change Management, Operational Risk, IT Governance |
| Inherent Likelihood | Medium |
| Inherent Impact | High |
| Inherent Risk Rating | High |
| Existing Controls | Manual governance review, CAB review, change documentation requirements |
| Control Gaps | Jira does not block progression when rollback documentation is missing. Review quality depends on manual detection. |
| Recommended Treatment | Mitigate |
| Mitigation Plan | Add required rollback fields, define rejection criteria, create Jira automation to flag or block incomplete production changes, and report exceptions in CAB metrics. |
| Risk Owner | IT Governance or Change Management Owner |
| Target Due Date | To be assigned |
| Residual Risk Expectation | Medium after workflow enforcement and reporting controls are implemented |

## Recommended Next Action

Create a Jira enhancement request to enforce rollback documentation for production changes before CAB approval.

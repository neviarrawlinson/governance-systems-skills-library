# Sample Output: Policy Exception Review

### Governance Decision Summary

Status: Not Ready  
Overall Risk: Medium  
Recommended Decision: Hold pending additional controls and approvals

### Key Findings

- The business justification is documented, but the exception is not time-bound.
- The request lacks compensating controls for monitoring during the restricted deployment window.
- Security and Compliance approvals are missing despite the production timing exception.

### Missing or Weak Areas

| Area | Issue | Required Fix | Owner / Reviewer |
|---|---|---|---|
| Duration | No expiration or review date | Add exception end date and remediation path | Requester |
| Monitoring | No compensating monitoring controls | Add post-change monitoring plan and owner | Requester / Ops |
| Approvals | Security and Compliance approvals missing | Obtain required approvals before approval | Governance |

### Governance Notes

Policy exception is not ready for approval. Request has a valid operational justification, but requires a defined expiration date, compensating monitoring controls, rollback details, and Security/Compliance review before governance approval.

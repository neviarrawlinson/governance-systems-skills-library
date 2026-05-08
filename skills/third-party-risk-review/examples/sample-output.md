# Sample Output: Third-Party Risk Review

### Governance Decision Summary

Status: Ready with Conditions  
Overall Risk: Medium  
Recommended Decision: Conditionally Approve pending DPA and integration review

### Key Findings

- The vendor will process Salesforce lead data through an API integration.
- Security evidence exists but should be reviewed for report period, scope, exceptions, and subservice organizations.
- A DPA is missing and should be completed before production use.

### Missing or Weak Areas

| Area | Issue | Required Fix | Owner / Reviewer |
|---|---|---|---|
| Privacy | No DPA attached | Route to Legal/Privacy for review | Procurement / Legal |
| Integration | API access not fully defined | Confirm scopes, permissions, and data flow | IT / Security |
| Evidence | SOC 2 report is from last year | Confirm current report or bridge letter | Vendor owner |

### Governance Notes

Vendor may proceed through conditional review but should not be approved for production integration until DPA, API scope, and current security evidence are reviewed.

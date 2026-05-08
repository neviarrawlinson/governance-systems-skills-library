# Sample Output: CAB Readiness Check

## CAB Readiness Decision

**CAB Status:** Not Ready  
**Decision:** Hold from CAB agenda until blockers are resolved  
**Primary Blockers:** Missing rollback plan and pending Security approval

## Readiness Review

| Category | Status | Notes |
|---|---|---|
| Implementation Plan | Complete | No blocker identified. |
| Validation Plan | Complete | No blocker identified. |
| Rollback Plan | Missing | CAB blocker. A production authentication change must include a tested rollback or contingency plan. |
| Risk Assessment | Complete | Medium risk appears reasonable. |
| Monitoring Plan | Complete | No blocker identified. |
| Manager Approval | Complete | No blocker identified. |
| Security Approval | Pending | CAB blocker due to authentication impact. |
| Compliance Approval | Not Required | Acceptable if routing logic is documented. |

## CAB Summary

This change should not move to CAB approval until the requester adds a rollback plan and Security approval is completed. The production authentication scope creates a material risk if rollback is not defined.

## Required Corrections

1. Add a rollback or contingency plan.
2. Confirm whether rollback has been tested in a lower environment.
3. Obtain Security approval before CAB review.

## Recommended Next Action

Return the change to the requester with a clear note that CAB review is blocked pending rollback documentation and Security approval.

# Sample Output: RCA Governance Analysis

## RCA Governance Review Summary

**RCA Quality:** Needs Revision  
**Governance Risk:** High  
**Executive Readiness:** Not Ready

## Key Findings

- The RCA identifies a technical cause, but it does not explain why the change was approved as low risk.
- Detection failed because Customer Support identified the issue before monitoring did.
- The runbook gap is documented, but ownership and review cycle are missing.
- Corrective actions are directionally appropriate but not specific enough to track to closure.

## Governance Gaps

| Gap Area | Issue | Required Improvement |
|---|---|---|
| Risk Classification | Change was approved as low risk despite authentication impact. | Add why the risk was underestimated and how risk scoring will be corrected. |
| Monitoring | Customer Support detected the issue before tools. | Add monitoring improvement owner, metric, alert threshold, and due date. |
| Runbook Governance | Runbook lacked token validation checks. | Add owner, approver, review date, and document control requirements. |
| Corrective Actions | Actions are not measurable. | Convert each action into a tracked Jira task with owner and due date. |

## Executive Summary

A production authentication issue caused intermittent login failures for 42 minutes after a configuration change. The immediate technical cause was token validation failure caused by the configuration update. The governance review identified additional process gaps in risk classification, monitoring coverage, and runbook completeness. Corrective actions should be tracked through Jira with clear ownership and due dates.

## Recommended Next Action

Revise the RCA to include detection failure analysis, risk classification failure, runbook governance gaps, and corrective action tracking details.

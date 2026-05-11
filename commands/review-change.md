# review-change

Review a technology change request for governance completeness, CAB readiness, risk, rollback, validation, monitoring, approvals, and audit readiness.

## Use when

Use this command when the user provides a change request, deployment ticket, Jira change, emergency change, production change, standard change, normal change, or CAB submission.

## Related skill

Use the `change-governance-review` skill first. If the request is specifically about CAB agenda readiness or approval conditions, also use the `cab-readiness-check` skill.

## Output format

### Change Governance Review

Status: Ready / Ready with Conditions / Not Ready  
Risk Rating: Low / Medium / High  
CAB Recommendation: Approve / Approve with Conditions / Hold / Reject

### Key Findings

- Finding 1
- Finding 2
- Finding 3

### Required Fixes Before Approval

| Area | Gap | Required Fix |
|---|---|---|

### Jira-Ready Governance Note

Provide a concise internal note suitable for a Jira change ticket.

### Next Action

Provide one clear next action.

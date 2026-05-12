# Test Case: Executive GRC Summary

## Skill Under Test

`executive-grc-summary`

## Scenario

Governance needs to brief leadership on recurring production change control gaps, evidence weaknesses, RCA issues, and open remediation ownership.

## Prompt

```text
Use the executive-grc-summary skill to turn the following governance activity into an executive-ready summary.

Governance Activity Summary:
During review of production change CM-2026-041 for the Reporting Service, governance identified control gaps across change approval, validation, rollback planning, monitoring, RCA quality, audit evidence readiness, and risk documentation.

Key Issues:
- Security review was pending at deployment.
- Validation evidence only said confirmed working.
- Rollback plan said revert if needed.
- Monitoring evidence was missing.
- Related outage was detected by business users.
- RCA root cause stated only configuration value was incorrect.
- Corrective actions lacked named owners and due dates.
- Risk register entry was created and residual risk remains high.

Audience: IT leadership and executive stakeholders.
```

## Expected Output

A concise executive summary with:

- Current status.
- Business impact.
- Key governance concerns.
- Risk posture.
- Leadership decisions needed.
- Recommended actions.

## Expected Findings

The output should identify:

- Active governance control gap.
- High residual risk.
- Audit evidence exposure.
- RCA quality issue.
- Corrective action ownership gap.
- Leadership decision needed to assign owners and enforce remediation.

## Scoring Notes

A strong output should be clear enough for executives and specific enough for governance follow-up.

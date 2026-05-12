# Test Case: Audit Evidence Quality Review

## Skill Under Test

`control-evidence-quality-check`

## Scenario

An audit evidence package for a production change has weak validation, pending security review, vague rollback, and missing monitoring traceability.

## Prompt

```text
Use the control-evidence-quality-check skill to evaluate the following evidence package for audit submission readiness.

Control Objective:
Production changes must be reviewed, approved, tested, implemented, validated, and monitored.

Evidence Package:
- Change ticket screenshot
- Manager approval screenshot
- Deployment note
- Slack discussion
- Validation note: confirmed working
- Rollback plan: revert if needed
- Application log screenshot taken the next day

Known Issues:
- Security review is listed as pending.
- No pre-deployment testing evidence is attached.
- Validation evidence does not include tester name, timestamp, test steps, or result.
- Monitoring evidence is not tied to the deployment window.
- A related RCA exists but is not linked.
- A related risk register entry exists but is not linked.
```

## Expected Decision

Do not submit as-is.

## Expected Findings

The output should identify:

- Evidence package is not audit-ready.
- Security approval gap must be resolved or disclosed.
- Testing evidence is missing.
- Validation evidence is weak.
- Rollback evidence is not actionable.
- Monitoring evidence is not tied to deployment window.
- Slack discussion is supporting context, not primary evidence.
- RCA and risk register should be linked.
- Submission should include explanatory cover note if gaps remain.

## Scoring Notes

A strong output should distinguish between missing evidence, weak evidence, and contradictory evidence.

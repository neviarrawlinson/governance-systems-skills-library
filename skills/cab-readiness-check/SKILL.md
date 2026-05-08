---
name: cab-readiness-check
description: Determines whether a technology change request is ready for Change Advisory Board review. Use when preparing CAB agendas, reviewing tickets before CAB, identifying approval blockers, or deciding whether a change should be held, approved, rejected, or approved with conditions.
---

# CAB Readiness Check

## Purpose

Use this skill to determine whether a change request is ready to be reviewed by the Change Advisory Board.

This skill focuses on CAB decision readiness. It should identify whether the change has enough information for the board to make a responsible decision without requiring unnecessary back-and-forth during the meeting.

## CAB Readiness Criteria

Review the change request for the following:

1. Submission Completeness
   - Change title is specific.
   - Business reason is clear.
   - Change type matches the actual work.
   - Environment is accurate.
   - Planned start and end times are present.

2. Implementation Readiness
   - Implementation steps are clear.
   - Owner is identified.
   - Dependencies are known.
   - Timing is realistic.

3. Validation Readiness
   - Success criteria are defined.
   - Testing or validation method is included.
   - Responsible validator is identified.
   - Post-change confirmation is planned.

4. Rollback Readiness
   - Backout steps are documented.
   - Rollback trigger is clear.
   - Rollback owner is identified.
   - No-rollback scenarios include a justification and contingency plan.

5. Risk Readiness
   - Operational, customer, security, compliance, and business impacts are addressed.
   - Risk level matches the scope and environment.
   - Risk mitigation is documented.

6. Approval Readiness
   - Manager approval is present where required.
   - Security review is present where required.
   - Compliance review is present where required.
   - Emergency approval is present where required.

7. Meeting Readiness
   - The requester can explain the change in plain language.
   - The change can be summarized in 1 to 3 sentences.
   - The board can clearly decide approve, approve with conditions, hold, or reject.

## CAB Decision Logic

Use this decision logic:

- Approve: Required information and approvals are complete, and risk is understood.
- Approve with Conditions: Minor items need correction, but they do not materially change the risk decision.
- Hold: Important information is missing and should be fixed before approval.
- Reject: The change is misclassified, high-risk without controls, scheduled during a restricted window without justification, or lacks required approvals.

## Output Format

### CAB Readiness Result

CAB Status: Ready / Ready with Conditions / Not Ready  
Recommended CAB Decision: Approve / Approve with Conditions / Hold / Reject  
Primary Reason:

### CAB Talking Points

- Point 1
- Point 2
- Point 3

### Blockers or Conditions

| Item | Severity | Owner | Required Action |
|---|---|---|---|
|  |  |  |  |

### CAB Summary Statement

Write a concise summary that can be used in a CAB agenda or readout.

### Final Recommendation

Provide the next action for governance, the requester, or the CAB chair.

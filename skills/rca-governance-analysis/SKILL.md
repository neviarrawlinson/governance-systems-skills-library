---
name: rca-governance-analysis
description: Reviews incident and RCA documentation for root cause quality, process gaps, monitoring gaps, ownership, corrective actions, recurrence risk, and executive readiness. Use when evaluating outage writeups, postmortems, incident reviews, RCA drafts, corrective action plans, or governance follow-up items.
---

# RCA Governance Analysis

## Purpose

Use this skill to review RCA documentation through a governance lens.

The goal is not only to confirm the technical cause. The goal is to determine whether the RCA explains what happened, why it happened, why controls did or did not prevent it, how it was detected, who owns corrective actions, and how recurrence will be reduced.

## Review Categories

1. Incident Summary
   - Is the incident explained clearly?
   - Are date, time, duration, systems, teams, and customer impact included?
   - Is the severity or priority reasonable?

2. Timeline Quality
   - Is the timeline complete and chronological?
   - Does it show detection, escalation, response, mitigation, recovery, and closure?
   - Are delays or handoff gaps visible?

3. Root Cause Quality
   - Does the RCA identify the actual root cause instead of only the symptom?
   - Are contributing factors included?
   - Does the analysis explain why the issue was not prevented?

4. Monitoring and Detection
   - How was the issue detected?
   - Should internal monitoring have detected it sooner?
   - Were alerts, logs, dashboards, or runbooks effective?
   - Were there detection gaps?

5. Process and Governance Gaps
   - Were change management, access management, runbook control, incident response, vendor oversight, or communication processes involved?
   - Were ownership or approval gaps present?
   - Were any documented procedures missing, outdated, or bypassed?

6. Corrective Actions
   - Are corrective actions specific, assigned, and time-bound?
   - Do they address root cause and contributing factors?
   - Are they tracked in a system of record?
   - Are preventive actions included, not only cleanup actions?

7. Executive Readiness
   - Can the RCA be summarized clearly for leadership?
   - Does it identify risk, impact, accountability, and next steps?
   - Are sensitive details handled appropriately?

## Output Format

### RCA Governance Review Summary

RCA Quality: Strong / Adequate / Needs Improvement / Insufficient  
Recurrence Risk: Low / Medium / High  
Executive Readiness: Ready / Needs Revision / Not Ready

### Key Observations

- Observation 1
- Observation 2
- Observation 3

### Gaps Identified

| Gap Area | Finding | Governance Concern | Required Action |
|---|---|---|---|
| Root Cause |  |  |  |
| Monitoring |  |  |  |
| Process |  |  |  |
| Ownership |  |  |  |
| Corrective Actions |  |  |  |

### Corrective Action Recommendations

| Action | Owner | Priority | Due Date Recommendation | Evidence Needed |
|---|---|---|---|---|
|  |  |  |  |  |

### Executive Summary

Write a concise leadership-ready summary of the incident, governance finding, recurrence risk, and required follow-up.

### Governance Follow-Up Note

Write a concise note that can be pasted into Jira, Confluence, or an RCA tracking ticket.

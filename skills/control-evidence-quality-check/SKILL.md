---
name: control-evidence-quality-check
description: Evaluates audit evidence for completeness, accuracy, traceability, date coverage, reviewer signoff, control relevance, and submission readiness. Use when reviewing SOC 2, ISO 27001, ITGC, access review, change management, incident, vendor, or policy evidence before submitting to auditors.
---

# Control Evidence Quality Check

## Purpose

Use this skill to determine whether evidence is audit-ready before it is submitted to an auditor, assessor, customer, or internal reviewer.

## Review Criteria

### Evidence Relevance
- Does the evidence directly support the control or request?
- Does it answer the specific auditor question?
- Is there unnecessary or sensitive information that should be removed?

### Completeness
- Does the evidence cover the full requested period?
- Are all populations, samples, screenshots, exports, approvals, or artifacts included?
- Are supporting explanations included where needed?

### Traceability
- Can the evidence be tied to a system, ticket, user, date, owner, reviewer, or control?
- Are filenames, request IDs, ticket IDs, and control references clear?

### Review and Approval
- Is reviewer signoff visible where required?
- Is management review documented?
- Are timestamps and evidence dates clear?

### Quality Risks
- Is the evidence blurry, incomplete, outdated, inconsistent, or missing context?
- Does anything contradict the control narrative?
- Could an auditor reasonably ask for follow-up?

## Expected Output

Evidence readiness rating, issues found, remediation checklist, and auditor-ready response language.

## Required Output Format

Return the review in this structure:

### Governance Decision Summary

Status: Ready / Ready with Conditions / Not Ready  
Overall Risk: Low / Medium / High / Critical  
Recommended Decision: Approve / Conditionally Approve / Hold / Reject / Escalate

### Key Findings

- Finding 1
- Finding 2
- Finding 3

### Missing or Weak Areas

| Area | Issue | Required Fix | Owner / Reviewer |
|---|---|---|---|
|  |  |  |  |

### Governance Notes

Provide concise notes suitable for Jira, Confluence, an audit workpaper, or an internal governance review record.

### Required Follow-Up Actions

List the top 3 to 5 actions needed before approval, closure, or escalation.

### Questions for the Requester

Ask only the questions needed to resolve material gaps.

## Operating Guidance

- Be practical, direct, and decision-oriented.
- Identify material gaps instead of rewriting every detail.
- Separate governance blockers from minor documentation improvements.
- Do not invent approvals, evidence, owners, dates, or risk acceptance.
- Where information is missing, state what is missing and why it matters.
- Keep final notes usable in Jira, Confluence, audit workpapers, or leadership summaries.

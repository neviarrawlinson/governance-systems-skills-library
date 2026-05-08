---
name: policy-exception-review
description: Reviews policy exception requests for business justification, risk impact, compensating controls, approval requirements, expiration date, ownership, and audit-ready documentation. Use when evaluating exceptions to security, IT, compliance, access, change management, vendor, or data governance policies.
---

# Policy Exception Review

## Purpose

Use this skill to evaluate whether a policy exception request is complete, justified, time-bound, risk-aware, and ready for approval or escalation.

## Review Criteria

### Exception Scope
- Is the policy, standard, control, or requirement being excepted clearly identified?
- Is the system, team, user group, vendor, or process in scope clearly named?
- Is the exception narrow enough to review and monitor?

### Business Justification
- Is the business need clear?
- Is there a time-sensitive operational reason?
- Has the requester explained why the standard process cannot be followed?

### Risk Impact
- Does the request explain security, compliance, operational, customer, financial, or audit risk?
- Is the risk level reasonable based on scope and exposure?
- Are downstream impacts identified?

### Compensating Controls
- Are alternative safeguards documented?
- Do the compensating controls reduce risk enough for temporary approval?
- Are monitoring, logging, review, or detective controls included?

### Duration and Expiration
- Is the exception temporary?
- Does it include an expiration or review date?
- Is there a remediation plan to return to compliance?

### Ownership and Approvals
- Is the risk owner identified?
- Are manager, security, compliance, legal, or executive approvals required?
- Is acceptance of residual risk explicit?

### Audit Readiness
- Would the record explain what was excepted, why, for how long, who approved it, and how it will be monitored?
- Can the organization defend the exception during an audit or review?

## Expected Output

Governance exception decision, risk summary, required conditions, approval path, and Jira/Confluence-ready governance note.

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

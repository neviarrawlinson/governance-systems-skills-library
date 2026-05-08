---
name: ai-governance-intake-review
description: Reviews proposed AI tools, models, automations, copilots, data uses, and AI-assisted workflows for governance, risk, privacy, security, compliance, ownership, transparency, and approval readiness. Use when evaluating AI tool intake, AI vendor requests, internal AI workflow proposals, or AI risk reviews.
---

# AI Governance Intake Review

## Purpose

Use this skill to evaluate whether an AI use case is ready for governance review and whether the proposed use introduces data, compliance, security, operational, reputational, or human oversight risk.

## Review Criteria

### Use Case and Ownership
- What AI tool, model, or workflow is being proposed?
- What business problem does it solve?
- Who owns the use case and ongoing monitoring?

### Data Classification
- What data will be entered, processed, stored, or generated?
- Does the use involve customer data, PHI, PII, financial data, employee data, confidential business data, or regulated information?
- Will prompts or outputs be retained by a vendor?

### Risk and Impact
- Could the AI output affect customers, employees, compliance decisions, financial decisions, access, health, legal matters, or production systems?
- What happens if the output is wrong, biased, incomplete, or unauthorized?

### Human Oversight
- Is a human reviewer required before use?
- Who validates the output?
- Are prohibited uses or approval boundaries defined?

### Vendor and Security Review
- Is this a third-party AI service, embedded feature, internal model, or automation?
- Are terms, data retention, admin controls, logging, SSO, and security evidence reviewed?

### Governance Decision
- Should the use case be approved, conditionally approved, sent to security/privacy/legal, piloted, or rejected?
- What conditions or controls are required?

## Expected Output

AI intake readiness decision, risk classification, required reviews, guardrails, and approval conditions.

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

---
name: third-party-risk-review
description: Reviews vendors, SaaS tools, service providers, integrations, and third-party relationships for security, privacy, compliance, operational, data, and business risk. Use when assessing new vendors, renewals, questionnaires, SOC reports, DPAs, contracts, or application intake requests.
---

# Third-Party Risk Review

## Purpose

Use this skill to evaluate third-party risk and produce a practical vendor review summary that is ready for procurement, security, compliance, legal, or leadership review.

## Review Criteria

### Vendor Context
- What product or service is being reviewed?
- What business problem does it solve?
- Who requested it and who will own it?

### Data and Access
- What data will the vendor access, process, store, or transmit?
- Does the vendor integrate with internal systems?
- Will the vendor have admin, API, SSO, production, customer, PHI, PII, financial, or sensitive data access?

### Security Evidence
- Is a SOC 2, ISO 27001 certificate, penetration test summary, security whitepaper, or questionnaire available?
- Is the evidence current and relevant to the product or service?
- Are exceptions or qualified findings present?

### Privacy and Contract Considerations
- Is a DPA, BAA, privacy policy, subprocessor list, or data retention statement required?
- Are data location and deletion obligations clear?
- Are breach notification terms known?

### Operational and Business Risk
- What teams depend on the vendor?
- Is the vendor mission critical?
- Is there redundancy, exit planning, or internal support readiness?

### Risk Rating and Decision
- What is the recommended risk rating?
- What conditions should be required before approval?
- Should the vendor be approved, conditionally approved, deferred, or rejected?

## Expected Output

Vendor risk summary, missing evidence list, approval conditions, residual risk statement, and stakeholder questions.

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

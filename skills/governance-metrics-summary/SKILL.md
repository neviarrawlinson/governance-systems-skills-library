---
name: governance-metrics-summary
description: Turns operational governance data into leadership-ready metrics, trends, risks, exceptions, and action-oriented summaries. Use when summarizing CAB metrics, change volume, emergency changes, delayed closures, RCA actions, audit requests, evidence status, policy exceptions, or GRC program health.
---

# Governance Metrics Summary

## Purpose

Use this skill to convert raw governance data into a concise executive-ready summary that supports decisions, accountability, and process improvement.

## Review Criteria

### Metric Context
- What period is covered?
- What process or program is being measured?
- Who is the intended audience?

### Core Metrics
- What are the counts, trends, categories, and status breakdowns?
- Are production, emergency, high-risk, delayed, rejected, or exception items separated?

### Risk Signals
- What patterns suggest control weakness, operational risk, compliance exposure, or process friction?
- Are there repeat offenders, aging items, missing approvals, or incomplete documentation?

### Executive Summary
- What should leaders know in 30 seconds?
- What decision, escalation, or action is needed?
- What is improving, worsening, or stable?

### Action Plan
- What are the top follow-up actions?
- Who owns them?
- What should be tracked next?

## Expected Output

Executive snapshot, metric table, trend observations, risk/exception callouts, and recommended actions.

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

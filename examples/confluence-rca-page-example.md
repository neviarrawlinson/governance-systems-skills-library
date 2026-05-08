# Confluence RCA Page Example

## RCA Title

Production Authentication Login Failures, May 3, 2026

## Document Control

| Field | Value |
|---|---|
| Owner | Engineering |
| Governance Reviewer | IT Governance |
| Status | Draft |
| Review Date | 2026-05-06 |
| Classification | Internal |

## Executive Summary

On May 3, 2026, production users experienced intermittent login failures for 42 minutes after a configuration change caused token validation failures. Customer Support reported the issue before monitoring alerts triggered. The immediate issue was resolved by reverting the configuration and restarting the authentication service.

## Root Cause

The direct technical cause was a configuration update that caused token validation failures for some active user sessions.

## Contributing Factors

| Area | Finding |
|---|---|
| Risk Classification | The change was classified as low risk despite authentication impact. |
| Monitoring | Monitoring did not alert before Customer Support detected the issue. |
| Runbook | The runbook did not include token validation checks. |
| Governance Review | Approval did not identify missing validation depth. |

## Corrective Actions

| Action | Owner | Due Date | Tracking Ticket |
|---|---|---|---|
| Update authentication deployment checklist | Engineering | 2026-05-20 | TBD |
| Add token validation monitoring | SRE | 2026-05-22 | TBD |
| Update runbook with token validation checks | Engineering | 2026-05-24 | TBD |
| Review risk scoring criteria for authentication changes | IT Governance | 2026-05-27 | TBD |

## Governance Review Notes

The RCA should be revised before executive readout to include detection failure analysis, clearer corrective action owners, due dates, and evidence expectations for closure.

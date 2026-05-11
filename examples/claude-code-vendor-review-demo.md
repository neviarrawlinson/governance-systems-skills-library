# Claude Code Demo: Vendor Review

## Scenario

A SaaS vendor requests production API access and CSV export capability before completing due diligence.

## Prompt

```text
Use the assess-vendor command to review this vendor intake.

Vendor: InsightDash Analytics
Type: SaaS analytics platform
Business Purpose: Improve internal reporting dashboards.
Data: Internal reporting data, employee user IDs, department metrics, CSV exports.
Access: SSO for 25 users, API connection to production Reporting Service, CSV export.
Evidence: SOC 2 not provided, DPA not reviewed, security questionnaire not completed.
Requested Decision: Approve production pilot within two weeks.
```

## Expected Outcome

The command should recommend holding production approval.

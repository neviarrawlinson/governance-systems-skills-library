# Test Case: Third-Party Risk Review

## Skill Under Test

`third-party-risk-review`

## Scenario

A SaaS analytics vendor is requested for production API integration, but SOC 2, DPA, and security questionnaire are missing.

## Prompt

```text
Use the third-party-risk-review skill to review the following vendor request.

Vendor Name: InsightDash Analytics
Vendor Type: SaaS reporting and analytics platform
Business Owner: Reporting Services Team
Purpose: Improve internal reporting dashboards.
Data Involved: Internal reporting data, employee user IDs, department metrics, exported CSV reports.
Access Requested: SSO for 25 users, API connection to Reporting Service, CSV export capability.
Compliance Context: SOC 2 not provided. DPA not reviewed. Security questionnaire not completed.
Integration Context: Vendor would connect to production Reporting Service through API.
Known Risk Context: Reporting Service has a recent outage and open high residual risk entry.
Requested Decision: Approve pilot within two weeks.
```

## Expected Decision

Hold production approval. Consider limited non-production pilot only.

## Expected Findings

The output should identify:

- SOC 2 missing.
- DPA missing.
- Security questionnaire missing.
- API production integration risk.
- CSV export risk.
- SSO and access review requirements.
- Open Reporting Service risk increases concern.
- Non-production synthetic-data pilot may be acceptable.
- Production approval requires security, privacy, legal, and governance review.

## Scoring Notes

A strong output should recommend a practical path forward without approving unsafe production use.

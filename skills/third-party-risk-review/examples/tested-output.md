# Tested Output: InsightDash Analytics Third-Party Risk Review

## Input Summary

Vendor Name: InsightDash Analytics  
Vendor Type: SaaS reporting and analytics platform  
Business Owner: Reporting Services Team  

Purpose:  
The team wants to use InsightDash Analytics to improve internal reporting dashboards and provide faster visibility into operational performance.

Data Involved:
- Internal reporting data
- Employee user IDs
- Department-level performance metrics
- Exported CSV reports from the Reporting Service

Access Requested:
- SSO access for 25 internal users
- API connection to the Reporting Service
- Ability to export reports to CSV

Compliance Context:
- SOC 2 report not provided.
- Vendor states SOC 2 is “in progress.”
- No DPA has been reviewed.
- No security questionnaire has been completed.

Integration Context:
- Tool would connect to the production Reporting Service through an API.
- Team wants to pilot within two weeks.

Known Risk Context:
- Reporting Service recently had a production outage related to a database configuration change.
- Governance has an open high residual risk entry related to weak validation, rollback, monitoring, and change evidence for this service.

Requested Decision:
Approve the vendor for pilot use.

## Third-Party Risk Review Summary

Status: Not Ready for Production Approval  
Recommended Decision: Hold  
Risk Rating: High  
Pilot Recommendation: Consider non-production pilot only after minimum guardrails are defined.  
Production Approval: Not approved as submitted.

## Key Findings

- The business need is legitimate, but the vendor request is not ready for production approval.
- The vendor has not provided a SOC 2 report or equivalent security assurance evidence.
- A DPA has not been reviewed, which is a significant privacy and legal concern because employee user IDs and internal reporting data may be processed by the vendor.
- A security questionnaire has not been completed.
- The requested API connection to the production Reporting Service introduces integration and operational risk.
- CSV export functionality introduces data egress, retention, access, and deletion concerns.
- The Reporting Service already has an open high residual risk entry, which increases concern around adding an external SaaS integration before internal control gaps are remediated.
- The requested two-week timeline is not realistic for production approval under current conditions.

## Decision Rationale

The recommended decision is **Hold**, not reject.

The request should be held because there is a path to approval, but the required third-party risk, privacy, security, and integration reviews are incomplete. The vendor may be acceptable after due diligence, but production use cannot be approved until the required evidence and controls are in place.

Three independent blockers support the hold decision:

| Blocker | Risk Concern | Required Action |
|---|---|---|
| Missing Security Evidence | No SOC 2 report, security questionnaire, or equivalent assurance evidence has been provided. | Send and complete the security questionnaire. Obtain SOC 2 report or compensating evidence. |
| Missing DPA | Employee user IDs and internal reporting data may be processed by the vendor. | Complete DPA review before any employee or internal reporting data is shared. |
| Open Reporting Service Risk | The production Reporting Service has an open high residual risk entry related to weak validation, rollback, monitoring, and change evidence. | Resolve or account for the open risk before approving production API integration. |

## Risk Area Review

| Risk Area | Rating | Assessment |
|---|---|---|
| Security Risk | High | Vendor security evidence has not been provided. SOC 2 is only described as “in progress.” |
| Privacy Risk | High | Employee user IDs and internal reporting data may be processed without a reviewed DPA. |
| Compliance Risk | High | Missing SOC 2, DPA, and security questionnaire create audit and vendor governance exposure. |
| Operational Risk | High | Production Reporting Service has recent outage history and open residual risk. |
| Integration Risk | High | API connection to production Reporting Service introduces technical and control risk. |
| Data Risk | High | CSV export capability creates data egress and retention concerns. |
| Business Risk | Medium | The business need is valid, but the implementation timeline is too aggressive for production use. |

## Production Approval Assessment

Production approval should not be granted as submitted.

The request does not include enough evidence to demonstrate that InsightDash Analytics can safely connect to the production Reporting Service, process employee identifiers, export internal reports, or meet security and privacy expectations.

Production use should remain blocked until:

1. Security questionnaire is completed and reviewed.
2. SOC 2 report or equivalent security evidence is obtained.
3. DPA is reviewed and approved.
4. Data classification and data flow are documented.
5. API integration design is reviewed.
6. CSV export controls are defined.
7. Access provisioning and deprovisioning process is documented.
8. Reporting Service open risk is reviewed in relation to this vendor request.
9. Pilot scope, success criteria, and exit criteria are defined.

## Non-Production Pilot Option

A limited non-production pilot may be considered if the team needs to evaluate the tool within the requested two-week timeline.

Recommended pilot guardrails:

- Use sandbox or non-production environment only.
- Use synthetic, anonymized, or non-sensitive data.
- Do not connect to the production Reporting Service.
- Do not export production data.
- Limit access to named pilot users.
- Disable or restrict CSV export if possible.
- Document pilot success criteria.
- Continue security, privacy, and vendor due diligence in parallel.
- Require approval before any production connection or live data transfer.

This approach allows the business team to evaluate functionality without creating unnecessary production, audit, privacy, or integration exposure.

## CSV Export Concern

CSV export capability requires separate review.

Once data is exported from a source system into an external SaaS platform, the organization may lose visibility into:

- Where the data is stored.
- Who can access the exported data.
- Whether the data is further shared or downloaded.
- How long the data is retained.
- Whether the data can be deleted on request.
- Whether access is logged and reviewable.

These concerns should be addressed in the DPA, security review, data flow documentation, and vendor access controls before any internal reporting data or employee identifiers are shared.

## Required Questions for Vendor and Business Owner

### Vendor Questions

1. Can the vendor provide a current SOC 2 Type II report?
2. If SOC 2 is still in progress, what equivalent security evidence can be provided?
3. What security controls protect customer data?
4. Where is customer data stored?
5. How is data encrypted in transit and at rest?
6. How are access logs retained and made available?
7. What subcontractors or subprocessors are used?
8. What is the data retention and deletion process?
9. Can CSV export be restricted or disabled?
10. What incident notification commitments are included?

### Business Owner Questions

1. Why is production access required for the pilot?
2. Can the pilot be performed using sandbox or anonymized data?
3. Which users need access and why?
4. What specific dashboards or reports will be tested?
5. What is the success criteria for the pilot?
6. What is the expected duration of the pilot?
7. Who owns access review and removal after the pilot?
8. Who will approve movement from pilot to production use?

## Required Evidence Before Production Approval

The following evidence should be collected before production use is approved:

- Completed security questionnaire.
- SOC 2 report or compensating security assurance evidence.
- Reviewed and approved DPA.
- Data classification and data flow diagram.
- API integration review.
- Access control and SSO configuration plan.
- User access list for pilot and production.
- CSV export control decision.
- Vendor risk assessment.
- Business owner approval.
- Security approval.
- Privacy or legal approval.
- Governance approval.
- Pilot success criteria and exit criteria.
- Production implementation and rollback plan.

## Governance Note

**Third-Party Risk Review**

- **Vendor**: InsightDash Analytics
- **Business Purpose**: Improve internal reporting dashboards and operational performance visibility.
- **Decision**: Hold. Not approved for production use as submitted.
- **Risk Summary**: High risk due to missing SOC 2 evidence, missing DPA, incomplete security questionnaire, production API integration request, CSV export capability, and open high residual risk associated with the Reporting Service.
- **Production Approval**: Not approved.
- **Pilot Option**: Non-production pilot may be considered using synthetic or anonymized data with no production API connection.
- **Required Actions**: Complete security questionnaire, obtain SOC 2 or equivalent evidence, complete DPA review, document data flows, review API integration, define CSV export controls, and establish pilot guardrails.

Governance review completed. Vendor request should remain on hold until third-party risk, privacy, security, and integration review requirements are satisfied.

## Recommended Next Action

Hold production approval and offer a limited non-production pilot path using synthetic or anonymized data. Begin vendor due diligence immediately by sending the security questionnaire, requesting SOC 2 or equivalent evidence, initiating DPA review, and documenting the proposed data flow and API integration.

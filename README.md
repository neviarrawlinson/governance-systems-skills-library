# Governance Systems Skills Library

Practical Claude-compatible skill packs for Governance Systems Engineering, change governance, RCA analysis, audit evidence, risk documentation, vendor risk, AI governance intake, and executive GRC reporting.

## Interactive Demo Site

The GitHub Pages site now includes an interactive project overview with searchable skill cards, category filters, direct links to skill folders, tested output examples, framework mapping resources, demo pathways, and the latest release download.

View the live site here:

https://neviarrawlinson.github.io/governance-systems-skills-library/

Supporting site documentation:

- [Interactive Site Guide](docs/interactive-site-guide.md)
- [Site Content Map](docs/site-content-map.md)
- [Site Upgrade Checklist](docs/site-upgrade-checklist.md)

## Project Preview

### Live Landing Page

![Governance Systems Skills Library Landing Page](assets/screenshots/landing-page-hero.png)

### Skill Library Overview

![Skill Library Section](assets/screenshots/skill-library-section.png)

### Tested Output Examples

![Tested Output Section](assets/screenshots/tested-output-section.png)

### Repository Structure

![GitHub Repository Structure](assets/screenshots/github-repo-structure.png)

### Skills Folder Structure

![Skills Folder Structure](assets/screenshots/skills-folder-structure.png)

### Tested Skill Output Example

![Tested Output Example](assets/screenshots/tested-output-example.png)

### Validation Workflow

![Actions Validation Success](assets/screenshots/actions-validation-success.png)

### Release Assets

![Release Assets](assets/screenshots/release-assets.png)

### Architecture and Methodology

![Architecture and Methodology](assets/screenshots/architecture-methodology.png)

## Why This Project Exists

Many governance programs fail because controls live in documents but do not show up consistently in tickets, approvals, evidence, reporting, or operational decisions.

Governance Systems Engineering turns governance expectations into repeatable systems, decision logic, checklists, workflows, skill packs, and audit-ready outputs.

This project was created to demonstrate how GRC work can move beyond static documentation and become a structured, repeatable, AI-assisted governance workflow.

## What Makes This Different

This is not a generic framework reference library. This project is workflow-centered and focuses on the work practitioners actually perform:

- Reviewing technology change requests
- Preparing CAB decisions
- Evaluating RCA quality
- Checking audit evidence before submission
- Creating risk register entries
- Reviewing policy exceptions
- Assessing third-party risk
- Summarizing governance metrics
- Reviewing AI use cases before approval
- Producing executive-ready GRC summaries

## Download Skill Packages

The latest packaged Claude-compatible skill bundle is available from the official GitHub release:

[Download governance-systems-skill-packages.zip](https://github.com/neviarrawlinson/governance-systems-skills-library/releases/tag/v1.3.0)

Current release: **v1.3.0 - Interactive Demo Site Upgrade**

## Claude Code Plugin Support

This repository now includes a Claude Code plugin manifest, making the Governance Systems Skills Library plugin-ready for Claude Code.

Plugin metadata:

- [.claude-plugin/plugin.json](.claude-plugin/plugin.json)

Plugin documentation:

- [Claude Code Plugin Installation Guide](docs/claude-code-plugin-installation.md)

The current plugin layer focuses on making the existing GRC skills library discoverable and installable as a Claude Code plugin-ready toolkit. The repository does not currently include custom Claude Code commands, agents, hooks, MCP servers, or monitors.

Current plugin-supported skill areas include:

- Change governance review
- CAB readiness
- RCA governance analysis
- Audit evidence review
- Risk register building
- Executive GRC reporting
- Policy exception review
- Third-party risk review
- Control evidence quality review
- Governance metrics summary
- AI governance intake review

## Getting Started

Use these guides to download, install, test, and apply the skills:

- [Quickstart Guide](docs/quickstart.md)
- [Installation and Usage Guide](docs/installation-and-usage-guide.md)
- [User Guide](docs/user-guide.md)
- [Skill Testing Prompt Library](docs/skill-testing-prompt-library.md)
- [Troubleshooting Guide](docs/troubleshooting-guide.md)
- [Skill Installation Checklist](docs/skill-installation-checklist.md)

For testing and documentation, use the included:

- [Skill Test Log Template](templates/skill-test-log-template.md)

## Framework Mapping

This library includes framework mapping documentation to show how each skill supports common governance, risk, compliance, audit, and control objectives.

Framework mapping resources:

- [Skill-to-Framework Matrix](framework-mapping/skill-to-framework-matrix.md)
- [ISO 27001 Skill Mapping](framework-mapping/iso-27001-skill-mapping.md)
- [SOC 2 Skill Mapping](framework-mapping/soc-2-skill-mapping.md)
- [NIST CSF Skill Mapping](framework-mapping/nist-csf-skill-mapping.md)
- [COBIT Skill Mapping](framework-mapping/cobit-skill-mapping.md)
- [AI Governance Skill Mapping](framework-mapping/ai-governance-skill-mapping.md)
- [Framework Mapping Guide](docs/framework-mapping-guide.md)
- [Framework Mapping Coverage Model](docs/framework-mapping-coverage-model.md)

These mappings are intended to show practical alignment, not to replace formal audit, legal, or regulatory interpretation.

## Project Highlights

- **11 Claude-compatible GRC skills** organized as reusable skill folders
- **11 tested output examples** using realistic governance scenarios
- **Automated validation** through GitHub Actions
- **Automated packaging** for downloadable skill bundles
- **Live GitHub Pages site** for project presentation
- **Framework mapping** for common governance and compliance references
- **Governance quality controls** for release readiness and review

## Skill Packs

| Skill | Category | Purpose |
|---|---|---|
| `change-governance-review` | Change Governance | Reviews change requests for governance completeness, CAB readiness, risk, rollback, validation, monitoring, approvals, and audit readiness. |
| `cab-readiness-check` | Change Governance | Determines whether a change request is ready for CAB review and decision-making. |
| `rca-governance-analysis` | Incident Governance | Reviews RCA documentation for root cause quality, process gaps, monitoring gaps, ownership, corrective actions, and executive readiness. |
| `audit-evidence-request` | Audit Readiness | Converts audit evidence requests into evidence checklists, owner questions, response plans, and submission guidance. |
| `risk-register-builder` | Risk Management | Converts findings, issues, incidents, and observations into structured risk register entries. |
| `executive-grc-summary` | Executive Reporting | Creates concise executive-ready summaries for governance, risk, compliance, audit, change, RCA, and control updates. |
| `policy-exception-review` | Policy Governance | Reviews policy exception requests for business justification, risk impact, compensating controls, approval requirements, expiration date, ownership, and audit-ready documentation. |
| `third-party-risk-review` | Vendor Risk | Reviews vendors, SaaS tools, service providers, integrations, and third-party relationships for security, privacy, compliance, operational, data, and business risk. |
| `control-evidence-quality-check` | Audit Readiness | Evaluates audit evidence for completeness, accuracy, traceability, date coverage, reviewer signoff, control relevance, and submission readiness. |
| `governance-metrics-summary` | Governance Reporting | Turns operational governance data into leadership-ready metrics, trends, risks, exceptions, and action-oriented summaries. |
| `ai-governance-intake-review` | AI Governance | Reviews proposed AI tools, models, automations, copilots, data uses, and AI-assisted workflows for governance, risk, privacy, security, compliance, ownership, transparency, and approval readiness. |

## Tested Skill Output

The library includes tested output examples using realistic governance scenarios.

- [Production Restart Change Review Tested Output](skills/change-governance-review/examples/tested-output.md)
- [Database Configuration CAB Readiness Tested Output](skills/cab-readiness-check/examples/tested-output.md)
- [Reporting Service Outage RCA Governance Analysis Tested Output](skills/rca-governance-analysis/examples/tested-output.md)
- [Change Management Audit Evidence Request Tested Output](skills/audit-evidence-request/examples/tested-output.md)
- [Production Change Governance Risk Register Entry Tested Output](skills/risk-register-builder/examples/tested-output.md)
- [Executive GRC Summary for Production Change Governance Finding Tested Output](skills/executive-grc-summary/examples/tested-output.md)
- [Temporary Production Change Security Review Exception Tested Output](skills/policy-exception-review/examples/tested-output.md)
- [InsightDash Analytics Third-Party Risk Review Tested Output](skills/third-party-risk-review/examples/tested-output.md)
- [Change Management Control Evidence Quality Check Tested Output](skills/control-evidence-quality-check/examples/tested-output.md)
- [Governance Metrics Leadership Summary Tested Output](skills/governance-metrics-summary/examples/tested-output.md)
- [AI Reporting Assistant Governance Intake Review Tested Output](skills/ai-governance-intake-review/examples/tested-output.md)

These examples demonstrate how the skills identify governance gaps in implementation planning, validation, rollback, monitoring, approvals, risk documentation, CAB readiness, root cause quality, corrective action ownership, change governance linkage, evidence quality, traceability, audit submission readiness, risk register documentation, executive reporting, policy exception review, compensating controls, risk acceptance, vendor due diligence, data protection, third-party risk review, control evidence quality, governance metrics, trend analysis, leadership reporting, AI governance, prompt retention, model training risk, transparency, and approval readiness.

## Methodology

The library follows a Governance Systems Engineering model:

```text
Governance Requirement
        ↓
Workflow Decision Point
        ↓
Evidence Requirement
        ↓
Risk / Exception Handling
        ↓
Leadership-Ready Output
        ↓
Audit-Ready Record
```

Read more:

- [Governance Systems Engineering Methodology](docs/governance-systems-engineering-methodology.md)
- [Project Architecture](docs/architecture.md)
- [Skill Output Index](docs/skill-output-index.md)
- [Portfolio Positioning Notes](docs/portfolio-positioning-notes.md)

## Repository Structure

```text
docs/                    Project documentation and guides
skills/                  Claude-compatible skill folders
templates/               Reusable governance templates
examples/                Sample inputs, outputs, release notes, and workflow examples
framework-mapping/       Governance workflow mappings to common frameworks
governance-quality/      Skill quality controls and release checklists
scripts/                 Validation scripts
.github/workflows/       GitHub Actions workflows
site/                    GitHub Pages source copy
dist/                    Packaged skill zip files
assets/screenshots/      Optional project screenshots for README and portfolio use
```

## How to Use This Library

You can use this repository in three ways:

1. **As a Claude Skills library**  
   Download the packaged skill bundle from the latest release and use the relevant skill files in Claude.

2. **As a GRC workflow reference library**  
   Review the skill instructions, examples, and templates to understand how governance workflows can be structured.

3. **As a Governance Systems Engineering portfolio project**  
   Use the repository structure, tested outputs, validation workflow, and release packaging model to demonstrate applied GRC engineering capability.

## Validate Skills

Run:

```bash
python scripts/validate-skills.py
```

The validation script checks whether each skill folder includes the expected Claude-compatible structure.

## Package Skills

Run:

```bash
bash package-skills.sh
```

Packages are generated in the `dist/` folder.

## GitHub Actions

This repository includes GitHub Actions workflows for:

- Validating skill structure
- Packaging skill zip files
- Supporting repeatable release readiness

## Intended Use

These skills are designed to help practitioners produce clearer and more consistent governance outputs.

They do not replace professional judgment, legal advice, audit advice, regulatory interpretation, or management approval.

## Current Status

Current project phase: **Complete tested outputs release**

Completed:

- Core skill library structure
- GitHub Pages landing page
- Initial GRC workflow skills
- Advanced governance skills
- Skill catalog
- Framework mapping folder
- Governance quality controls
- Automated validation workflow
- Automated packaging workflow
- Official GitHub releases
- Tested skill output examples for all 11 skills

## Public Launch and Portfolio Resources

This project includes resources to support public launch, portfolio integration, interviews, and professional positioning.

Launch and portfolio resources:

- [Public Launch Plan](docs/public-launch-plan.md)
- [GitHub About Section](docs/github-about-section.md)
- [GitHub Profile README Snippet](docs/github-profile-readme-snippet.md)
- [Resume Project Bullets](docs/resume-project-bullets.md)
- [LinkedIn v1 Project Announcement](docs/linkedin-v1-project-announcement.md)
- [Hashnode Article Draft](docs/hashnode-article-draft.md)
- [Portfolio Project Page](docs/portfolio-project-page.md)
- [Interview Talking Points](docs/interview-talking-points.md)
- [Demo Script](docs/demo-script.md)
- [Project Launch Checklist](templates/project-launch-checklist.md)

These resources are designed to help explain the project as a Governance Systems Engineering portfolio asset for GRC, audit readiness, risk management, AI governance, and operational governance roles.

## Demo and Use Case Resources

This project includes demo resources to show how the skills can be applied across practical governance scenarios.

Demo and use case resources:

- [Demo Walkthrough](docs/demo-walkthrough.md)
- [Use Case Library](docs/use-case-library.md)
- [Recruiter Demo Guide](docs/recruiter-demo-guide.md)
- [Hiring Manager Summary](docs/hiring-manager-summary.md)
- [End-to-End Change Governance Demo](examples/end-to-end-change-governance-demo.md)
- [End-to-End Audit Evidence Demo](examples/end-to-end-audit-evidence-demo.md)
- [End-to-End AI Governance Demo](examples/end-to-end-ai-governance-demo.md)
- [End-to-End Third-Party Risk Demo](examples/end-to-end-third-party-risk-demo.md)
- [Demo Evaluation Scorecard](templates/demo-evaluation-scorecard.md)

These resources are designed to help demonstrate how the library supports real GRC workflows from intake through review, evidence, risk documentation, leadership reporting, and audit-ready output.

## Roadmap

Planned future improvements:

- Add screenshots to the README
- Add more Jira and Confluence workflow examples
- Add release governance examples
- Expand framework mappings
- Add additional AI governance and vendor risk scenarios
- Improve live site navigation
- Add downloadable individual skill buttons to the live site
- Publish v1.0.0 after screenshots, site polish, and expanded workflow examples are complete

## License

MIT License.

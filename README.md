# Governance Systems Skills Library

![Release](https://img.shields.io/github/v/release/neviarrawlinson/governance-systems-skills-library)
![License](https://img.shields.io/github/license/neviarrawlinson/governance-systems-skills-library)
![Skills](https://img.shields.io/badge/skills-11-teal)
![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin--ready-blue)
![Validation](https://img.shields.io/badge/validation-passing-brightgreen)
![GRC](https://img.shields.io/badge/GRC-Governance%20Systems%20Engineering-0f766e)

Practical Claude-compatible skill packs for Governance Systems Engineering, change governance, RCA analysis, audit evidence, risk documentation, vendor risk, AI governance intake, and executive GRC reporting.

## Table of Contents

- [Live Demo](#live-demo)
- [Project Preview](#project-preview)
- [Why This Project Exists](#why-this-project-exists)
- [What Makes This Different](#what-makes-this-different)
- [What Are Claude Skills?](#what-are-claude-skills)
- [Who This Is For](#who-this-is-for)
- [Download Skill Packages](#download-skill-packages)
- [Getting Started](#getting-started)
- [Installation Options](#installation-options)
- [Claude Code Plugin Support](#claude-code-plugin-support)
- [Claude Code Plugin Components](#claude-code-plugin-components)
- [Evaluation and Testing Framework](#evaluation-and-testing-framework)
- [Framework Mapping](#framework-mapping)
- [Project Highlights](#project-highlights)
- [Skill Packs](#skill-packs)
- [Potential Use Cases](#potential-use-cases)
- [Tested Skill Output](#tested-skill-output)
- [Methodology](#methodology)
- [Demo and Use Case Resources](#demo-and-use-case-resources)
- [Public Launch and Portfolio Resources](#public-launch-and-portfolio-resources)
- [Repository Structure](#repository-structure)
- [How to Use This Library](#how-to-use-this-library)
- [Validate Skills](#validate-skills)
- [Validate Plugin Readiness](#validate-plugin-readiness)
- [Package Skills](#package-skills)
- [GitHub Actions](#github-actions)
- [Intended Use](#intended-use)
- [Disclaimer](#disclaimer)
- [Current Status](#current-status)
- [Roadmap](#roadmap)
- [License](#license)

## Live Demo

View the project landing page here:

https://neviarrawlinson.github.io/governance-systems-skills-library/

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

The purpose is to show how governance can be embedded into operational workflows instead of remaining isolated in policy documents.

## What Are Claude Skills?

Claude Skills are reusable instruction packages that help Claude perform a specialized workflow more consistently.

In this project, each skill is designed around a practical GRC workflow such as change review, CAB readiness, RCA analysis, audit evidence review, vendor risk review, policy exception review, AI governance intake, or executive reporting.

Each skill includes a `SKILL.md` file and may also include examples, references, tested outputs, and supporting documentation.

A skill can help standardize:

- What information should be reviewed
- What risks should be identified
- What evidence should be requested
- What decisions should be recommended
- What output format should be produced
- What governance gaps should be escalated

## Who This Is For

This project is designed for:

- GRC analysts and managers
- IT governance teams
- Change management owners
- CAB coordinators
- Audit readiness teams
- ITGC control owners
- Security governance teams
- Vendor risk teams
- AI governance reviewers
- Compliance automation builders
- GRC Engineering practitioners
- Hiring managers evaluating practical GRC engineering ability

## Download Skill Packages

The latest packaged Claude-compatible skill bundle is available from the official GitHub release:

[Download governance-systems-skill-packages.zip](https://github.com/neviarrawlinson/governance-systems-skills-library/releases/tag/v1.4.0)

Current release: **v1.4.0 - Plugin Validation and Evaluation Framework**

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

## Installation Options

| Option | Best For | Description |
|---|---|---|
| Download release package | Claude skill users | Download the latest packaged skill bundle from the release page. |
| Use the repo directly | GRC practitioners and reviewers | Browse the skills, tested outputs, examples, and framework mappings directly in GitHub. |
| Claude Code plugin-ready structure | Developers and technical teams | Use the plugin manifest, commands, agents, and validation workflow as a Claude Code-ready toolkit. |
| GitHub Pages site | Recruiters, hiring managers, and portfolio reviewers | Review the live site for a visual overview of the project, skills, demos, and methodology. |

## Claude Code Plugin Support

This repository includes a Claude Code plugin manifest, making the Governance Systems Skills Library plugin-ready for Claude Code.

Plugin metadata:

- [.claude-plugin/plugin.json](.claude-plugin/plugin.json)

Plugin documentation:

- [Claude Code Plugin Installation Guide](docs/claude-code-plugin-installation.md)

The current plugin layer focuses on making the existing GRC skills library discoverable and installable as a Claude Code plugin-ready toolkit.

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

## Claude Code Plugin Components

The plugin expansion adds Claude Code-ready commands and specialized agent instructions to make the Governance Systems Skills Library easier to use in developer and GRC workflow environments.

Plugin components include:

- [Commands](commands/)
- [Agents](agents/)
- [Claude Code Command Guide](docs/claude-code-command-guide.md)
- [Claude Code Agent Guide](docs/claude-code-agent-guide.md)
- [Plugin Component Map](docs/plugin-component-map.md)
- [Plugin Testing Guide](docs/plugin-testing-guide.md)

Included command workflows:

- `review-change`
- `prepare-cab-summary`
- `assess-vendor`
- `review-ai-intake`
- `summarize-governance-metrics`

Included agent profiles:

- `governance-reviewer`
- `audit-evidence-reviewer`
- `ai-governance-reviewer`
- `third-party-risk-reviewer`

These components extend the project from a skill library into a more complete Claude Code plugin-ready governance toolkit.

## Evaluation and Testing Framework

This repository includes a governance skills evaluation framework to support repeatable testing, scoring, and quality review of skill outputs.

Evaluation resources:

- [Evaluation Framework](tests/README.md)
- [Governance Skills Test Plan](tests/governance-skills-test-plan.md)
- [Evaluation Scorecard](tests/evaluation-scorecard.md)
- [Expected Output Rubric](tests/expected-output-rubric.md)
- [Sample Grader Prompts](tests/sample-grader-prompts.md)
- [Evaluation Methodology](docs/evaluation-methodology.md)
- [Evaluation Results Summary](docs/evaluation-results-summary.md)
- [Evaluation Run Log Template](templates/evaluation-run-log-template.md)

Included test cases:

- [Change Governance Test Case](tests/test-case-change-governance.md)
- [Audit Evidence Test Case](tests/test-case-audit-evidence.md)
- [Third-Party Risk Test Case](tests/test-case-third-party-risk.md)
- [AI Governance Test Case](tests/test-case-ai-governance.md)
- [Executive Summary Test Case](tests/test-case-executive-summary.md)

The evaluation framework is designed to test whether skill outputs:

- Identify governance gaps
- Produce appropriate recommendations
- Document evidence requirements
- Highlight risk and ownership issues
- Generate leadership-ready or audit-ready outputs
- Align with the expected workflow outcome

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
- **Claude Code plugin-ready structure** with manifest, commands, and agents
- **Automated validation** through GitHub Actions
- **Automated packaging** for downloadable skill bundles
- **Plugin readiness validation** for Claude Code plugin components
- **Evaluation framework** for testing skill output quality
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

## Potential Use Cases

| Scenario | Relevant Skill |
|---|---|
| Reviewing a production change before CAB | `change-governance-review` |
| Determining whether a change is ready for CAB | `cab-readiness-check` |
| Reviewing an incomplete RCA | `rca-governance-analysis` |
| Preparing an audit evidence response | `audit-evidence-request` |
| Converting a finding into a risk register entry | `risk-register-builder` |
| Summarizing governance status for leadership | `executive-grc-summary` |
| Reviewing a request to bypass a policy requirement | `policy-exception-review` |
| Assessing a vendor SaaS intake request | `third-party-risk-review` |
| Checking whether control evidence is audit-ready | `control-evidence-quality-check` |
| Turning governance metrics into leadership reporting | `governance-metrics-summary` |
| Reviewing an AI tool or AI-assisted workflow intake | `ai-governance-intake-review` |

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

## Repository Structure

```text
.claude-plugin/          Claude Code plugin manifest
.github/workflows/       GitHub Actions workflows
agents/                  Claude Code-ready agent profiles
assets/screenshots/      Project screenshots for README and portfolio use
commands/                Claude Code-ready command workflows
dist/                    Packaged skill zip files
docs/                    Project documentation and guides
examples/                Sample inputs, outputs, release notes, and workflow examples
framework-mapping/       Governance workflow mappings to common frameworks
governance-quality/      Skill quality controls and release checklists
scripts/                 Validation scripts
site/                    GitHub Pages source copy
skills/                  Claude-compatible skill folders
templates/               Reusable governance templates
tests/                   Evaluation framework, test cases, scorecards, and rubrics
```

## How to Use This Library

You can use this repository in four ways:

1. **As a Claude Skills library**  
   Download the packaged skill bundle from the latest release and use the relevant skill files in Claude.

2. **As a Claude Code plugin-ready toolkit**  
   Use the plugin manifest, commands, agents, and skills structure as the foundation for Claude Code workflows.

3. **As a GRC workflow reference library**  
   Review the skill instructions, examples, templates, test cases, and framework mappings to understand how governance workflows can be structured.

4. **As a Governance Systems Engineering portfolio project**  
   Use the repository structure, tested outputs, validation workflows, release packaging, and evaluation framework to demonstrate applied GRC engineering capability.

## Validate Skills

Run:

```bash
python scripts/validate-skills.py
```

The validation script checks whether each skill folder includes the expected Claude-compatible structure.

## Validate Plugin Readiness

Run:

```bash
python scripts/validate-plugin.py
```

The plugin validation script checks whether the Claude Code plugin-ready components are present, including the plugin manifest, skills, commands, agents, and supporting documentation.

## Package Skills

Run:

```bash
bash package-skills.sh
```

Packages are generated in the `dist/` folder.

## GitHub Actions

This repository includes GitHub Actions workflows for:

- Validating skill structure
- Validating plugin readiness
- Packaging skill zip files
- Supporting repeatable release readiness

## Intended Use

These skills are designed to help practitioners produce clearer and more consistent governance outputs.

They do not replace professional judgment, legal advice, audit advice, regulatory interpretation, or management approval.

## Disclaimer

This project is for educational, portfolio, and workflow demonstration purposes.

It does not replace legal advice, audit advice, regulatory interpretation, organizational approval processes, or professional judgment. Users are responsible for validating outputs against their own policies, controls, risk appetite, compliance obligations, and governance requirements.

## Current Status

Current project phase: **Plugin Validation and Evaluation Framework**

Completed:

- Core skill library structure
- GitHub Pages landing page
- Interactive demo site
- Initial GRC workflow skills
- Advanced governance skills
- Claude Code plugin manifest
- Claude Code-ready commands
- Claude Code-ready agents
- Skill catalog
- Framework mapping folder
- Governance quality controls
- Evaluation and testing framework
- Automated skill validation workflow
- Automated plugin readiness validation workflow
- Automated packaging workflow
- Official GitHub releases
- Tested skill output examples for all 11 skills
- Public launch and portfolio documentation
- Demo and use case resources

## Roadmap

Planned future improvements:

- Add scenario pack expansion
- Add benchmark-style evaluation results
- Add baseline comparison documentation
- Add more Jira and Confluence workflow examples
- Add release governance examples
- Expand team adoption documentation
- Add community feedback log after public launch
- Add downloadable individual skill buttons to the live site
- Improve plugin marketplace readiness documentation
- Continue expanding Governance Systems Engineering use cases

## License

MIT License.

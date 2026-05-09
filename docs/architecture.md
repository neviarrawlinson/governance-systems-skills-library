# Project Architecture

The Governance Systems Skills Library is organized as a practical, portfolio-ready skills system.

## Architecture Overview

```text
governance-systems-skills-library/
│
├── skills/                  Claude-compatible skill folders
│   └── skill-name/
│       ├── SKILL.md          Skill instructions and trigger description
│       ├── README.md         Skill overview and usage notes
│       ├── examples/         Sample input and tested output
│       └── references/       Checklists, rules, and supporting notes
│
├── docs/                    Methodology, testing, release, and architecture docs
├── templates/               Reusable governance templates
├── examples/                Cross-skill examples and release notes
├── framework-mapping/       Workflow mapping to common frameworks
├── governance-quality/      Quality checklists and review rubrics
├── scripts/                 Validation scripts
├── .github/workflows/       Validation and packaging workflows
├── dist/                    Packaged skill zip files
├── site/                    GitHub Pages source copy
└── index.html               Root GitHub Pages landing page
```

## Skill Folder Pattern

Each skill follows a consistent structure:

```text
skill-name/
├── SKILL.md
├── README.md
├── examples/
│   ├── sample-input.md
│   └── tested-output.md
└── references/
```

## Validation Layer

The validation layer checks that each skill follows the expected structure.

```text
scripts/validate-skills.py
.github/workflows/validate-skills.yml
```

This supports repeatability and helps prevent incomplete skill folders from being added.

## Packaging Layer

The packaging layer creates downloadable skill bundles.

```text
package-skills.sh
.github/workflows/package-skills.yml
dist/
```

The packaged bundle can be attached to GitHub releases.

## Presentation Layer

The project includes two presentation surfaces:

1. **README.md**  
   Main portfolio and technical overview.

2. **GitHub Pages site**  
   A public-facing landing page for quick review by recruiters, hiring managers, GRC professionals, and collaborators.

## Governance Quality Layer

The governance quality folder provides review aids that help keep the project consistent.

```text
governance-quality/
├── skill-quality-checklist.md
├── review-rubric.md
└── release-readiness-checklist.md
```

## Release Model

The project currently follows a milestone release model:

| Version | Focus |
|---|---|
| v0.4.0 | Advanced governance skills and quality controls |
| v0.5.0 | Tested outputs for every skill |
| v0.6.0 | Portfolio polish and site upgrade |
| v1.0.0 | Full public-ready release with screenshots, refined site, and expanded examples |
```

## Data Flow

```text
Skill authoring
    ↓
Skill validation
    ↓
Tested output creation
    ↓
Package workflow
    ↓
GitHub release
    ↓
README and site update
    ↓
Portfolio presentation
```

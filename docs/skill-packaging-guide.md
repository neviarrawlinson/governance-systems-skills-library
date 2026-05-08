# Skill Packaging Guide

## Purpose

This guide explains how to package each skill folder into a downloadable zip file.

## Manual Packaging

Each skill folder should be packaged as its own zip file.

Example structure:

```text
change-governance-review.zip
└── change-governance-review/
    ├── SKILL.md
    ├── README.md
    ├── references/
    └── examples/
```

## Script Packaging

From the repository root, run:

```bash
bash package-skills.sh
```

The script creates zip files under:

```text
dist/
```

## Uploading to GitHub

Commit the `dist/` folder if you want visitors to download skill packages directly from the repository.

## Notes

Claude skill upload behavior can vary by environment and plan. If a zip package does not upload correctly, try zipping the contents of the skill folder instead of the parent folder.

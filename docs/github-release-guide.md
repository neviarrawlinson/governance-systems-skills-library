# GitHub Release Guide

Use this guide when publishing a new version of the Governance Systems Skills Library.

## Versioning approach

Use simple semantic versioning:

- Patch: small edits, typo fixes, example improvements.
- Minor: new skills, new templates, new docs, improved packaging.
- Major: major structure changes or breaking skill format updates.

## Release checklist

1. Run `python scripts/validate-skills.py`.
2. Run `bash package-skills.sh` to refresh packaged skill zip files.
3. Update `CHANGELOG.md`.
4. Update `skill-catalog.json` if skills changed.
5. Confirm `dist/` contains current packages.
6. Commit changes.
7. Create a GitHub release with release notes.

## Suggested release title format

`v0.4.0 - Advanced Governance Skills Expansion`

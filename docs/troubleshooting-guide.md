# Troubleshooting Guide

Use this guide when something does not work as expected.

## Issue: GitHub upload removes folder structure

### Symptom

Files upload as loose files instead of staying inside folders.

### Fix

Do not open the folder and upload individual files. Drag the folder itself, or drag the contents from the extracted update package while preserving the visible paths.

Correct paths should look like:

```text
docs/quickstart.md
skills/change-governance-review/SKILL.md
assets/screenshots/landing-page-hero.png
```

Incorrect paths look like:

```text
quickstart.md
SKILL.md
landing-page-hero.png
```

## Issue: README headings appear greyed out

### Symptom

A large section of the README looks grey or appears inside a code block.

### Cause

A Markdown code fence was opened but not closed properly.

### Fix

Make sure code blocks end with three backticks only.

## Issue: GitHub Actions validation fails

### Likely causes

- A skill folder is missing `SKILL.md`.
- A `SKILL.md` file is missing required frontmatter.
- A skill name is not lowercase or includes spaces.
- A file path was uploaded incorrectly.
- A folder was nested inside the wrong folder.

### Fix

Open the failed workflow logs and identify the failing skill. Then confirm the skill folder includes the expected structure.

## Issue: Package workflow runs but no artifact appears

### Likely causes

- `package-skills.sh` did not run successfully.
- `dist/` was not created.
- No `.zip` files were generated.
- The artifact upload path is incorrect.

### Fix

Check the Package Skills workflow logs. Confirm the workflow is uploading:

```text
dist/*.zip
```

## Issue: Release asset downloads with a number in the filename

### Symptom

The asset appears as:

```text
governance-systems-skill-packages.2.zip
```

### Cause

The computer already had a file with the same name, so the browser added a number.

### Fix

Rename the file before uploading it to the release:

```text
governance-systems-skill-packages.zip
```

Then delete the incorrectly named release asset and upload the clean version.

## Issue: GitHub Pages does not update immediately

### Fix

Wait a few minutes and refresh the page. Then check:

```text
Actions → pages build and deployment
```

Confirm the latest deployment has a green check.

## Issue: Claude output includes visual or CSS artifacts

### Symptom

Claude output includes content such as:

```text
::view-transition-group(*)
Vvisualize
show_widget
```

### Fix

Add or strengthen an Output Discipline section in the relevant skill:

```markdown
## Output Discipline

Do not include CSS, HTML, widget code, visualization markup, transition code, or interface artifacts in the response.

Do not generate charts or visual widgets unless the user explicitly asks for one.

Always return the review in plain text or Markdown using the required output format.
```

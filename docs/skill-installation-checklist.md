# Skill Installation Checklist

Use this checklist when preparing or reviewing a skill package.

## Repository checklist

- [ ] The repo has a clear README.
- [ ] The live GitHub Pages site is linked.
- [ ] The latest release link is current.
- [ ] The release asset is attached.
- [ ] The package artifact has a clean filename.
- [ ] GitHub Actions validation passes.
- [ ] GitHub Actions packaging passes.

## Skill folder checklist

Each skill folder should include:

- [ ] `SKILL.md`
- [ ] `README.md`
- [ ] `examples/`
- [ ] `examples/tested-output.md`
- [ ] `references/` where applicable

## SKILL.md checklist

Each `SKILL.md` should include:

- [ ] YAML frontmatter.
- [ ] `name` field.
- [ ] `description` field.
- [ ] Clear purpose.
- [ ] Review criteria.
- [ ] Output format.
- [ ] Output discipline instructions.
- [ ] Instructions to avoid inventing missing details.
- [ ] Guidance for audit-ready language.

## Tested output checklist

Each tested output should include:

- [ ] Input summary.
- [ ] Review summary.
- [ ] Key findings.
- [ ] Gap table or issue table.
- [ ] Governance note.
- [ ] Recommended next action.
- [ ] Professional, audit-safe language.
- [ ] No unsupported claims.
- [ ] No CSS, widget, or visual artifacts.

## Release checklist

Before publishing a release:

- [ ] Run Validate Skills workflow.
- [ ] Run Package Skills workflow.
- [ ] Download the packaged artifact.
- [ ] Draft the release notes.
- [ ] Attach the packaged artifact.
- [ ] Publish the release.
- [ ] Update the README download link.
- [ ] Confirm the release asset appears under Assets.
- [ ] Confirm the live site still loads.

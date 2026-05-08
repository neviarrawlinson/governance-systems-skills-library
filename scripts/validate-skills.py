#!/usr/bin/env python3
"""Validate Governance Systems skill folders."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = text[4:end].strip().splitlines()
    data = {}
    for line in fm:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main():
    errors = []
    if not SKILLS_DIR.exists():
        errors.append("skills/ directory is missing")
    else:
        for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            if not NAME_RE.match(skill_dir.name):
                errors.append(f"{skill_dir.name}: folder name must use lowercase letters, numbers, and hyphens")
            if not skill_file.exists():
                errors.append(f"{skill_dir.name}: missing SKILL.md")
                continue
            text = skill_file.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if not fm:
                errors.append(f"{skill_dir.name}: missing YAML frontmatter")
                continue
            if fm.get("name") != skill_dir.name:
                errors.append(f"{skill_dir.name}: frontmatter name must match folder name")
            if not fm.get("description"):
                errors.append(f"{skill_dir.name}: missing description")
            if len(fm.get("description", "")) < 50:
                errors.append(f"{skill_dir.name}: description should be more specific")
            if not (skill_dir / "README.md").exists():
                errors.append(f"{skill_dir.name}: missing README.md")
            if not (skill_dir / "examples" / "sample-input.md").exists():
                errors.append(f"{skill_dir.name}: missing examples/sample-input.md")
            if not (skill_dir / "examples" / "sample-output.md").exists():
                errors.append(f"{skill_dir.name}: missing examples/sample-output.md")
    if errors:
        print("Skill validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1
    print("All skills passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate Claude Code plugin readiness for the Governance Systems Skills Library."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    ".claude-plugin/plugin.json",
    "skills",
    "commands",
    "agents",
    "docs/claude-code-plugin-installation.md",
    "docs/claude-code-command-guide.md",
    "docs/claude-code-agent-guide.md",
    "docs/plugin-component-map.md",
    "docs/plugin-testing-guide.md",
    "tests/README.md",
    "tests/evaluation-scorecard.md",
]

REQUIRED_COMMANDS = [
    "review-change.md",
    "prepare-cab-summary.md",
    "assess-vendor.md",
    "review-ai-intake.md",
    "summarize-governance-metrics.md",
]

REQUIRED_AGENTS = [
    "governance-reviewer.md",
    "audit-evidence-reviewer.md",
    "ai-governance-reviewer.md",
    "third-party-risk-reviewer.md",
]


def error(message: str) -> None:
    print(f"ERROR: {message}")


def ok(message: str) -> None:
    print(f"OK: {message}")


def validate_required_paths() -> list[str]:
    failures: list[str] = []
    for relative in REQUIRED_PATHS:
        path = ROOT / relative
        if not path.exists():
            failures.append(f"Missing required path: {relative}")
        else:
            ok(f"Found {relative}")
    return failures


def validate_manifest() -> list[str]:
    failures: list[str] = []
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        return ["Missing .claude-plugin/plugin.json"]

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"plugin.json is not valid JSON: {exc}"]

    required_fields = ["name", "version", "description", "repository", "license"]
    for field in required_fields:
        if not manifest.get(field):
            failures.append(f"plugin.json missing required metadata field: {field}")
        else:
            ok(f"plugin.json includes {field}")

    return failures


def validate_skills() -> list[str]:
    failures: list[str] = []
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        return ["Missing skills directory"]

    skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]
    if not skill_dirs:
        failures.append("No skill directories found in skills/")
        return failures

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            failures.append(f"Missing SKILL.md in {skill_dir.relative_to(ROOT)}")
        else:
            ok(f"Found {skill_file.relative_to(ROOT)}")

    return failures


def validate_commands() -> list[str]:
    failures: list[str] = []
    commands_dir = ROOT / "commands"
    for filename in REQUIRED_COMMANDS:
        path = commands_dir / filename
        if not path.exists():
            failures.append(f"Missing command file: commands/{filename}")
        else:
            ok(f"Found commands/{filename}")
    return failures


def validate_agents() -> list[str]:
    failures: list[str] = []
    agents_dir = ROOT / "agents"
    for filename in REQUIRED_AGENTS:
        path = agents_dir / filename
        if not path.exists():
            failures.append(f"Missing agent file: agents/{filename}")
        else:
            ok(f"Found agents/{filename}")
    return failures


def main() -> int:
    print("Validating Claude Code plugin readiness...\n")

    failures: list[str] = []
    failures.extend(validate_required_paths())
    failures.extend(validate_manifest())
    failures.extend(validate_skills())
    failures.extend(validate_commands())
    failures.extend(validate_agents())

    if failures:
        print("\nPlugin validation failed:\n")
        for failure in failures:
            error(failure)
        return 1

    print("\nPlugin validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

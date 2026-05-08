#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$ROOT_DIR/skills"
DIST_DIR="$ROOT_DIR/dist"

mkdir -p "$DIST_DIR"

for skill_path in "$SKILLS_DIR"/*; do
  if [[ -d "$skill_path" && -f "$skill_path/SKILL.md" ]]; then
    skill_name="$(basename "$skill_path")"
    zip_file="$DIST_DIR/$skill_name.zip"
    rm -f "$zip_file"
    (cd "$SKILLS_DIR" && zip -qr "$zip_file" "$skill_name")
    echo "Packaged $skill_name -> dist/$skill_name.zip"
  fi
done

echo "Skill packaging complete."

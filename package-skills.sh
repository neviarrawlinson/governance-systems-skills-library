#!/usr/bin/env bash
set -euo pipefail

mkdir -p dist

for skill_dir in skills/*; do
  if [ -d "$skill_dir" ] && [ -f "$skill_dir/SKILL.md" ]; then
    skill_name=$(basename "$skill_dir")
    zip_path="dist/${skill_name}.zip"
    rm -f "$zip_path"
    zip -r "$zip_path" "$skill_dir" -x "*.DS_Store" >/dev/null
    echo "Packaged $zip_path"
  fi
done

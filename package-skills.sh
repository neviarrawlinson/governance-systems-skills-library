#!/usr/bin/env bash
set -euo pipefail

mkdir -p dist
for skill_dir in skills/*/; do
  skill_name=$(basename "$skill_dir")
  zip -r "dist/${skill_name}.zip" "$skill_dir" > /dev/null
  echo "Packaged ${skill_name}"
done

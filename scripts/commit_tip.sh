#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/commit_tip.sh "artifacts/tip_20250...txt" "Commit message"
FILE="$1"
MSG="${2:-Add tip artifact from CI}"

git config user.email "latonya.johnson0921@gmail.com"
git config user.name "LaTonya Johnson"

git add "$FILE" || true
git commit -m "$MSG" || echo "Nothing to commit"
git push origin HEAD

#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/commit_tip_fixed.sh "artifacts/tip_20250...txt" "Commit message"
#
# This is a drop-in replacement for scripts/commit_tip.sh for CI environments where
# the build may be running in a detached HEAD. It pushes the current HEAD to the
# target remote branch using the full refspec (HEAD:refs/heads/<branch>).

FILE="${1:-}"
MSG="${2:-Add tip artifact from CI}"
TARGET_BRANCH="${GIT_TARGET_BRANCH:-main}"

git config user.email "latonya.johnson0921@gmail.com"
git config user.name "LaTonyaJ"

if [ -z "$FILE" ]; then
  echo "Usage: $0 <file> [commit message]"
  exit 1
fi

# Stage the file; continue even if the file was missing
git add "$FILE" || true

# Try to commit; if there is nothing to commit, just exit successfully
if git commit -m "$MSG"; then
  # Rebase to avoid commit errors and ensure we're up-to-date
  echo "Rebasing with remote changes..."
  if ! git pull --rebase origin main; then
    echo "Rebase failed, aborting rebase and exiting"
    git rebase --abort
    exit 1
  fi
  
  # Determine current branch name. When detached, this returns 'HEAD'.
  CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "HEAD")
  if [ "$CURRENT_BRANCH" = "HEAD" ]; then
    echo "Detached HEAD detected — pushing current HEAD to '${TARGET_BRANCH}' on origin"
    # Use full refname for the destination to avoid 'not a full refname' errors
    git push origin "HEAD:refs/heads/${TARGET_BRANCH}"
  else
    echo "On branch '${CURRENT_BRANCH}' — pushing branch to origin"
    git push origin "$CURRENT_BRANCH"
  fi
else
  echo "Nothing to commit"
fi
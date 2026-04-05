#!/usr/bin/env bash
# Fetch Ductor upstream; print merge/rebase commands (does not modify branches).
set -euo pipefail
UPSTREAM_REMOTE="${UPSTREAM_REMOTE:-upstream}"
UPSTREAM_BRANCH="${UPSTREAM_BRANCH:-main}"

if ! git remote get-url "$UPSTREAM_REMOTE" &>/dev/null; then
  echo "No remote '$UPSTREAM_REMOTE'. Add it, e.g.:"
  echo "  git remote add upstream https://github.com/PleasePrompto/ductor.git"
  exit 1
fi

git fetch "$UPSTREAM_REMOTE"
echo "Fetched $UPSTREAM_REMOTE."
echo ""
echo "Current branch: $(git branch --show-current)"
echo ""
echo "Integrate Ductor upstream:"
echo "  git merge ${UPSTREAM_REMOTE}/${UPSTREAM_BRANCH}"
echo "  # or:"
echo "  git rebase ${UPSTREAM_REMOTE}/${UPSTREAM_BRANCH}"
echo ""
echo "Afterwards: run tests / bot smoke test with your claw binary."
echo "Two-axis doc: docs/UPSTREAM_SYNC.md (Ductor + Claw CLI)"

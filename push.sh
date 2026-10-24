#!/usr/bin/env bash
set -e

# Change to the repository root directory
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# Ensure it's a git repo
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a Git repository. Run 'git init' first."
    exit 1
fi

# Detect current branch or default to main
CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || echo "main")
if [ -z "$CURRENT_BRANCH" ]; then
    CURRENT_BRANCH="main"
    git branch -M "$CURRENT_BRANCH"
fi

# Check for changes
git add -A

if git diff --cached --quiet; then
    echo "ℹ️  No changes to commit. Everything is up to date."
else
    # Determine commit message
    if [ -n "$1" ]; then
        COMMIT_MSG="$1"
    else
        DEFAULT_MSG="Update exercises - $(date '+%Y-%m-%d %H:%M')"
        if [ -t 0 ]; then
            read -r -p "Enter commit message [Default: $DEFAULT_MSG]: " USER_INPUT
            COMMIT_MSG="${USER_INPUT:-$DEFAULT_MSG}"
        else
            COMMIT_MSG="$DEFAULT_MSG"
        fi
    fi

    echo "📦 Committing: $COMMIT_MSG"
    git commit -m "$COMMIT_MSG"
fi

echo "🚀 Pushing to GitHub (origin/$CURRENT_BRANCH)..."
git push -u origin "$CURRENT_BRANCH"

echo "✅ All changes pushed successfully to GitHub!"

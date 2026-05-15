#!/bin/bash
# Ralph Loop Orchestrator
# Usage: ./ralph-loop.sh [max_iterations]

set -e

# 1. Parse Arguments & Setup Paths
MAX_ITERATIONS=${1:-10}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ARCHIVE_DIR="archive"
LAST_BRANCH_FILE=".last-branch"
PROGRESS_FILE="memory-bank/progress.md"

echo "Starting Autonomous Ralph Loop (Native Gemini CLI)"
echo "Max iterations: $MAX_ITERATIONS"

# 2. The Archiving Ritual
# Archive previous run if branch changed
if [ -f "$PRD_FILE" ] && [ -f "$LAST_BRANCH_FILE" ]; then
  CURRENT_BRANCH=$(jq -r '.branchName // empty' "$PRD_FILE" 2>/dev/null || echo "")
  LAST_BRANCH=$(cat "$LAST_BRANCH_FILE" 2>/dev/null || echo "")
  
  if [ -n "$CURRENT_BRANCH" ] && [ -n "$LAST_BRANCH" ] && [ "$CURRENT_BRANCH" != "$LAST_BRANCH" ]; then
    # Archive the previous run
    DATE=$(date +%Y-%m-%d)
    # Strip "ralph/" prefix from branch name for folder
    FOLDER_NAME=$(echo "$LAST_BRANCH" | sed 's|^ralph/||')
    ARCHIVE_FOLDER="$ARCHIVE_DIR/$DATE-$FOLDER_NAME"
    
    echo "Archiving previous run: $LAST_BRANCH"
    mkdir -p "$ARCHIVE_FOLDER"
    [ -f "$PRD_FILE" ] && cp "$PRD_FILE" "$ARCHIVE_FOLDER/"
    [ -f "$PROGRESS_FILE" ] && cp "$PROGRESS_FILE" "$ARCHIVE_FOLDER/"
    [ -d "memory-bank" ] && cp -r "memory-bank" "$ARCHIVE_FOLDER/"
    echo "   Archived to: $ARCHIVE_FOLDER"
    
    # Update last branch record
    echo "$CURRENT_BRANCH" > "$LAST_BRANCH_FILE"
  fi
fi

# 3. Execution Loop
for i in $(seq 1 $MAX_ITERATIONS); do
    echo "---------------------------------------------------------------"
    echo "  Iteration $i of $MAX_ITERATIONS"
    echo "---------------------------------------------------------------"

    # Invoke the Ralph sub-agent natively.
    # In headless/autonomous mode, we use the CLI flags to ensure it doesn't wait for human OK.
    gemini --prompt "@ralph Continue working on the next task using tracker tools. Follow Memory Bank rituals." --approval-mode=yolo


    # Objective check of completion state via Native Tracker
    # If no open tasks remain, we consider the loop successful.
    OPEN_TASKS=$(gemini -p "tracker_list_tasks" | grep -c '"status": "open"' || echo "0")
    
    if [ "$OPEN_TASKS" == "0" ]; then
        echo "SUCCESS: No open tasks remain in the native tracker."
        exit 0
    fi

    echo "Iteration $i complete. Tasks still open: $OPEN_TASKS. Checking next task..."
done

echo "FAILURE: Reached max iterations ($MAX_ITERATIONS) without finishing all tasks."
exit 1

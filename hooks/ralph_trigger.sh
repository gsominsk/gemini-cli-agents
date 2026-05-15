#!/bin/bash

# Ralph Background Trigger Hook
# This script is called by Gemini CLI after each agent turn.
# It ensures that the Ralph Loop is running in the background if there are open tasks.

PROJECT_DIR=$(pwd)
RALPH_SCRIPT="$HOME/.gemini/skills/ralph-loop/scripts/ralph-loop.sh"
PID_FILE="$HOME/.gemini/tmp/ralph_loop.pid"

# Check if Ralph is already running
if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null; then
        # Already running
        echo "{}"
        exit 0
    fi
fi

# Check if there are any open tasks (using gemini tracker list natively)
# We use a quick check to see if "open" exists in the output
OPEN_TASKS=$(gemini tracker list | grep "open")

if [ ! -z "$OPEN_TASKS" ]; then
    # Launch Ralph Loop in background
    # Redirect output to a log file so we can monitor it
    nohup "$RALPH_SCRIPT" --project "$PROJECT_DIR" > "$HOME/.gemini/tmp/ralph_background.log" 2>&1 &
    
    # Save PID
    echo $! > "$PID_FILE"
fi

# Always return valid empty JSON for the hook
echo "{}"
exit 0

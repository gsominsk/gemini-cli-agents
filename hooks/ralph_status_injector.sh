#!/bin/bash

# Ralph Status Injector Hook
# This script is called by Gemini CLI before each agent turn.
# It provides information about the background Ralph process.

PID_FILE="$HOME/.gemini/tmp/ralph_loop.pid"
LOG_FILE="$HOME/.gemini/tmp/ralph_background.log"

STATUS="idle"
LAST_LOG=""

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null; then
        STATUS="running (PID: $PID)"
        if [ -f "$LOG_FILE" ]; then
            LAST_LOG=$(tail -n 1 "$LOG_FILE" | sed 's/"/\\"/g')
        fi
    else
        STATUS="stopped"
        rm "$PID_FILE"
    fi
fi

# Return context to the main agent
echo "{
  \"hookSpecificOutput\": {
    \"additionalContext\": \"[SYSTEM INFO]: Ralph Background Worker is $STATUS. Last activity: $LAST_LOG\"
  }
}"
exit 0

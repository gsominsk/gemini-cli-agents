---
name: ralph-loop
description: Autonomous Iterative Evolution & Reality Check loop. Manages project tasks via native Task Tracker, tracks technical progress in `memory-bank/progress.md`, and evolves project knowledge in `AGENTS.md`. Designed for multi-step tasks requiring fresh context and persistent memory.
---

# Ralph Loop Skill

Implement complex features through iterative evolution, where each task is managed by the native Task Tracker, verified by a "Reality Check", and results in project-wide "Evolution" of knowledge. This skill is tightly integrated with the `memory-bank` system.

## Infrastructure Tools

These scripts are located in the `scripts/` directory of this skill:
- `init_project.py`: Initializes the environment (Memory Bank, Task Tracker configuration, Agents knowledge).
- `archiver.py`: Automatically archives previous session context when the project branch changes.
- `ralph-loop.sh`: Orchestrates the autonomous loop using the native Gemini CLI Task Tracker.

## Core Principles

- **Fresh Context, Persistent Memory**: Each iteration starts with a clean slate but leverages the native Task Tracker, `memory-bank/progress.md`, and `AGENTS.md` for context.
- **The Oracle Protocol**: The native Task Tracker (`tracker_*`) is the source of truth for task status. A task is only `closed` if the Reality Check (tests/build/lint) succeeds.
- **Iterative Evolution**: After every task, the agent MUST update `AGENTS.md` or the "System Standards" section of `memory-bank/systemPatterns.md` with reusable learnings (following the Surgical Protocol).

## Rituals

### 0. The Planning Ritual (Requirement Gathering)
**Trigger**: Request to "plan a feature" or "spec out".

1. **Clarification**: Ask 3-5 essential clarifying questions with lettered options (e.g., A, B, C, D). This allows for quick "1A, 2C" responses.
2. **Structure**: Define a clear plan with:
   - **Overview & Goals**: What and why.
   - **Tasks**: Small, verifiable units of work.
   - **Acceptance Criteria**: Must include "Typecheck passes" and "Verify in browser" for UI.
3. **Task Creation**: Use `tracker_create_task` to populate the native Task Tracker with the approved units of work.

### 0.7 The Archiving Ritual (Clean Slate)
**Trigger**: Starting a new feature or changing project branches.

1. **Verify Change**: Use `archiver.py` to check if the current project context needs to be moved to the `archive/` directory.
2. **Archive**: Move the `memory-bank/` directory into a timestamped folder in `archive/`.
3. **Reset**: Re-initialize the Memory Bank for the new feature via `init_project.py`. This ensures the agent starts with a "Fresh Context" while keeping "Persistent Memory" available in the archive.

### 1. The Context Ritual (Start of Iteration)
**Trigger**: Activation of the `ralph-loop` skill or start of a new task.

1. **Read Oracle**: Use `tracker_list_tasks` to identify the next `open` task.
2. **Read Brain**: Load `memory-bank/activeContext.md` and `memory-bank/progress.md`.
3. **Read Knowledge**: Load `AGENTS.md` for project patterns.
4. **Narrative**: Use `update_topic` to announce the current task ID being implemented.

### 2. The Execution Ritual (Implementation)
**Trigger**: Picking a task from the native tracker.

1. **Surgical Work**: Implement the *single* task picked. Follow the **Surgical Protocol** (use `replace` for documentation).
2. **Standardization**: Follow patterns found in `AGENTS.md` and `systemPatterns.md`.

### 3. The Reality Check Ritual (Verification)
**Trigger**: Completion of code changes for the current task.

1. **Verify**: Run mandatory project checks using `run_shell_command` (e.g., `npm test`, `tsc`, `lint`, `go test`).
2. **Frontend Check**: If the task involves UI, use `pencil` (screenshot/layout) or `web_fetch` to verify the visual state.
3. **Requirement**: A task is NOT complete until all checks pass. Never commit broken code.

### 4. The Evolution Ritual (Post-Task Learning)
**Trigger**: Successful Reality Check.

1. **Distill**: Identify reusable patterns, "gotchas", or non-obvious requirements discovered during the task.
2. **Update Knowledge**: 
   - Update `AGENTS.md` surgically if new patterns were discovered.
   - Update `memory-bank/progress.md` with the task ID, status, and specific learnings.
3. **Sync Tracker**: Use `tracker_update_task` to set the task status to `closed`.
4. **Commit**: Commit changes with a message like `feat: [Task ID] - [Description]`.

## Multi-Agent Attribution
Follow the `memory-bank` standard for timestamps and names:
`[YYYY-MM-DD HH:MM:SS] [AgentName] - [Description]`

## Stop Condition
When ALL tasks in the native tracker are `closed`, the project is considered complete.

## Tool Mapping

| Ralph Logic | Gemini CLI Equivalent |
|-------------|-----------------------|
| Task Management | `tracker_create_task` / `tracker_list_tasks` / `tracker_update_task` |
| Persistent Memory | `memory-bank/` |
| Knowledge Base | `AGENTS.md` |
| Reality Check | `run_shell_command` |
| Browser Testing | `pencil` (screenshot/layout) / `web_fetch` |
| `update_topic` | `update_topic` (Mandatory for transparency) |
 |
/layout) / `web_fetch` |
| `update_topic` | `update_topic` (Mandatory for transparency) |

---
name: ralph-loop
description: Autonomous Iterative Evolution & Reality Check loop. Manages high-level project goals via `prd.json`, tracks technical progress in `memory-bank/progress.md`, and evolves project knowledge in `AGENTS.md`. Designed for multi-step tasks requiring fresh context and persistent memory.
---

# Ralph Loop Skill

Implement complex features through iterative evolution, where each task is verified by a "Reality Check" and results in project-wide "Evolution" of knowledge. This skill is tightly integrated with the `memory-bank` system.

## Infrastructure Tools

These scripts are located in the `scripts/` directory of this skill:
- `init_project.py`: Initializes the environment (Memory Bank, PRD, Agents knowledge).
- `archiver.py`: Automatically archives previous session context when the project branch changes.

## Core Principles

- **Fresh Context, Persistent Memory**: Each iteration starts with a clean slate but leverages `prd.json`, `memory-bank/progress.md`, and `AGENTS.md` for context.
- **The Oracle Protocol**: `prd.json` is the source of truth for task status. A task is only `passes: true` if the Reality Check (tests/build/lint) succeeds.
- **Iterative Evolution**: After every task, the agent MUST update `AGENTS.md` or the "Codebase Patterns" section of `memory-bank/progress.md` with reusable learnings.

## Rituals

### 0. The Planning Ritual (Requirement Gathering)
**Trigger**: Request to "plan a feature", "write a PRD", or "spec out".

1. **Clarification**: Ask 3-5 essential clarifying questions with lettered options (e.g., A, B, C, D). This allows for quick "1A, 2C" responses.
2. **Structure**: Generate a PRD in `tasks/prd-[feature-name].md` including:
   - **Overview & Goals**: What and why.
   - **User Stories**: Small, verifiable units of work (US-001, US-002...).
   - **Acceptance Criteria**: Must include "Typecheck passes" and "Verify in browser" for UI.
   - **Non-Goals**: Defining boundaries to prevent scope creep.
3. **Important**: This ritual is strictly for planning. Do NOT start implementation until the PRD is approved and converted to `prd.json`.

### 0.5 The Management Ritual (PRD to JSON Conversion)
**Trigger**: Request to "convert PRD", "start implementation", or "create prd.json".

1. **Story Sizing**: Each user story MUST be completable in one iteration. Rule of thumb: if a change cannot be described in 2-3 sentences, split it.
2. **Dependency Ordering**: Order stories by technical dependency:
   - Database/Schema -> Backend/Logic -> UI Components -> Aggregations.
3. **Conversion**: Convert the Markdown PRD from `tasks/` into `prd.json` in the project root.
   - Assign sequential IDs (US-001, US-002...).
   - Set all `passes: false`.
   - Derive `branchName` from the feature name (e.g., `ralph/feature-name`).

### 0.7 The Archiving Ritual (Clean Slate)
**Trigger**: Starting a new feature when `prd.json` already exists.

1. **Verify Change**: If the new feature's `branchName` differs from the current `prd.json`:
   - Create an archive folder: `archive/YYYY-MM-DD-old-feature-name/`.
   - Move the current `prd.json` and `memory-bank/` directory into the archive folder.
2. **Reset**: Re-initialize the Memory Bank for the new feature. This ensures the agent starts with a "Fresh Context" while keeping "Persistent Memory" available in the archive.

### 1. The Context Ritual (Start of Iteration)
**Trigger**: Activation of the `ralph-loop` skill or start of a new task.

1. **Read Oracle**: Load `prd.json`. Check `branchName` and identify the current active story.
2. **Read Brain**: Load `memory-bank/activeContext.md` and `memory-bank/progress.md`.
3. **Read Knowledge**: Load `AGENTS.md` for project patterns.
4. **Narrative**: Use `update_topic` to announce the current story being implemented.

### 2. The Execution Ritual (Implementation)
**Trigger**: Picking a story from `prd.json`.

1. **Surgical Work**: Implement the *single* user story picked. Avoid scope creep.
2. **Standardization**: Follow patterns found in `AGENTS.md` and `systemPatterns.md`.

### 3. The Reality Check Ritual (Verification)
**Trigger**: Completion of code changes for the current story.

1. **Verify**: Run mandatory project checks using `run_shell_command` (e.g., `npm test`, `tsc`, `lint`, `go test`).
2. **Frontend Check**: If the story involves UI, use `pencil` (screenshot/layout) or `web_fetch` to verify the visual state.
3. **Requirement**: A story is NOT complete until all checks pass. Never commit broken code.

### 4. The Evolution Ritual (Post-Task Learning)
**Trigger**: Successful Reality Check.

1. **Distill**: Identify reusable patterns, "gotchas", or non-obvious requirements discovered during the task.
2. **Update Knowledge**: 
   - Update `AGENTS.md` in the relevant directories with long-term knowledge.
   - Update `memory-bank/progress.md` with the story ID, status, and specific learnings.
   - If a pattern is general, add it to `memory-bank/systemPatterns.md`.
3. **Update Oracle**: Set `passes: true` for the story in `prd.json`.
4. **Commit**: Commit changes with a message like `feat: [Story ID] - [Story Title]`.

## Multi-Agent Attribution
Follow the `memory-bank` standard for timestamps and names:
`[YYYY-MM-DD HH:MM:SS] [AgentName] - [Description]`

## Stop Condition
When ALL stories in `prd.json` have `passes: true`, the project is considered complete.

## Tool Mapping

| Ralph Logic | Gemini CLI Equivalent |
|-------------|-----------------------|
| `amp` / `claude` | Current Agent Session |
| `prd.json` | `read_file` / `write_file` / `replace` |
| `AGENTS.md` | `read_file` / `write_file` / `replace` |
| Reality Check | `run_shell_command` |
| Browser Testing | `pencil` (screenshot/layout) / `web_fetch` |
| `update_topic` | `update_topic` (Mandatory for transparency) |
 |
/layout) / `web_fetch` |
| `update_topic` | `update_topic` (Mandatory for transparency) |

# Codebase Knowledge: Gemini CLI Environment

## General Patterns
- **Skill Structure**: All skills must be in `~/.gemini/skills/` and follow the `SKILL.md` / `references/` / `assets/` structure. Use `assets/` for templates and non-context resources. `references/` is for documentation loaded into context.
- **Context Preservation**: Always preserve original source files in `references/` before adapting.
- **Narrative**: Mandatory use of `update_topic` for all complex workflows.
- **Attribution**: All log entries must use the `[YYYY-MM-DD HH:MM:SS] [AgentName]` format.

## Ralph Loop Protocols
- **The Oracle**: The **native Gemini CLI Task Tracker** (`tracker_*`) is the source of truth for task progress.
- **Reality Check**: Use `run_shell_command` to validate work before closing tasks.
- **Evolution**: Every completed task must result in an update to `AGENTS.md` or `memory-bank/systemPatterns.md`.
- **State Continuity**: Track task IDs and specific learnings in `memory-bank/progress.md`.
- **Transparency**: Mandatory use of `update_topic` to maintain narrative in the native UI.

## Agent-to-Agent Communication
- **Delegation**: When invoking a sub-agent (e.g., `@ralph`), the main agent MUST provide the current Story ID and a mission summary.
- **Context Handoff**: Sub-agents MUST read `memory-bank/activeContext.md` and `memory-bank/progress.md` at the start of their session.
- **Synchronization**: Sub-agents MUST update the Memory Bank files before completion to return the updated state to the main agent.

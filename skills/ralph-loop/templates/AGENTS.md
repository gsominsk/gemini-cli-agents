# Codebase Knowledge & Agent Rules

## General Standards
- **Source of Truth**: The native Gemini CLI Task Tracker (`tracker_*`) is the primary source for task status.
- **Persistence**: Use the `memory-bank/` directory for long-term project context.
- **Surgical Protocol**: NEVER use `write_file` to edit existing documentation. ALWAYS use the `replace` tool for atomic, surgical updates to `AGENTS.md`, `GEMINI.md`, and `memory-bank/*.md`.

## Ralph Loop Protocols
- **Initialization**: Every task starts with the **Context Ritual** (reading `activeContext.md` and `progress.md`).
- **Execution**: Implement only ONE task at a time. Maintain focus.
- **Reality Check**: Run mandatory project checks (tests, lint, build) before marking a task as closed.
- **Evolution**: Distill significant architectural learnings into this file (`AGENTS.md`) after completing a major task.

## Multi-Agent Attribution
Follow the `memory-bank` standard for all logs and updates:
`[YYYY-MM-DD HH:MM:SS] [AgentName] - [Description]`

## Forbidden Actions
- Do NOT use destructive commands like `rm` (unless explicitly asked).
- Do NOT overwrite documentation files via `write_file`.
- Do NOT skip the Reality Check ritual.

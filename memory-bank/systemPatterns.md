# System Patterns

- **Knowledge Base**: `AGENTS.md` in the project root is the primary repository for long-term architectural patterns and agent "learnings".
- **Memory Bank Integration**: All skills and agents must synchronize state via the `memory-bank/` directory.
 *Optional*

This file documents recurring patterns and standards used in the project.
It is optional, but recommended to be updated as the project evolves.
YYYY-MM-DD HH:MM:SS - Log of updates made.

*

## System Standards

### The Surgical Protocol
- **Constraint**: `write_file` is strictly forbidden for existing project documentation.
- **Enforcement**: Programmatic blocking via `ralph-guardrails.toml` (Policy Engine).
- **Mandatory Tool**: All documentation updates MUST use the `replace` tool for atomic, surgical edits.
- **Workflow**: `read_file` (target chunk) -> `replace` (surgical update).

### Native Task Management
- **Source of Truth**: The native Gemini CLI Task Tracker (`tracker_*`).
- **Automation**: Scripts must query the CLI status rather than parsing local files like `prd.json`.

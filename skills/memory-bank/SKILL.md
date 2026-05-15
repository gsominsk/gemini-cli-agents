---
name: memory-bank
description: Persistent Project Context for AI-Assisted Development based on the Roo Code Memory Bank pattern. Maintains project context, decisions, and progress across sessions using a structured set of Markdown files in a `memory-bank/` directory. Triggers on phrases like "initialize memory bank", "update memory bank", "sync context", "UMB".
---

# Memory Bank Skill

Maintain deep project context across sessions by managing a structured memory system.

## Core Principles

- **Status Transparency**: Begin every response involving memory bank actions with either `[MEMORY BANK: ACTIVE]` or `[MEMORY BANK: INACTIVE]`.
- **Narrative Continuity**: Always use `update_topic` to explain memory bank rituals (initialization, updates, synchronization).
- **Source of Truth**: Respect `GEMINI.md` as the foundational instruction source and `memory-bank/` as the project-specific knowledge base.

## Rituals

### 1. Initialize Memory Bank
**Trigger**: First interaction in a new project or explicit request to "initialize memory bank".

1. **Check**: Scan for `memory-bank/` directory using `list_directory`.
2. **Brief Check**: Look for `projectBrief.md` in the project root. If found, read it to seed the context.
3. **Offer**: If `memory-bank/` is missing, inform the user and offer to initialize it.
4. **Create**: Upon approval, create the directory and populate core files using templates from `templates/`:
   - `productContext.md`
   - `activeContext.md`
   - `progress.md`
   - `decisionLog.md`
   - `systemPatterns.md` (Optional)
5. **Timestamp & Attribution**: Ensure all entries include a timestamp and agent name: `[YYYY-MM-DD HH:MM:SS] [AgentName] - Description`.

### 2. Incremental Updates
**Trigger**: Significant architectural decisions, task completion, or changes in focus.

- **Multi-Agent Collaboration**: If multiple agents are working on the project, each agent MUST identify itself in the logs to maintain a clear audit trail.
- **Decision Log (`decisionLog.md`)**: Update when a significant architectural decision is made. Include agent name and rationale.
- **Progress (`progress.md`)**: Update when a task begins, is completed, or changes status. Mark who performed the action.
- **Active Context (`activeContext.md`)**: Update when focus shifts. Tracks current agent focus.
- **Product Context (`productContext.md`)**: Update when the high-level project description, goals, features, or overall architecture changes significantly.
- **System Patterns (`systemPatterns.md`)**: Update when new architectural patterns are introduced or existing ones are modified.

### 3. Synchronization (UMB - Update Memory Bank)
**Trigger**: Explicit command "Update Memory Bank" or "UMB", or before closing a complex session.

1. **Review**: Analyze the complete chat history. Extract cross-mode information and track activity relationships.
2. **Update**: Update all affected `*.md` files. Ensure cross-consistency and preserve activity context.
3. **Recap**: Confirm: "[MEMORY BANK: UPDATED] - Session synchronized." using `update_topic`.

## Tool Mapping (Roo Code -> Gemini CLI)

| Roo Code Tool | Gemini CLI Equivalent |
|---------------|-----------------------|
| `write_to_file` | `write_file` |
| `apply_diff` | `replace` |
| `list_files` | `list_directory` / `glob` |
| `read_file` | `read_file` |
| `ask_followup_question` | `ask_user` |

## Security & Rules

- **No Overwrites**: Never overwrite the entire `decisionLog.md` or `progress.md`; always append or use surgical `replace`.
- **Reference Awareness**: Refer to `references/developer-primer.md` for deep guidance on the Memory Bank philosophy.
- **Strict Adherence**: Follow the patterns established in `templates/` to maintain structural consistency.

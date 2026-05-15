# Ralph Loop Skill

This skill defines the standards, templates, and protocols for the **Ralph Loop** methodology—an autonomous development cycle focused on iterative evolution and persistent memory.

## Agent vs. Skill: The Distinction

To understand how this system works, it is important to distinguish between the **Agent** and the **Skill**:

*   **The Agent (Ralph):** The "Actor" or "Engineer". Defined in `~/.gemini/agents/ralph.md`. It contains the specific prompt, personality, and execution rituals.
*   **The Skill (ralph-loop):** The "Knowledge Base" and "Toolbox". Located here in `~/.gemini/skills/ralph-loop/`. It contains the reference standards, MD templates, and best practices that the Agent follows to ensure consistency across projects.

## Interaction Architecture

The following diagram illustrates how the Gemini CLI, the Ralph Agent, and the Guardrails interact with the Memory Bank and the project codebase.

```text
       [ USER / MAIN AGENT ]
              |
              v
      +-----------------------+      [ GLOBAL MEMORY ]
      |  MAIN AGENT           |<---- (~/.gemini/GEMINI.md)
      | (Orchestrator)        |      "Global Rules"
      +----------+------------+
                 |
        (Task Delegation)
                 |
                 v
      +-----------------------+      [ AGENTS CONFIG ]
      |   SUBAGENT (RALPH)    |<---- (~/.gemini/agents/ralph.md)
      |  "Autonomous Lead"    |      "Personality & Rituals"
      +----------+------------+
                 |
        (Tool Calls)
                 |                 +-----------------------+
                 v                 |   RALPH-LOOP SKILL    |
      +-----------------------+    | (~/skills/ralph-loop/)|
      |   GUARDRAILS (TOML)   |<---| - Protocol Standards  |
      |  "Policy Filter"      |    | - MD Templates        |
      +----------+------------+    | - Best Practices      |
                 |                 +-----------------------+
        (Security Check)
                 |
    +------------+------------+---------------------------+
    |                         |                           |
    v                         v                           v
[ TOOLS / MCP ]         [ MEMORY BANK ]            [ GLOBAL KNOWLEDGE ]
- read_file             (memory-bank/)             (AGENTS.md / systemPatterns.md)
- replace               - progress.md (Tasks)      - Architectural Patterns
- run_shell_command     - activeContext.md (Focus) - Discovered Solutions
- tracker_*             - productContext.md (Goals)- Global Standards
```

## Core Rituals

The Ralph Agent follows four mandatory rituals defined by this skill:

1.  **The Context Ritual:** Initialize session by reading Memory Bank state.
2.  **The Execution Ritual:** Implement changes using the **Surgical Protocol** (mandated atomic edits via `replace`).
3.  **The Reality Check Ritual:** Verify work via automated tests, linting, or builds.
4.  **The Evolution Ritual:** Capture significant architectural learnings into `AGENTS.md`.

## Surgical Protocol & Guardrails

To prevent documentation corruption by LLMs:
- **Rule:** `write_file` is forbidden for existing documentation (Memory Bank, AGENTS.md, etc.).
- **Enforcement:** Mandated via `~/.gemini/policies/ralph-guardrails.toml` (Policy Engine).
- **Tool:** Use `replace` for all atomic/surgical updates.

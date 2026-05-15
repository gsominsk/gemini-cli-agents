# Product Context

This project manages the **Gemini CLI Environment**, including specialized agents, custom skills, and the standardized "Memory Bank" workflow.

## Project Goal
To create a robust, autonomous agent environment where context is preserved across sessions using the "Ralph Loop" and "Memory Bank" patterns.

## Key Features
- **Standardized Skills**: `skill-creator`, `skill-installer`, and `memory-bank`.
- **Custom Agents**: Specialized subagents for research, coding, and management (future).
- **Persistent Context**: Automated updates of project state.

## Overall Architecture
- **Global Config**: `~/.gemini/` as the hub.
- **Skills**: Modular expertise in `~/.gemini/skills/`.
- **Agents**: Global subagents in `~/.gemini/agents/`.
- **Memory**: Project-specific `memory-bank/` directories.

2026-05-15 12:00:00 - Initialized Product Context based on environment setup.

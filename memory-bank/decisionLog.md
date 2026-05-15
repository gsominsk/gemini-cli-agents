# Decision Log

## Decision: Iterative Migration of Roo Code patterns
**Rationale**: Avoid losing original context and logic while adapting to Gemini CLI. Preserving original files in `references/` allows for deep lookups if needed.
**Implementation Details**: Copied all original files to `references/`, extracted clean templates to `templates/`.

## Decision: Global Storage for Agents and Skills
**Rationale**: Ensures that specialized capabilities are available across all user projects (sandbox, katana, etc.) without duplication.
**Implementation Details**: Using `~/.gemini/agents/` and `~/.gemini/skills/`.

## Decision: Programmatic Enforcement of "Surgical Protocol"
**Date**: 2026-05-15
**Rationale**: LLMs, especially weaker models, may accidentally overwrite critical documentation files when attempting to rewrite them. Programmatic enforcement at the tool level is more reliable than prompting alone.
**Implementation Details**:
- Added rules to `~/.gemini/policies/ralph-guardrails.toml` with `priority = 600`.
- Denies `write_file` for `AGENTS.md`, `GEMINI.md`, `systemPatterns.md`, and `memory-bank/*`.
- Mandates the use of the `replace` tool for these files.

## Decision: Native Task Tracker Integration
**Date**: 2026-05-15
**Rationale**: Using the built-in Gemini CLI `tracker_*` tools reduces friction and eliminates the risk of "state drift" between local JSON files and the CLI's internal state.
**Implementation Details**: Updated `ralph-loop.sh` to check for open tasks via native CLI queries.

## Decision: Use 'assets/' for Skill Templates and non-context resources
**Date**: 2026-05-15
**Agent**: Ralph (Audit by Gemini CLI)
**Rationale**: Using `templates/` for non-context resources can conflict with some automated skill-processing scripts (like `skill-creator`). Moving templates to `assets/` ensures they remain available for injection without being prematurely loaded into the agent's prompt context as part of the skill's instructions.
**Implementation Details**: Updated `AGENTS.md` and applied this structure to the `agent-orchestrator` skill.

2026-05-15 12:00:00 - Initialized Decision Log.

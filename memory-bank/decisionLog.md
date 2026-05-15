# Decision Log

## Decision: Iterative Migration of Roo Code patterns
**Rationale**: Avoid losing original context and logic while adapting to Gemini CLI. Preserving original files in `references/` allows for deep lookups if needed.
**Implementation Details**: Copied all original files to `references/`, extracted clean templates to `templates/`.

## Decision: Global Storage for Agents and Skills
**Rationale**: Ensures that specialized capabilities are available across all user projects (sandbox, katana, etc.) without duplication.
**Implementation Details**: Using `~/.gemini/agents/` and `~/.gemini/skills/`.

## Decision: Iterative Refinement of Ralph Agent Infrastructure
**Date**: 2026-05-15
**Rationale**: The initial implementation lacked critical "cleanup" (archiving) and "setup" (initialization) scripts found in the original Ralph pattern. Iterative refinement ensures that we don't break the working base while adding advanced features.
**Implementation Details**:
- Adding `archiver.py` and `init_project.py` to `ralph-loop/scripts/`.
- Enforcing `[Ralph]` attribution for all autonomous logs.
- Integrating Memory Bank sync into the Ralph Loop "Evolution" ritual.

2026-05-15 12:00:00 - Initialized Decision Log.

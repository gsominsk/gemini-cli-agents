---
name: agent-orchestrator
description: Formalizes agent-to-agent delegation, planning, and context management. Use when a complex goal requires breaking into stories/tasks and delegating to specialized sub-agents (e.g., Ralph).
---

# Agent Orchestrator

This skill provides a framework for a "Main" agent to manage "Sub-agents" (specialized loops like Ralph) to achieve complex engineering goals.

## Core Workflow

### 1. The Planning Phase (Manager)
Break high-level requirements into small, verifiable units.
- **Goal**: High-level objective.
- **Stories**: Feature-level grouping.
- **Tasks**: Implementation-level units.
- **Tracker**: Use `tracker_create_task` to record these in the native Task Tracker.

### 2. The Delegation Phase (Orchestrator)
Invoke specialized agents for specific tasks.
- **Direct Trigger**: Use `invoke_agent` for synchronous execution (blocks current session).
- **Background Trigger**: Create a task via `tracker_create_task`. Native hooks (`AfterAgent`) will automatically launch `@ralph` if tasks are open.
- **Handoff**: Use the **Mission Template** (see `assets/mission-handoff.md`).

### 3. The Monitoring Phase (Controller)
Track sub-agent progress.
- **Passive Monitoring**: Read `[SYSTEM INFO]` provided by the `BeforeAgent` hook in your additional context.
- **Active Check**: Check `tracker_list_tasks` and `memory-bank/progress.md`.
- **Intervention**: Only intervene if a blocker is reported in the Memory Bank.

### 4. The Integration Phase (Lead)
Aggregate results and verify the whole feature.
- **Sync**: Read the final state of the Memory Bank from the sub-agent.
- **Verification**: Run comprehensive integration tests.

## Delegation Protocol

When delegating to a sub-agent (e.g., `@ralph`):
1. **State the Mission**: Clear description of the task.
2. **Provide the Story ID**: Link the work to the project structure.
3. **Specify the Entry Point**: Which file or feature to start with.
4. **Define Acceptance Criteria**: How the loop knows it is done.

## Reference Material
- See [references/delegation-patterns.md](references/delegation-patterns.md) for best practices.
- Use [assets/mission-handoff.md](assets/mission-handoff.md) for delegating work.

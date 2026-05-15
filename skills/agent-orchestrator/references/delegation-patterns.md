# Delegation Patterns

## The "Handoff" Pattern
Main agent creates tasks -> Sub-agent picks task -> Sub-agent completes and closes task -> Main agent verifies.

## The "Observer" Pattern
Main agent launches sub-agent in background -> Main agent continues other work -> Main agent checks for completion signals.

## The "Native Background Worker" Pattern
Main agent creates a task in the native tracker -> `AfterAgent` hook triggers `@ralph` in the background -> Main agent monitors status via `additionalContext` (injected by `BeforeAgent` hook).

## Common Pitfalls
- **Over-delegation**: Delegating a task that takes more time to explain than to do.
- **Context Loss**: Sub-agent doesn't have access to the full Memory Bank.
- **Loop Conflicts**: Two sub-agents working on the same file without coordination.

## Technical Example (invoke_agent)
When delegating to `@ralph`, use the following structure:
```json
{
  "agent_name": "ralph",
  "prompt": "[STORY-ID]: ST-001\n[MISSION]: Implement X following patterns in AGENTS.md.\n[ACCEPTANCE]: \n- Feature Y works\n- Tests pass\n- Memory Bank updated"
}
```

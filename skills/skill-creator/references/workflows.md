# Gemini CLI Workflow Patterns

This reference defines the mandatory operational cycles for high-quality skill execution within the Gemini CLI environment.

## 1. The Core Lifecycle: Research -> Strategy -> Execution

Every complex task must follow this three-phase approach:

### Research
- **Goal**: Map the codebase and validate all assumptions.
- **Mandate**: Use `grep_search` and `glob` extensively. Always verify assumptions with `read_file`.
- **Validation**: If fixing a bug, first create a reproduction script or test case to confirm the failure.

### Strategy
- **Goal**: Formulate a grounded plan.
- **Mandate**: Present a concise summary of the proposed solution and wait for user acknowledgment if the change is architectural or cross-cutting.

### Execution
- **Goal**: Apply changes and verify.
- **Mandate**: Use the **Plan -> Act -> Validate** cycle for each sub-task.

## 2. Iterative Execution: Plan -> Act -> Validate

For every atomic change during the Execution phase:

1. **Plan**: Define the specific implementation approach and the testing strategy.
2. **Act**: Apply targeted, surgical changes. Adhere to existing project conventions found in `GEMINI.md`.
3. **Validate**: Run tests, linters, or visual checks (via Pencil tools) to confirm success. **Validation is mandatory for task finality.**

## 3. Narrative Transparency: `update_topic`

Skills must instruct Gemini CLI to use `update_topic` to maintain a clear narrative:
- **When to call**: At the start of a task, when transitioning between logical phases (e.g., Research to Strategy), or when an unexpected event requires a strategic detour.
- **Content**: Provide a clear `strategic_intent` and a detailed `summary` of progress and next steps.

## 4. Strategic Re-evaluation

If an implementation fails 3 consecutive times:
1. Stop and re-read the original task description.
2. Explicitly list current assumptions and identify potential flaws.
3. Propose a different architectural approach rather than patching a failed one.

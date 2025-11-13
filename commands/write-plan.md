---
description: Create plan and tasklist from planning discussion
---

# Plan Command

Formalize the planning discussion from plan mode into structured documentation.

## Bootstrap

1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete, then proceed with instructions below.

## Context

This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the plan has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

Use the feature name parsing pattern from cfw-planning skill.

**Special case for write-plan:** If no feature name is provided, SUGGEST a feature name based on the conversation (don't list existing plans, since this creates NEW plans):

```
Based on our conversation about adding document query functionality, I suggest
the feature name: "query-command"

This will create:
- plans/query-command-plan.md
- plans/query-command-tasklist.md

Should I proceed with "query-command" as the feature name?
```

## Instructions

Review the conversation history from plan mode and create two documents in the `plans/` directory.

### Document Structure

The cfw-planning skill provides complete structure requirements for both documents. See the skill for detailed templates, examples, and validation criteria.

## Requirements

- Stay faithful to what was discussed and agreed upon in plan mode
- Ensure tasks reflect the implementation approach from the discussion
- Make sure completing each phase leaves the codebase in a stable state
- Use clear, concise language

## Validation

Before finalizing documents, validate against cfw-planning skill's validation reference.

## Example Output

For a feature called "query-command", create:
- `plans/query-command-plan.md` (following skill's plan structure)
- `plans/query-command-tasklist.md` (following skill's tasklist structure)

Refer to cfw-planning skill for complete templates and examples.

# Implement Command

Implement the **$ARGUMENTS** feature by following the plan and tasklist documents.

## Context

This command is called in a fresh chat session. You need to bootstrap yourself by reading the planning documents for the **$ARGUMENTS** feature.

**Arguments**: `$ARGUMENTS` captures the feature name if provided (e.g., `/implement query-command`).

## Instructions

0. **Determine feature name**:
   - If `$ARGUMENTS` is provided, use that as the feature name
   - If `$ARGUMENTS` is empty:
     - List all plan files in the `plans/` directory (look for `*-plan.md` files)
     - Extract feature names from filenames (e.g., `query-plan.md` → `query`)
     - Present available features to the user
     - Ask user to select which feature to implement
     - Use the selected feature name for the rest of the command

1. **Read the planning documents**:
   - `plans/$ARGUMENTS-plan.md` - for implementation guidance and context
   - `plans/$ARGUMENTS-tasklist.md` - for the task checklist

2. **Check progress and resume from current position**:
   - Review the tasklist to identify which tasks are already completed (marked with `[x]`)
   - Identify which phases are complete
   - Find the first incomplete task in the first incomplete phase
   - If all tasks in a phase are complete, start with the next phase
   - If all phases are complete, inform the user that implementation is finished
   - Communicate clearly where you're resuming from

3. **Phase-by-phase implementation**:
   - Work through tasks in order, one phase at a time
   - Implement each task according to the plan
   - **Check off tasks** by editing `plans/$ARGUMENTS-tasklist.md` and changing `- [ ]` to `- [x]` for completed tasks
   - After completing ALL tasks in a phase, STOP and inform the user
   - Wait for user approval before proceeding to the next phase

4. **Task completion workflow**:
   - Read the current task from the tasklist
   - Implement the task following the plan and coding constitution
   - Test that the code works
   - Edit the tasklist file to mark the task as complete: `- [x] [PX.Y] Task description`
   - Move to the next task in the same phase
   - After the last task in a phase:
     - Present phase completion with detailed summary of changes (use ✅ checkmarks)
     - Include a "Phase Checkpoint" explaining current state and referencing constitution principles
     - Suggest a commit message following conventional commits format:
       - Format: `<type>: <short description>\n\n<detailed body explaining WHY and HOW>`
       - Types: feat, fix, docs, refactor, test, chore, perf, style, ci, build
       - Short description: concise summary (max 72 chars)
       - Detailed body: 1-2 sentences focusing on **WHY** and **HOW**, not WHAT
     - STOP for review

## Requirements

- **Check existing progress first** - don't restart completed work
- **Follow the coding constitution** (see CLAUDE.md and constitution.md)
- **Ensure code is runnable** after each phase
- **Run quality checks** when appropriate (ruff, mypy, pre-commit)
- **Actually edit the tasklist file** to check off tasks - don't just say you did it
- **Be explicit** about which task you're working on using its ID
- **Stop after each phase** - do not proceed to the next phase without user approval
- **Communicate clearly** when a phase is complete and you're waiting for review

## Example Flow - Starting Fresh (With Feature Name)

````text
Reading plans for feature: $ARGUMENTS
- Plan document: plans/$ARGUMENTS-plan.md
- Tasklist: plans/$ARGUMENTS-tasklist.md

Progress check: No tasks completed yet. Starting from Phase 1.

Starting Phase 1: Foundation

Working on [P1.1]: Set up basic module structure
[implements the task]
✓ Marked [P1.1] as complete

Working on [P1.2]: Create core data models
[implements the task]
✓ Marked [P1.2] as complete

Phase 1 Complete! ✅

Summary of changes:
✅ Created new directory structure for modular architecture
✅ Implemented core data models with Pydantic validation
✅ Added type hints throughout for better IDE support
✅ Set up proper __init__.py exports following encapsulation principle

Phase 1 Checkpoint: The foundation layer is complete following constitution
principles of orthogonality (clear module boundaries) and encapsulation
(minimal public APIs). All code is type-safe and passes quality checks.
Ready for Phase 2: Business Logic implementation.

Suggested commit message:

```
feat: establish foundational architecture

Enables modular development by implementing core models with strict type
validation and clear module boundaries.
```

Stopping here for manual review. Please review and approve before proceeding to Phase 2.
````

## Example Flow - No Feature Name Provided

```text
No feature name provided. Scanning plans/ directory...

Found the following features:
1. query - Document query and search functionality
2. export - Data export capabilities
3. user-auth - User authentication system

Which feature would you like to implement? (1-3)

[User selects 1]

Proceeding with feature: query
- Plan document: plans/query-plan.md
- Tasklist: plans/query-tasklist.md

Progress check: No tasks completed yet. Starting from Phase 1.
[continues with implementation...]
```

## Example Flow - Resuming Work

````text
Reading plans for feature: $ARGUMENTS
- Plan document: plans/$ARGUMENTS-plan.md
- Tasklist: plans/$ARGUMENTS-tasklist.md

Progress check:
✓ Phase 1: Complete (3/3 tasks done)
✓ Phase 2: Complete (4/4 tasks done)
→ Phase 3: In progress (1/3 tasks done)

Resuming from Phase 3, Task [P3.2]...

Working on [P3.2]: Add integration tests
[implements the task]
✓ Marked [P3.2] as complete

Working on [P3.3]: Update documentation
[implements the task]
✓ Marked [P3.3] as complete

Phase 3 Complete! ✅

Summary of changes:
✅ Added comprehensive integration tests covering happy paths and error cases
✅ Updated README.md with usage examples and architecture overview
✅ Added inline documentation to public APIs
✅ All tests passing and code quality checks green

Phase 3 Checkpoint: All implementation complete! The feature is fully tested,
documented, and follows all constitution principles (DRY, YAGNI, orthogonality).
The codebase is production-ready.

Suggested commit message:

```
test: complete feature testing and documentation

Ensures maintainability by adding integration tests and comprehensive API
documentation covering all public interfaces.
```

All phases finished. Ready for final review and merge.
````

## Notes

### Handling Unclear Tasks

- **First attempt**: If a task description is unclear, refer to the plan document (`plans/$ARGUMENTS-plan.md`) for additional context
- **Check related sections**: Look for relevant sections in the plan that explain the architecture, approach, or design decisions
- **Still unclear?**: If after reading the plan document a task or phase is STILL unclear or ambiguous:
  - STOP implementation
  - **Use the AskUserQuestion tool** to get clarification with specific options
  - Clearly explain what is unclear (be specific about which task ID and what information is missing)
  - Provide 2-4 concrete options for how to proceed
  - Do NOT make assumptions or guesses about critical implementation details
  - Example using AskUserQuestion:
    - Question: "Task [P2.3] requires query optimization but the plan doesn't specify the strategy. Which approach should I use?"
    - Options: "Implement caching layer", "Add database indexes", "Both caching and indexing", etc.

### Discovering Issues

- If you discover technical issues, blockers, or problems with the plan during implementation:
  - Document the issue clearly
  - **Use the AskUserQuestion tool** if there are multiple valid approaches or critical decisions to make
  - Suggest specific options or alternative approaches
  - Continue with reasonable assumptions if the issue is minor
  - Stop and ask the user if the issue is significant or affects the architecture

### Code Quality

- Keep the codebase in a working, runnable state throughout
- Run tests after implementing functionality to ensure nothing breaks
- Follow DRY, YAGNI, and other principles from the coding constitution
- When in doubt about design decisions, refer to existing patterns in the codebase

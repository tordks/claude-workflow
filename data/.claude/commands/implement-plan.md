# Implement Command

Implement a feature by following the plan and tasklist documents.

## Bootstrap

1. Use the SlashCommand tool to execute: `/prime-planning-commands`
2. Use the SlashCommand tool to execute: `/read-constitution`
3. Wait for both to complete, then proceed with instructions below.

## Context

This command is called in a fresh chat session to implement a planned feature. After bootstrapping, read the planning documents for the feature and execute tasks phase by phase.

## Arguments

**Input**: `$ARGUMENTS`

Use the standard feature name parsing pattern from `/prime-planning-commands`.

## Instructions

1. **Read the planning documents**:
   - `plans/{feature-name}-plan.md` - for architectural context, design decisions, and project structure
   - `plans/{feature-name}-tasklist.md` - for step-by-step task execution and progress tracking

   **How to use both documents**:
   - The **plan** provides WHY (rationale) and WHAT (architecture) - use it to understand the overall design
   - The **tasklist** provides WHEN (phase order) and HOW (specific steps) - use it for execution
   - Read the plan first to understand the architecture, then follow the tasklist for implementation
   - Refer back to the plan when task details are unclear or you need more context

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
   - **Check off tasks** by editing `plans/{feature-name}-tasklist.md` and changing `- [ ]` to `- [x]` for completed tasks
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

## Example Workflow

```text
# Starting fresh
Reading plans for feature: query-command
- Plan: plans/query-command-plan.md
- Tasklist: plans/query-command-tasklist.md

Progress check: No tasks completed yet. Starting from Phase 1.

# Executing tasks
Working on [P1.1]: Set up basic module structure
[implements the task]
✓ Marked [P1.1] as complete

Working on [P1.2]: Create core data models
[implements the task]
✓ Marked [P1.2] as complete

# Phase completion
Phase 1 Complete! ✅

Summary of changes:
✅ Created directory structure for modular architecture
✅ Implemented core data models with Pydantic validation
✅ Added type hints and proper __init__.py exports

Phase 1 Checkpoint: Foundation layer complete following constitution principles
(orthogonality, encapsulation). All code type-safe and passes quality checks.

Suggested commit:
```
feat: establish foundational architecture

Enables modular development with core models, strict type validation,
and clear module boundaries.
```

Stopping for review. Please approve before proceeding to Phase 2.

# If resuming mid-feature
Progress check:
✓ Phase 1: Complete (2/2 tasks)
✓ Phase 2: Complete (4/4 tasks)
→ Phase 3: In progress (1/3 tasks)

Resuming from Phase 3, Task [P3.2]...
```

## Notes

### When Tasks Are Unclear
1. **Check plan document** sections: Project Structure, Design Decisions, Technical Approach
2. **Still unclear?** STOP and use AskUserQuestion tool:
   - Specify which task ID and what's unclear
   - Provide 2-4 concrete options
   - Don't guess critical implementation details

### When Issues Arise
- Document the issue clearly
- Use AskUserQuestion for multiple valid approaches or critical decisions
- Continue with reasonable assumptions if minor
- Stop and ask if significant or affects architecture

### Code Quality
- Keep codebase runnable throughout
- Run tests after implementing functionality
- Follow constitution principles (DRY, YAGNI, orthogonality)
- Refer to existing patterns when in doubt

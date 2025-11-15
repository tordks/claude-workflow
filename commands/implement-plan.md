---
description: Execute plan phase-by-phase following tasklist
---

# Implement Command

Implement a feature by following the plan and tasklist documents.

## Bootstrap

1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete, then proceed with instructions below.

## Context

This command is called in a fresh chat session to implement a planned feature. After bootstrapping, read the planning documents for the feature and execute tasks phase by phase.

## Arguments

**Input**: `$ARGUMENTS`

Parse input arguments using the standard parsing pattern from the cfw-planning skill's `parsing-arguments.md` reference.


## Implementation workflow

1. **Load documents:**
   - **FIRST:** Read `plans/{feature-name}-plan.md` in full
   - **SECOND:** Read `plans/{feature-name}-tasklist.md` for execution guidance

   The plan provides architectural context (WHY/WHAT). The tasklist provides execution steps (WHEN/HOW).

2. **Check progress:** Review tasklist to find first incomplete task in first incomplete phase. Communicate clearly where resuming from.

3. **Execute phase-by-phase and task-by-task:**
   - Implement each task following plan and constitution
   - Mark complete: edit tasklist changing `- [ ]` to `- [x]`
   - After ALL phase tasks complete:
     - Apply checkpoint instructions
     - present summary with ✅
     - suggest conventional commit format (`<type>: <description>\n\n<body with WHY/HOW>`)
     - STOP for approval

**Task workflow:** Read task → implement → test → mark task complete → next task. After last task in phase: stop and wait for approval before next phase.


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

Phase 1 Checkpoint: Foundation layer complete following constitution principles. All code type-safe and passes quality checks.

Suggested commit:
feat: establish foundational architecture
```

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


## When Tasks Are Unclear
1. Check relevant sections in the plan document first
2. Still unclear? Use AskUserQuestion tool with task ID, what's unclear, which plan sections checked, and recommended approach

## When Issues Arise
- Document the issue clearly
- Use AskUserQuestion for multiple valid approaches or critical decisions
- Continue with reasonable assumptions if minor
- Stop and ask if significant or affects architecture

## Code Quality
- Keep codebase runnable throughout
- Run tests after implementing functionality
- Follow constitution and project principles

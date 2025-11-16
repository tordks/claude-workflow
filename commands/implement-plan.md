---
description: Execute plan phase-by-phase following tasklist
---

# Implement Command

Implement a feature by following the plan and tasklist documents.

## Bootstrap

**Check if CWF skills are already loaded in this session:**
- Do you have the cfw-planning skill loaded with access to reference documents (plan-spec.md, tasklist-spec.md)?

**If NO (skills not yet loaded):**
1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete

**If YES (skills already loaded):**
- Skip skill loading, knowledge is already available


## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/implement-plan {feature-name} [implementation instructions]`

**Parsing:**
- First token: feature name (must match existing plan)
- Remaining tokens: optional implementation scope or behavior
  - Example: `query-command implement phase 1 and 2, then stop`

**If no feature name provided:**
1. List existing plans: `find plans/ -name "*-plan.md" -exec basename {} -plan.md \;`
2. If exactly 1 plan found: use automatically and inform user
3. If multiple plans found: present list (optionally with progress status), use AskUserQuestion to ask user to select
4. If 0 plans found: inform user and suggest running `/write-plan` first

**Feature name usage:**
- Loads: `plans/{feature-name}-plan.md` and `plans/{feature-name}-tasklist.md`


## Implementation workflow

1. **Load documents:**
   - **FIRST:** Read `plans/{feature-name}-plan.md` in full
   - **SECOND:** Read `plans/{feature-name}-tasklist.md` for execution guidance

   The plan provides architectural context (WHY/WHAT). The tasklist provides execution steps (WHEN/HOW).

2. **Check progress:** Review tasklist to find first incomplete task in first incomplete phase. Communicate clearly where resuming from.

3. **Execute phase-by-phase and task-by-task:**

   **Task workflow:**
   - Read task → implement → test → mark complete (`- [ ]` to `- [x]`) → next task

   **After ALL phase tasks complete:**
   - Execute each checkpoint sequentially, marking complete as you go
   - If checkpoint fails: fix issue and retry until passing
   - When all checkpoints pass:
     - Output "Phase X Complete" summary with ✅
     - Suggest conventional commit format
     - **STOP for human review** (DO NOT proceed to next phase)

   **Between phases:** Human reviews, optionally runs `/clear` and if so runs this command again.


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
All Phase 1 tasks complete. Executing checkpoints...

Checkpoint: Self-review implementation against phase deliverable
✓ Marked checkpoint complete

Checkpoint: Code quality - ruff check src/
✓ Passed. Marked checkpoint complete

Checkpoint: Code complexity - radon cc src/
✓ Passed. Marked checkpoint complete

Phase 1 Complete! ✅

Summary of changes:
✅ Created directory structure for modular architecture
✅ Implemented core data models with Pydantic validation
✅ Added type hints and proper __init__.py exports

All checkpoints passed. Foundation layer complete following constitution principles.

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

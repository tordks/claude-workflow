---
description: Execute plan phase-by-phase following tasklist
---

# Implement Command

Implement a feature by following the plan and tasklist documents.

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
`{feature-name}` is a placeholder that gets replaced with the extracted feature name throughout this command.

Example file paths:
- `plans/{feature-name}-plan.md`
- `plans/{feature-name}-tasklist.md`


## Instructions

### 1. Load Context

1. If skill `read-constitution` not loaded, load it
2. If skill `cfw-planning` not loaded, load it

---

### 2. Read Planning Documents

Read the following if they are not already loaded:
- `plans/{feature-name}-plan.md` (WHY/WHAT - architectural context)
- `plans/{feature-name}-tasklist.md` (WHEN/HOW - sequential tasks)

---

### 3. Identify Next Work

Find the first incomplete task in the first incomplete phase:
- Scan tasklist for unchecked tasks: `- [ ] [PX.Y] Task description`
- Identify current phase and task number
- If all tasks complete: inform user feature is complete

---

### 4. Execute Tasks

For each task in the current phase:

1. **Read** the task description from tasklist
2. **Implement** the task following plan guidance
3. **Test** the task according to project standards
4. **Mark complete** in `plans/{feature-name}-tasklist.md`:
   - Change `- [ ] [PX.Y]` to `- [x] [PX.Y]`

Repeat until all tasks in current phase are complete.

---

### 5. Run Phase Checkpoints

After all phase tasks are marked complete:

1. Execute checkpoints sequentially (defined in tasklist)
2. Mark each checkpoint complete as it passes
3. If checkpoint fails: fix the issue is minor and retry until passing, else alert user.
4. Continue until all checkpoints pass

---

### 6. Complete Phase and Stop

When all checkpoints pass:

1. Output "Phase X Complete ✅" summary
2. Summarize what was accomplished
3. Suggest commit message if appropriate
4. **STOP for human review** - do NOT proceed to next phase

**Between phases:** Human reviews work, optionally runs `/clear` and if so continues with a new call to `/implement-plan {feature-name}` to resume.


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

Enables modular development with core models, strict type validation,
and clear module boundaries.


Stopping for review. Please approve before proceeding to Phase 2.
```

If resuming mid-feature:

```
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

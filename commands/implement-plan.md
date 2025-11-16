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
- Loads: `plans/{feature-name}-plan.md` and `plans/{feature-name}-tasklist.md`


## Implementation workflow

1. If skill `read-constitution` not loaded, load it
2. If skill `cfw-planning` not loaded, load it

3. **Read documents** if they are not already loaded 
   - `plans/{feature-name}-plan.md` (WHY/WHAT)
   - `plans/{feature-name}-tasklist.md` (WHEN/HOW)

4. **Check progress** - Find first incomplete task in first incomplete phase

5. **Execute tasks** - For each task: read → implement → test → mark complete (`- [ ]` to `- [x]`)

6. **After phase tasks complete**:
   - Execute checkpoints sequentially, marking complete
   - If checkpoint fails: fix and retry until passing
   - When all pass: Output "Phase X Complete ✅" summary, suggest commit
   - **STOP for human review** (do NOT proceed to next phase)

7. **Between phases** - Human reviews, optionally runs `/clear`, then continue implementation.


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

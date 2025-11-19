---
description: Execute plan phase-by-phase following tasklist
---

# Implement Command

Implement a feature by following the plan and tasklist documents. This command executes an existing plan phase-by-phase, reading the plan for architectural context and the tasklist for sequential execution. Your job is to execute tasks systematically and produce working code. Work proceeds one phase at a time with human review between phases.

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
3. If checkpoint fails:
   - Minor issues (linting, formatting, types): fix and retry until passes or stuck
   - Major issues (architectural issues, complex problems): stop, describe to user and ask user for direction.
   - If stuck: ask user for guidance
4. Continue until all checkpoints pass

---

### 6. Complete Phase and Stop

When all checkpoints pass:

**Before signaling phase complete, verify:**
- [ ] All tasks in phase marked complete
- [ ] All checkpoints passed
- [ ] Code is runnable
- [ ] Tests pass (if applicable)

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

Assess task clarity using these criteria:

**Clear (✅ - proceed with implementation):**
- Task goal is explicit
- Acceptance criteria defined or obvious
- Required files/components identified
- Approach is straightforward or documented in plan

**Minor ambiguity (⚠️ - make reasonable assumption):**
- Task goal is clear but approach has 2-3 valid options
- Some details missing but not critical to core functionality
- Can infer intent from context and plan
- Document assumption in code comments

**Major ambiguity (❌ - stop and ask):**
- Task goal is vague or has multiple interpretations
- Missing critical information (which component, what data structure, etc.)
- Approach unclear and not documented in plan
- Decision affects architecture or future phases

**Process:**
1. Read task description carefully
2. Check relevant plan sections for context
3. Assess clarity level using criteria above
4. If Major ambiguity: Use AskUserQuestion with task ID, what's unclear, which plan sections checked, and recommended approach
5. If Minor ambiguity: Proceed with documented assumption
6. If Clear: Proceed with implementation

## When Issues Arise
- Document the issue clearly
- Use AskUserQuestion for multiple valid approaches or critical decisions
- Continue with reasonable assumptions if minor
- Stop and ask if significant or affects architecture

## Code Quality
- Keep codebase runnable throughout
- Run tests after implementing functionality
- Follow constitution and project principles

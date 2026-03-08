---
description: Execute spec phase-by-phase following state document
disable-model-invocation: true
argument-hint: [feature-name] [instructions]
---

# Implement Command

Implement a feature by following the spec and state documents. This command executes an existing spec phase-by-phase, reading the spec for architectural context and the state for sequential execution. Your job is to execute tasks systematically and produce working code. Work proceeds one phase at a time with human review between phases.

## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/implement {feature-name} [implementation instructions]`

**Parsing:**

- First argument: feature name (must match existing spec)
- Remaining text: optional implementation scope or behavior
  - Example: `query-command implement phase 1 and 2, then stop`

**If no feature name provided:**

1. List existing specs: `find .cwf -maxdepth 2 -name "*-spec.md" -exec sh -c 'basename "$1" -spec.md' _ {} \;`
2. If exactly 1 spec found: use automatically and inform user
3. If multiple specs found: present list (optionally with progress status), use AskUserQuestion to ask user to select
4. If 0 specs found: inform user and suggest running `/write-spec` first

**Feature name usage:**
`{feature-name}` is a placeholder that gets replaced with the extracted feature name throughout this command.

Example file paths:

- `.cwf/{feature-name}/{feature-name}-spec.md`
- `.cwf/{feature-name}/{feature-name}-state.md`

## Instructions

### 1. Load Context

If skill `claude-workflow` is not loaded, load it using the Skill tool

---

### 2. Read Planning Documents

Read the following if they are not already loaded:

- `.cwf/{feature-name}/{feature-name}-spec.md` (WHY/WHAT - architectural context)
- `.cwf/{feature-name}/{feature-name}-state.md` (WHEN/HOW - sequential tasks)

---

### 3. Identify Next Work

Find the first incomplete task in the first incomplete phase:

- Scan state for unchecked tasks: `- [ ] [PX.Y] **ComponentName** — description`
- Identify current phase and task
- If all tasks complete: inform user feature is complete

---

### 4. Execute Tasks

For each task in the current phase:

1. **Read** the task description from state
2. **Implement** the task following spec guidance
3. **Mark complete** in `.cwf/{feature-name}/{feature-name}-state.md`:
   - Change `- [ ] [PX.Y] **ComponentName**` to `- [x] [PX.Y] **ComponentName**`
   - MAY add agent note as blockquote under task: `> Used X approach because Y`

Agent MAY add discovered tasks during implementation, but only to incomplete phases. Never modify completed tasks or phases.

Repeat until all tasks in current phase are complete.

---

### 5. Run Phase Checkpoints

After all phase tasks are marked complete:

1. Execute checkpoints sequentially (defined in state)
2. Mark each checkpoint complete as it passes
3. If checkpoint fails:
   - Minor issues (linting, formatting, types): fix and retry until passes or stuck
   - Major issues (architectural issues, complex problems): stop, describe to user and ask user for direction.
   - If stuck: ask user for guidance
4. Continue until all checkpoints pass

---

### 6. Complete Phase and Stop

When all checkpoints pass:

1. Output "Phase X Complete" summary
2. Summarize what was accomplished
3. Suggest commit message if appropriate
4. **STOP for human review** - do NOT proceed to next phase

**Between phases:** Human reviews work, optionally runs `/clear` and if so continues with a new call to `/implement {feature-name}` to resume.

## Output Templates

### Progress Check (always output first)

```text
✓ Phase 1: Complete (N/N tasks)
→ Phase 2: In progress (N/M tasks)
  Phase 3: Not started
```

### Phase Completion (output after all checkpoints pass)

```text
Phase X Complete!
- [summary of what was accomplished]
✓ All checkpoints passed.
Stopping for review.
```

## When Tasks Are Unclear

**Clear** — Task goal is explicit, approach straightforward or documented in spec. Proceed with implementation.

**Minor ambiguity** — Goal is clear but approach has 2-3 valid options. Pick the best option, proceed, and document the assumption as an agent note (`>`) under the task in the state document.

**Major ambiguity** — Goal is vague, has multiple interpretations, or decision affects architecture/future phases. Stop and use AskUserQuestion with task name, what's unclear, and recommended approach.

## Code Quality

- Keep codebase runnable throughout
- Follow project principles and rules

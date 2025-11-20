---
description: Update existing plan and tasklist based on conversation
---

# Amend Plan Command

Update an existing plan and tasklist based on conversation context. This command is used when amendments, changes, or extensions to an existing plan have been discussed. Your job is to understand those changes from the conversation and apply them safely.

## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/amend-plan {feature-name} [amendment description]`

**Parsing:**

- First token: feature name (must match existing plan)
- Remaining tokens: optional description of changes
  - Example: `query-command Add caching to Phase 3`

**If no feature name provided:**

1. List existing plans: `find plans/ -name "*-plan.md" -exec basename {} -plan.md \;`
2. If exactly 1 plan found: use automatically and inform user
3. If multiple plans found: use AskUserQuestion to present list and ask user to select
4. If 0 plans found: inform user and suggest running `/write-plan` first

**Feature name usage:**
`{feature-name}` is a placeholder that gets replaced with the extracted feature name throughout this command.

Example file paths:

- `plans/{feature-name}-plan.md`
- `plans/{feature-name}-tasklist.md`

## Instructions

### 1. Load and Analyze

1. If skill `read-constitution` not loaded, load it
2. If skill `cfw-planning` not loaded, load it

Read the following if not already loaded:

- `references/amendment.md`

Read existing documents:

- `plans/{feature-name}-plan.md`
- `plans/{feature-name}-tasklist.md`

If either missing: inform user and suggest running `/write-plan` or verifying feature name. STOP.

Analyze recent conversation history (last 10-20 messages before this command) to extract:

- Specific changes discussed
- New tasks/phases to add
- Plan sections to modify
- Where insertions should occur

Identify current state from tasklist:

- Which phases complete/in-progress/not-started
- Highest task number in each phase

---

### 2. Propose Amendments Interactively

**STOP and present proposal** to user:

```markdown
## Proposed Amendments to {feature-name} Plan

### Changes to Plan Document (plans/{feature-name}-plan.md)
- [List sections to add/modify with brief preview]

### Changes to Tasklist (plans/{feature-name}-tasklist.md)
- [List tasks to add with IDs and descriptions]
- [OR: New phases with goals]

### Safety Check

Assess amendment risk level:

**Safe amendments (✅):**
- Adding tasks to incomplete phases only
- Creating new phases for future work
- Adding new plan sections (no modifications)
- No changes to completed tasks

**Risky amendments (⚠️ - requires extra care):**
- Modifying incomplete tasks in current phase
- Changing phase structure or dependencies
- Removing tasks or phases
- Significant scope changes

**Blocked amendments (❌ - reject and explain):**
- Modifying or removing completed tasks
- Modifying or removing completed phases
- Changing task IDs of completed work
- Retroactive changes to finished phases

Assessment: [Safe/Risky/Blocked]
Warnings: [List any concerns]

Is this correct? Should I proceed?
```

Wait for confirmation. Use AskUserQuestion if needed to clarify.

**Proposal Refinement:**

Present the proposed amendments to the user. Then:

- IF user accepts: Proceed to Section 3
- IF user rejects: Ask what's missing/wrong/needs changing, revise the amendments, and present revised proposal (loop until accepted or aborted)
- IF user provides feedback: Incorporate the feedback and make new proposal. Ask question if the user intent is unclear (loop until accepted or aborted)

---

### 3. Apply and Validate

After confirmation, apply the accepted changes:

1. Apply each change using the Edit tool
2. Validate structural conformance:
   - New sections use same markdown heading levels and structure as existing sections
   - New tasks use `- [ ] [PX.Y] Description` format matching existing tasks
   - Task IDs are sequential with no gaps (e.g., P3.5 → P3.6 → P3.7)
3. If validation fails: fix and re-validate

---

### 4. Confirm Completion

Present summary:

```markdown
## Amendments Applied ✅

### Updated Files
- plans/{feature-name}-plan.md - [changes]
- plans/{feature-name}-tasklist.md - [changes]

### Summary
- [What was added/modified]
- [New task IDs if applicable]

### Next Steps
- Continue amendment
- Resume implementation
```

## Requirements

- Follow safety rules from amendment.md
- ALWAYS confirm understanding before changes
- Make inline updates, no separate amendment sections

## Example Flow

```text
Loading plan: query-command
- Read plans/query-command-plan.md ✅
- Read plans/query-command-tasklist.md ✅

Analyzing conversation...
You want to: add caching to Phase 3, create Phase 4 for performance testing

Current state:
- Phase 1: ✅ Complete (3/3)
- Phase 2: ✅ Complete (4/4)
- Phase 3: ⏳ In Progress (2/5 complete)

## Proposed Amendments

**Tasklist:**
- Phase 3: Add tasks [P3.6]-[P3.8] for caching
- Phase 4: New phase with 4 tasks for performance testing

**Plan:**
- Add "Caching Strategy" subsection to Architecture section

Safety check: ✅ All amendments target incomplete phases

Proceed? [User confirms]

Applying...
✅ Updated plans/query-command-plan.md (added Caching Strategy section)
✅ Updated plans/query-command-tasklist.md (added P3.6-P3.8, new Phase 4)

Validating amendments...
✓ Plan sections match existing structure and style
✓ Tasklist tasks match existing format
✓ Phase 4 structure matches existing phases
✓ Task IDs sequential (P3.6, P3.7, P3.8, P4.1, P4.2, P4.3, P4.4)
✓ Checkboxes preserved
✓ No completed tasks modified

Done! Resume with `/implement query-command`.
```

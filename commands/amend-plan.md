---
description: Update existing plan and tasklist based on conversation
---

# Amend Plan Command

Update an existing plan and tasklist based on conversation context.

## Bootstrap

**Check if CWF skills are already loaded in this session:**
- Do you have the cfw-planning skill loaded with access to reference documents (plan-spec.md, tasklist-spec.md)?

**If NO (skills not yet loaded):**
1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete

**If YES (skills already loaded):**
- Skip skill loading, knowledge is already available

## Required References

**Check if required references are already loaded in this session:**
- Do you have access to amendment.md content (amendment safety rules for what operations are allowed)?

**If NO (not yet loaded):**
- Use the Read tool to load: `references/amendment.md`

**If YES (already loaded):**
- Skip loading, reference knowledge is already available

Then proceed with instructions below.

**Note:** Plan and tasklist structure will be inferred from the existing documents rather than reading specs, reducing context overhead.

## Context

This command is used when amendments, changes, or extensions to an existing plan have been discussed. Your job is to understand those changes from the conversation and apply them safely.

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
- Loads: `plans/{feature-name}-plan.md` and `plans/{feature-name}-tasklist.md`

## Instructions

### 1. Load Existing Documents

Read the existing planning documents:
- `plans/{feature-name}-plan.md`
- `plans/{feature-name}-tasklist.md`

**If either file is missing:**
- Inform user: "Cannot find plan files for '{feature-name}'"
- Suggest: "Run `/write-plan {feature-name}` to create new plan, or verify feature name"
- STOP - do not proceed

When both documents loaded successfully, proceed to Section 2.

---

### 2. Analyze Conversation for Amendment Intent

Review recent conversation messages (approximately last 10-20 messages) to understand:

- What specific changes were discussed
- Which sections need to be amended
- What new tasks or phases need to be added
- What modifications to plan sections are needed
- Why the amendments are being made

Extract specific details:

- New task descriptions and where they should be inserted
- New phase descriptions and goals
- Section updates in the plan document
- Any clarifications or examples to add

When conversation analysis complete, proceed to Section 3.

---

### 3. Identify Current State

Examine the tasklist to determine:

- Which phases are complete (all tasks marked `[x]`)
- Which phases are in progress (some tasks marked `[x]`)
- Which phases are not started (no tasks marked `[x]`)
- The highest task number in each phase (for ID allocation)

When current state identified, proceed to Section 4.

---

### 4. Propose Amendments Interactively

**STOP and present a clear summary** of proposed changes to the user:

```markdown
## Proposed Amendments to {feature-name} Plan

Based on the conversation, I understand you want to make the following changes:

### Changes to Plan Document (plans/{feature-name}-plan.md)
- [List specific sections to add/modify, e.g., "Add new subsection 'Caching Strategy' to Architecture section"]
- [Show brief preview of new content]

### Changes to Tasklist (plans/{feature-name}-tasklist.md)
- [List specific tasks to add, e.g., "Add tasks P3.4-P3.6 to Phase 3: [descriptions]"]
- [OR: "Add new Phase 4: [goal and tasks]"]
- [Show where tasks will be inserted]

### Safety Check
- ✅ No modifications to completed tasks
- ⚠️ [Any warnings about edge cases or potential issues]

Is this understanding correct? Should I proceed with these amendments?
```

**Wait for user confirmation** before proceeding. Use the AskUserQuestion tool if needed to clarify ambiguous requirements.

**If user rejects proposal:**
1. Ask for specific concerns or required changes
2. Revise proposal based on feedback
3. Re-present updated proposal (return to beginning of Section 4)
4. Repeat until user approves

When user approves, proceed to Section 5.

---

### 5. Apply Amendments Safely

After receiving user confirmation in Section 4, apply amendments following these steps:

1. Read amendment.md from cfw-planning skill for safety rules
2. For each proposed change:
   - Verify it's an allowed operation (amendment.md defines allowed/blocked operations)
   - Apply using Edit tool
   - Mark change as applied
3. Verify no blocked operations attempted (e.g., modifying completed tasks)

When all changes applied, proceed to Section 5.5.

---

### 5.5 Validate Amended Documents

After applying amendments, verify structural conformance:

**Structural validation:**
1. New sections match existing section structure and style
2. Markdown formatting consistent with existing content
2. New tasks match existing task format
3. New phases match existing phase structure

**Amendment Safety Validation:**
1. Only allowed operations performed

If ANY validation fails:
- Identify the issue
- Fix the affected document
- Re-run validation for that document
- Repeat until all validations pass

When all validations pass, proceed to Section 6.

---

### 6. Confirm Completion

After applying amendments, provide a summary:

```markdown
## Amendments Applied ✅

### Updated Files
- plans/{feature-name}-plan.md - [brief description of changes]
- plans/{feature-name}-tasklist.md - [brief description of changes]

### Summary of Changes
- [List what was added/modified]
- [Show new task IDs if applicable]

### Next Steps
The amended plan is ready. You can:
- Continue iterating with `/amend-plan {feature-name}` for further changes
- Start/resume implementation with `/implement {feature-name}`
- Review the updated files to verify changes
```

## Requirements


All amendments MUST follow safety rules from amendment.md.

Command-specific requirements:
- **Conversation analysis:** Thoroughly review conversation to understand amendment intent
- **Interactive confirmation:** ALWAYS confirm understanding before making changes
- **Clear communication:** Show exactly what will change and why
- **Inline changes:** Make direct updates to files, no separate "amendment" sections


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

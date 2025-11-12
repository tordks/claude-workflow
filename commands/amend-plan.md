---
description: Update existing plan and tasklist based on conversation
---

# Amend Plan Command

Update an existing plan and tasklist based on conversation context.

## Bootstrap

Use the Skill tool to load: `cfw-planning`

Wait for it to complete, then proceed with instructions below.

## Context

This command is used when amendments, changes, or extensions to an existing plan have been discussed. Your job is to understand those changes from the conversation and apply them safely.

## Arguments

**Input**: `$ARGUMENTS`

Use the feature name parsing pattern from cfw-planning skill.

## Instructions

### 1. Load Existing Documents

Read the existing planning documents:
- `plans/{feature-name}-plan.md`
- `plans/{feature-name}-tasklist.md`

(See cfw-planning skill for document relationship and synergy principles)

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

### 3. Identify Current State

Examine the tasklist to determine:

- Which phases are complete (all tasks marked `[x]`)
- Which phases are in progress (some tasks marked `[x]`)
- Which phases are not started (no tasks marked `[x]`)
- The highest task number in each phase (for ID allocation)

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

### 5. Apply Amendments Safely

Once confirmed, apply the changes following amendment safety rules from cfw-planning skill's amendment.md reference.

See cfw-planning skill for complete amendment safety rules, allowed/blocked operations, and detailed guidelines.

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

- **Conversation analysis**: Thoroughly review recent messages to understand intent
- **Interactive confirmation**: ALWAYS confirm understanding before making changes
- **Safety first**: NEVER modify completed work - block and explain
- **Preserve structure**: Maintain all formatting, task IDs, and organizational structure
- **Clear communication**: Show exactly what will change and why
- **Inline changes**: Make direct updates to files without separate "amendment" sections (unless context requires it)
- **Consistent formatting**: Match the existing document style precisely

## Amendment Safety

For complete amendment rules, allowed/blocked operations, and when blocked guidance, see cfw-planning skill's amendment.md reference.

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

Done! Resume with `/implement query-command`.
```

## Notes

- Thoroughly analyze conversation - don't miss details
- Always confirm proposed changes before applying
- Explain safety blocks and suggest alternatives
- Ensure amendments integrate naturally with existing structure
- Follow sequential task ID numbering within phases
- Test that amendments work seamlessly with `/implement`

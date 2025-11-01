# Amend Plan Command

Update an existing plan and tasklist based on conversation context.

## Bootstrap

Use the SlashCommand tool to execute: `/prime-planning-commands`

Wait for it to complete, then proceed with instructions below.

## Context

This command is used when amendments, changes, or extensions to an existing plan have been discussed. Your job is to understand those changes from the conversation and apply them safely.

## Arguments

**Input**: `$ARGUMENTS`

Use the standard feature name parsing pattern from `/prime-planning-commands`.

## Instructions

### 1. Load Existing Documents

Read the existing planning documents:

- `plans/{feature-name}-plan.md` - the comprehensive plan document (provides architectural context and design decisions)
- `plans/{feature-name}-tasklist.md` - the phase-based tasklist (provides step-by-step execution tracking)

**Document relationship**: The plan provides WHY and WHAT (architecture), while the tasklist provides WHEN and HOW (execution steps). Amendments should maintain this synergy.

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

Once confirmed, apply the changes following these rules:

#### Safety Rules (CRITICAL)

- **NEVER modify completed tasks**: Tasks marked `[x]` are immutable
- **NEVER modify completed phases**: Phases where all tasks are `[x]` cannot be changed
- **NEVER change task IDs**: Existing task IDs like `[P1.2]` must remain unchanged
- **BLOCK invalid operations**: If user requests modifying completed work, explain why it cannot be done and suggest alternatives

#### Allowed Operations

**For Tasklist Amendments**:

1. **Add tasks to incomplete phases**:
   - Insert after the last existing task in that phase
   - Use next sequential task ID (e.g., if last task is `[P2.3]`, new task is `[P2.4]`)
   - New tasks start with `[ ]` (unchecked)
   - Preserve phase goal and deliverable statements

2. **Add new phases**:
   - Add after the highest existing phase number or as a sub-phase, ie Phase 3.1, depending on context.
   - Follow phase structure: Goal, Deliverable, Tasks section
   - Start all tasks unchecked `[ ]`
   - Number tasks starting from `.1` (e.g., `[P4.1]`, `[P4.2]`)

3. **Modify incomplete task descriptions**:
   - Only if task is marked `[ ]` (not `[x]`)
   - Preserve task ID and checkbox format
   - Update description text inline

4. **Update phase goals/deliverables**:
   - Only for incomplete phases
   - Preserve the section structure and formatting

**For Plan Document Amendments**:

1. **Add new sections**:
   - Insert in logical position (e.g., new architecture subsection)
   - Match existing formatting and header levels
   - Include context about why the amendment was made

2. **Update existing sections**:
   - Enhance or clarify existing content
   - Add examples, diagrams, or code snippets
   - Preserve original section structure

3. **Add clarifications**:
   - Inline additions to existing sections
   - New subsections for substantial additions
   - Keep amendments focused and concise

#### File Update Process

1. Use the Edit tool to make precise changes
2. Preserve all existing formatting (headers, lists, code blocks)
3. Maintain consistent markdown style
4. Keep line breaks and spacing consistent with original
5. For tasklist: Ensure task ID sequences are continuous within each phase
6. Verify checkboxes remain in correct format: `- [ ]` or `- [x]`

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

## Amendment Types

| Type | Example | Allowed? |
|------|---------|----------|
| Add tasks to incomplete phase | Add [P3.4], [P3.5] to Phase 3 (has incomplete tasks) | ✅ Yes |
| Add new phase | Create Phase 4 after Phase 3 | ✅ Yes |
| Modify incomplete task description | Change `[ ] [P3.2] Add tests` to `[ ] [P3.2] Add unit and integration tests with >90% coverage` | ✅ Yes |
| Update plan sections | Add new subsection "Caching Strategy" to Architecture | ✅ Yes |
| Modify completed task | Change `[x] [P2.1]` description | ❌ No - immutable |
| Add task to completed phase | Add task to Phase 1 (all tasks `[x]`) | ❌ No - inconsistent |

### When Blocked

If user requests modification of completed work:
1. Explain why it's not allowed (immutability, implementation history)
2. Suggest alternatives: new task, new phase, or refactoring phase
3. Use AskUserQuestion tool to present options

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

---
description: Update existing spec and state based on conversation
disable-model-invocation: true
argument-hint: [feature-name] [amendment description]
---

# Amend Command

Update an existing spec and state based on conversation context. This command is used when amendments, changes, or extensions to an existing spec have been discussed. Your job is to understand those changes from the conversation and apply them safely.

## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/amend {feature-name} [amendment description]`

**Parsing:**

- First token: feature name (must match existing spec)
- Remaining tokens: optional description of changes
  - Example: `query-command Add caching to Phase 3`

**If no feature name provided:**

1. List existing specs: `find .cwf -maxdepth 2 -name "*-spec.md" -exec sh -c 'basename "$1" -spec.md' _ {} \;`
2. If exactly 1 spec found: use automatically and inform user
3. If multiple specs found: use AskUserQuestion to present list and ask user to select
4. If 0 specs found: inform user and suggest running `/write-spec` first

**Feature name usage:**
`{feature-name}` is a placeholder that gets replaced with the extracted feature name throughout this command.

Example file paths:

- `.cwf/{feature-name}/{feature-name}-spec.md`
- `.cwf/{feature-name}/{feature-name}-state.md`

## Instructions

### 1. Load and Analyze

If skill `claude-workflow` is not loaded, load it using the Skill tool

Read the following if not already loaded:

- `references/amendment.md`

Read existing documents:

- `.cwf/{feature-name}/{feature-name}-spec.md`
- `.cwf/{feature-name}/{feature-name}-state.md`

If either missing: inform user and suggest running `/write-spec` or verifying feature name. STOP.

Analyze conversation history to extract (focus on recent messages, but review further back if needed):

- Specific changes discussed
- New tasks/phases to add
- Spec sections to modify
- Where insertions should occur

Identify current state from state document:

- Which phases complete/in-progress/not-started
- Tasks in each phase

---

### 2. Propose Amendments Interactively

**STOP and present proposal** to user:

```markdown
## Proposed Amendments to {feature-name} Spec

### Changes to Spec Document (.cwf/{feature-name}/{feature-name}-spec.md)
- [List sections to add/modify with brief preview]

### Changes to State (.cwf/{feature-name}/{feature-name}-state.md)
- [List tasks to add with descriptions]
- [OR: New phases with goals]

### Safety Check

Assess amendment risk level:

**Safe amendments:**
- Adding tasks to incomplete phases only
- Creating new phases for future work
- Adding new spec sections (no modifications)
- No changes to completed tasks

**Risky amendments (requires extra care):**
- Modifying incomplete tasks in current phase
- Changing phase structure or dependencies
- Removing tasks or phases
- Significant scope changes

**Blocked amendments (reject and explain):**
- Modifying or removing completed tasks
- Modifying or removing completed phases
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
   - New tasks use `- [ ] [PX.Y] **ComponentName** — description` format matching existing tasks
   - New task IDs are sequential (continuing from the last ID in the phase)
   - Tasks are logically organized within phases
3. If validation fails: fix and re-validate

---

### 4. Confirm Completion

Present summary:

```markdown
## Amendments Applied

### Updated Files
- .cwf/{feature-name}/{feature-name}-spec.md - [changes]
- .cwf/{feature-name}/{feature-name}-state.md - [changes]

### Summary
- [What was added/modified]
- [New tasks if applicable]

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
Loading spec: query-command
- Read .cwf/query-command/query-command-spec.md
- Read .cwf/query-command/query-command-state.md

Analyzing conversation...
You want to: add caching to Phase 3, create Phase 4 for performance testing

Current state:
- Phase 1: Complete (3/3)
- Phase 2: Complete (4/4)
- Phase 3: In Progress (2/5 complete)

## Proposed Amendments

**State:**
- Phase 3: Add tasks [P3.6] **CacheSetup**, [P3.7] **CacheIntegration**, [P3.8] **CacheInvalidation** for caching
- Phase 4: New phase with 4 tasks ([P4.1]–[P4.4]) for performance testing

**Spec:**
- Add "Caching Strategy" subsection to Architecture section

Safety check: All amendments target incomplete phases

Proceed? [User confirms]

Applying...
Updated .cwf/query-command/query-command-spec.md (added Caching Strategy section)
Updated .cwf/query-command/query-command-state.md (added caching tasks, new Phase 4)

Validating amendments...
✓ Spec sections match existing structure and style
✓ State tasks match existing format
✓ Phase 4 structure matches existing phases
✓ Checkboxes preserved
✓ No completed tasks modified

Done! Resume with `/implement query-command`.
```

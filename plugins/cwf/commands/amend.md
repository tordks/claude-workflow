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

- First argument: feature name (must match existing spec)
- Remaining text: optional description of changes
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

### Safety Assessment
- Classify each change: Safe (new tasks/phases/sections) / Risky (modifying incomplete work) / Blocked (touching completed work)
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

- ALWAYS confirm understanding before changes
- Make inline updates, no separate amendment sections

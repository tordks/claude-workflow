# Implementation Essentials

Minimal guide for implementing features following CWF plans and tasklists.

## Finding Plan Files

To locate planning documents for a feature:

1. Look in `plans/` directory
2. Find `{feature-name}-plan.md` for architectural context
3. Find `{feature-name}-tasklist.md` for execution steps

**Pattern:**
- Plan files: `plans/*-plan.md`
- Tasklist files: `plans/*-tasklist.md`
- Feature name: filename minus `-plan.md` or `-tasklist.md` suffix

## Implementation Workflow

Follow this sequence when implementing:

### 1. Read Plan First
Load `plans/{feature-name}-plan.md` in full to understand:
- Overall architecture
- WHY decisions were made
- How components relate
- Technical constraints and dependencies

### 2. Read Tasklist Second
Load `plans/{feature-name}-tasklist.md` for execution guidance:
- Find first incomplete phase
- Review phase goal and deliverable
- Start with first unchecked task

### 3. During Implementation
Execute tasks in order:
- Implement task
- Test the change
- Mark task complete (change `[ ]` to `[x]`)
- Move to next task

**Refer back to plan when:**
- Task details are unclear
- Need architectural context
- Unsure about implementation approach
- Question trade-offs or design decisions

**Stop at phase boundaries:**
- When all tasks in phase marked `[x]`
- Present summary and checkpoint
- Wait for approval before next phase

## Phase Structure

Each phase follows this structure:

```markdown
## Phase X: Descriptive Name

**Goal:** One sentence describing what this phase accomplishes

**Deliverable:** Concrete outcome

**Tasks:**
- [ ] [PX.1] Specific task description
- [ ] [PX.2] Another task description
- [ ] [PX.3] Write tests
- [ ] [PX.4] Verify tests pass

**Phase X Checkpoint:** System state after completion
```

**Phase 0 is special:**
- Always branch setup only
- Single task: Create git branch
- Must complete before Phase 1

## Task IDs and Completion

### Task ID Format
`[PX.Y]` where:
- **P** = Phase prefix
- **X** = Phase number (0, 1, 2, ...)
- **Y** = Task number within phase (1, 2, 3, ...)

### Marking Tasks Complete
Change checkbox when task is done:
```markdown
- [ ] [P2.3] Incomplete task  →  - [x] [P2.3] Completed task
```

**Rules:**
- Edit the tasklist file directly
- Change exactly one task at a time
- Never modify task IDs
- Never modify already completed tasks `[x]`

## When to Reference Full Guides

If you need more detail, see:

| Need... | Reference |
|---------|-----------|
| Plan document structure | `plan-structure.md` |
| Tasklist document structure | `tasklist-structure.md` |
| Document relationship details | `document-synergy.md` |
| Feature naming conventions | `conventions.md` |

## Quick Validation

Before starting implementation, verify:
- ✅ Plan has 5 required sections
- ✅ Tasklist has Phase 0 with branch setup
- ✅ Task IDs follow [PX.Y] format
- ✅ Each phase has Goal, Deliverable, Tasks, Checkpoint

If validation fails, refer to full structure guides for details.

## Example: Checking Task Details

**Task:** `[P2.1] Implement TF-IDF scoring in ranker.py`

**Questions that might arise:**
- What parameters should scoring function take?
  → Check plan: Technical Approach → Integration Points
- Should this use a library or custom implementation?
  → Check plan: Design Decisions → Dependencies rationale
- How to handle edge cases?
  → Check plan: Technical Approach → Error Handling

The plan provides the WHY and context; the task tells you WHAT to do.

---

**This is the minimal guide for implementation.** For comprehensive structure details, templates, and amendment rules, see the full reference guides.

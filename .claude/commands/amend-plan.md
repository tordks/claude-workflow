# Amend Plan Command

Update the existing plan and tasklist for the **$ARGUMENTS** feature based on conversation context.

## Context

This command is used when you've discussed amendments, changes, or extensions to an existing plan with the user. The user has already discussed specific modifications they want to make. Your job is to understand those changes from the conversation and apply them safely.

**Arguments**: `$ARGUMENTS` captures the feature name (e.g., `/amend-plan query-command`).

## Instructions

### 1. Load Existing Documents

Read the existing planning documents:

- `plans/$ARGUMENTS-plan.md` - the comprehensive plan document
- `plans/$ARGUMENTS-tasklist.md` - the phase-based tasklist

**If `$ARGUMENTS` is empty**:

- List all plan files in the `plans/` directory (look for `*-plan.md` files)
- Extract feature names from filenames (e.g., `query-plan.md` → `query`)
- Present available features to the user
- Ask user to select which plan to amend
- Use the selected feature name for the rest of the command

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
## Proposed Amendments to {feature} Plan

Based on the conversation, I understand you want to make the following changes:

### Changes to Plan Document (plans/{feature}-plan.md)
- [List specific sections to add/modify, e.g., "Add new subsection 'Caching Strategy' to Architecture section"]
- [Show brief preview of new content]

### Changes to Tasklist (plans/{feature}-tasklist.md)
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
- plans/{feature}-plan.md - [brief description of changes]
- plans/{feature}-tasklist.md - [brief description of changes]

### Summary of Changes
- [List what was added/modified]
- [Show new task IDs if applicable]

### Next Steps
The amended plan is ready. You can:
- Continue iterating with `/amend-plan` for further changes
- Start/resume implementation with `/implement {feature}`
- Review the updated files to verify changes
```

## Requirements

- **Feature name**: Must be provided or selected from available plans
- **Conversation analysis**: Thoroughly review recent messages to understand intent
- **Interactive confirmation**: ALWAYS confirm understanding before making changes
- **Safety first**: NEVER modify completed work - block and explain
- **Preserve structure**: Maintain all formatting, task IDs, and organizational structure
- **Clear communication**: Show exactly what will change and why
- **Inline changes**: Make direct updates to files without separate "amendment" sections (unless context requires it)
- **Consistent formatting**: Match the existing document style precisely

## Amendment Types Supported

### 1. Add Tasks to Existing Phase

```markdown
## Phase 2: Implementation

**Goal**: Build core functionality

**Tasks**:
- [x] [P2.1] Implement parser
- [x] [P2.2] Add validation
- [ ] [P2.3] Add error handling        ← existing incomplete task
- [ ] [P2.4] Add logging and metrics   ← NEW TASK (added via amendment)
- [ ] [P2.5] Add rate limiting         ← NEW TASK (added via amendment)
```

### 2. Add New Phase

```markdown
## Phase 4: Performance Optimization    ← NEW PHASE

**Goal**: Optimize query performance and add caching

**Deliverable**: System handles 1000+ queries/sec with <100ms latency

**Tasks**:
- [ ] [P4.1] Implement Redis caching layer
- [ ] [P4.2] Add query result caching
- [ ] [P4.3] Add performance benchmarks
- [ ] [P4.4] Optimize database queries

**Phase 4 Checkpoint**: Performance targets met, caching operational
```

### 3. Modify Incomplete Task

```markdown
Before:
- [ ] [P3.2] Add tests

After:
- [ ] [P3.2] Add comprehensive unit and integration tests with >90% coverage
```

### 4. Update Plan Section

```markdown
## Architecture & Design

### Core Components
[existing content...]

### Caching Strategy    ← NEW SUBSECTION
We'll implement a two-tier caching approach:
- L1: In-memory LRU cache (5000 items, 5min TTL)
- L2: Redis distributed cache (50000 items, 1hr TTL)

[detailed explanation...]
```

## Safety Violations and Responses

### ❌ Attempting to Modify Completed Task

**User request**: "Change task P2.1 to include database optimization"
**Response**:

```text
Cannot modify task [P2.1] because it is already completed (marked [x]).
Completed tasks are immutable to preserve implementation history.

Alternative approaches:
1. Add a new task to Phase 2: "[P2.X] Add database optimization to existing parser"
2. Create a new phase for optimization work
3. Create a refactoring phase to revisit completed work

Would you like me to add a new task instead?
```

### ❌ Attempting to Add Task to Completed Phase

**User request**: "Add a new task to Phase 1"
**Response**:

```text
Cannot add tasks to Phase 1 because all tasks in this phase are completed.
Adding tasks to completed phases would be inconsistent with implementation history.

Alternative approaches:
1. Create a new phase (e.g., "Phase 1B: Additional Foundation Work")
2. Add the task to the next incomplete phase if logically appropriate
3. Create a new phase specifically for the new functionality

Which approach would you prefer?
```

### ✅ Valid Amendment

**User request**: "Add caching tasks to Phase 3"
**Response**:

```text
Phase 3 has 2 incomplete tasks, so I can safely add new tasks here.

Proposed amendments:
- Add [P3.4] Implement Redis caching layer
- Add [P3.5] Add cache invalidation logic
- Add [P3.6] Add caching integration tests

These will be added after existing task [P3.3]. Proceed?
```

## Example Flow

```text
Loading plan for feature: query-command
- Reading: plans/query-command-plan.md ✅
- Reading: plans/query-command-tasklist.md ✅

Analyzing recent conversation...

From the conversation, I understand you want to:
1. Add caching functionality to Phase 3
2. Create a new Phase 4 for performance testing
3. Update the Architecture section with caching design

Current state:
- Phase 1: ✅ Complete (3/3 tasks)
- Phase 2: ✅ Complete (4/4 tasks)
- Phase 3: ⏳ In Progress (2/5 tasks complete)
- Last task in Phase 3: [P3.5]

## Proposed Amendments

### Tasklist Changes
**Phase 3: Add 3 new tasks**
- [P3.6] Implement Redis caching client with connection pooling
- [P3.7] Add caching middleware to query pipeline
- [P3.8] Add cache hit/miss metrics and monitoring

**Phase 4: New phase**
- Goal: Validate performance and scalability
- 4 tasks for load testing, benchmarking, optimization

### Plan Document Changes
**Architecture section**: Add "Caching Strategy" subsection with:
- Two-tier caching design (L1: memory, L2: Redis)
- Cache key strategy and TTL policies
- Invalidation approach

Safety check: ✅ All amendments target incomplete phases only

Is this correct? Should I proceed?

[User confirms]

Applying amendments...

✅ Updated plans/query-command-plan.md
   - Added "Caching Strategy" subsection to Architecture (45 lines added)

✅ Updated plans/query-command-tasklist.md
   - Added tasks [P3.6] through [P3.8] to Phase 3
   - Added Phase 4 with tasks [P4.1] through [P4.4]

Amendments applied successfully! The plan now includes caching functionality
and performance validation. Resume implementation with `/implement query-command`.
```

## Notes

- **Be thorough in conversation analysis**: Don't miss important details from the discussion
- **Confirm before acting**: Always present proposed changes and wait for approval
- **Explain safety blocks**: If a requested change violates safety rules, explain why and suggest alternatives
- **Maintain consistency**: Ensure amendments fit naturally with existing plan structure
- **Preserve context**: Keep the plan cohesive - new additions should integrate well with existing content
- **Be precise with IDs**: Task ID allocation must follow sequential numbering within each phase
- **Test integration**: Amendments should work seamlessly with `/implement` command

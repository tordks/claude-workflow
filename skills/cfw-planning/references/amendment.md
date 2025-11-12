# Amendment Reference

Guidelines for safely modifying existing CWF plans and tasklists.

## Core Amendment Principles

### Protect Completed Work

**Do not modify:**
- Completed tasks (marked [x]) - they represent implemented code
- Completed phases (all tasks marked [x]) - history is immutable
- Task IDs - they are stable references
- Historical decisions - document new decisions instead

### Safe Amendment Practices

**When amending:**
- Add new tasks to incomplete phases only
- Use next sequential task ID when adding tasks
- Preserve existing task IDs when modifying descriptions
- Confirm changes with user before applying
- Explain why certain operations aren't safe

**If user requests unsafe modifications:**
- Block the operation
- Explain why it's not recommended
- Suggest safe alternatives

## Why These Rules Exist

**Completed tasks represent implemented code:**
- Changing them breaks the implementation record
- Code exists that matches the completed task description
- Historical accuracy matters for understanding what was built

**Task IDs are stable references:**
- Used in discussion, commits, and tracking
- Changing them breaks all references
- Sequential IDs enable clear progress tracking

**Implementation history matters:**
- Need to know what was done and when
- Helps understand evolution of the feature
- Enables troubleshooting and rollback if needed

**Immutability ensures reliable progress tracking:**
- What's marked [x] can be trusted as complete
- Provides clear state at any point in time
- No ambiguity about what's been implemented

## Allowed Operations

### Add Tasks to Incomplete Phase

Insert new tasks after the last existing task, using next sequential task ID:

```markdown
## Phase 2: Ranking (IN PROGRESS)
- [x] [P2.1] Implement TF-IDF scoring
- [x] [P2.2] Add document ranking
- [ ] [P2.3] Add caching layer  ← NEW (next sequential ID)
- [ ] [P2.4] Write tests for caching  ← NEW
- [ ] [P2.5] Verify tests pass (original P2.3, renumbered)
```

**Requirements:**
- Only add to phases with at least one incomplete task `[ ]`
- Use next sequential ID (if last task is P2.2, next is P2.3)
- Start new tasks unchecked `[ ]`
- Preserve phase goal and deliverable
- May need to renumber existing incomplete tasks

### Add New Phase

Create a new phase after the highest existing phase number:

```markdown
## Phase 4: Caching Optimization  ← NEW

**Goal:** Add caching to improve query performance

**Deliverable:** Query cache with LRU eviction

**Tasks:**
- [ ] [P4.1] Create cache.py with CacheManager
- [ ] [P4.2] Integrate cache with QueryRanker
- [ ] [P4.3] Add tests for cache behavior

**Phase 4 Checkpoint:** Query cache operational, performance improved
```

**Requirements:**
- Follow standard phase structure (Goal, Deliverable, Tasks, Checkpoint)
- All tasks start unchecked `[ ]`
- Task numbering starts at .1 (e.g., P4.1, P4.2, ...)
- Include clear phase checkpoint

### Modify Incomplete Task Description

Update task description while preserving task ID:

```markdown
BEFORE: - [ ] [P2.3] Write tests for ranking
AFTER:  - [ ] [P2.3] Write unit tests for ranking in test_ranker.py
```

**Requirements:**
- Only modify tasks marked `[ ]` (not `[x]`)
- Keep task ID unchanged
- Keep checkbox format `- [ ]` unchanged
- Update description text only

### Update Plan Sections

Add or modify sections in the plan document:

```markdown
## Technical Approach

### Caching Strategy  ← NEW SECTION
- Use LRU cache with 1000 entry limit
- Cache key: query string hash
- Invalidate on index update
```

**Requirements:**
- Add new subsections as needed
- Clarify or enhance existing sections
- Document rationale for new decisions
- Preserve existing section structure

## Blocked Operations

### Cannot Modify Completed Task

```markdown
- [x] [P2.1] Implement TF-IDF scoring ← COMPLETED, CANNOT CHANGE
```

**Why blocked:** Task marked [x] means code was implemented. Changing the description would misrepresent what was actually built.

**Alternative:** Create new task or phase to modify the implementation.

### Cannot Change Task ID

```markdown
- [ ] [P2.3] Original task ← CANNOT BECOME [P2.4]
```

**Why blocked:** Task IDs are stable references used in commits, discussions, and tracking. Changing them breaks all references.

**Alternative:** Keep the ID, update the description if task is incomplete.

### Cannot Add to Completed Phase

```markdown
## Phase 1: Foundation (ALL TASKS [x])
- [x] [P1.1] Create models
- [x] [P1.2] Add validation
- [x] [P1.3] Write tests
- [ ] [P1.4] NEW TASK ← BLOCKED, phase is complete
```

**Why blocked:** Phase is complete means all work is done and code is stable. Adding tasks would make the phase inconsistent.

**Alternative:** Create new phase for additional work.

## When to Update Each Document

### Update Plan When:
- Discovered new technical constraints
- Need to add new sections (e.g., Caching Strategy, Security Considerations)
- Want to clarify existing design decisions
- Found better approach and want to document rationale
- Need to add risks or considerations

### Update Tasklist When:
- Need to add tasks to incomplete phases
- Want to create new phases for additional work
- Need to clarify incomplete task descriptions
- Discovered tasks were missed during planning

### DON'T Update:
- Completed tasks or phases (history is immutable)
- Task IDs (stable references)
- Historical decisions (document new decisions instead)

## When Blocked

If user requests modification of completed work:

1. **Explain why it's not allowed:**
   - "This task is marked [x], meaning it's been implemented"
   - "Changing it would misrepresent what code was actually built"
   - "Task IDs are stable references used throughout the project"

2. **Suggest alternatives:**
   - New task in current incomplete phase
   - New phase for refactoring or enhancements
   - Update plan's Risks section to note technical debt

3. **Present options:**
   - Use AskUserQuestion tool to offer 2-4 concrete alternatives
   - Let user choose the appropriate approach
   - Don't proceed without confirmation

## Quick Reference: Amendment Types

| Type | Example | Allowed? |
|------|---------|----------|
| Add tasks to incomplete phase | Add [P3.4], [P3.5] to Phase 3 (has incomplete tasks) | ✅ Yes |
| Add new phase | Create Phase 4 after Phase 3 | ✅ Yes |
| Modify incomplete task description | Change `[ ] [P3.2] Add tests` to `[ ] [P3.2] Add unit and integration tests with >90% coverage` | ✅ Yes |
| Update plan sections | Add new subsection "Caching Strategy" to Architecture | ✅ Yes |
| Modify completed task | Change `[x] [P2.1]` description | ❌ No - immutable |
| Add task to completed phase | Add task to Phase 1 (all tasks `[x]`) | ❌ No - inconsistent |
| Change task ID | Renumber [P2.3] to [P2.5] | ❌ No - stable references |

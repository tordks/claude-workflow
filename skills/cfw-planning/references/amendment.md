# Amendment Reference

Safety rules for modifying CWF plans and tasklists during implementation.

## Core Principle

**Completed work is immutable.** Tasks marked `[x]` represent implemented code and form a trusted implementation history. Changing completed work breaks trust in the plan as source of truth and creates confusion about what was actually built. This immutability enables reliable progress tracking, troubleshooting, and context preservation across sessions.

## Amendment Operations

| Operation | Allowed? | Rules | Example |
|-----------|----------|-------|---------|
| **Add tasks to incomplete phase** | ✅ Yes | Phase must have at least one `[ ]` task. Use next sequential ID. | Add `[P2.3]`, `[P2.4]` to Phase 2 (has incomplete tasks) |
| **Add new phase** | ✅ Yes | Use next phase number. Include Goal, Deliverable, Tasks, Checkpoint. All tasks start `[ ]`. | Create Phase 4 after Phase 3 |
| **Modify incomplete task description** | ✅ Yes | Only `[ ]` tasks. Preserve ID and checkbox, update description only. | Change `[ ] [P3.2] Add tests` → `[ ] [P3.2] Add unit tests with 90% coverage` |
| **Update plan sections** | ✅ Yes | Add subsections, clarify decisions, document new constraints. | Add "Caching Strategy" subsection to Technical Approach |
| **Modify completed task** | ❌ No | Code already built. Changing description misrepresents implementation. | Use new task/phase to modify implementation instead |
| **Add task to completed phase** | ❌ No | All tasks `[x]` means phase done. Adding creates inconsistency. | Create new phase for additional work |
| **Change task ID** | ❌ No | IDs are stable references in commits/discussions. Changing breaks references. | Never renumber task IDs |

## Allowed Operation Patterns

### Add Tasks to Incomplete Phase

```markdown
## Phase 2: Ranking (IN PROGRESS)
- [x] [P2.1] Implement TF-IDF scoring
- [x] [P2.2] Add document ranking
- [ ] [P2.3] Add caching layer         ← NEW (sequential ID)
- [ ] [P2.4] Write caching tests       ← NEW
```

### Add New Phase

```markdown
## Phase 4: Caching Optimization

**Goal:** Improve query performance with caching
**Deliverable:** LRU cache with 1000 entry limit

**Tasks:**
- [ ] [P4.1] Create cache.py
- [ ] [P4.2] Integrate with QueryRanker
- [ ] [P4.3] Add cache tests

**Phase 4 Checkpoint:** Cache operational, performance improved
```

### Modify Incomplete Task

```markdown
- [ ] [P2.3] Write tests
- [ ] [P2.3] Write unit tests in test_ranker.py  ← Description updated, ID preserved
```

### Update Plan Section

```markdown
## Technical Approach

### Caching Strategy  ← NEW SUBSECTION
- LRU cache, 1000 entry limit
- Cache key: query hash
- Invalidate on index update
```

## Before Amending

**Verify:**

- [ ] Task/phase to modify is incomplete (has `[ ]` tasks)
- [ ] Not changing any task IDs
- [ ] Not modifying completed tasks `[x]`
- [ ] New tasks use sequential IDs

**When to amend:** Requirements change, new constraints discovered, additional work needed in incomplete phases.

**When NOT to amend:** Never modify completed work—create new phases instead.

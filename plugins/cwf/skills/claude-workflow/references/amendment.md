# Amendment Reference

Safety rules for modifying CWF specs and state documents during implementation.

## Core Principle

**Completed work is immutable.** Tasks marked `[x]` represent implemented code and form a trusted implementation history. Changing completed work breaks trust in the state document as source of truth and creates confusion about what was actually built. This immutability enables reliable progress tracking, troubleshooting, and context preservation across sessions.

## Amendment Operations

| Operation | Allowed? | Rules | Example |
|-----------|----------|-------|---------|
| **Add task to incomplete phase** | Yes | Phase must have at least one `[ ]` task. | Add `**SearchCache**` to Phase 2 (has incomplete tasks) |
| **Add new phase** | Yes | Use next phase number. Include Goal, Deliverable, Tasks, Checkpoints. All tasks start `[ ]`. | Create Phase 4 after Phase 3 |
| **Modify incomplete task description** | Yes | Only `[ ]` tasks. Preserve name and checkbox, update description only. | Change `[ ] **SearchCache** — Basic cache` to `[ ] **SearchCache** — LRU cache with 1000 entry limit` |
| **Update spec sections** | Yes | Add subsections, clarify decisions, document new constraints. | Add "Caching Strategy" subsection to Technical Specification |
| **Modify completed task** | No | Code already built. Changing description misrepresents implementation. | Use new task/phase to modify implementation instead |
| **Add task to completed phase** | No | All tasks `[x]` means phase done. Adding creates inconsistency. | Create new phase for additional work |
| **Change completed task ID** | No | Task IDs are stable references. Changing breaks cross-references. | Never change `[PX.Y]` on completed tasks |
| **Rename completed task** | No | Names are stable references in state and spec. Changing breaks references. | Never rename completed task names |

## Allowed Operation Patterns

### Add Task to Incomplete Phase

```markdown
## Phase 2: API and Caching (IN PROGRESS)
- [x] [P2.1] **SearchAPI** — HTTP endpoint with pagination
- [x] [P2.2] **QueryParser** — Add query validation
- [ ] [P2.3] **SearchCache** — LRU cache for frequent queries        ← NEW
- [ ] [P2.4] **CacheInvalidation** — Invalidate cache on index update ← NEW
```

### Add New Phase

```markdown
## Phase 4: Caching Optimization

**Goal:** Improve query performance with intelligent caching

**Deliverable:** LRU cache with 1000 entry limit and cache invalidation

**Tasks:**
- [ ] [P4.1] **SearchCache** — Implement LRU eviction with configurable size
- [ ] [P4.2] **CacheMetrics** — Track hit rates and eviction patterns

**Checkpoints:**
- [ ] Code quality: `ruff check src/`
- [ ] Self-review: Verify cache improves response times

**Phase 4 Complete:** Cache operational, search response times under 50ms for cached queries.
```

### Modify Incomplete Task

```markdown
- [ ] [P2.3] **SearchCache** — Basic cache
- [ ] [P2.3] **SearchCache** — LRU cache with 1000 entry limit  ← Description updated, name/ID preserved
```

### Update Spec Section

```markdown
## Technical Specification

### Caching Strategy  ← NEW SUBSECTION
- LRU cache, 1000 entry limit
- Cache key: query hash
- Invalidate on index update
```

## Before Amending

**Verify:**

- [ ] Task/phase to modify is incomplete (has `[ ]` tasks)
- [ ] Not changing any task IDs on completed tasks
- [ ] Not renaming any completed tasks
- [ ] Not modifying completed tasks `[x]`

**When to amend:** Requirements change, new constraints discovered, additional work needed in incomplete phases.

**When NOT to amend:** Never modify completed work — create new phases instead.

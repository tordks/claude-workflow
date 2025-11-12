# Tasklist Document Structure

The tasklist document provides step-by-step execution guidance (WHEN and HOW).

## Tasklist Header

Include this at the top of every tasklist:

```markdown
> **Using This Tasklist**
> - Each task is designed to take 15-30 minutes
> - Complete all tasks in a phase before moving to the next
> - Code must be runnable after each phase
> - Refer to `{feature-name}-plan.md` for architectural context
```

## Phase Structure

Every phase follows this exact structure:

```markdown
## Phase X: Descriptive Name

**Goal:** One-sentence description of what this phase accomplishes

**Deliverable:** Concrete outcome (e.g., "Working data models with validation passing tests")

**Tasks:**
- [ ] [PX.1] Specific atomic action - file/component detail
- [ ] [PX.2] Another specific action with clear scope
- [ ] [PX.3] Write tests for implemented functionality
- [ ] [PX.4] Verify tests pass and code quality checks succeed

**Phase X Checkpoint:** Brief description of system state after phase completion
```

## Phase 0 Special Case

**Phase 0 is ALWAYS branch setup only:**

```markdown
## Phase 0: Branch Setup

**Goal:** Create feature branch

**Deliverable:** New git branch ready for commits

**Tasks:**
- [ ] [P0.1] Create branch using: `git checkout -b {prefix}-{feature-name}`

**Phase 0 Checkpoint:** Feature branch created, ready for implementation
```

**Requirements:**
- Always exactly one task
- Always branch creation with git command
- Branch name follows format: `{prefix}-{feature-name}` (see conventions.md)
- Must complete before Phase 1

## Task Granularity Guidelines

**Every task must meet these criteria:**

**Time:** 15-30 minutes to complete
- Too small: Overhead of context switching
- Too large: Hard to track progress, risky to complete

**Atomic:** Complete in one go without interruption
- Can be done start to finish
- Natural unit of work
- Single logical change

**Testable:** Can verify completion
- Has clear done criteria
- Observable output or behavior
- Can be tested/validated

**File-specific:** References concrete files or components
- Mentions specific file names (e.g., "in parser.py")
- Identifies specific components (e.g., "QueryParser class")
- Clear scope boundaries

**Examples:**

✅ **Good tasks:**
- `[P1.1] Create query/ directory and __init__.py`
- `[P1.2] Create QueryModel class with Pydantic in models.py`
- `[P1.3] Add field validation to QueryModel (required fields, type checks)`
- `[P1.4] Write unit tests for QueryModel validation in test_models.py`

❌ **Too vague:**
- `[P1.1] Set up module`
- `[P1.2] Add query stuff`

❌ **Too large:**
- `[P1.1] Implement entire query system with models, parser, and ranking`

❌ **Not file-specific:**
- `[P1.1] Create data models`
- `[P1.2] Add validation`

## Task Ordering Principles

**Standard task flow within a phase:**

1. **Setup** - Create files, directories, boilerplate
2. **Implementation** - Write core functionality
3. **Testing** - Write tests for implemented code
4. **Validation** - Verify tests pass, run quality checks

**Dependency rule:** Tasks that depend on others come AFTER

**Example of good ordering:**
```markdown
- [ ] [P2.1] Create ranker.py with RankerClass stub
- [ ] [P2.2] Implement TF-IDF scoring in RankerClass.score()
- [ ] [P2.3] Add document ranking in RankerClass.rank()
- [ ] [P2.4] Write unit tests for TF-IDF scoring in test_ranker.py
- [ ] [P2.5] Write unit tests for document ranking in test_ranker.py
- [ ] [P2.6] Verify all tests pass: pytest tests/query/test_ranker.py
```

**Why this order:**
- P2.1 creates file (dependency for P2.2, P2.3)
- P2.2 implements scoring (dependency for P2.3)
- P2.3 uses scoring (dependency for P2.4, P2.5)
- P2.4, P2.5 test implementation (dependency for P2.6)
- P2.6 validates everything works

## Task ID Format

**Structure:** `[PX.Y]`
- **P:** Prefix indicating "Phase"
- **X:** Phase number (0, 1, 2, 3...)
- **Y:** Task number within phase (1, 2, 3...)

**Rules:**
- Phase 0 is always setup
- Task numbering starts at 1 within each phase (NOT 0)
- Sequential numbering within phases (no gaps)
- IDs are immutable once created
- Never reuse or skip IDs

**Checkbox Format:**
```markdown
- [ ] [P2.3] Incomplete task description
- [x] [P2.3] Completed task description
```

**Example Sequence:**
```markdown
## Phase 0: Branch Setup
- [ ] [P0.1] Create feature branch feat-query-command

## Phase 1: Foundation
- [x] [P1.1] Create query/ directory and __init__.py
- [x] [P1.2] Create QueryModel class with Pydantic
- [ ] [P1.3] Add validation to QueryModel
- [ ] [P1.4] Write unit tests for QueryModel
```

## Checkpoint Format

**Every phase ends with a checkpoint describing system state.**

**Format:** 1-2 sentences answering:
- What capabilities now exist?
- What's ready for the next phase?
- What validation has been completed?

**Examples:**

✅ **Good checkpoints:**
- "Core data models validated, ready for parser implementation"
- "Query parser complete with DSL support, validated against test cases"
- "End-to-end query flow working with TF-IDF ranking, ready for optimization"

❌ **Too vague:**
- "Phase complete"
- "All done"

❌ **Lists tasks instead of state:**
- "Implemented models, parser, and tests successfully"
- "Created files and ran tests"

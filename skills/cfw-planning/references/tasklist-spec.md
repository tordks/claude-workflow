# Tasklist Document Specification

Specification for creating conformant tasklist documents in the CWF planning system.

> **Note (Informative):** See `SKILL.md` for conformance levels and RFC 2119 keyword definitions.

---

## What is a Tasklist Document?

The tasklist document provides **step-by-step execution guidance** (WHEN and HOW). It breaks down the feature into phases and concrete, actionable tasks that implementers can execute sequentially.

**Plan = WHY/WHAT** | **Tasklist = WHEN/HOW**

---

## Document Header Structure

Every tasklist document MUST start with YAML frontmatter and a usage header to make it self-contained.

### YAML Frontmatter Template

```yaml
---
feature: {feature-name}
plan_file: plans/{feature-name}-plan.md
tasklist_file: plans/{feature-name}-tasklist.md
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

**Field descriptions:**
- `feature`: The feature name (e.g., `query-command`)
- `plan_file`: Path to companion plan document
- `tasklist_file`: Path to this tasklist document
- `created`: Date when tasklist was created (YYYY-MM-DD format)
- `last_updated`: Date of last amendment (same as created initially)

### Usage Header Template

After the frontmatter and title, implementations MUST include a usage blockquote:

```markdown
# {Feature Name} - Implementation Tasklist

> **How to Use This Tasklist**
>
> **Purpose:** This tasklist provides step-by-step execution tasks (WHEN/HOW) for the `{feature-name}` feature.
>
> **Before starting:**
> 1. **Read `plans/{feature-name}-plan.md` FIRST** for full architectural context
> 2. Understand WHY decisions were made, HOW components relate
> 3. Then come to this tasklist for concrete execution steps
>
> **During implementation:**
> - Execute tasks in order: implement → test → mark `[x]` → next
> - Stop at phase boundaries (all phase tasks complete) for review
> - **Refer back to plan** when tasks need clarification
> - Code MUST be runnable after each phase
>
> **Task unclear?**
> 1. Check relevant sections in the plan document first
> 2. Still unclear? Use AskUserQuestion tool with:
>    - Task ID ([PX.Y])
>    - What's unclear
>    - Which plan sections you checked
>    - Recommended approach (if any)
>
> **Task IDs:** `[PX.Y]` = Phase X, Task Y (e.g., [P2.3] = Phase 2, Task 3)
>
> **Related documents:**
> - **Plan:** `plans/{feature-name}-plan.md` - Architectural context (WHY/WHAT)
```

**Rationale (Informative):**
- Makes tasklist self-documenting - readable without running `/implement-plan` command
- Provides clear cross-reference to plan document
- Explains escalation path when tasks are unclear
- Documents the complete implementation workflow inline

---

> **CRITICAL**: Every tasklist document MUST start with YAML frontmatter and usage header (see "Document Header Structure" above) before any phases or tasks.

## Required Syntax

Every task in the tasklist MUST follow this exact markdown format:

```markdown
- [ ] [PX.Y] Task description with file/component specifics
```

**Required elements:**
- **Checkbox:** `- [ ]` for incomplete tasks, `- [x]` for completed tasks
- **Task ID:** `[PX.Y]` format where P = Phase, X = phase number, Y = task number
- **Description:** Clear, file-specific action statement

**Critical:** Tasks MUST NOT use markdown headings (`###`). Tasks MUST be checkboxes for tracking.

**Example (Informative):**
```markdown
## Phase 1: Foundation

- [ ] [P1.1] Create query/ directory and __init__.py
- [ ] [P1.2] Create QueryModel class with Pydantic in models.py
- [x] [P1.3] Add field validation to QueryModel (required fields, type checks)
```

---

## Phase Structure

Every phase MUST follow this standard structure:

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

**Required Components:**

Each phase MUST include:
- **Header:** `## Phase X: Descriptive Name`
- **Goal:** One-sentence description of what this phase accomplishes
- **Deliverable:** Concrete outcome statement
- **Tasks:** List of tasks with `[PX.Y]` format IDs
- **Checkpoint:** Description of system state after completion

---

## Task Granularity Guidelines

> **CRITICAL**: All tasks MUST use checkbox format (`- [ ]` or `- [x]`). Tasks MUST NOT use markdown headings (`###`).

### Requirements

Tasks SHOULD meet these quality criteria:

- **Time:** Tasks SHOULD take 5-10 minutes to complete
- **Atomic:** Tasks SHOULD be completable in one go without interruption (single logical change)
- **Testable:** Tasks SHOULD have clear done criteria (observable output or verifiable behavior)
- **File-specific:** Tasks SHOULD reference concrete files or components

**Note (Informative):** These are guidelines for effective task breakdown. Real-world tasks MAY occasionally deviate based on feature complexity and context.

### Rationale (Informative)

Why these criteria matter:

- **Time (5-10 min):** Tasks that are too small create context-switching overhead. Tasks that are too large are hard to track progress and risky to complete without interruption.
- **Atomic:** Natural units of work that can be done start to finish create clear progress markers and reduce the risk of partially-complete states.
- **Testable:** Clear done criteria enable validation and ensure tasks have measurable completion states.
- **File-specific:** Mentioning specific files (e.g., "in parser.py") or components (e.g., "QueryParser class") provides clear scope boundaries and makes tasks actionable.

### Examples (Informative)

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

---

## Task Ordering Principles

### Requirements

Tasks that depend on others MUST be ordered after their dependencies.

### Typical Task Flow (Informative)

This is a common pattern for task ordering, though teams MAY adapt based on their approach:

1. **Setup** - Create files, directories, boilerplate
2. **Implementation** - Write core functionality
3. **Testing** - Write tests for implemented code
4. **Validation** - Verify tests pass, run quality checks

**Note (Informative):** Adapt for your approach (e.g., TDD reverses implementation and testing, some teams validate continuously, tracer bullets write one functional solution and then incremental improvements). The key is logical dependency ordering.

**Example of good ordering (Informative):**
```markdown
- [ ] [P2.1] Create ranker.py with RankerClass stub
- [ ] [P2.2] Implement TF-IDF scoring in RankerClass.score()
- [ ] [P2.3] Add document ranking in RankerClass.rank()
- [ ] [P2.4] Write unit tests for TF-IDF scoring in test_ranker.py
- [ ] [P2.5] Write unit tests for document ranking in test_ranker.py
- [ ] [P2.6] Verify all tests pass: pytest tests/query/test_ranker.py
```

**Why this order (Informative):**
- P2.1 creates file (dependency for P2.2, P2.3)
- P2.2 implements scoring (dependency for P2.3)
- P2.3 uses scoring (dependency for P2.4, P2.5)
- P2.4, P2.5 test implementation (dependency for P2.6)
- P2.6 validates everything works

---

## Task ID Format

**Structure:** `[PX.Y]` where tasks MUST use checkbox format

**ID Components:**
- **P:** Prefix indicating "Phase"
- **X:** Phase number (0, 1, 2, 3...)
- **Y:** Task number within phase (1, 2, 3...)

**Rules:**
- Task numbering MUST start at 1 within each phase
- Numbering MUST be sequential within phases (no gaps)
- IDs MUST NOT be reused or skipped

**Required Checkbox Format:**
```markdown
- [ ] [PX.Y] Task description for incomplete task
- [x] [PX.Y] Task description for completed task
```

> **CRITICAL**: Tasks MUST use checkboxes (`- [ ]` or `- [x]`). Tasks MUST NOT use markdown headings (`###`).

**Example (Informative):**
```markdown
## Phase 1: Foundation
- [x] [P1.1] Create query/ directory and __init__.py
- [x] [P1.2] Create QueryModel class with Pydantic
- [ ] [P1.3] Add validation to QueryModel
- [ ] [P1.4] Write unit tests for QueryModel
```

---

## Checkpoint Format

### Requirements

Every phase MUST end with a checkpoint describing system state.

Checkpoints SHOULD be 1-2 sentences answering:
- What capabilities now exist?
- What's ready for the next phase?
- What validation has been completed?

### Examples (Informative)

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

---

## Validation Requirements

Before finalizing your tasklist document, it MUST satisfy these conformance requirements:

### Level 1 Requirements (MUST)

**Document Header:**
- YAML frontmatter MUST be present with all REQUIRED fields
- Usage header MUST be present after title

**Required Syntax (CRITICAL):**
- Every task MUST use checkbox format: `- [ ]` or `- [x]`
- Tasks MUST NOT use markdown headings (`###`) for tasks
- Every task MUST have `[PX.Y]` format ID in brackets
- Task details (if any) MUST be indented 2 spaces under checkbox

**Phase Structure (all phases):**
- Header format MUST be: `## Phase X: Descriptive Name`
- Goal MUST be present (one-sentence description)
- Deliverable MUST be present (concrete outcome statement)
- Tasks MUST be checkbox list with `[PX.Y]` format IDs
- Checkpoint MUST be present (system state after completion)

**Task IDs:**
- Pattern MUST be `[PX.Y]` where P = Phase prefix
- Phase number (X) MUST be 0, 1, 2, 3...
- Task number (Y) MUST start at 1 (NOT 0)
- Numbering MUST be sequential within phase (no gaps)
- Task IDs MUST NOT skip numbers within a phase
- Task IDs MUST NOT be reused after completion

### Level 2 Requirements (SHOULD)

**Task Granularity:**
- Tasks SHOULD take 5-10 minutes each
- Tasks SHOULD be atomic (complete in one go)
- Tasks SHOULD be testable (can verify completion)
- Tasks SHOULD be file-specific (reference concrete files or components)

**Task Ordering:**
- Dependencies SHOULD come first

**Typical flow (Informative):** Setup → Implementation → Testing → Validation

### Checkpoint Quality
Checkpoints SHOULD be 1-2 sentences that describe system capabilities and state, not just a list of tasks completed.

### Content Focus
Tasklists MUST contain execution steps (WHEN/HOW).

Tasklists MUST NOT contain architectural rationale.

Tasklists MUST NOT contain design alternatives or lengthy context.

### Prohibited Patterns

The following patterns MUST NOT appear in conformant tasklist documents:

**Task Format Violations:**
- Tasks MUST NOT use markdown headings (`###`) instead of checkboxes
- Tasks MUST NOT omit task IDs in `[PX.Y]` format
- Task IDs MUST NOT skip numbers within a phase
- Task IDs MUST NOT be reused after completion

**Content Violations:**
- Tasklists MUST NOT contain architectural rationale (belongs in plan)
- Tasklists MUST NOT contain design alternatives (belongs in plan)
- Tasklists MUST NOT contain lengthy contextual explanations (belongs in plan)
- Tasks MUST NOT be vague without file/component specificity

**Structure Violations:**
- Phases MUST NOT omit required components (Goal, Deliverable, Tasks, Checkpoint)
- Checkpoints MUST NOT simply list completed tasks without describing system state


---

## Common Mistakes to Avoid

**The following best practices (Informative) help avoid common mistakes:**

### ❌ Using Headings Instead of Checkboxes

**Bad - Using markdown headings:**
```markdown
### Task 1.1: Create output_utils.py module

**ID**: `sim-out-1.1`

**Description**: Create new module...
```

**Good - Using checkbox format:**
```markdown
- [ ] [P1.1] Create output_utils.py module with utility functions
```

> **CRITICAL**: Tasks MUST use checkbox format (`- [ ]`), NOT markdown headings (`###`). Checkboxes enable progress tracking.

### ❌ Missing Task IDs

**Bad - No task ID:**
```markdown
- [ ] Create utilities module
- [ ] Add validation
```

**Good - Task IDs present:**
```markdown
- [ ] [P1.1] Create utilities module in utils.py
- [ ] [P1.2] Add field validation to QueryModel in models.py
```

### ❌ Mixing architectural rationale into tasklist

**Bad:**
- Tasklist contains WHY decisions were made
- Long explanations of alternatives considered

**Good:**
- Tasklist says WHAT to do and WHEN
- Move rationale to plan document

### ❌ Tasks without file/component specificity

**Bad:**
- "Add validation"
- "Set up module"

**Good:**
- "Add field validation to QueryModel in models.py"
- "Create query/ directory and __init__.py"

### ❌ Tasks too large (>10 minutes)

**Bad:**
- Tasks that take 30+ minutes
- Multiple unrelated actions in one task

**Good:**
- Break down into 5-10 minute atomic tasks
- Each task completable in one sitting

### ❌ Missing checkpoints

**Bad:**
- Phase ends without checkpoint
- Checkpoint just lists completed tasks

**Good:**
- Every phase ends with checkpoint
- Checkpoint describes system state and capabilities

### ❌ Vague task descriptions

**Bad:**
- "Set up module" → Too vague
- "Add stuff" → No specifics

**Good:**
- "Create query/ directory and __init__.py" → Clear and specific
- "Add field validation to QueryModel (required fields, type checks)" → Detailed scope

---

## Conformance by Feature Complexity

Features SHOULD select the appropriate conformance level based on their complexity:

**Simple features** (bug fixes, small utilities) → **Level 1 (Minimal)**:
- Fewer phases (typically 2-3 total including Phase 0)
- MUST satisfy Level 1 syntax requirements
- MAY have simpler tasks (2-3 tasks per phase)
- Checkpoints MAY be brief

**Medium features** (new components) → **Level 2 (Standard)**:
- Moderate phases (typically 3-5 total including Phase 0)
- MUST satisfy Level 1 requirements
- SHOULD satisfy Level 2 requirements (task granularity, ordering)
- SHOULD have standard task breakdown (3-6 tasks per phase)
- Checkpoints SHOULD clearly describe system state

**Complex features** (major systems) → **Level 3 (Comprehensive)**:
- More phases (typically 5-8 total including Phase 0)
- MUST satisfy Level 1 and Level 2 requirements
- SHOULD have detailed task breakdown (4-8 tasks per phase)
- Checkpoints MUST be comprehensive with validation details

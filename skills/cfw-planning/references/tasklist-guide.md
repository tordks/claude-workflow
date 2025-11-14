# Tasklist Document Guide

Complete guide for creating high-quality tasklist documents in the CWF planning system.

## What is a Tasklist Document?

The tasklist document provides **step-by-step execution guidance** (WHEN and HOW). It breaks down the feature into phases and concrete, actionable tasks that implementers can execute sequentially.

**Plan = WHY/WHAT** | **Tasklist = WHEN/HOW**

---

## Document Header Structure

Every tasklist document must start with YAML frontmatter and a usage header to make it self-contained.

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

After the frontmatter and title, include a usage blockquote:

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
> - Code must be runnable after each phase
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

**Why this header?**
- Makes tasklist self-documenting - readable without running `/implement-plan` command
- Provides clear cross-reference to plan document
- Explains escalation path when tasks are unclear
- Documents the complete implementation workflow inline

---

## Required Syntax

Every task in the tasklist MUST follow this exact markdown format:

```markdown
- [ ] [PX.Y] Task description with file/component specifics
```

**Required elements:**
- **Checkbox:** `- [ ]` for incomplete tasks, `- [x]` for completed tasks
- **Task ID:** `[PX.Y]` format where P = Phase, X = phase number, Y = task number
- **Description:** Clear, file-specific action statement

**Critical:** Do NOT use markdown headings (`###`) for tasks. Tasks must be checkboxes for tracking.

**Example:**
```markdown
## Phase 1: Foundation

- [ ] [P1.1] Create query/ directory and __init__.py
- [ ] [P1.2] Create QueryModel class with Pydantic in models.py
- [x] [P1.3] Add field validation to QueryModel (required fields, type checks)
```

---

## Phase Structure

Every phase should follow this standard structure:

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
- **Header:** `## Phase X: Descriptive Name`
- **Goal:** One-sentence description
- **Deliverable:** Concrete outcome
- **Tasks:** List of `[PX.Y]` tasks
- **Checkpoint:** System state after completion

---

## Task Granularity Guidelines

> **CRITICAL**: All tasks must use checkbox format (`- [ ]` or `- [x]`). Never use markdown headings (`###`) for tasks.

Tasks should aim to meet these criteria:

### Time: 5-10 minutes to complete
- Too small: Overhead of context switching
- Too large: Hard to track progress, risky to complete

### Atomic: Complete in one go without interruption
- Can be done start to finish
- Natural unit of work
- Single logical change

### Testable: Can verify completion
- Has clear done criteria
- Observable output or behavior
- Can be tested/validated

### File-specific: References concrete files or components
- Mentions specific file names (e.g., "in parser.py")
- Identifies specific components (e.g., "QueryParser class")
- Clear scope boundaries

**Note:** These are guidelines for effective task breakdown. Real-world tasks may occasionally deviate based on feature complexity and context.

### Examples

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

**Common task flow within a phase:**

1. **Setup** - Create files, directories, boilerplate
2. **Implementation** - Write core functionality
3. **Testing** - Write tests for implemented code
4. **Validation** - Verify tests pass, run quality checks

**Note:** This is a typical pattern. Adapt for your approach (e.g., TDD reverses implementation and testing, some teams validate continuously, tracer bullets write one functional solution and then inrcemental improvements). The key is logical dependency ordering.

### Dependency Rule

Tasks that depend on others come AFTER.

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

---

## Task ID Format

**Structure:** `[PX.Y]` where tasks MUST use checkbox format

**ID Components:**
- **P:** Prefix indicating "Phase"
- **X:** Phase number (0, 1, 2, 3...)
- **Y:** Task number within phase (1, 2, 3...)

**Rules:**
- Task numbering starts at 1 within each phase
- Sequential numbering within phases (no gaps)
- Never reuse or skip IDs

**Required Checkbox Format:**
```markdown
- [ ] [PX.Y] Task description for incomplete task
- [x] [PX.Y] Task description for completed task
```

> **CRITICAL**: Tasks must use checkboxes (`- [ ]` or `- [x]`). Never use markdown headings (`###`) for tasks.

**Example:**
```markdown
## Phase 1: Foundation
- [x] [P1.1] Create query/ directory and __init__.py
- [x] [P1.2] Create QueryModel class with Pydantic
- [ ] [P1.3] Add validation to QueryModel
- [ ] [P1.4] Write unit tests for QueryModel
```

---

## Checkpoint Format

Every phase ends with a checkpoint describing system state.

**Format:** 1-2 sentences answering:
- What capabilities now exist?
- What's ready for the next phase?
- What validation has been completed?

### Examples

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

## Tasklist Validation Checklist

Before finalizing your tasklist document, validate against these criteria:

### Document Header
✅ **YAML frontmatter present** with all required fields

✅ **Usage header present** after title with required fields

### Required Syntax (CRITICAL)
✅ **Every task uses checkbox format:** `- [ ]` or `- [x]`

✅ **NO markdown headings for tasks:** Never use `###` for tasks

✅ **Task IDs in brackets:** Every task has `[PX.Y]` format ID

✅ **Proper indentation:** Task details (if any) indented 2 spaces under checkbox

### Phase Structure (all phases)
✅ **Header format:** `## Phase X: Descriptive Name`

✅ **Goal:** One-sentence description

✅ **Deliverable:** Concrete outcome statement

✅ **Tasks:** Checkbox list of `[PX.Y]` format tasks

✅ **Checkpoint:** System state after completion

### Task IDs
✅ **Pattern:** `[PX.Y]` where P = Phase prefix

✅ **Phase number (X):** 0, 1, 2, 3...

✅ **Task number (Y):** Starts at 1, NOT 0

✅ **Sequential within phase:** No gaps in numbering

✅ **Examples:** `[P1.1]`, `[P1.2]`, `[P2.1]`

### Task Granularity
✅ **Time:** 5-10 minutes each

✅ **Atomic:** Complete in one go

✅ **Testable:** Can verify completion

✅ **File-specific:** References concrete files or components

### Task Ordering
✅ **Dependencies come first**

✅ **Common flow:** Setup → Implementation → Testing → Validation

✅ **Logical flow within phase**

### Checkpoint Quality
✅ **1-2 sentences**

✅ **Describes system capabilities and state**

✅ **Not just list of tasks completed**

### Content Focus
✅ **Contains execution steps** (WHEN/HOW)

✅ **Does NOT contain architectural rationale**

✅ **Does NOT contain design alternatives or lengthy context**


---

## Common Mistakes to Avoid

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

> **CRITICAL**: Tasks must use checkbox format (`- [ ]`), NOT markdown headings (`###`). Checkboxes enable progress tracking.

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

## Adapting to Feature Complexity

**Simple features** (bug fixes, small utilities):
- Fewer phases (maybe 2-3 total including Phase 0)
- Simpler tasks (may have 2-3 tasks per phase)
- Brief checkpoints

**Medium features** (new components):
- Moderate phases (3-5 total including Phase 0)
- Standard task breakdown (3-6 tasks per phase)
- Clear checkpoints describing system state

**Complex features** (major systems):
- More phases (5-8 total including Phase 0)
- Detailed task breakdown (4-8 tasks per phase)
- Comprehensive checkpoints with validation details

The validation checklist represents comprehensive validation. Adapt the level of detail to your feature's complexity while maintaining the core structure.

# Tasklist Document Specification

Specification for creating conformant tasklist documents in CWF.

---

## What is a Tasklist Document?

Tasklist documents provide **step-by-step execution guidance**. They break features into phases and concrete, actionable tasks that implementers execute sequentially.

Plan = WHY/WHAT | **Tasklist = WHEN/HOW**

---

## Conformance

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

> **Note:** See `SKILL.md` for conformance levels (1-3) tailoring documentation depth.

---

## Task Syntax

Every task in the tasklist MUST follow this markdown format:

```markdown
- [ ] [PX.Y] Task description with file/component specifics
```

**Task ID Format:** `[PX.Y]` where P = "Phase", X = phase number, Y = task number within phase

**Requirements:**

- Tasks MUST use checkboxes: `- [ ]` for incomplete, `- [x]` for completed
- Task numbering MUST start at 1 within each phase
- Numbering MUST be sequential within phases (no gaps)
- Task IDs MUST NOT be reused or skipped
- Tasks MUST NOT use markdown headings (`###`)
- Descriptions MUST specify the file or component being modified
- Tasks MAY provide task-critical information in bulletpoints

**Example (Informative):**

```markdown
- [x] [P1.1] Create query/ directory and __init__.py
- [x] [P1.2] Create QueryModel class with Pydantic in models.py
- [ ] [P1.3] Add validation to QueryModel (required fields, type checks)
- [ ] [P1.4] Write unit tests for QueryModel validation in test_models.py
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
- [ ] [PX.4] Run tests: pytest tests/module/

**Checkpoints:**
- [ ] Code quality: Run `ruff check src/`
- [ ] Code complexity: Run `ruff check src/ --select C901`
- [ ] Review: Self review implementation and verify phase deliverable achieved

**Phase X Complete:** Brief description of system state after phase completion
```

---

## Checkpoint Requirements

Checkpoints are end-of-phase validation operations performed after all tasks in a phase are complete.

**Requirements:**

- Checkpoints MUST use checkbox format: `- [ ] Checkpoint description`
- Additional checkpoints SHOULD be project-specific validation or quality operations
- Checkpoints MUST NOT duplicate functional test tasks (tests belong in Tasks section)
- Checkpoint commands SHOULD be concrete and executable (e.g., `ruff check src/`)

**Common Checkpoint Types:**

- **Self-review:** Agent reviews implementation against deliverable
- **Code quality:** Linting, formatting, type checking (e.g., ruff, black, mypy)
- **Code complexity:** Complexity analysis (e.g., radon cc)

**Note (Informative):** Use only tools your project already has. Checkpoints provide quality control for AI-driven development.

---

## Task Granularity Guidelines

Tasks SHOULD meet these quality criteria:

- **Time:** 5-20 minutes to complete
- **Atomic:** Completable in one go without interruption (single logical change)
- **Testable:** Clear done criteria (observable output or verifiable behavior)
- **File-specific:** Reference concrete files or components

**Example (Informative):**

```markdown
- [P1.1] Create query/ directory and __init__.py
- [P1.2] Create QueryModel class with Pydantic in models.py
- [P1.3] Add field validation to QueryModel (required fields, type checks)
- [P1.4] Write unit tests for QueryModel validation in test_models.py
```

---

## Task Ordering Principles

Tasks that depend on others MUST be ordered after their dependencies.

**Example (Informative):**

```markdown
- [ ] [P2.1] Create ranker.py with RankerClass stub
- [ ] [P2.2] Implement TF-IDF scoring in RankerClass.score()
- [ ] [P2.3] Add document ranking in RankerClass.rank()
- [ ] [P2.4] Write unit tests for TF-IDF scoring in test_ranker.py
- [ ] [P2.5] Write unit tests for document ranking in test_ranker.py
- [ ] [P2.6] Verify all tests pass: pytest tests/query/test_ranker.py
```

---

## Phase Complete Statement

Every phase MUST end with a "Phase X Complete" statement describing system state after phase completion.

The statement SHOULD be 1-3 sentences describing what capabilities now exist, what's ready for the next phase, and what validation has been completed.

**Example (Informative):**

- "Core data models validated, ready for parser implementation"
- "Query parser complete with DSL support, validated against test cases"
- "End-to-end query flow working with TF-IDF ranking, ready for optimization"

---

## Validation

Tasklists are conformant when they:

- Include required elements in every phase (Goal, Deliverable, Tasks, Checkpoints, Phase Complete)
- Use correct task ID format `[PX.Y]` with checkboxes
- Specify concrete files/components in task descriptions
- Order tasks after their dependencies
- Use checkpoints for quality/validation (not functional tests)
- Contain no architectural rationale or design alternatives (belongs in plan)

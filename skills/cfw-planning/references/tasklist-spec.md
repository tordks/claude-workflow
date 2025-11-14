# Tasklist Document Specification

Specification for creating conformant tasklist documents in CWF.

---

## What is a Tasklist Document?

The tasklist document provides **step-by-step execution guidance** (WHEN and HOW). It breaks down the feature into phases and concrete, actionable tasks that implementers can execute sequentially.

Plan = WHY/WHAT | **Tasklist = WHEN/HOW**

---

## Conformance

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

> **Note:** See `SKILL.md` for conformance level definitions and RFC 2119 keyword explanations.

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
- [ ] [PX.4] Verify tests pass and code quality checks succeed

**Phase X Checkpoint:** Brief description of system state after phase completion
```


---

## Task Granularity Guidelines

Tasks SHOULD meet these quality criteria:

- **Time:** Tasks SHOULD take 5-20 minutes to complete
- **Atomic:** Tasks SHOULD be completable in one go without interruption (single logical change)
- **Testable:** Tasks SHOULD have clear done criteria (observable output or verifiable behavior)
- **File-specific:** Tasks SHOULD reference concrete files or components

**Note (Informative):** These are guidelines for effective task breakdown. Real-world tasks MAY occasionally deviate based on feature complexity and context.

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

## Checkpoint Format

Every phase MUST end with a checkpoint describing system state.

Checkpoints SHOULD be 1-3 sentences describing what capabilities now exist, what's ready for the next phase, and what validation has been completed.

**Example (Informative):**
- "Core data models validated, ready for parser implementation"
- "Query parser complete with DSL support, validated against test cases"
- "End-to-end query flow working with TF-IDF ranking, ready for optimization"

---

## Validation Checklist

- [ ] Task IDs follow `[PX.Y]` pattern with checkboxes (`- [ ]` or `- [x]`)
- [ ] No tasks use markdown headings (`###`)
- [ ] Every phase has: Header, Goal, Deliverable, Tasks, Checkpoint
- [ ] Tasks reference specific files/components (no vague tasks)
- [ ] Tasks are atomic, testable, and take 5-20 minutes
- [ ] Dependencies ordered before dependent tasks
- [ ] No architectural rationale or design alternatives (belongs in plan)

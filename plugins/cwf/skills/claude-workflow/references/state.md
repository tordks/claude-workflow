# State Document Specification

Specification for creating conformant state documents in CWF.

---

## What is a State Document?

State documents provide **phase-structured execution guidance**. They break features into phases with named tasks that track implementation progress at the module/service level.

Spec = WHY/WHAT | **State = WHEN/HOW**

---

## Conformance

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

---

## Task Syntax

Every task in the state document MUST follow this markdown format:

```markdown
- [ ] [PX.Y] **Task name** — What this task delivers
```

Where `P` is a literal prefix, `X` is the phase number, and `Y` is the task number within that phase.

**Requirements:**

- Tasks MUST use checkboxes: `- [ ]` for incomplete, `- [x]` for completed
- Tasks MUST include a task ID in `[PX.Y]` format before the bold name
- Task IDs MUST be sequential within each phase (no gaps, no reuse)
- Task names MUST be bold: `**Task name**`
- Task names MUST be short noun phrases identifying the component or capability
- Names MUST be separated from descriptions by an em dash (` — `)
- Descriptions SHOULD state what the task concretely delivers, not restate the name
- Tasks SHOULD each represent one component — a module, service, or feature boundary (not file operations, not entire features)
- Tasks MUST NOT use markdown headings (`###`)
- The same task name MAY appear in multiple phases with different descriptions
- Agent MAY add discovered tasks during implementation (using the next sequential ID)

**Task Granularity (Informative):**

Each task should represent one component — a module, service, or feature boundary. Ask: "does this task have a clear before/after in the system?"

- Too coarse: `**Entire search feature**` — multiple components lumped together
- Right level: `**Search cache**` — one component with clear responsibility
- Too fine: `**Cache imports**` — a file operation, not a deliverable

**Agent Notes:**

Agent notes MAY be added as single-line blockquotes directly under a task. These preserve cross-session context about implementation decisions, discoveries, or approach taken.

```markdown
- [x] [P1.2] **Query parser** — Parses user search strings into structured queries
  > Used recursive descent instead of regex for nested operator support
- [ ] [P1.3] **Search cache** — LRU cache for frequent queries
```

**Example (Informative):**

```markdown
- [x] [P1.1] **Document indexer** — Builds TF-IDF index from document corpus
  > Chose scikit-learn's TfidfVectorizer over manual implementation for reliability
- [x] [P1.2] **Query ranker** — Ranks documents using cosine similarity
- [ ] [P1.3] **Search cache** — LRU cache with configurable entry limit
- [ ] [P1.4] **Search endpoint** — HTTP endpoint exposing search functionality
```

---

## Document Title

State documents MUST begin with a level-1 heading (`# Feature Name State`) that identifies the feature.

---

## Phase Structure

Phases MUST be numbered sequentially starting from 1. Every phase MUST follow this standard structure:

```markdown
## Phase 1: Descriptive Name

**Goal:** One-sentence description of what this phase accomplishes

**Deliverable:** Concrete outcome (e.g., "Working search indexer with validated TF-IDF scoring")

**Tasks:**
- [ ] [P1.1] **Task name** — What this task delivers
  > Optional agent note added during implementation
- [ ] [P1.2] **Another task** — Description with clear scope

**Checkpoints:**
- [ ] Code quality: `ruff check src/`
- [ ] Self-review: Verify deliverable achieved

**Phase 1 Complete:** Brief description of system state after phase completion.
```

---

## Checkpoint Requirements

Checkpoints are end-of-phase validation operations performed after all tasks in a phase are complete.

**Requirements:**

- Checkpoints MUST use checkbox format: `- [ ] Checkpoint description`
- Additional checkpoints SHOULD be project-specific validation or quality operations
- Checkpoints MUST NOT duplicate task work (tests belong in Tasks section)
- Checkpoint commands SHOULD be concrete and executable (e.g., `ruff check src/`)

**Common Checkpoint Types:**

- **Self-review:** Agent reviews implementation against deliverable
- **Code quality:** Linting, formatting, type checking (e.g., ruff, black, mypy)
- **Code complexity:** Complexity analysis (e.g., radon cc)

**Note (Informative):** Use only tools your project already has. Checkpoints provide quality control for AI-driven development.

---

## Task Ordering

Tasks that depend on others SHOULD be ordered after their dependencies within a phase.

**Example (Informative):**

```markdown
- [ ] [P1.1] **Document indexer** — Builds TF-IDF index from document corpus
- [ ] [P1.2] **Query ranker** — Ranks documents against query using cosine similarity
- [ ] [P1.3] **Search cache** — LRU cache wrapping QueryRanker results
```

---

## Phase Complete Statement

Every phase MUST end with a "Phase N Complete" statement describing system state after phase completion.

The statement SHOULD be 1-3 sentences describing what capabilities now exist, what's ready for the next phase, and what validation has been completed.

**Example (Informative):**

- "Core search components validated, ready for API integration"
- "Query parser complete with DSL support, validated against test cases"
- "End-to-end search flow working with TF-IDF ranking, ready for optimization"

---

## Output Template

````markdown
# [Feature Name] State

## Phase 1: [Descriptive Name]

**Goal:** [One-sentence description of what this phase accomplishes]

**Deliverable:** [Concrete outcome that can be verified]

**Tasks:**
- [ ] [P1.1] **[Task name]** — [What this task delivers]
- [ ] [P1.2] **[Task name]** — [What this task delivers]

**Checkpoints:**
- [ ] Code quality: `[project-specific linting/formatting command]`
- [ ] Self-review: [What to verify against deliverable]

**Phase 1 Complete:** [System state after phase completion]

## Phase 2: [Descriptive Name]

[Same structure as Phase 1, with P2.Y task IDs]
````

---

## Context Independence

State documents MUST be understandable without conversation history. Task descriptions MUST be clear enough to execute when read alongside the spec. The state MUST NOT duplicate architectural rationale from the spec (WHY/WHAT belongs in the spec; WHEN/HOW belongs in the state).

---

## Validation

State documents are conformant when they:

- Begin with a level-1 heading identifying the feature
- Number phases sequentially starting from 1
- Include required elements in every phase (Goal, Deliverable, Tasks, Checkpoints, Phase Complete)
- Use correct task syntax (`- [ ] [PX.Y] **Name** — description`)
- Use sequential task IDs within each phase (no gaps, no reuse)
- Use short noun phrases for task names
- Order tasks after their dependencies
- Use checkpoints for quality/validation (not functional work)
- Contain no architectural rationale or design alternatives (belongs in spec)

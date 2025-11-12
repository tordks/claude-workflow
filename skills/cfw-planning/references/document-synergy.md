# Document Synergy

How plan and tasklist work together to guide implementation.

## WHY/WHAT vs WHEN/HOW Separation

**CRITICAL:** Maintain strict separation of concerns between documents.

**Plan Document (WHY and WHAT):**
- **WHY:** Architectural decisions with RATIONALE
  - Why this approach over alternatives?
  - Why these trade-offs make sense?
  - Why this architecture fits the problem?
- **WHAT:** System components and relationships
  - What pieces make up the solution?
  - What dependencies exist?
  - What risks should we be aware of?
- **DO NOT include:** Step-by-step execution instructions, specific file editing commands, task checklists

**Tasklist Document (WHEN and HOW):**
- **WHEN:** Sequential execution order
  - When to do each task (phase ordering)
  - When phases are complete (checkpoints)
  - When to stop for review (phase boundaries)
- **HOW:** Concrete implementation steps
  - How to create each file
  - How to implement each function
  - How to run tests and verify results
- **DO NOT include:** Architectural rationale, design alternatives, lengthy technical context

## Examples of Correct Separation

✅ **Plan says:**
```markdown
**Decision:** Use TF-IDF ranking algorithm
**Rationale:** Simple, well-understood algorithm with good performance for keyword search.
Can upgrade to neural ranking in v2 if needed.
**Alternatives:** BM25 (more complex), neural ranking (requires training data)
**Trade-offs:** Fast implementation vs. semantic understanding
```

✅ **Tasklist says:**
```markdown
- [ ] [P2.1] Implement TF-IDF scoring in ranker.py
- [ ] [P2.2] Add tests for TF-IDF ranking with sample documents
```

❌ **Wrong - architectural rationale in tasklist:**
```markdown
- [ ] [P2.1] Implement TF-IDF scoring (we chose this because it's simple
  and well-understood, better than BM25 for our use case)
```

❌ **Wrong - step-by-step execution in plan:**
```markdown
First create ranker.py, then add TFIDFRanker class, then implement score()
method, then write tests in test_ranker.py, then run pytest.
```

## Document Relationship: How to Use Together

**Implementation workflow:**

1. **FIRST: Read plan in full**
   - Understand overall architecture
   - Learn WHY decisions were made
   - Grasp how components relate
   - Identify technical constraints

2. **SECOND: Read tasklist for current phase**
   - See what to implement next
   - Follow tasks in order
   - Mark tasks complete as you go
   - Stop at phase checkpoint

3. **DURING: Refer back to plan when needed**
   - Task unclear? Check plan's Technical Approach
   - Need context? Check plan's Architecture & Design
   - Unsure about approach? Check plan's Design Decisions
   - Question trade-offs? Check plan's Rationale

**Why this order matters:**
- Plan provides architectural context needed for good implementation decisions
- Tasks may be atomic, but understanding the WHY prevents incorrect assumptions
- Referring back to plan helps when clarification is needed

**Example scenario:**

**Task:** `[P2.1] Implement TF-IDF scoring in ranker.py`

**Questions that arise:**
- What parameters should the scoring function take?
  - **Check plan:** Technical Approach → Integration Points
- Should this use scikit-learn or custom implementation?
  - **Check plan:** Design Decisions → Dependencies rationale
- How should edge cases be handled?
  - **Check plan:** Technical Approach → Error Handling

## Consistency Rules

**Feature name must match:**
- Plan filename: `{feature-name}-plan.md`
- Tasklist filename: `{feature-name}-tasklist.md`
- Branch name: `{prefix}-{feature-name}`
- All references in documents

**Phases should align:**
- If plan mentions "Phase 2: Ranking Algorithm", tasklist should have "Phase 2: Ranking Implementation"
- Phase numbers match between documents
- Phase goals reflect plan's architecture

**File references should be consistent:**
- Files mentioned in plan's Project Structure should appear in tasklist tasks
- [CREATE] markers in plan should have corresponding "Create X file" tasks
- [MODIFY] markers in plan should have corresponding "Update X file" tasks

**Example alignment:**

**Plan Architecture & Design:**
```markdown
src/query/
├── parser.py [CREATE]
└── ranker.py [CREATE]
```

**Tasklist Phase 1:**
```markdown
- [ ] [P1.1] Create query/ directory and __init__.py
- [ ] [P1.2] Create parser.py with ParserClass stub
- [ ] [P1.3] Create ranker.py with RankerClass stub
```

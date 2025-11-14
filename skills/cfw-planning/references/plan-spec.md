# Plan Document Specification

Specification for creating conformant plan documents in the CWF workflow.

---

## What is a Plan Document?

The plan document captures **architectural context and design rationale** (WHY and WHAT). It provides the foundation for implementation by documenting decisions, alternatives, and reasoning.

**Plan = WHY/WHAT** | Tasklist = WHEN/HOW

---

## Conformance

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

---

## Core Plan Sections

Plan documents MUST include the four core sections defined below: Overview, Architecture & Design, Technical Approach, and Implementation Strategy.

### Section 1: Overview

The Overview section MUST provide a high-level summary of the feature.

**Requirements:**

The Overview section MUST include:
- A problem statement identifying the user need being addressed
- A feature purpose describing what the feature does
- A scope definition identifying what is included and what is explicitly excluded

The Overview section SHOULD include:
- Success criteria defining how completion and correctness will be verified

Success criteria SHOULD be quantifiable or objectively verifiable to enable clear validation.

**Example (Informative):**
```markdown
## Overview

**Problem:** Users need to search documentation by keywords and see relevant results.

**Purpose:** Add document search functionality with keyword filtering and ranking.

**Scope:**
- IN: Keyword search, TF-IDF ranking, result filtering
- OUT: Natural language queries, semantic search, advanced operators

**Success Criteria:**
- Users can search by keywords
- Results ranked by relevance
- Search completes in <100ms for 1000 documents
- Test coverage >80%
```

---

### Section 2: Architecture & Design

The Architecture & Design section MUST document component structure and design decisions with rationale.

**Requirements:**

The Architecture & Design section MUST include:
- A component overview identifying the pieces that make up the feature
- A project structure showing a file tree with operation markers
- Design decisions documenting choices made with WHY rationale

The Architecture & Design section SHOULD include:
- Data flow descriptions showing how information moves through the system

**Design Decision Format:**

When documenting design decisions, Implementations SHOULD use this structure:

```markdown
**Decision:** [What was chosen]
**Rationale:** [WHY this choice was made - primary reason]
**Alternatives Considered:**
- [Option 1]: [Why not chosen]
- [Option 2]: [Why not chosen]
**Trade-offs:**
- Pro: [Benefits of chosen approach]
- Con: [Limitations or downsides]
```

**File Tree Format:**

File trees MUST use markers to indicate file operations:
- New files MUST be marked with `[CREATE]`
- Modified files MUST be marked with `[MODIFY]`
- Removed files MUST be marked with `[REMOVE]`
- Existing unchanged files MUST NOT include markers

**Example (Informative):**
````markdown
## Architecture & Design

### Component Overview
- QueryParser: Parse search keywords and operators
- QueryRanker: Rank documents by TF-IDF relevance
- SearchIndex: In-memory document index
- QueryAPI: HTTP endpoint for search requests

### Project Structure
```
src/
├── query/
│   ├── __init__.py [CREATE]
│   ├── parser.py [CREATE]
│   ├── ranker.py [CREATE]
│   └── index.py [CREATE]
├── api/
│   └── search.py [MODIFY]
└── tests/
    └── query/ [CREATE]
        ├── test_parser.py [CREATE]
        └── test_ranker.py [CREATE]
```

### Design Decisions

**Decision:** Use TF-IDF ranking algorithm
**Rationale:** Simple, well-understood algorithm with good performance for keyword search. No training data required. Can upgrade to neural ranking in v2 if needed.
**Alternatives Considered:**
- BM25: More complex, marginal improvement for our use case
- Neural ranking: Requires training data and GPU, overkill for current needs
**Trade-offs:**
- Pro: Fast implementation, predictable results, no dependencies
- Con: Doesn't understand semantics, sensitive to exact keyword matches
````

---

### Section 3: Technical Approach

The Technical Approach section MUST document implementation details and dependencies.

**Requirements:**

The Technical Approach section MUST include:
- Dependencies identifying required libraries, services, or APIs
- Integration points describing how the feature connects to existing code

The Technical Approach section SHOULD include:
- Error handling approach describing how failures will be managed
- Configuration needs identifying runtime or deployment configuration

**Example (Informative):**
```markdown
## Technical Approach

### Dependencies
- scikit-learn 1.3+ (for TF-IDF vectorization)
- FastAPI 0.100+ (existing, for API endpoints)
- pytest 7.4+ (existing, for testing)

### Integration Points
- Reads from existing DocumentStore
- Exposes new /api/search endpoint
- Uses existing authentication middleware

### Error Handling
- Invalid query syntax → 400 error with helpful message
- No results found → 200 with empty list
- Index not ready → 503 with retry-after header
- Timeout (>5s) → 408 with partial results
```

---

### Section 4: Implementation Strategy

The Implementation Strategy section MUST describe how implementation will proceed.

**Requirements:**

The Implementation Strategy section MUST include:
- A phase breakdown providing a summary of the tasklist phases

**Phase Alignment:** The phase breakdown MUST align with the phases defined in the corresponding tasklist document. Phase names and sequence SHOULD match to maintain consistency between documents.

The Implementation Strategy section SHOULD include:
- A testing approach describing the testing strategy (unit, integration, e2e)

The Implementation Strategy section MUST NOT include step-by-step execution instructions or task checklists. These belong in the tasklist document, not the plan.

---

## Context Independence

Plans MUST NOT assume the implementer has access to planning conversation context. Implementation may occur in fresh sessions after context has been cleared. All architectural decisions and rationale must be self-contained within the plan document.

---

## Validation Checklist

- [ ] All four core sections present with required content
- [ ] File trees present and uses [CREATE]/[MODIFY]/[REMOVE]
- [ ] Design decisions include WHY rationale
- [ ] Plan is self-contained (no assumed conversation context)
- [ ] No step-by-step execution instructions or task checklists

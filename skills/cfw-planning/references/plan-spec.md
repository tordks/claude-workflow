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

The Overview section provides a high-level summary of the problem and solution (WHY build this, WHAT does it do).

**MUST include:**
- Problem statement (current pain point or gap)
- Feature purpose (solution being built)
- Scope (What is IN/OUT of scope)

**SHOULD include:**
- Success criteria (quantifiable completion validation)

**Example (Informative):**
```markdown
## Overview

### Problem
Users currently search documentation by manually scanning files or using basic text search. This is slow (10+ minutes per search) and misses relevant documents that use different terminology. Support tickets show 40% of questions are about "how to find X in the docs."

### Purpose
Add keyword-based document search with relevance ranking. Users enter search terms and receive ranked results within 1 second, improving discoverability and reducing support load.

### Scope
**IN scope:**
- Keyword search with boolean AND/OR operators
- TF-IDF relevance ranking
- Result filtering by document type
- Search result caching

**OUT of scope:**
- Natural language queries ("find me information about...")
- Semantic/embedding-based search
- Advanced operators (NEAR, wildcards, regex)

### Success Criteria
- Users can search by keywords and receive ranked results
- Search completes in <100ms for 10,000 documents
- Results include documents even with terminology variations
- Test coverage >80% for core search logic
- Zero regressions in existing functionality
```

---

### Section 2: Architecture & Design

The Architecture & Design section documents structural composition and design rationale (WHAT are the pieces, WHY this structure).

**MUST include:**
- Component overview (logical pieces that make up the feature and their  responsibilities)
- Project structure (file tree with operation markers)
- Design decisions (WHY rationale)

**SHOULD include:**
- Component relationships (dependencies and communication patterns)

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

**Core Components:**
- **QueryParser:** Parses user search strings into structured queries (operators, quoted phrases)
- **DocumentIndexer:** Builds and maintains TF-IDF index from document corpus
- **QueryRanker:** Ranks documents against query using cosine similarity
- **SearchCache:** LRU cache for frequent queries
- **SearchAPI:** HTTP endpoint exposing search functionality

### Project Structure
```
src/
├── search/
│   ├── __init__.py [CREATE]
│   ├── parser.py [CREATE]
│   ├── indexer.py [CREATE]
│   ├── ranker.py [CREATE]
│   └── cache.py [CREATE]
├── api/
│   └── search.py [CREATE]
├── models/
│   └── document.py [MODIFY]
└── tests/
    └── search/
        ├── test_parser.py [CREATE]
        └── test_ranker.py [CREATE]
```

### Design Decisions

**Decision:** Use TF-IDF with cosine similarity for ranking
**Rationale:** Well-understood algorithm with predictable behavior. No training data or ML infrastructure required.
**Alternatives Considered:**
- BM25: Marginal improvement for our corpus size, added complexity not justified
- Neural/embedding-based: Requires GPU, training data, model management - overkill for current needs
**Trade-offs:**
- Pro: Fast to implement, predictable results, no infrastructure dependencies
- Con: Doesn't understand semantic similarity, sensitive to exact keyword matches

### Component Relationships
- SearchAPI depends on QueryParser, SearchCache
- QueryRanker depends on DocumentIndexer
- SearchCache depends on QueryRanker
- All components use shared Document model
````

---

### Section 3: Technical Approach

The Technical Approach section documents runtime behavior and implementation details (HOW it works, WHAT makes it run).

**MUST include:**
- Dependencies (required libraries, services, APIs)
- Integration points (connections to existing systems)

**SHOULD include:**
- Runtime behavior (algorithms, execution flow, state management)
- Error handling (failure detection and management)
- Configuration needs (runtime or deployment settings)

**Example (Informative):**
````markdown
## Technical Approach

### Dependencies

**New:**
- scikit-learn 1.3+ (TF-IDF vectorization, cosine similarity)
- nltk 3.8+ (text preprocessing, stopword removal)

**Existing:**
- FastAPI 0.100+ (API framework)
- SQLAlchemy 2.0+ (document retrieval)
- pytest 7.4+ (testing)

### Integration Points
- **Inbound:** Exposes `/api/v1/search` endpoint, uses existing FastAPI middleware
- **Outbound:** Reads from `documents` table, listens to `document_updated` events

### Runtime Behavior
1. Parse query → structured query (operators, phrases)
2. Check cache (LRU, 1000 entries)
3. On cache miss: vectorize query, compute cosine similarity, rank results
4. Return paginated results (25 per page)


### Error Handling

**Invalid Input:**
- Empty query → 400 "Query cannot be empty"
- Invalid operators → 400 "Invalid syntax: [specific error]"
- Query too long (>500 chars) → 400 "Query exceeds maximum length"

**Runtime Errors:**
- Index not ready → 503 "Search index is building, retry in [X] seconds"
- Timeout (>5s) → 408 "Query timeout, try simplifying search terms"
- No results found → 200 with empty list (not an error)

**System Errors:**
- Database unavailable → 500, log error, alert on-call
- Index corruption → Rebuild from database, log incident

### Configuration
```python
SEARCH_INDEX_PATH = "/data/search-index.pkl"
SEARCH_CACHE_SIZE = 1000
SEARCH_TIMEOUT_MS = 5000
```
````

---

### Section 4: Implementation Strategy

The Implementation Strategy section describes the high-level approach that guides phase and task structure (WHEN to build what, HOW to validate).

**MUST include:**
- Development approach (incremental, outside-in, vertical slice, bottom-up, etc.)

**SHOULD include:**
- Testing approach (test-driven, integration-focused, comprehensive, etc.)
- Risk mitigation strategy (tackle unknowns first, safe increments, prototype early, etc.)
- Checkpoint strategy (quality and validation operations at phase boundaries)

The strategy SHOULD explain WHY the tasklist is structured as it is.

**MUST NOT include:**
- Step-by-step execution instructions or task checklists
- Task-level details

**Example (Informative):**
```markdown
## Implementation Strategy

### Development Approach

**Incremental with Safe Checkpoints**

Build bottom-up with validation at each layer:
1. **Foundation First:** Core search components (indexer, ranker) before API
2. **Runnable Increments:** Each phase produces working, testable code
3. **Early Validation:** Algorithm performance validated early before building around it


### Testing Approach
Integration-focused with targeted unit tests:
- Unit tests for complex logic (parsing, scoring)
- Integration tests for component interactions
- E2E tests for critical user flows

### Checkpoint Strategy
Each phase ends with mandatory validation before proceeding:
- Self-review: Agent reviews implementation against phase deliverable
- Code quality: Linting and formatting with ruff
- Code complexity: Complexity check with Radon

These checkpoints ensure AI-generated code meets project standards before continuing to next phase.

**Note (Informative):** Checkpoint types are project-specific. Use only the tools your project already has. If the project doesn't use linting or complexity analysis, omit those checkpoints.
```

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

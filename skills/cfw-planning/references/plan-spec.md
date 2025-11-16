# Plan Document Specification

Specification for creating conformant plan documents in the CWF workflow.

---

## What is a Plan Document?

The plan document captures **architectural context and design rationale** (WHY and WHAT). It provides the foundation for implementation by documenting decisions, alternatives, and reasoning.

**Plan = WHY/WHAT** | Tasklist = WHEN/HOW

---

## Conformance

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

> **Note:** See `SKILL.md` for RFC 2119 keyword explanations and guidance on tailoring documentation depth.

---

## Core Plan Sections

Plan documents MUST include the three core sections defined below: Overview, Solution Design, and Implementation Strategy.

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

### Section 2: Solution Design

The Solution Design section documents the complete solution (WHAT is being built and WHY it's designed this way).

#### 2.1 System Architecture

System Architecture describes the structural composition of the solution (WHAT are the pieces and HOW they relate).

**MUST include:**
- Component overview (logical pieces and their responsibilities)
- Project structure (file tree with operation markers)

**SHOULD include:**
- Component relationships (dependencies and communication patterns between new components)
- Relationship to existing codebase (where the feature fits architecturally, which existing modules are used/extended)

**File Tree Format:**

File trees MUST use markers to indicate file operations:
- New files MUST be marked with `[CREATE]`
- Modified files MUST be marked with `[MODIFY]`
- Removed files MUST be marked with `[REMOVE]`
- Existing unchanged files MUST NOT include markers

---

#### 2.2 Design Rationale

Design Rationale documents the reasoning behind structural and technical choices (WHY this design).

**MUST include:**
- Rationale for key design choices (WHY decisions were made)

**SHOULD include:**
- Alternatives considered and why they were not chosen
- Trade-offs accepted by the chosen approach

**MAY include:**
- Constraints that influenced decisions
- Principles or patterns applied

**Tip (Informative):** Format flexibly - inline rationale, comparison tables, or structured decision records all work. Focus on capturing WHY, not following a template.

---

#### 2.3 Technical Specification

Technical Specification describes runtime behavior and operational requirements (WHAT the system needs to run and HOW it behaves).

**MUST include:**
- Dependencies (required libraries and external systems)

**SHOULD include:**
- Runtime behavior (algorithms, execution flow, state management)
- Error handling (failure detection and recovery strategies)
- Configuration needs (runtime or deployment settings)

**Example (Informative):**
````markdown
## Solution Design

### System Architecture

**Core Components:**
- **QueryParser:** Parses user search strings into structured queries (operators, quoted phrases)
- **DocumentIndexer:** Builds and maintains TF-IDF index from document corpus
- **QueryRanker:** Ranks documents against query using cosine similarity
- **SearchCache:** LRU cache for frequent queries
- **SearchAPI:** HTTP endpoint exposing search functionality

**Project Structure:**
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

**Component Relationships:**
- SearchAPI depends on QueryParser, SearchCache
- QueryRanker depends on DocumentIndexer
- SearchCache depends on QueryRanker
- All components use shared Document model

**Relationship to Existing Codebase:**
- Architectural layer: Service layer (alongside existing `src/api/` endpoints)
- Domain: Search functionality (new domain area)
- Extends: `BaseAPIHandler` pattern used throughout repository
- Uses: Existing `AuthMiddleware` for authentication
- Uses: Application `CacheManager` for result caching
- Follows: Repository's service-oriented architecture and dependency injection patterns

### Design Rationale

**Use TF-IDF with cosine similarity for ranking**

Well-understood algorithm with predictable behavior. No training data or ML infrastructure required.

Alternatives considered:
- BM25: Marginal improvement for our corpus size, added complexity not justified
- Neural/embedding-based: Requires GPU, training data, model management - overkill for current needs

Trade-offs accepted:
- Pro: Fast to implement, predictable results, no infrastructure dependencies
- Con: Doesn't understand semantic similarity, sensitive to exact keyword matches

### Technical Specification

**Dependencies:**

Required libraries (new):
- scikit-learn 1.3+ (TF-IDF vectorization, cosine similarity)
- nltk 3.8+ (text preprocessing, stopword removal)

Required systems:
- PostgreSQL (stores `documents` table)
- Redis (event stream for `document_updated` events)
- InfluxDB (search metrics and monitoring)

Existing (from project):
- FastAPI 0.100+ (API framework)
- SQLAlchemy 2.0+ (database ORM)
- pytest 7.4+ (testing framework)

**Runtime Behavior:**
1. Parse query → structured query (operators, phrases)
2. Check cache (LRU, 1000 entries)
3. On cache miss: vectorize query, compute cosine similarity, rank results
4. Return paginated results (25 per page)

**Error Handling:**

Invalid Input:
- Empty query → 400 "Query cannot be empty"
- Invalid operators → 400 "Invalid syntax: [specific error]"
- Query too long (>500 chars) → 400 "Query exceeds maximum length"

Runtime Errors:
- Index not ready → 503 "Search index is building, retry in [X] seconds"
- Timeout (>5s) → 408 "Query timeout, try simplifying search terms"
- No results found → 200 with empty list (not an error)

System Errors:
- Database unavailable → 500, log error, alert on-call
- Index corruption → Rebuild from database, log incident

**Configuration:**
```python
SEARCH_INDEX_PATH = "/data/search-index.pkl"
SEARCH_CACHE_SIZE = 1000
SEARCH_TIMEOUT_MS = 5000
```
````

---

### Section 3: Implementation Strategy

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

- [ ] All three core sections present with required content
- [ ] Solution Design includes all three subsections (System Architecture, Design Rationale, Technical Specification)
- [ ] File trees present and use [CREATE]/[MODIFY]/[REMOVE] markers
- [ ] Design rationale includes WHY decisions were made
- [ ] Plan is self-contained (no assumed conversation context)
- [ ] No step-by-step execution instructions or task checklists

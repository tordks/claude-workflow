# Plan Document Specification

Specification for creating conformant plan documents in the CWF workflow.

> **Note:** See `SKILL.md` for conformance levels and RFC 2119 keyword definitions.

---

## What is a Plan Document?

The plan document captures **architectural context and design rationale** (WHY and WHAT). It provides the foundation for implementation by documenting decisions, alternatives, and reasoning.

**Plan = WHY/WHAT** | Tasklist = WHEN/HOW

---

## Document Header Structure

Every plan document MUST start with YAML frontmatter and a usage header to make it self-contained.

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
- `plan_file`: Path to this plan document
- `tasklist_file`: Path to companion tasklist document
- `created`: Date when plan was created (YYYY-MM-DD format)
- `last_updated`: Date of last amendment (same as created initially)

### Usage Header Template

After the frontmatter and title, implementations MUST include a usage blockquote:

```markdown
# {Feature Name} - Implementation Plan

> **How to Use This Plan**
>
> **Purpose:** This plan provides architectural context (WHY/WHAT) for the `{feature-name}` feature.
> It explains design decisions, rationale, and how components fit together.
>
> **When to read:**
> 1. **Before implementation:** Read in full to understand the overall architecture
> 2. **During implementation:** Refer back when tasks are unclear or need clarification
> 3. **When blocked:** Check relevant sections before asking questions
>
> **Related documents:**
> - **Tasklist:** `plans/{feature-name}-tasklist.md` - Step-by-step execution tasks (WHEN/HOW)
>
> **Document structure:**
> - **Overview** - What and why we're building
> - **Architecture & Design** - How components fit together, design decisions with rationale
> - **Technical Approach** - Dependencies, integration points, error handling
> - **Implementation Strategy** - Phase breakdown and testing approach
> - **Risks & Considerations** - Potential issues and mitigations
```

---

> **CRITICAL**: Every plan document MUST start with YAML frontmatter and usage header (see "Document Header Structure" above) before any content sections.

## Core Plan Sections

Every plan document MUST include these sections. The level of detail SHALL be adapted based on feature complexity and conformance level (see Conformance Levels above).

### Section 1: Overview

**Purpose:** High-level summary of the feature

**Typical Content (Informative):**
- Problem statement (what user need does this solve?)
- Feature purpose (what does this feature do?)
- Scope (what's included and what's explicitly out of scope)
- Success criteria (how will we know this is complete and working?)

**Conformance Requirements:**
- Level 1 (Minimal): Problem and purpose MUST be present; scope and success criteria MAY be brief
- Level 2 (Standard): All four items SHOULD be present with sufficient detail to guide implementation
- Level 3 (Comprehensive): All four items MUST be documented with specific examples and detailed justification

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

**Purpose:** Component structure and design decisions with rationale

**Typical Content (Informative):**
- Component overview (what pieces make up this feature)
- Project structure (file tree showing where code lives)
- Design decisions (what choices were made and WHY)
- Data flow (how information moves through the system)

**File Tree Format:**
Implementations MUST use markers to show file operations:
- `[CREATE]` for new files
- `[MODIFY]` for changed files
- `[REMOVE]` for removed files
- No marker for existing unchanged files

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

**Purpose:** Implementation details and dependencies

**Typical Content (Informative):**
- Dependencies (libraries, services, APIs)
- Integration points (how this connects to existing code)
- Error handling approach
- Configuration needs

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

**Purpose:** How implementation will proceed and what the strategy for implementation is.

**Typical Content (Informative):**
- Phase breakdown (summary of tasklist phases)
- Feature appropriate testing approach (unit, integration, e2e)


---

### Section 5: Risks & Considerations

**Purpose:** Potential issues and mitigation strategies

**Typical Content (Informative):**
Identify and document risks relevant to your feature. Common categories include:
- **Technical challenges:** Implementation difficulties, edge cases, complexity
- **Performance implications:** Speed, memory, scalability, cost impacts
- **Security concerns:** Vulnerabilities, data exposure, authentication/authorization
- **Technical debt:** Shortcuts taken, future refactoring needs, limitations

**Guidelines (Implementations SHOULD):**
- Include only categories relevant to your feature
- For each risk, provide specific mitigation strategy
- If no risks in a category, omit that subsection entirely
- Add other risk categories if needed (e.g., "Data Migration Risks", "Dependency Risks")
- Be specific about impact and likelihood

**Example (Informative):**
```markdown
## Risks & Considerations

### Technical Challenges
- TF-IDF memory usage grows with document count
  - Mitigation: Index only recent documents, paginate old ones
  - Impact: Affects deployments with >10K documents
- Query parsing edge cases (special characters, quotes)
  - Mitigation: Extensive test coverage, clear error messages

### Performance Implications
- Index rebuild takes ~5s for 1000 documents
  - Mitigation: Background rebuild, serve from stale index during update
  - Impact: Brief staleness during reindex, acceptable for use case
- Memory: ~50MB per 1000 documents
  - Mitigation: Acceptable for current scale, monitor growth

### Security Concerns
- Query injection through special characters
  - Mitigation: Input validation, parameterized queries
  - Testing: Fuzz testing with OWASP payloads
- Exposure of document content in search results
  - Mitigation: Respect existing document permissions

### Technical Debt
- In-memory index doesn't persist across restarts
  - Future: Add persistent storage (Phase 2 feature)
  - Impact: 5s rebuild on each restart, acceptable for now
- Single-threaded index updates
  - Future: Parallel processing if needed for >10K documents
```

**Note:** This example shows all four common categories. Your feature may only need 0-2 categories. For instance, a simple utility function might only have "Technical Challenges" and omit the others entirely.

---


## Design Decision Template

When documenting design decisions, implementations SHOULD use this structure:

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

This ensures architectural context is captured with clear reasoning for future reference.

---

## Validation Requirements

Before finalizing your plan document, it MUST satisfy these conformance requirements:

### Level 1 Requirements (MUST)

**Document Header:**
- YAML frontmatter MUST be present with all REQUIRED fields
- Usage header MUST be present after title

**Core Sections:**
- All five core sections MUST be present:
  1. Overview (Problem and Purpose REQUIRED; Scope and Success Criteria OPTIONAL)
  2. Architecture & Design (Components and Structure REQUIRED)
  3. Technical Approach (Dependencies REQUIRED)
  4. Implementation Strategy (Phase Breakdown REQUIRED)
  5. Risks & Considerations (MAY be brief)

**File Tree Format:**
- File operation markers MUST be used correctly:
  - `[CREATE]` for new files
  - `[MODIFY]` for changed files
  - `[REMOVE]` for removed files
  - No marker for existing unchanged files

### Level 2 Requirements (SHOULD)

**Core Sections:**
- Overview SHOULD include all four items (Problem, Purpose, Scope, Success Criteria)
- Architecture & Design SHOULD include Data Flow
- Technical Approach SHOULD include Integration points and Error Handling

**Design Decisions:**
- Design decisions SHOULD include WHY rationale (not just WHAT)
- Alternatives considered SHOULD be documented
- Trade-offs SHOULD be explained (pros and cons)

### Level 3 Requirements (MAY)

**Content Enhancement:**
- Data flow diagrams MAY be included
- Performance considerations MAY be documented
- Extended examples MAY be provided

### Content Focus (All Levels)
- Plan documents MUST contain architectural context (WHY/WHAT)
- Plan documents MUST NOT contain step-by-step execution instructions
- Plan documents MUST NOT contain task checklists

### File Naming (All Levels)
- Plan filenames MUST follow the pattern: `plans/{feature-name}-plan.md`
- Examples (Informative): `query-command-plan.md`, `user-auth-plan.md`, `data-export-plan.md`

---

## Common Mistakes to Avoid

These practices help create effective plan documents:

**❌ Mixing execution steps into plan**
- **Best Practice:** Plans explain WHY and WHAT, not HOW step-by-step
- **Tip:** Move execution details to tasklist

**❌ Missing WHY rationale in design decisions**
- **Tip:** Don't just say "Use Redis for caching"
- **Best Practice:** Explain: "Use Redis for caching because it provides sub-millisecond latency and persistence, crucial for our high-traffic API. Considered Memcached (faster but no persistence) and in-memory (simpler but doesn't survive restarts)."

**❌ File tree without markers**
- **Best Practice:** Always use `[CREATE]` and `[MODIFY]` markers
- **Rationale:** Helps implementers know what files to create vs modify

**❌ Vague success criteria**
- **Tip:** Don't say "Feature works correctly"
- **Best Practice:** Say "Search returns results in <100ms, handles 1000+ documents"

---

## Conformance by Feature Complexity

Features SHOULD select the appropriate conformance level based on their complexity:

**Simple features** (bug fixes, small utilities) → **Level 1 (Minimal)**:
- Brief sections (1-2 paragraphs each)
- MUST satisfy Level 1 requirements only
- MAY omit optional subsections (e.g., Data Flow, Security Concerns)
- Focus on core information needed for implementation

**Medium features** (new components) → **Level 2 (Standard)**:
- Moderate detail in all sections
- MUST satisfy Level 1 requirements
- SHOULD satisfy Level 2 requirements
- SHOULD include most subsections
- SHOULD document key design decisions with rationale and alternatives considered

**Complex features** (major systems) → **Level 3 (Comprehensive)**:
- Comprehensive detail in all sections
- MUST satisfy Level 1 and Level 2 requirements
- SHOULD satisfy Level 3 requirements where applicable
- SHOULD include all subsections
- MUST provide extensive design decision documentation
- SHOULD document multiple risks and mitigations

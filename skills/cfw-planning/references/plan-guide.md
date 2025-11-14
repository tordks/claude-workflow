# Plan Document Guide

Complete guide for creating high-quality plan documents in the CWF workflow.

## What is a Plan Document?

The plan document captures **architectural context and design rationale** (WHY and WHAT). It provides the foundation for implementation by documenting decisions, alternatives, and reasoning.

**Plan = WHY/WHAT** | Tasklist = WHEN/HOW

---

## Document Header Structure

Every plan document must start with YAML frontmatter and a usage header to make it self-contained.

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

After the frontmatter and title, include a usage blockquote:

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

Every plan should include these sections, adapting the level of detail to feature complexity. Simple features may have brief sections; complex features need more depth.

### Section 1: Overview

**Purpose:** High-level summary of the feature

**Contains:**
- Problem statement (what user need does this solve?)
- Feature purpose (what does this feature do?)
- Scope (what's included and what's explicitly out of scope)
- Success criteria (how will we know this is complete and working?)

**Guidelines:**
- All items are recommended but adapt to feature complexity
- Simple features may combine problem/purpose into one statement
- For small changes, success criteria might be brief (e.g., "Tests pass, documentation updated")
- Complex features should thoroughly document all four items

**Example:**
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

**Contains:**
- Component overview (what pieces make up this feature)
- Project structure (file tree showing where code lives)
- Design decisions (what choices were made and WHY)
- Data flow (how information moves through the system)

**File Tree Format:**
Use markers to show file operations:
- `[CREATE]` for new files
- `[MODIFY]` for changed files
- `[REMOVE]` for removed files
- No marker for existing unchanged files

**Example:**
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

**Contains:**
- Dependencies (libraries, services, APIs)
- Integration points (how this connects to existing code)
- Error handling approach
- Configuration needs

**Example:**
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

**Contains:**
- Phase breakdown (summary of tasklist phases)
- Feature appropriate testing approach (unit, integration, e2e)


---

### Section 5: Risks & Considerations

**Purpose:** Potential issues and mitigation strategies

**Contains:**
Identify and document risks relevant to your feature. Common categories include:
- **Technical challenges:** Implementation difficulties, edge cases, complexity
- **Performance implications:** Speed, memory, scalability, cost impacts
- **Security concerns:** Vulnerabilities, data exposure, authentication/authorization
- **Technical debt:** Shortcuts taken, future refactoring needs, limitations

**Guidelines:**
- Include only categories relevant to your feature
- For each risk, provide specific mitigation strategy
- If no risks in a category, omit that subsection entirely
- Add other risk categories if needed (e.g., "Data Migration Risks", "Dependency Risks")
- Be specific about impact and likelihood

**Example:**
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

When documenting design decisions, use this structure:

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

## Plan Validation Checklist

Before finalizing your plan document, validate against these criteria:

### Document Header
✅ **YAML frontmatter present** with all required fields.

✅ **Usage header present** after title with required fields.

### Core Sections
✅ **All sections present** (adapt depth to feature complexity):
1. Overview (Problem, Purpose, Scope, Success Criteria)
2. Architecture & Design (Components, Structure, Decisions, Data Flow)
3. Technical Approach (Dependencies, Integration, Error Handling)
4. Implementation Strategy (Phase Breakdown, Testing Approach)
5. Risks & Considerations (Relevant categories only)

### File Tree Format
✅ **Markers used correctly:**
- `[CREATE]` for new files
- `[MODIFY]` for changed files
- `[REMOVE]` for removed files
- No marker for existing unchanged files

### Design Decisions
✅ **Include WHY rationale** (not just WHAT)
✅ **Document alternatives considered**
✅ **Explain trade-offs** (pros and cons)

### Content Focus
✅ **Contains architectural context** (WHY/WHAT)
✅ **Does NOT contain step-by-step execution instructions**
✅ **Does NOT contain task checklists**

### File Naming
✅ **Plan filename:** `plans/{feature-name}-plan.md`
✅ **Examples:** `query-command-plan.md`, `user-auth-plan.md`, `data-export-plan.md`

---

## Common Mistakes to Avoid

**❌ Mixing execution steps into plan**
- Plan should explain WHY and WHAT, not HOW step-by-step
- Move execution details to tasklist

**❌ Missing WHY rationale in design decisions**
- Don't just say "Use Redis for caching"
- Explain: "Use Redis for caching because it provides sub-millisecond latency and persistence, crucial for our high-traffic API. Considered Memcached (faster but no persistence) and in-memory (simpler but doesn't survive restarts)."

**❌ File tree without markers**
- Always use `[CREATE]` and `[MODIFY]` markers
- Helps implementers know what files to create vs modify

**❌ Vague success criteria**
- Don't say "Feature works correctly"
- Say "Search returns results in <100ms, handles 1000+ documents"

---

## Adapting to Feature Complexity

**Simple features** (bug fixes, small utilities):
- Brief sections (1-2 paragraphs each)
- May skip some subsections (e.g., Data Flow, Security Concerns)
- Focus on core information needed for implementation

**Medium features** (new components):
- Moderate detail in all sections
- Include most subsections
- Document key design decisions thoroughly

**Complex features** (major systems):
- Comprehensive detail in all sections
- Include all subsections
- Extensive design decision documentation
- Multiple risks and mitigations

The validation checklist represents comprehensive validation. Not every item is mandatory for every feature type - adapt to your needs.

# Spec Document Specification

Specification for creating conformant spec documents in the CWF workflow.

---

## Core Spec Sections

Spec documents MUST include three core sections: Overview, Solution Design, and Implementation Strategy.

### Section 1: Overview

Provides high-level summary of problem and solution.

**MUST include:**

- Problem statement (current pain point or gap)
- Feature purpose (solution being built)

**SHOULD include:**

- Scope (What is IN/OUT of scope)
- Success criteria (quantifiable completion validation)

---

### Section 2: Solution Design

Documents the complete solution architecture and technical approach.

#### 2.1 System Architecture

**MUST include:**

- Component overview (named components with descriptions — these map to state components)

**SHOULD include:**

- Component relationships (dependencies and communication patterns)
- Project structure (file tree with operation markers)
- Relationship to existing codebase (where feature fits, what it extends/uses)

**Component Naming:**
Components MUST use named labels in the format `**Name** — description`. Names SHOULD be short noun phrases that clearly identify the module, service, or feature area. Component names SHOULD be recognizable in state task names.

**File Tree Format:**
File trees MUST use operation markers:

- `[CREATE]` for new files
- `[MODIFY]` for modified files
- `[REMOVE]` for removed files
- No marker for existing unchanged files

---

#### 2.2 Design Rationale

Documents reasoning behind structural and technical choices.

**MUST include:**

- Rationale for key design choices

**SHOULD include:**

- Alternatives considered and why not chosen
- Trade-offs accepted

**MAY include:**

- Constraints influencing decisions
- Principles or patterns applied

---

#### 2.3 Technical Specification

Describes runtime behavior and operational requirements.

**MUST include:**

- Dependencies (libraries, external systems)

**SHOULD include:**

- Runtime behavior (algorithms, execution flow, state management)

**MAY include:**

- Error handling (failure detection and recovery)
- Configuration needs (runtime or deployment settings)

---

### Section 3: Implementation Strategy

Describes the high-level approach guiding phase and component structure.

**MUST include:**

- Development approach (incremental, outside-in, vertical slice, bottom-up, etc.)

Common integration strategies include, but are not limited to:

- **Bottom-up:** foundational/core components first, integration later
- **Outside-in:** API/interface first, internals later
- **Vertical slice:** one end-to-end flow first, then broaden coverage
- **Strangler fig:** progressively replace existing system piece by piece

Modifiers (compose with any strategy):

- **Risk-first:** most uncertain/complex component first to validate feasibility early
- **Contract-first:** define interfaces between components before implementing them

Other strategies or modifiers MAY be used when appropriate.

**SHOULD include:**

- Testing approach (test-driven, integration-focused, comprehensive, etc.)
- Checkpoint strategy (quality and validation operations at phase boundaries)

**MUST NOT include:**

- Phase enumeration or step-by-step execution plans

The strategy SHOULD explain WHY the state document is structured as it is, without enumerating the phases themselves.

Checkpoint strategy SHOULD reference specific project tools discovered during planning. If the project doesn't use linting, complexity analysis, or dead code detection, omit those checkpoints.

---

## Output Template

````markdown
## Overview

### Problem
[1-2 paragraphs: current pain point, quantify impact where possible]

### Purpose
[1-2 paragraphs: solution being built, key user benefit]

### Scope
**IN scope:**
- [capabilities being built]

**OUT of scope:**
- [explicit exclusions]

### Success Criteria
- [measurable completion outcomes]

## Solution Design

### System Architecture

**Components:**
- **[Component name]** — [what it does]

**Component Relationships:**
- [dependency and communication patterns between components]

**Project Structure:**
```
[file tree with [CREATE]/[MODIFY]/[REMOVE] markers]
```

**Relationship to Existing Codebase:**
- [architectural layer, what it extends/uses, patterns followed]

### Design Rationale
[format flexibly: rationale for key choices, alternatives considered, trade-offs accepted]

### Technical Specification

**Dependencies:**
- New libraries: [name, version, purpose]
- Required systems: [external dependencies]
- Existing (from project): [project dependencies being used]

**Runtime Behavior:**
[algorithm or execution flow]

## Implementation Strategy

### Development Approach
[approach + why this determines phase ordering]

### Testing Approach
[How tests relate to implementation: alongside each component, separate test phase, TDD, etc.]
[Where test files live in the project structure]
[What types of tests: unit, integration, e2e — and what each covers]

### Checkpoint Strategy
[project-specific validation tools discovered during planning]
````

---

## Context Independence

The spec and state documents together MUST be self-contained for implementation. Implementation may occur in fresh sessions after context has been cleared. All architectural decisions and rationale MUST be in the spec document — the state document MUST NOT need to repeat them.

---

## Validation

Specs are conformant when they:

- Include all three core sections (Overview, Solution Design, Implementation Strategy)
- Overview includes problem statement and feature purpose
- Solution Design includes all three subsections (System Architecture, Design Rationale, Technical Specification)
- System Architecture includes component overview with named labels (`**Name** — description`)
- Design Rationale includes rationale for key design choices
- Technical Specification includes dependencies
- Implementation Strategy includes development approach
- Use file tree operation markers correctly (`[CREATE]`, `[MODIFY]`, `[REMOVE]`)
- Document WHY for design decisions
- Are self-contained (no assumed conversation context)
- Contain no phase enumeration or step-by-step execution instructions

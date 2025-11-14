---
name: cfw-planning
description: Load for any CWF planning task including: explaining the workflow, answering planning questions, creating plans, amending plans, and implementing features. Contains conventions, phase structure, task formats, validation rules, and templates.
---

# CFW Planning

Knowledge repository for Claude Workflow (CWF) planning system.

## Overview

CWF is a plan-driven development workflow using two complementary documents that work together to guide feature implementation:

**Plan Document (`{feature-name}-plan.md`):**
- Captures architectural context and design rationale
- Documents WHY decisions were made and WHAT the solution is
- Contains: Overview, Architecture & Design, Technical Approach, Implementation Strategy, Risks & Considerations
- **Follows structure defined in `plan-spec.md`**

**Tasklist Document (`{feature-name}-tasklist.md`):**
- Provides step-by-step execution guidance
- Documents WHEN to do tasks and HOW to implement them
- Contains: Phase-by-phase tasks with IDs, goals, deliverables, and checkpoints
- **Follows structure defined in `tasklist-spec.md`**

**Both documents follow the conformance requirements defined below.**

---

## Conformance Requirements

**All CWF planning documents (plans and tasklists) use these conformance definitions.**

The specifications in `plan-spec.md` and `tasklist-spec.md` use RFC 2119 keywords to define requirements:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

### Conformance Levels

CWF specifications define three conformance levels:

| Level | Requirements | Suitable For |
|-------|--------------|--------------|
| **Level 1 (Minimal)** | MUST requirements only | Simple features, bug fixes, small utilities |
| **Level 2 (Standard)** | MUST + SHOULD requirements | Most features, new components, medium complexity |
| **Level 3 (Comprehensive)** | MUST + SHOULD + MAY requirements | Complex features, major systems, architectural changes |

### Selecting the Right Level

- Simple features (bug fixes, utilities) → Level 1
- Medium features (components, modules) → Level 2
- Complex features (systems, frameworks) → Level 3

### How Conformance Applies

**For Plan Documents** (see `plan-spec.md` for details):
- **Level 1**: Core sections present with minimal detail
- **Level 2**: All sections with adequate design decision rationale
- **Level 3**: Comprehensive sections with extensive documentation

**For Tasklist Documents** (see `tasklist-spec.md` for details):
- **Level 1**: Basic task structure and phase organization
- **Level 2**: Detailed tasks with proper granularity and ordering
- **Level 3**: Comprehensive tasks with extensive checkpoints

**Important:** Both plan and tasklist for a feature SHOULD use the same conformance level

---

## CWF Workflow

The CWF planning workflow follows these stages:

### 1. Planning Phase
- Discuss feature requirements and approach
- Consider architecture, design decisions, and trade-offs
- Identify phases, tasks, and dependencies

### 2. Documentation
- Create plan document with architectural context
- Create tasklist document with execution steps
- Validate structure and consistency between documents

### 3. Implementation
- Read plan first for architectural understanding
- Follow tasklist phase-by-phase
- Mark tasks complete as work progresses
- Stop at phase boundaries for review

### 4. Amendment
- Add tasks to incomplete phases as needed
- Create new phases for additional work
- Update plan sections with new context
- Follow amendment safety rules (completed work is immutable)

## Quick Reference

| Need to understand... | Read This Reference | Contains |
|----------------------|---------------------|----------|
| **Plan document specification** | `references/plan-spec.md` | Plan structure requirements (uses conformance levels above) |
| **Tasklist document specification** | `references/tasklist-spec.md` | Tasklist structure requirements (uses conformance levels above) |
| **Amendment rules and safety** | `references/amendment.md` | Rules for safely modifying plans and tasklists |
| **Argument parsing for commands** | `references/parsing-arguments.md` | Command argument parsing logic and discovery patterns |
| **Feature naming and file structure** | `references/conventions.md` | Feature naming and file structure standards |


---

**Skill loaded.** CWF planning concepts and patterns are now available.

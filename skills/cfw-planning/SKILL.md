---
name: cfw-planning
description: This skill should be used for plan-driven development - provides planning conventions, phase structure, task ID formats, and file naming patterns
---

# CFW Planning

Knowledge repository for Claude Workflow (CWF) planning system.

## Overview

CWF is a plan-driven development workflow using two complementary documents that work together to guide feature implementation:

**Plan Document (`{feature-name}-plan.md`):**
- Captures architectural context and design rationale
- Documents WHY decisions were made and WHAT the solution is
- Contains: Overview, Architecture & Design, Technical Approach, Implementation Strategy, Risks & Considerations

**Tasklist Document (`{feature-name}-tasklist.md`):**
- Provides step-by-step execution guidance
- Documents WHEN to do tasks and HOW to implement them
- Contains: Phase-by-phase tasks with IDs, goals, deliverables, and checkpoints

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

| Need to understand... | Read This Reference |
|----------------------|---------------------|
| **Implementation workflow (minimal, start here)** | `references/implementation-essentials.md` |
| **Validation checklist** | `references/validation.md` |
| **Amendment rules and safety** | `references/amendment.md` |
| Plan document structure and requirements | `references/plan-structure.md` |
| Tasklist document structure and requirements | `references/tasklist-structure.md` |
| How plan and tasklist work together | `references/document-synergy.md` |
| Feature naming, file structure, branch naming | `references/conventions.md` |

## Reference Organization

### references/implementation-essentials.md
**Content:** Minimal guide for implementing features (LOAD THIS FIRST for implementation)

- Finding plan and tasklist files
- Implementation workflow (3 steps: read plan → read tasklist → execute)
- Phase structure basics
- Task ID format and marking complete
- When to reference full guides
- Quick validation checklist

**This is the starting point for implementation.** It provides just enough to begin executing tasks, with pointers to full guides when needed.

### references/validation.md
**Content:** Quick validation checklist for plans and tasklists

- Feature naming validation (kebab-case, branch names, file names)
- Plan document validation (5 required sections, file tree format, design decisions)
- Tasklist document validation (Phase 0, task IDs, phase structure, granularity)
- Document synergy validation (WHY/WHAT vs WHEN/HOW, consistency rules)
- Quick validation checklist (complete list for commands)
- Validation failure guidance

**Use when:** Creating or validating plans/tasklists, checking document structure before implementation.

### references/amendment.md
**Content:** Amendment rules and safety guidelines

- Core principles (NEVER/ALWAYS rules)
- Why amendment rules exist (immutability rationale)
- Allowed operations (add tasks, add phases, modify descriptions, update plan sections)
- Blocked operations (modify completed work, change task IDs)
- When to update each document
- Quick reference table of amendment types

**Use when:** Modifying existing plans or tasklists, adding tasks/phases to in-progress features, clarifying incomplete tasks.

### references/conventions.md
**Content:** Shared naming and structure conventions

- Feature name format (kebab-case, 2-3 words)
- File structure (plans/ directory layout)
- Branch naming convention ({prefix}-{feature-name})
- Discovery patterns

### references/plan-structure.md
**Content:** Plan document structure (WHY and WHAT)

- Required sections (Overview, Architecture & Design, Technical Approach, Implementation Strategy, Risks & Considerations)
- File tree format with [CREATE]/[MODIFY] markers
- Design decision template with rationale
- Examples for each section

### references/tasklist-structure.md
**Content:** Tasklist document structure (WHEN and HOW)

- Tasklist header template
- Phase structure (Goal, Deliverable, Tasks, Checkpoint)
- Phase 0 special case (branch setup only)
- Task granularity guidelines (15-30 min, atomic, testable, file-specific)
- Task ordering principles
- Task ID format and rules ([PX.Y])
- Checkpoint format

### references/document-synergy.md
**Content:** How plan and tasklist work together

- WHY/WHAT vs WHEN/HOW separation principles
- Document relationship and implementation workflow
- Consistency rules (feature names, phases, file references)

## Critical Principles

These principles are fundamental to CWF planning:

1. **Plan = WHY/WHAT** (architecture, rationale) | **Tasklist = WHEN/HOW** (execution, steps)
2. **Phase 0 is always branch setup only** - never anything else
3. **Task IDs are immutable** - [PX.Y] format, never change once created
4. **Completed work is immutable** - never modify tasks marked [x] or completed phases
5. **Tasks are 15-30 minutes** - atomic, testable, file-specific
6. **Code must be runnable after each phase** - no broken states between phases

## Document Relationship

Plans and tasklists are complementary:

**For implementation, start with `implementation-essentials.md`** which provides:
- Minimal workflow guidance
- How to find and use plan/tasklist files
- Task completion basics
- Quick validation

**Read plan first** to understand:
- Overall architecture
- WHY decisions were made
- How components relate
- Technical constraints

**Then follow tasklist** to:
- Execute tasks in order
- Track progress with checkboxes
- Stop at phase boundaries
- Verify deliverables

**Refer back to plan** when:
- Tasks are unclear
- Need architectural context
- Question implementation approach
- Want to understand trade-offs

**Load full reference guides** when:
- Creating new plans/tasklists (use plan-structure.md, tasklist-structure.md)
- Amending existing documents (use document-synergy.md)
- Need detailed structure validation
- Implementing and need clarification on standards

---

**Skill loaded.** CWF planning concepts and patterns are now available.

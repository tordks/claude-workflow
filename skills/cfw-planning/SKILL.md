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

| Need to understand... | Read This Reference | Contains |
|----------------------|---------------------|----------|
| **Plan document guide** | `references/plan-guide.md` | Plan document structure with core sections |
| **Tasklist document guide** | `references/tasklist-guide.md` | Tasklist structure with phases and task IDs |
| **Amendment rules and safety** | `references/amendment.md` | Rules for safely modifying plans and tasklists |
| **Argument parsing for commands** | `references/parsing-arguments.md` | Command argument parsing logic and discovery patterns |
| **Feature naming and file structure** | `references/conventions.md` | Feature naming and file structure standards |


---

**Skill loaded.** CWF planning concepts and patterns are now available.

---
description: Create plan and tasklist from planning discussion
---

# Plan Command

Formalize the planning discussion from plan mode into structured documentation.

## Bootstrap

**Check if CWF skills are already loaded in this session:**
- Do you have access to `plan-spec.md` and `tasklist-spec.md` reference documents?
- Do you have knowledge of CWF conformance levels and planning patterns?

**If NO (skills not yet loaded):**
1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete

**If YES (skills already loaded):**
- Skip skill loading, knowledge is already available

Then proceed with instructions below.

**Key references from cfw-planning:**
- `conventions.md` - Feature name format validation
- `plan-spec.md` - Plan document specification with structure and validation requirements
- `tasklist-spec.md` - Tasklist document specification with structure and validation requirements

## Context

This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the plan has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

Parse input arguments using the standard parsing pattern from the cfw-planning skill's `parsing-arguments.md` reference.


## Instructions

### 1. Extract Planning Context

**Step 1: Read conversation history**

Extract from the planning discussion:
- Requirements and scope boundaries (what's IN and OUT)
- Design decisions with rationale (WHY specific approaches chosen)
- Alternatives considered and rejected (what was ruled out and why)
- Technical constraints and dependencies (external systems, libraries, APIs)
- File and component structure discussed

**Step 2: Assess feature complexity**

Classify the feature complexity using conformance level criteria from SKILL.md (Simple/Medium/Complex → L1/L2/L3). Consider affected components, files, and integration points.

**Step 3: Select conformance level**

Map assessed complexity to conformance level:
- Simple → Level 1 conformance
- Medium → Level 2 conformance
- Complex → Level 3 conformance

The selected level will be applied to BOTH plan.md and tasklist.md.

**Step 4: Read specifications**

- Read plan-spec.md, focusing on requirements for your selected conformance level
- Read tasklist-spec.md, focusing on requirements for your selected conformance level

When context is extracted and conformance level selected, proceed to Section 2.

---

### 2. Create Planning Documents

**Step 1: Draft plan document**

Create `plans/{feature-name}-plan.md`:
- Follow plan-spec.md structure requirements for your conformance level
- Use the extracted context from Section 1

**Step 2: Draft tasklist document**

Create `plans/{feature-name}-tasklist.md`:
- Follow tasklist-spec.md structure requirements for your conformance level
- Break down into phases aligned with plan's Implementation Strategy
- Include checkpoints following SKILL.md guidance

**Requirements to apply during drafting:**
- Stay faithful to what was discussed and agreed upon in plan mode
- Ensure tasks reflect the implementation approach from the discussion
- Follow task granularity guidelines from tasklist-spec.md
- Use clear, concise language

When both documents are drafted, proceed to Section 3.

---

### 3. Validate Individual Documents

**Step 1: Validate plan document**

1. Read the validation checklist from plan-spec.md
2. Check each item against `plans/{feature-name}-plan.md`
3. Note any failing items

**Step 2: Validate tasklist document**

1. Read the validation checklist from tasklist-spec.md
2. Check each item against `plans/{feature-name}-tasklist.md`
3. Note any failing items

**Step 3: Revise if needed**

If ANY checklist items fail:
1. Revise the affected document(s) to address failures
2. Re-run validation for revised document(s)
3. Repeat until all checklist items pass

When all individual document validations pass, proceed to Section 4.

---

### 4. Validate Cross-Document Coherence

**Step 1: Run coherence checks**

Verify each of the following:

1. ✓ **Phases match plan** - Each tasklist phase implements components/features described in plan's Implementation Strategy
2. ✓ **Files align** - Files in plan's file tree (`[CREATE]`/`[MODIFY]`) appear in tasklist tasks
3. ✓ **Tests covered** - Testing approach in plan matches test tasks in tasklist
4. ✓ **Deliverables align** - Phase deliverables match plan's Implementation Strategy phase breakdown
5. ✓ **Detail consistency** - Both documents use similar documentation depth

**Step 2: Revise if misalignment found**

If ANY check fails:
1. Identify which document contains the inconsistency
2. Revise that document to align with the other
3. Re-run the failing coherence check(s)
4. Repeat until all coherence checks pass

When all coherence checks pass, proceed to Section 5.

---

### 5. Finalization

**Step 1: Verify artifacts created**

- Confirm `plans/{feature-name}-plan.md` exists and is valid
- Confirm `plans/{feature-name}-tasklist.md` exists and is valid

**Step 2: Present summary to user**

Output the following summary:

```
Planning documents created successfully! ✅

Created:
- plans/{feature-name}-plan.md
- plans/{feature-name}-tasklist.md

Conformance Level: L{X} ({Simple|Medium|Complex})

Implementation Structure:
- {N} phases defined
- {M} total tasks

Next Steps:
Run `/implement-plan {feature-name}` to begin phase-by-phase implementation.
```

**YOU ARE NOW DONE.** Wait for user to run `/implement-plan {feature-name}`.

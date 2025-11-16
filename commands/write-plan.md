---
description: Create plan and tasklist from planning discussion
---

# Plan Command

Formalize the planning discussion from plan mode into structured documentation.

## Bootstrap

**Check if CWF skills are already loaded in this session:**
- Do you have the cfw-planning skill loaded with access to reference documents (plan-spec.md, tasklist-spec.md)?

**If NO (skills not yet loaded):**
1. Use the Skill tool to load: `read-constitution`
2. Use the Skill tool to load: `cfw-planning`
3. Wait for both to complete

**If YES (skills already loaded):**
- Skip skill loading, knowledge is already available

## Required References

**Check if required references are already loaded in this session:**
- Do you have access to plan-spec.md (plan document specification)?
- Do you have access to tasklist-spec.md (tasklist document specification)?

**If NO (not yet loaded):**
Use the Read tool to load any missing references:
- `references/plan-spec.md` - Plan document specification with structure and validation requirements
- `references/tasklist-spec.md` - Tasklist document specification with structure and validation requirements

**If YES (all already loaded):**
- Skip loading, reference knowledge is already available

Then proceed with instructions below.

## Context

This command is run AFTER iterating with Claude in plan mode. The user has already discussed and refined the approach. Your job is to capture and formalize what was discussed.

Assume the engineer using the plan has zero context for the codebase. Document everything they need: which files to touch, code/testing/docs to check, how to test. Assume they are skilled but know little about the toolset or problem domain.

## Arguments

**Input**: `$ARGUMENTS`

**Expected format**: `/write-plan {feature-name} [planning context]`

**Parsing:**
- First token: feature name
- Remaining tokens: optional planning guidance or focus areas
  - Example: `user-auth focus on OAuth2 and session management`

**Feature name requirements:**
- Format: kebab-case (lowercase with hyphens)
- Length: 1-3 words, concise and descriptive
- Characters: lowercase letters, numbers, hyphens only
- Examples: `query-command`, `user-auth`, `auth`, `export`
- Avoid: special characters, uppercase, underscores

**If no feature name provided:**
- Analyze conversation to suggest an appropriate feature name based on discussion
- Present suggestion: "Based on our discussion, I suggest the feature name: '{suggested-name}'"
- Ask user to confirm before creating files

**Feature name usage:**
- Creates: `plans/{feature-name}-plan.md` and `plans/{feature-name}-tasklist.md`


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

Assess the feature complexity (Simple/Medium/Complex) to guide documentation depth. Consider:
- Affected components, files, and integration points
- Architectural impact and integration complexity
- Number of stakeholders and systems involved

Use this assessment to determine which SHOULD and MAY requirements from the specifications will add value.

**Step 3: Read specifications**

- Read references/plan-spec.md to understand plan structure and requirements
- Read references/tasklist-spec.md to understand tasklist structure and requirements
- Review the tailoring guidance in SKILL.md to understand how to adapt depth to feature complexity

When context is extracted and complexity assessed, proceed to Section 2.

---

### 2. Create Planning Documents

**Step 1: Draft plan document**

Create `plans/{feature-name}-plan.md`:
- Follow plan-spec.md structure requirements, tailoring depth to feature complexity
- Use the extracted context from Section 1

**Step 2: Draft tasklist document**

Create `plans/{feature-name}-tasklist.md`:
- Follow tasklist-spec.md structure requirements, tailoring depth to feature complexity
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

Implementation Structure:
- {N} phases defined
- {M} total tasks

Next Steps:
Run `/implement-plan {feature-name}` to begin phase-by-phase implementation.
```

**YOU ARE NOW DONE.** Wait for user to run `/implement-plan {feature-name}`.

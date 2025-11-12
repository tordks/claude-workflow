# Validation Reference

Use these guidelines to validate CWF plans and tasklists. Adapt validation criteria based on feature complexity:
- **Simple features** (bug fixes, small utilities): May skip some optional items
- **Medium features** (new components): Should follow most guidelines
- **Complex features** (major systems): Follow all guidelines thoroughly

The checkboxes below represent comprehensive validation. Not every item is mandatory for every feature type.

## Feature Naming Validation

✅ **Feature name format:**
- Pattern: kebab-case (lowercase with hyphens)
- Length: 2-3 words, concise and descriptive
- Characters: lowercase letters, numbers, hyphens only
- Examples: `query-command`, `user-auth`, `data-export`

✅ **Branch name format:**
- Pattern: `{prefix}-{feature-name}`
- Valid prefixes: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`
- Example: `feat-query-command`

✅ **File naming:**
- Plan: `plans/{feature-name}-plan.md`
- Tasklist: `plans/{feature-name}-tasklist.md`
- Feature name must match across all files

## Plan Document Validation

✅ **Core sections (all 5 recommended, adapt depth to complexity):**
1. Overview
   - Problem statement
   - Feature purpose
   - Scope (IN/OUT)
   - Success criteria
2. Architecture & Design
   - Component overview
   - Project structure with file tree
   - Design decisions with WHY rationale
   - Data flow (optional for simple changes)
3. Technical Approach
   - Dependencies (if adding new ones)
   - Integration points
   - Error handling (for features with failure modes)
4. Implementation Strategy
   - Phase breakdown
   - Testing approach (adapt to feature complexity)
5. Risks & Considerations
   - Include only relevant categories (may have 0-4 subsections)
   - Technical challenges, performance, security, technical debt

✅ **File tree format:**
- Use `[CREATE]` marker for new files
- Use `[MODIFY]` marker for changed files
- No marker for existing unchanged files

✅ **Design decisions:**
- Include WHY rationale (not just WHAT)
- Document alternatives considered
- Explain trade-offs

✅ **Content focus:**
- Contains architectural context (WHY/WHAT)
- Does NOT contain step-by-step execution instructions
- Does NOT contain task checklists

## Tasklist Document Validation

✅ **Header:**
- Includes usage instructions
- References plan document for context

✅ **Phase 0 (typical pattern):**
- Typically branch setup only (adapt for your workflow)
- Usually one task: Create git branch
- Task ID: `[P0.1]`
- Generally complete before Phase 1 (unless branch already exists)

✅ **Phase structure (all phases must have):**
- Header: `## Phase X: Descriptive Name`
- Goal: One-sentence description
- Deliverable: Concrete outcome
- Tasks: List of `[PX.Y]` tasks
- Checkpoint: System state after completion

✅ **Task ID format:**
- Pattern: `[PX.Y]`
- P = Phase prefix
- X = Phase number (0, 1, 2, ...)
- Y = Task number within phase (starts at 1, NOT 0)
- Sequential within phase (no gaps)
- Examples: `[P1.1]`, `[P1.2]`, `[P2.1]`

✅ **Task granularity:**
- Time: 15-30 minutes each
- Atomic: Complete in one go
- Testable: Can verify completion
- File-specific: References concrete files or components

✅ **Task ordering:**
- Dependencies come first
- Setup → Implementation → Testing → Validation
- Logical flow within phase

✅ **Checkpoint format:**
- 1-2 sentences
- Describes system capabilities and state
- Not just list of tasks completed

✅ **Content focus:**
- Contains execution steps (WHEN/HOW)
- Does NOT contain architectural rationale
- Does NOT contain design alternatives or lengthy context

## Document Synergy Validation

✅ **Separation of concerns:**
- Plan = WHY/WHAT (architecture, rationale)
- Tasklist = WHEN/HOW (execution, steps)
- No architectural rationale in tasklist
- No step-by-step execution in plan

✅ **Feature name consistency:**
- Plan filename matches tasklist filename
- Branch name derives from feature name
- All references use same feature name

✅ **Phase alignment:**
- Phase numbers match between documents
- Phase goals in tasklist reflect plan's architecture
- If plan mentions "Phase 2: Ranking", tasklist has similar

✅ **File reference consistency:**
- Files in plan's Project Structure appear in tasklist tasks
- `[CREATE]` markers have corresponding "Create X file" tasks
- `[MODIFY]` markers have corresponding "Update X file" tasks

## Quick Validation Checklist

Use this checklist before finalizing documents:

**Feature & Branching:**
- [ ] Feature name is kebab-case, 2-3 words
- [ ] Branch name follows `{prefix}-{feature-name}` format
- [ ] Filenames match: `{feature-name}-plan.md` and `{feature-name}-tasklist.md`

**Plan Document:**
- [ ] Includes all 5 required sections
- [ ] File tree uses `[CREATE]`/`[MODIFY]` markers
- [ ] Design decisions include WHY rationale
- [ ] Contains architectural context, NOT execution steps

**Tasklist Document:**
- [ ] Has usage header
- [ ] Phase 0 is branch setup only (single task `[P0.1]`)
- [ ] Task IDs follow `[PX.Y]` format, start at .1
- [ ] Tasks are 15-30 min, atomic, testable, file-specific
- [ ] Each phase has Goal, Deliverable, Tasks, Checkpoint
- [ ] Checkpoints describe system state in 1-2 sentences
- [ ] Contains execution steps, NOT architectural rationale

**Document Synergy:**
- [ ] WHY/WHAT in plan, WHEN/HOW in tasklist
- [ ] Feature names match across all files
- [ ] Phase numbers align between documents
- [ ] File references consistent (plan structure ↔ tasklist tasks)

## Validation Failures

If validation fails:

**Missing sections in plan:**
- Add the missing required sections
- Each section has specific purpose (see plan-structure.md)

**Phase 0 issues:**
- Ensure Phase 0 exists
- Ensure it contains only branch setup
- Ensure task ID is `[P0.1]`

**Task ID issues:**
- Check format: `[PX.Y]` not `[PX.0]` or `[X.Y]`
- Check sequential: no gaps in numbering
- Check starting point: each phase starts at .1

**Phase structure issues:**
- Add missing components (Goal, Deliverable, Tasks, Checkpoint)
- Follow exact format (see tasklist-structure.md)

**Synergy issues:**
- Move architectural rationale from tasklist to plan
- Move execution steps from plan to tasklist
- Align feature names across all files
- Match file references between documents

# CWF Design Principles

This document explains the design principles and architectural decisions behind Claude Workflow.

NOTE: will be moved to repo constitution. For agent under development.

## Core Design Principles

### Single Source of Truth

**Principle:** Each piece of knowledge lives in exactly one place.

**Application in CWF:**
- Domain knowledge → skills
- Workflow logic → commands
- Execution details → during implementation

**Why This Matters:**

When conventions change, update one skill file. All three commands using `cfw-planning` automatically benefit.

**Example:**
- Task structure rules live in `cfw-planning/references/tasklist-structure.md` only
- `/write-plan`, `/implement-plan`, and `/amend-plan` all reference this same source
- Update task conventions once → all commands use new conventions

**Anti-pattern:** Embedding task rules in each command, requiring three updates for one change.

---

### Orthogonality

**Principle:** Design components so changes to one don't require changes to others.

**Application in CWF:**
- Change skills → commands automatically benefit
- Change commands → skills remain unchanged
- Add new skills → no changes to existing commands

**Why This Matters:**

Components compose cleanly. Improve planning conventions without touching commands. Add new commands reusing existing skills.

**Example:**
- Update `cfw-planning` to support new task format
- `/write-plan` and `/implement-plan` automatically use new format
- No command code changes needed

**Anti-pattern:** Tight coupling where skill changes force command rewrites.

---

### Explicit Over Implicit

**Principle:** Make relationships and dependencies clear.

**Application in CWF:**
- Commands explicitly invoke skills by name
- Skills explicitly reference resources
- Data flow clearly visible

**Why This Matters:**

No hidden dependencies. Reading a command shows exactly what skills it loads. New contributors understand quickly.

**Example:**
```markdown
# In command
1. Load cfw-planning skill
2. Read plan and tasklist
3. Execute tasks
```

**Anti-pattern:** Commands assuming skills magically loaded, or skills with hidden resource dependencies.

---


## Architectural Decisions

### Why Skills Instead of Inline Knowledge?

**Decision:** Store planning conventions in `cfw-planning` skill, not embedded in commands

**Rationale:**

1. **Single Source of Truth**
   - Planning conventions in `cfw-planning` skill only
   - All three commands (`/write-plan`, `/implement-plan`, `/amend-plan`) use same knowledge
   - Update once, all benefit

   **Example:** Task ID format rules live in one place. Change from `[P1.1]` to `[Phase1.Task1]`? Update skill once, all commands use new format.

2. **Easy Updates**
   - Improve task conventions? Update skill once
   - All commands automatically benefit
   - No risk of inconsistencies between commands

   **Example:** Add new validation rule for phase goals. Update `cfw-planning/references/validation.md`. Next time any command loads the skill, it uses the new rule.

3. **Composable**
   - New commands reuse existing skills
   - Want `/validate-plan`? Just load `cfw-planning`
   - Want `/export-plan-to-pdf`? Reuse same skill

   **Example:** Future `/review-plan` command can load `cfw-planning` and get all conventions without duplicating knowledge.

4. **Testable**
   - Skills validated independently of commands
   - Ensure conventions correct before implementing commands
   - Can test skill content without running full workflow

   **Example:** Verify `plan-structure.md` has all required sections before building commands that rely on that structure.

**Why This Matters:**

Without skills, each command would embed its own copy of planning conventions. Three copies to maintain. Update task format? Change three files. Miss one? Inconsistent behavior. Debugging nightmare.

With skills, one source of truth. Update once, all commands benefit. Add commands without duplicating knowledge.

---

### Why Phase-Based Implementation?

**Decision:** Break features into sequential phases with review checkpoints

**Rationale:**

1. **Runnable Code at Each Step**
   - Code must be runnable after each phase
   - No "almost working" states
   - System always in known-good state
   - Can deploy or demo after any phase

   **Example:** After Phase 1 (models), system has working data layer. After Phase 2 (API), can use API endpoints. After Phase 3 (CLI), user-facing complete. Each phase independently valuable.

2. **Built-in Review Points**
   - Stop for user review between phases
   - Validate direction before continuing
   - Prevents wasted effort
   - Catch issues before they compound

   **Example:** Implement Phase 1 (authentication models). Review shows passwords stored as plaintext (security issue). Fix before building Phase 2 (API endpoints). If discovered later, would require rewriting both phases.

3. **Incremental Progress**
   - Each phase delivers concrete value
   - Phase 1 = core models, Phase 2 = API, Phase 3 = CLI
   - Independently valuable
   - Can ship partial features

   **Example:** Ship Phase 1-2 (models + API) as v1 for backend developers. Phase 3 (CLI) can wait for v2. Deliver value incrementally.

4. **Atomic Commits**
   - One commit per phase with clear checkpoint
   - Git history shows feature evolution
   - Easy to understand what changed when
   - Natural rollback points

   **Example:** Git log shows:
   ```
   feat(auth): Phase 3 - CLI interface complete
   feat(auth): Phase 2 - API endpoints working
   feat(auth): Phase 1 - Core models with validation
   feat(auth): Phase 0 - Create branch
   ```

   Need to revert CLI? Revert one commit. Clear, atomic changes.

5. **Risk Reduction**
   - Small phases = small changes
   - Easy to review, test, rollback if needed
   - Reduces integration problems
   - Lower cognitive load

   **Example:** Phase with 5 tasks (30 min each) vs. one task (2.5 hours). Small tasks easier to understand, review, and test. If problem found, smaller scope to debug.

**Why This Matters:**

Without phases, features implemented as one large chunk:
- No natural review points → wasted effort in wrong direction
- Code not runnable until end → integration problems discovered late
- Unclear progress → hard to estimate completion
- Large commits → difficult code review
- High risk → big changes hard to validate

With phases, clear structure and safety:
- Review after each phase → catch issues early
- Runnable code always → continuous validation
- Clear progress → know exactly where you are
- Small commits → easy review
- Low risk → incremental validation

**Alternative Considered:** Single large task list without phase boundaries.

**Rejected Because:**
- No natural stopping point for validation (when do you review?)
- Reviewers can't understand progress ("40% done" meaningless)
- Code may not be runnable until very end (integration risk)
- High risk of extended work in wrong direction (wasted effort)
- Difficult to estimate or track progress (unclear milestones)

---

## Design Patterns in Practice

### How Principles Work Together

The principles reinforce each other:

1. **Single Source + Skills** → Planning conventions in one place, loaded by all commands
2. **Orthogonality + Skills** → Update skills without touching commands
3. **Explicit + Commands** → Commands clearly show what skills they load
4. **Progressive Disclosure + Skills** → Load detailed specs only when needed
5. **Phase-Based + Review** → Stop at checkpoints, validate before continuing

**Result:** Maintainable system where changes are localized, relationships are clear, and context is managed efficiently.

### Example: Adding New Task Convention

**Scenario:** Want to add task time estimates to tasklist

**Without these principles:**
- Update `/write-plan` command code
- Update `/implement-plan` command code
- Update `/amend-plan` command code
- Update examples in multiple places
- Risk inconsistencies if miss one

**With these principles:**
1. Update `cfw-planning/references/tasklist-structure.md` (Single Source of Truth)
2. Done. All commands automatically use new convention (Orthogonality)
3. Commands explicitly load skill, so change flows through (Explicit)
4. New format in level 3 resource, only loaded if needed (Progressive Disclosure)

**One change, automatic propagation, no inconsistencies.**

---

## For More Information

- **Usage Guide:** See [cwf-workflow.md](cwf-workflow.md) for how to use CWF
- **Troubleshooting:** See [troubleshooting.md](troubleshooting.md) for common issues
- **Examples:** See `examples/` directory for complete plan/tasklist examples
- **Implementation:** See `skills/cfw-planning/SKILL.md` for detailed specifications

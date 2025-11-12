# Workflow Guide

Complete guide to using CWF commands. For CWF concepts and workflow, see `cwf-concepts.md`. For complete command reference, see `commands-reference.md`. For general skills/commands/agents pattern, see `concepts.md`.

## End-to-End Workflow

### 1. Planning Phase

**Goal:** Define feature scope and create structured implementation plan

**Process:**

1. **Enter plan mode** in Claude Code conversation
2. **Discuss the feature:**
   - What problem it solves
   - What's in scope / out of scope
   - High-level approach
   - Technical constraints
   - Dependencies and integration points
3. **Iterate until confident** in approach
4. **Run `/write-plan {feature-name}`:**
   - Command analyzes conversation
   - Creates `plans/{feature-name}-plan.md`
   - Creates `plans/{feature-name}-tasklist.md`
5. **Review generated documents:**
   - Check plan captures discussions
   - Verify tasklist has actionable tasks
   - Confirm phase breakdown makes sense

**Tips:**
- Take time in planning - it saves time in implementation
- Be explicit about scope boundaries
- Discuss alternatives and document WHY choices were made
- Break large features into smaller sub-features if needed

**Example:**
```
User: I want to add document search functionality with keyword filtering

[Discussion about approach, design, architecture...]

User: /write-plan query-command

[Creates plans/query-command-plan.md and plans/query-command-tasklist.md]
```

### 2. Implementation Phase

**Goal:** Execute plan phase-by-phase until feature complete

**Process:**

1. **Clear conversation history** (fresh context for implementation)
2. **Run `/implement-plan {feature-name}`:**
   - Command loads planning conventions (cfw-planning skill)
   - Command loads coding principles (read-constitution skill)
   - Command reads plan and tasklist
   - Command identifies first incomplete task
3. **Execute current phase:**
   - Implements each task sequentially
   - Marks tasks complete in tasklist ([x])
   - Runs tests and quality checks
   - Verifies code is runnable
4. **Phase completion:**
   - Command presents summary with ✅
   - Suggests conventional commit message
   - **STOPS and waits for approval**
5. **User reviews and approves:**
   - Reviews changes
   - Runs additional tests if needed
   - Commits changes (or asks Claude to)
   - Tells Claude to continue
6. **Repeat steps 3-5** until all phases complete

**Tips:**
- Clear conversation between phases to manage context
- Review code after each phase before continuing
- Commit after each phase (atomic progress)
- Stop and amend if discovered new requirements

**Example:**
```
User: /implement-plan query-command

[Phase 1 executes: Foundation layer]

Claude: Phase 1 Complete! ✅
Summary of changes:
✅ Created query/ module structure
✅ Implemented QueryModel with Pydantic
✅ Added validation and tests

Suggested commit:
feat(query): establish foundation layer

Stopping for review. Please approve before proceeding to Phase 2.

User: Looks good! continue

[Phase 2 executes: Parser implementation]
...
```

### 3. Amendment Cycle

**Goal:** Update plan mid-implementation when requirements change

**When to Amend:**
- Discovered new requirements during implementation
- Realized better approach while coding
- Need to add tasks to current phase
- Want to add new phases
- Need to clarify plan details

**Process:**

1. **Discuss changes** in current conversation
2. **Run `/amend-plan {feature-name}`:**
   - Command loads planning conventions
   - Command reads existing plan and tasklist
   - Command analyzes conversation for changes
   - Command identifies current progress state
3. **Command proposes amendments:**
   - Shows specific changes to plan
   - Shows tasks to add/modify in tasklist
   - Performs safety check (no completed task changes)
   - **Waits for confirmation**
4. **User confirms or clarifies**
5. **Command applies amendments:**
   - Updates plan.md with new content
   - Adds tasks to tasklist.md
   - Creates new phases if needed
6. **Continue implementation:**
   - Run `/implement-plan {feature-name}` again
   - Resumes from first incomplete task

**Safety Rules:** See `cwf-concepts.md` for complete amendment rules and constraints.

**Tips:**
- Amend early when you discover issues
- Better to add phases than cram into existing
- Document WHY amendment was needed
- Review amended tasklist before resuming

**Example:**
```
User: I realized we need caching for query results

[Discussion about caching approach]

User: /amend-plan query-command

Claude: Based on conversation, I understand you want to:
- Add "Caching Strategy" section to plan
- Add tasks [P3.4]-[P3.6] to Phase 3 for cache implementation

Safety check: ✅ Phase 3 is incomplete, amendments allowed

Proceed with these changes?

User: Yes

Claude: Amendments Applied ✅
- Added caching section to plan
- Added 3 new tasks to Phase 3

User: /implement-plan query-command

[Resumes implementation with new tasks]
```

## Best Practices

### Planning

**Do:**
- Spend adequate time discussing and refining approach
- Document WHY behind decisions, not just WHAT
- Break down features into 15-30 min tasks
- Define clear phase boundaries with testable deliverables
- Specify which files will be created/modified
- Include scope boundaries (what's NOT included)

**Don't:**
- Rush through planning to start coding faster
- Skip documenting alternatives considered
- Create tasks that are too large or vague
- Mix setup and implementation in same phase
- Leave technical decisions ambiguous

### Implementation

**Do:**
- Clear conversation history between phases
- Review and test after each phase
- Commit after phase completion
- Mark tasks complete immediately in tasklist
- Stop and amend if requirements change
- Follow constitution principles (DRY, YAGNI, type hints)
- Run quality checks (ruff, mypy, tests)

**Don't:**
- Skip ahead to future phases
- Leave phases partially complete
- Batch multiple phase completions
- Modify completed tasks
- Ignore failing tests
- Commit without review

### Amendments

**Do:**
- Amend early when discovering issues
- Discuss changes clearly before amending
- Add new phases rather than expanding existing
- Document rationale for amendments
- Review amended tasklist before resuming

**Don't:**
- Try to modify completed work
- Skip confirmation step
- Make amendments without discussion
- Change task IDs
- Delete historical decisions

### General

**Do:**
- Use descriptive feature names (kebab-case)
- Keep feature scope focused and manageable
- Break large features into sub-features
- Review generated plans before implementing
- Maintain runnable code after each phase
- Clear conversation history to manage context

**Don't:**
- Create overly large features
- Skip planning phase
- Ignore phase checkpoints
- Continue without reviewing phases
- Let conversation context grow too large

## Common Workflows

### Simple Feature (Single Session)

```
1. Plan mode discussion
2. /write-plan feature-name
3. Review plan and tasklist
4. /implement-plan feature-name
5. [All phases execute]
6. Feature complete
7. Final commit and merge
```

### Complex Feature (Multiple Sessions)

```
Session 1:
1. Plan mode discussion
2. /write-plan feature-name
3. Review and refine

Session 2:
1. /implement-plan feature-name
2. [Phase 1-2 complete]
3. Commit progress

Session 3:
1. /implement-plan feature-name (resumes)
2. [Phase 3-4 complete]
3. Feature complete
```

### Feature with Mid-Implementation Changes

```
1. /write-plan feature-name
2. /implement-plan feature-name
3. [Phase 1-2 complete]
4. [Discover new requirement]
5. Discuss changes
6. /amend-plan feature-name
7. /implement-plan feature-name (resumes)
8. [Complete amended phases]
9. Feature complete
```

### Incremental Feature Development

```
1. /write-plan feature-v1 (basic version)
2. /implement-plan feature-v1
3. Complete and merge

4. /write-plan feature-v2 (enhancements)
5. /implement-plan feature-v2
6. Complete and merge

[Repeat as needed]
```

## Troubleshooting

### Plan not capturing discussion

**Problem:** Generated plan missing key details

**Solution:**
- Be more explicit in planning discussion
- Reference specific technical details
- Mention files, components, approaches explicitly
- Amend plan after creation to add missing sections

### Tasks too large

**Problem:** Tasks taking >30 minutes

**Solution:**
- Amend tasklist to break down large tasks
- Add intermediate tasks with clearer steps
- Reference specific files/components in descriptions

### Lost context mid-implementation

**Problem:** Claude forgot earlier phases

**Solution:**
- Read plan document (has full context)
- Check tasklist for progress
- Continue from first incomplete task
- Clear conversation and restart /implement-plan

### Need to change completed work

**Problem:** Want to modify finished phase

**Solution:**
- Cannot modify completed tasks (immutable)
- Add new phase for refactoring
- Add tasks to current incomplete phase
- Document why changes needed in plan

### Unclear what command to use

**Problem:** Unsure which command fits situation

**Solution:**
- Planning? → /write-plan
- Implementing? → /implement-plan
- Changing plans? → /amend-plan
- Need principles? → /read-constitution

### Feature scope too large

**Problem:** Plan has 8+ phases

**Solution:**
- Break into multiple smaller features
- Create feature-v1, feature-v2, etc.
- Focus each feature on single capability
- Implement incrementally
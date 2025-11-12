# Command Reference

Complete API-style reference for all CWF commands. For workflow examples and step-by-step guides, see [workflow-guide.md](workflow-guide.md). For command concepts, see [cwf-concepts.md](cwf-concepts.md).

## /write-plan

**Purpose:** Create plan and tasklist from planning discussion

**Usage:** `/write-plan {feature-name}`

**When to Use:**
- After discussing feature in plan mode
- When ready to formalize architecture and approach
- Before starting implementation

**What It Does:**
1. Loads cfw-planning skill
2. Analyzes conversation history
3. Creates `plans/{feature-name}-plan.md`
4. Creates `plans/{feature-name}-tasklist.md`
5. Validates structure against skill's validation reference

**Required Input:**
- Feature name in kebab-case OR
- Suggestion based on conversation (if name not provided)

**Output:**
- Two markdown files in plans/ directory
- Plan with architecture and rationale
- Tasklist with phase breakdown and task IDs

## /implement-plan

**Purpose:** Execute implementation phase-by-phase

**Usage:** `/implement-plan {feature-name}`

**When to Use:**
- After creating plan and tasklist
- When resuming implementation after break
- After amending plan

**What It Does:**
1. Loads cfw-planning skill (implementation-essentials.md)
2. Loads read-constitution skill
3. Reads and validates plan and tasklist documents
4. Finds first incomplete task
5. Executes tasks sequentially
6. Marks completed tasks with [x]
7. Stops at phase boundaries for review

**Required Input:**
- Feature name matching existing plan files

**Output:**
- Implemented code
- Updated tasklist with progress
- Test results
- Phase completion summaries

## /amend-plan

**Purpose:** Update existing plan and tasklist

**Usage:** `/amend-plan {feature-name}`

**When to Use:**
- Mid-implementation when requirements change
- When adding tasks to incomplete phases
- When creating new phases
- When clarifying plan sections

**What It Does:**
1. Loads cfw-planning skill (amendment.md)
2. Reads existing plan and tasklist
3. Analyzes conversation for changes
4. Proposes specific amendments
5. Waits for confirmation
6. Applies changes following amendment safety rules

**Required Input:**
- Feature name matching existing plan files
- Conversation discussing desired changes

**Output:**
- Updated plan.md
- Updated tasklist.md with new/modified tasks
- Amendment summary

**Safety Features:**
- Blocks modifications to completed work
- Explains why operations not allowed
- Suggests alternatives for blocked changes

## /read-constitution

**Purpose:** Load coding principles into context

**Usage:** `/read-constitution`

**When to Use:**
- Start of implementation session
- When need reminder of principles
- When reviewing code quality

**What It Does:**
1. Invokes read-constitution skill
2. Skill reads all `.constitution/*.md` files
3. Loads principles into context

**Required Input:** None

**Output:**
- Confirmation that constitution loaded
- Principles available for reference

**Automatically Loaded By:**
- `/implement-plan` command (during bootstrap)

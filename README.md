# Claude Workflow

Experimental plan/spec-driven development workflow for Claude Code with phase-based implementation. The intent for this repo is to be a playground for me to investigate Agent driven development.


**Spec Driven Development tools/workflows/alternatives:**
* [spec-kit](https://github.com/github/spec-kit): Provides a specify->clarify->plan->task->analyze->implement workflow with thourough spec creation.
* [spec-kitty](https://github.com/Priivacy-ai/spec-kitty): built on spec-kit. Adds tracking through dashboard.
* [superclaude](https://github.com/SuperClaude-Org/SuperClaude_Framework/tree/master): brainstorm->write plan->implement workflow. Uses Claude Skills and pre session hook to provide context.
* [cc-sessions](https://github.com/GWUDCAP/cc-sessions): another workflow, but less documented.
* [superpowers](https://github.com/obra/superpowers): brainstorm->write plan -> implement workflow w. skills, commands and agents.

**Other resources:**
* Martin Fowlers post on Spec Driven Development: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html


**Current thoughts:**

The workflow `brainstorm/plan -> write phase based plan -> review plan -> implement phase -> review phase -> next phase until done`, with an additional `amend plan` step during development, seems to be the way to go. All the alternatives above implement this workflow in some way or another.

## What This Repo Provides

**Slash Commands** (.claude/commands/):
- `/read-constitution` - Load all constitution documents into context
- `/write-plan` - Create plan and tasklist from planning discussion
- `/implement-plan` - Execute plan one phase at a time
- `/amend-plan` - Update plans during development

**Coding Constitution**:
```
.constitution/
├── software-engineering.md   # Universal software engineering principles
└── python-standards.md       # Python-specific standards and idioms
```

## Installation

### With uv/uvx (Recommended)

[uv](https://docs.astral.sh/uv/) is a fast Python package installer and resolver.

#### Option 1: Run without installing (uvx)

```bash
# Run without installing (using uvx with git URL)
uvx --from git+https://github.com/tordks/claude-workflow.git claude-workflow install /path/to/project

# Update existing installation
uvx --from git+https://github.com/tordks/claude-workflow.git claude-workflow update /path/to/project
```

#### Option 2: Install with uv tool

```bash
# Install the tool globally with uv
uv tool install git+https://github.com/tordks/claude-workflow.git

# Use the installed command
claude-workflow install /path/to/project

# Update existing installation
claude-workflow update /path/to/project

# Upgrade the tool itself
uv tool upgrade claude-workflow
```

### CLI Options

- `--dry-run` - Preview what would be installed without making changes
- `--force` - Overwrite user-modified files during update


### After Installation

1. Edit `CLAUDE.md` with your project-specific details
2. Review constitution documents in `.constitution/` (software-engineering.md, python-standards.md)
3. Run `/read-constitution` to load the constitution into your first development session
4. Configure quality checks in your `pyproject.toml` if needed

## Development Workflow

### Workflow Summary

0. Run `/read-constitution` to read the constitution into context
1. Plan feature in plan mode
2. Use `/write-plan {feature-name}` to create plan and tasklist
3. Review `plans/{feature-name}-plan.md` and `plans/{feature-name}-tasklist.md`
4. Use `/implement-plan {feature-name}` to implement next unfinished phase
5. Review changes and commit manually
6. Clear conversation history (optional but recommended for context management)
7. Repeat steps 4-6 until all phases are complete

**To amend during development**: Use `/amend-plan {feature-name}` after discussing changes in plan mode.

### Why Clear Conversation History?

Clearing conversation history between phases or before amendment helps:
- Manage token limits on long features
- Keep context focused on current phase
- Prevent Claude from getting confused by earlier discussion

The workflow is resumable - `/implement-plan` reads the tasklist to know where to continue.

### Creating project plans

1. Enter plan mode and discuss your feature with Claude
2. Use `/write-plan {feature-name}` to generate:
   - `plans/{feature-name}-plan.md` - Detailed implementation plan with phases
   - `plans/{feature-name}-tasklist.md` - Tracking checklist for each phase
3. Review both files to ensure the plan matches your requirements

### Implementing plans

1. Use `/implement-plan {feature-name}` to execute the next incomplete phase
2. Claude will:
   - Read the tasklist to determine current progress
   - Implement the next phase following constitution guidelines
   - Run quality checks (type checking, linting, tests)
   - Provide a checkpoint with suggested commit message
3. Review the changes and commit manually
4. Clear conversation history (optional but recommended)
5. Repeat steps 1-4 until all phases are complete

### Amending Plans (Optional - Anytime During Development)

1. Enter plan mode and discuss needed changes with Claude
2. Use `/amend-plan {feature-name}` to update the plan
3. Claude will:
   - Read the existing plan and tasklist
   - Incorporate your changes
   - Update both `plans/{feature-name}-plan.md` and `plans/{feature-name}-tasklist.md`
   - Preserve completed phases while adjusting remaining work
4. Continue with `/implement-plan {feature-name}` using the updated plan

## Example Session

```bash
# Step 1-2: Plan in plan mode
> "I want to add user authentication"
[Discussion about approach, requirements, etc.]

# Step 3: Write plan
> /write-plan user-auth
Created: plans/user-auth-plan.md
Created: plans/user-auth-tasklist.md

# Step 4: Review plan files
# (Review the generated markdown files)

# Step 5: Implement first phase
> /clear
> /implement-plan user-auth

Phase 0 Complete
- Created branch: feat-user-auth
[Checkpoint with suggested commit]

# Step 6: Approve
> continue

Phase 1 Complete
- Implemented authentication models
- Added type hints and validation
[Checkpoint with suggested commit]

# Step 7: Review and commit
# (Commit changes)

# Step 8: Clear history and continue
> /clear
> /implement-plan user-auth

Resuming from Phase 2...

Phase 2 Complete
- Implemented auth endpoints
- Added error handling
[Checkpoint]

> continue

All phases complete!
```

## TODO
To test:
- Test superpowers, seems to be more lightweight than spec-kit
- fork and adapt superpowers?

Improvements:
  - Add a more defined plan and tasklist structure. Plan should provide context, while the tasklist phase division and bite-sized tasks.
  - Add skills that can be read on demand, to avoid manual steps and selectively update context.
    - See superpowers for examples
    - eg:
      - read-constitution (allows for selectively reading relevant parts)
      - review-plan
      - etc.

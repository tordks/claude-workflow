# Claude Workflow

Experimental plan-driven development workflow for Claude Code with phase-based implementation and automated quality checks.

Inspired by [spec-kit](https://github.com/github/spec-kit), which is more thorough in documenting features, but also heavier to use. The intent for this repo is to be a (slightly opinionated) Claude Code specific workflow.

## What This Repo Provides

**Slash Commands** (.claude/commands/):
- `/write-plan` - Create plan and tasklist from planning discussion
- `/implement-plan` - Execute plan one phase at a time
- `/amend-plan` - Update plans during development

**Coding Constitution**:
```
.constitution/
├── README.md                     # Overview and quick reference
├── workflow.md                   # Development protocols
├── principles/
│   ├── software-engineering.md   # Universal principles
│   └── python-standards.md       # Python-specific standards
└── tools/
    ├── uv.md                     # Package and dependency management
    ├── ruff.md                   # Linting and code formatting
    ├── mypy.md                   # Static type checking
    └── pre-commit.md             # Git hooks and automated quality checks
```

**Template**: CLAUDE.md for project-specific instructions

## Installation

```bash
# Copy files to your project
cp -r .constitution /path/to/project/
cp -r .claude /path/to/project/

# Install pre-commit hooks
cd /path/to/project
uv sync  # or: pip install pre-commit
pre-commit install

# Customize CLAUDE.md from templates/CLAUDE.md.template
# This file provides Claude with project-specific context and instructions
cp templates/CLAUDE.md.template /path/to/project/CLAUDE.md
# Edit CLAUDE.md with your project details
```

**Note**: Configure quality checks in your `pyproject.toml`. Add description of tol usage to constitution/tools/`.

## Development Workflow

### Workflow Summary

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

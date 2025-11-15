# CWF Plugin Repository Context

You are in the **claude-workflow repository**, which distributes the Claude Workflow (CWF) plugin for Claude Code.

## Repository Purpose

**This repository IS the CWF plugin.**

Your role depends on the user's intent:

**If the user is browsing/evaluating the plugin:**
- Explain what CWF provides (plan-driven workflow with phase-based implementation)
- Reference README.md for detailed documentation
- Show available commands: /write-plan, /implement-plan, /amend-plan

**If the user is developing/contributing to the plugin:**
- They should run `/prime-cwf-dev` to load development skills
- Development context is provided by this file (CLAUDE.md) and README.md
- Changes made here will be distributed to all plugin users

## What CWF Provides to Users

When users install this plugin (`/plugin install cwf@claude-workflow`), they get:
- **Commands**: /write-plan, /implement-plan, /amend-plan, /read-constitution, /create-claude-md
- **Skills**: cfw-planning (workflow knowledge), read-constitution (coding standards)
- **Workflow**: Plan-driven development with preserved context across sessions

## CWF Workflow (Quick Reference)

The plugin provides a plan-driven workflow:

1. **Planning** (plan mode discussion) → `/write-plan <feature>`
   - Creates plan.md (WHY/WHAT: architectural decisions, design rationale, checkpoint strategy)
   - Creates tasklist.md (WHEN/HOW: phase-by-phase execution steps with checkpoints)

2. **Implementation** → `/implement-plan <feature>`
   - Works phase-by-phase through tasklist
   - Each phase ends with checkpoints (self-review; code quality and complexity if project uses those tools)
   - Stops at phase boundaries for human review after checkpoint validation
   - User runs `/clear` between phases to manage context

3. **Amendment** → `/amend-plan <feature>` (if requirements change)
   - Safely updates plan and tasklist
   - Preserves completed work

## Repository Structure

**Plugin Identity:**
- Repository: `tordks/claude-workflow`
- Plugin name: `cwf@claude-workflow`
- Installation: `/plugin install cwf@claude-workflow`
- Purpose: Provides plan-driven development workflow to Claude Code users

**What Gets Distributed to Users:**
```
claude-workflow/
├── commands/              → User slash commands (distributed)
│   ├── write-plan.md      → /write-plan command
│   ├── implement-plan.md  → /implement-plan command
│   ├── amend-plan.md      → /amend-plan command
│   ├── read-constitution.md → /read-constitution command
│   └── create-claude-md.md  → /create-claude-md command
├── skills/                → Plugin skills (distributed)
│   ├── cfw-planning/      → Planning workflow knowledge (critical for understanding specs)
│   └── read-constitution/ → Constitution loader
├── .claude-plugin/        → Plugin metadata (distributed)
│   ├── plugin.json        → Plugin manifest
│   └── marketplace.json   → Marketplace configuration
├── .constitution/         → Example constitution files (distributed)
```

**Development-Only (NOT distributed):**
```
.claude/
```

**Development vs User Context:**

When developing (you):
- Work IN this repository
- Modify specifications, commands, and skills
- Use `/prime-cwf-dev` to load development skills
- Changes you make will be distributed to users

When users install:
- Run `/plugin install cwf@claude-workflow` in their projects
- Get access to /write-plan, /implement-plan, /amend-plan commands
- Can load `cfw-planning` and `read-constitution` skills
- Use CWF workflow in their own projects, not this repo

**Release Process:**
1. Make changes in this repository
2. Test locally (update version in `.claude-plugin/plugin.json`)
3. Commit and tag release (e.g., `v0.2.0`)
4. Users update with `/plugin update cwf@claude-workflow`

## Design Principles

Understanding these principles helps you make consistent development decisions aligned with CWF's architecture.

### Single Source of Truth

**Principle:** Each piece of knowledge lives in exactly one place.

**Application in CWF:**
- Domain knowledge → skills
- Workflow logic → skills
- Workflow execution → commands

**Why This Matters:** When conventions change, update one skill file. All commands using `cfw-planning` automatically benefit.

**Example:** Task structure rules live in `cfw-planning/references/tasklist-spec.md` only. `/write-plan`, `/implement-plan`, and `/amend-plan` all reference this same source. Update task conventions once → all commands use new conventions.

**Anti-pattern:** Embedding task rules in each command, requiring three updates for one change.

### Orthogonality

**Principle:** Design components so changes to one don't require changes to others.

**Application in CWF:**
- Change skills → commands automatically benefit
- Change commands → skills remain unchanged
- Add new skills → no changes to existing commands

**Why This Matters:** Components compose cleanly. Improve planning conventions without touching commands. Add new commands reusing existing skills.

**Example:** Update `tasklist-spec` to support new task format → `/write-plan` and `/implement-plan` automatically use new format → no command code changes needed.

**Anti-pattern:** Tight coupling where skill changes force command rewrites.


### Explicit Over Implicit

**Principle:** Make relationships and dependencies clear.

**Application in CWF:**
- Commands explicitly invoke skills by name
- Skills explicitly reference resources
- Data flow clearly visible

**Why This Matters:** No hidden dependencies. Reading a command shows exactly what skills it loads. New contributors understand quickly.

**Example:** Commands use bootstrap pattern: "1. Load cfw-planning skill, 2. Read plan and tasklist, 3. Execute tasks"

**Anti-pattern:** Commands assuming skills magically loaded, or skills with hidden resource dependencies.


## Development Areas

The claude-workflow repository consists of:

### Core Specifications
- `skills/cfw-planning/references/plan-spec.md` - Plan document specification (RFC 2119)
- `skills/cfw-planning/references/tasklist-spec.md` - Tasklist document specification (RFC 2119)
- `skills/cfw-planning/references/conventions.md` - Feature naming and file structure
- `skills/cfw-planning/references/parsing-arguments.md` - Command argument parsing
- `skills/cfw-planning/references/amendment.md` - Amendment safety rules

### Skills
- `skills/cfw-planning/` - Core CWF planning knowledge repository
- `skills/read-constitution/` - Constitution loader skill
- `.claude/skills/writing-conformant-specs/` - RFC 2119 spec writing guidance (dev-only)

### Commands
- `commands/write-plan.md` - Plan creation workflow
- `commands/implement-plan.md` - Implementation workflow
- `commands/amend-plan.md` - Plan amendment workflow
- `commands/read-constitution.md` - Constitution loading
- `commands/create-claude-md.md` - CLAUDE.md template generation

### Plugin Configuration
- `.claude-plugin/plugin.json` - Plugin manifest
- `.claude-plugin/marketplace.json` - Marketplace configuration

### Documentation
- `README.md` - Main documentation and usage guide
- `docs/design-principles.md` - Architectural decisions and rationale
- `docs/backlog.md` - Feature backlog and planned improvements

### Constitution
- `.constitution/software-engineering.md` - Engineering principles (DRY, YAGNI, orthogonality)
- `.constitution/testing.md` - Testing philosophy and coverage expectations
- `.constitution/python-standards.md` - Python conventions

## Key Development Guidelines

### When working on specifications (plan-spec.md, tasklist-spec.md):
- Maintain RFC 2119 conformance (use MUST/SHOULD/MAY keywords correctly)
- Apply RFC 2119 decision tree from writing-conformant-specs skill
- Use proper keyword capitalization (MUST, SHOULD, MAY)
- Separate normative requirements from informative content
- Label informative sections explicitly: "(Informative)", "Best Practice:", "Example:"
- Validate changes against RFC 2119 checklist

### When working on skills:
- Follow single source of truth principle
- Maintain orthogonality between skill components
- Keep references self-contained and focused
- Update SKILL.md descriptions when changing structure
- Follow Claude Code skill patterns from developing-claude-code-plugins

### When working on commands:
- Follow bootstrap pattern: load skills first, then execute
- Reference skill knowledge, don't duplicate content
- Keep workflow logic clear and explicit
- Use standard argument parsing from parsing-arguments.md
- Test with actual CWF usage scenarios
- Follow Claude Code command conventions

### When working on plugin configuration:
- Maintain plugin.json with correct version, dependencies, structure
- Follow Claude Code plugin specification from working-with-claude-code
- Test plugin installation and loading
- Validate marketplace.json if distributing

### When working on documentation:
- Keep README as entry point for users
- Document design decisions in design-principles.md
- Update examples when changing specifications
- Maintain consistency with loaded skills
- Update documentation when needed, ie.
  - New skills or commands are introduced
  - Intent or purpose of existing skills/commands changes
  - Workflow behavior changes
- Implementation-only changes (no intent/workflow change) do not require documentation updates

## Development Workflow Pattern

CWF development follows its own workflow:

```
Identify need → Plan in plan-mode → Write/Edit → Test → Validate → Commit
```

For major changes:
1. Discuss approach in plan mode
2. Use `/write-plan` if needed for complex features
3. Implement following CWF principles and loaded constitution
4. Test with actual usage scenarios
5. Validate specifications with writing-conformant-specs guidance
6. Update documentation
7. Commit with clear message

## Responding to Users

**For questions about using CWF:**
- Reference README.md for detailed documentation
- Explain workflow: plan → implement → amend
- Show command usage examples

**For development/contribution questions:**
- Direct them to run `/prime-cwf-dev` to load development skills
- This file (CLAUDE.md) provides repository structure and guidelines
- README.md provides user-facing documentation

**For general inquiries:**
- This plugin solves: lost context, inconsistent structure, changing requirements, loss of control
- Best for: multi-session work, complex features, work requiring checkpoints

# CWF Plugin Repository Context

You are in the **claude-workflow repository**, which distributes the Claude Workflow (CWF) plugin for Claude Code.

## Repository Purpose

**This repository IS the CWF plugin.** For workflow documentation, see README.md.

**Documentation by audience:**

- **README.md** - User entrypoint (how to install and use CWF)
- **SKILL.md** (`plugins/cwf/skills/claude-workflow/`) - Agent workflow knowledge (loaded when executing CWF commands)
- **CLAUDE.md** - Development context (loaded when working in this repository)

## Repository Structure

**Plugin Identity:**

- Repository: `tordks/claude-workflow`
- Plugin name: `cwf@claude-workflow`
- Installation: `/plugin install cwf@claude-workflow`
- Purpose: Provides plan-driven development workflow to Claude Code users

**Project Structure:**

```text
claude-workflow/
├── plugins/                    → Plugin packages (distributed to users)
│   └── cwf/                    → CWF plugin
│       ├── .claude-plugin/
│       │   └── plugin.json         → Plugin manifest
│       ├── commands/               → User slash commands
│       │   ├── write-plan.md
│       │   ├── implement-plan.md
│       │   ├── amend-plan.md
│       │   ├── brainstorm.md
│       │   └── read-constitution.md
│       └── skills/                 → Plugin skills
│           ├── claude-workflow/    → Planning workflow knowledge
│           └── read-constitution/  → Constitution loader
├── .claude-plugin/             → Marketplace configuration
│   └── marketplace.json            → Points to plugins/cwf
├── .claude/                    → Development-only (NOT distributed)
├── .constitution/              → CWF project-specific constitution
├── .constitution-examples/     → Example constitution files for users
```

## Quality checks

Run pre-commit in a subagent after making changes. If there are
linting/formatting issues, the subagent should fix them:

```bash
uvx pre-commit run
```

## Development Areas

The claude-workflow repository consists of:

### Core Specifications

- `plugins/cwf/skills/claude-workflow/references/plan-spec.md` - Plan document specification (RFC 2119)
- `plugins/cwf/skills/claude-workflow/references/tasklist-spec.md` - Tasklist document specification (RFC 2119)
- `plugins/cwf/skills/claude-workflow/references/conventions.md` - Feature naming and file structure
- `plugins/cwf/skills/claude-workflow/references/parsing-arguments.md` - Command argument parsing
- `plugins/cwf/skills/claude-workflow/references/amendment.md` - Amendment safety rules

### Skills

- `plugins/cwf/skills/claude-workflow/` - Core CWF planning knowledge repository
- `plugins/cwf/skills/read-constitution/` - Constitution loader skill
- `.claude/skills/writing-conformant-specs/` - RFC 2119 spec writing guidance (dev-only)

**Important:** Skills are self-contained knowledge packages. When an agent loads a skill (e.g., `claude-workflow`), it only sees files under that skill's directory (`plugins/cwf/skills/claude-workflow/`). This is why `claude-workflow` contains all workflow knowledge in `SKILL.md` and `references/` - it cannot reference files outside its directory. Skills are the complete CWF workflow knowledge shipped to agents.

### Commands

- `plugins/cwf/commands/brainstorm.md` - Feature exploration workflow
- `plugins/cwf/commands/write-plan.md` - Plan creation workflow
- `plugins/cwf/commands/implement-plan.md` - Implementation workflow
- `plugins/cwf/commands/amend-plan.md` - Plan amendment workflow
- `plugins/cwf/commands/read-constitution.md` - Constitution loading

### Plugin Configuration

- `plugins/cwf/.claude-plugin/plugin.json` - Plugin manifest
- `.claude-plugin/marketplace.json` - Marketplace configuration

### Documentation

- `README.md` - Main documentation and usage guide
- `docs/design-principles.md` - Architectural decisions and rationale
- `docs/backlog.md` - Feature backlog and planned improvements

### Constitution

- `.constitution/cwf-principles.md` - Design philosophy (Single Source of Truth, Orthogonality, Explicit Over Implicit)
- `.constitution/cwf-guidelines.md` - Component development guidelines
- `.constitution/rfc-2119.md` - RFC 2119 conformance rules
- `.constitution/cwf-workflow.md` - Development workflow pattern
- `.constitution-examples/` - Example constitution files for users

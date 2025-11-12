# Claude Workflow

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/tordks/claude-workflow/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.com/claude-code)

Plan-driven development workflow for Claude Code with phase-based implementation.

## Quick Start

1. **Install:** `/plugin marketplace add tordks/claude-workflow && /plugin install cwf`
2. **Plan:** Discuss your feature in conversation
3. **Create plan:** `/write-plan {feature-name}`
4. **Implement:** `/implement-plan {feature-name}`
5. **Update as needed:** `/amend-plan {feature-name}`

→ See [Workflow Guide](docs/workflow-guide.md) for complete usage instructions and examples.

## Core Concepts

**Plans & Tasklists** - Complementary documents that guide implementation
- **Plan:** WHY and WHAT (architecture, design decisions, rationale)
- **Tasklist:** WHEN and HOW (phases, tasks, step-by-step execution)
- Created together, used together

→ See [CWF Concepts](docs/cwf-concepts.md) for definitions and structure.

**Phase-Based Implementation** - Break work into reviewable chunks
- Each phase has goal, deliverable, tasks ([PX.Y] IDs), checkpoint
- Code must be runnable after each phase
- Stop for review between phases

→ See [CWF Concepts](docs/cwf-concepts.md) for phase and task details.

**Skills-First Architecture** - Knowledge separated from workflows
- **Skills:** Planning conventions (cfw-planning), coding principles (read-constitution)
- **Commands:** /write-plan, /implement-plan, /amend-plan
- **Agents:** Claude Code's agents execute following loaded guidance

→ See [Concepts](docs/concepts.md) for general pattern, [CWF Concepts](docs/cwf-concepts.md) for CWF specifics.

## Commands

| Command | Description |
|---------|-------------|
| `/write-plan {feature-name}` | Create plan and tasklist from discussion |
| `/implement-plan {feature-name}` | Execute plan phase-by-phase |
| `/amend-plan {feature-name}` | Update plan during implementation |
| `/read-constitution` | Load coding principles manually |

→ See [Workflow Guide](docs/workflow-guide.md) for detailed command usage, options, and examples.

## What This Provides

**2 Skills** - Planning conventions (cfw-planning) and coding principles (read-constitution)

**4 Commands** - /write-plan, /implement-plan, /amend-plan, /read-constitution

**Coding Constitution** - Principles in `.constitution/` directory:
- `software-engineering.md` - DRY, YAGNI, orthogonality, fail-fast, separation of concerns
- `testing.md` - Testing philosophy, what to test/skip, test quality
- `python-standards.md` - PEP 8, type hints, modern idioms

→ See [Skills Reference](docs/skills-reference.md) for what each skill contains.

## Documentation

**Get Started:**
- [Workflow Guide](docs/workflow-guide.md) - How to use CWF step-by-step

**Understand CWF:**
- [CWF Concepts](docs/cwf-concepts.md) - Plans, phases, workflow, architecture
- [Concepts](docs/concepts.md) - General skills/commands/agents pattern
- [Commands Reference](docs/commands-reference.md) - Complete command API reference

**Future:**
- [Future Phases](docs/future-phases.md) - Roadmap, Phase 1+ features, v2 vision

## Installation

In Claude Code:

```bash
/plugin marketplace add tordks/claude-workflow
/plugin install cwf
```

## Example Session

```bash
# Plan your feature
> "I want to add user authentication"
[Discussion about approach, requirements...]

# Create plan and tasklist
> /write-plan user-auth
Created: plans/user-auth-plan.md
Created: plans/user-auth-tasklist.md

# Review files, then implement
> /implement-plan user-auth

Phase 0 Complete ✅
- Created branch: feat-user-auth

> continue

Phase 1 Complete ✅
- Implemented authentication models
- Added validation and tests

# Commit, then continue
> /implement-plan user-auth

Phase 2 Complete ✅
- Implemented auth endpoints
...
```

## Alternatives & Resources

**Similar Tools:**
- [spec-kit](https://github.com/github/spec-kit) - Specify→clarify→plan→task→implement workflow
- [superclaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Brainstorm→plan→implement with skills
- [superpowers](https://github.com/obra/superpowers) - Plan-driven workflow with skills, commands, agents
- [BMAD-method](https://github.com/bmad-code-org/BMAD-METHOD) - Multi-scale planning framework

**Resources:**
- [awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) - Skill collection
- [Martin Fowler on Spec-Driven Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

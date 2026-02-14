# Claude Workflow

[![Version](https://img.shields.io/badge/version-0.2.2-blue.svg)](https://github.com/tordks/claude-workflow/releases)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.com/claude-code)

Claude Workflow (CWF) defines a plan-driven development workflow for Claude Code with phase-based implementation.

CWF is my personal exploration of agent development workflows. Other frameworks vary in rigor and documentation requirements, but most share the core concept of persisting specifications to maintain context between session. See links to other resources below.

## What Problem Does CWF Solve?

AI-assisted development faces two core challenges:

1. **Context is lost between sessions.** When a session ends or context is compacted, everything the agent learned disappears. Architectural decisions, implementation progress and requirements that were refined during development are no longer available. The next session starts from scratch, forcing the agent to re-derive what was already decided.

2. **Developers lose ownership of the codebase.** Agents can produce large volumes of code from brief instructions. Without a pre-prepared plan/spec and checkpoints for review, developers cannot follow what was built or verify that it matches their intent. Problems compound silently across files, and the codebase accumulates code that nobody fully understands.

CWF addresses both. Persistent plan documents preserve decisions and progress across sessions, so agents always have the full picture. Phase-based implementation with human review and code quality/complexity checks between each phase keeps the developer in control of every change and ensures the codebase remains maintainable.

## The Workflow

Based on an input context (specification, design discussion, or brainstorm), CWF produces a plan and tasklist that break down the work into phases with runnable deliverables. The agent implements phase-by-phase, running quality checkpoints and pausing for human review before proceeding to the next phase.

Each phase is started manually with `/implement-plan`, which continues from the next incomplete task and accepts free-form instructions to control scope. This allows you to pause and resume implementation across sessions without losing context or progress.

```text
       input context (plan draft, design discussion, specification file)
               │
               ├── /brainstorm (optional: structured exploration
               │                to extract requirements and
               │                design decisions)
               ↓
           /write-plan
               ↓
         Review plan + tasklist
               ↓
        /implement-plan ←──────┐
               ↓               │
        Execute phase tasks    │ repeat
               ↓               │ per
        Run checkpoints        │ phase
               ↓               │
        Human review           │
               ↓               │
            /clear ────────────┘
               ↓ (all phases done)
         Feature complete

    /amend-plan: update documents when requirements change
```

## When to Use CWF

The workflow should match the complexity of the work. CWF is designed for features that involve architectural decisions, touch multiple components, or span multiple sessions. For quick fixes or single-session work, chat mode or plan mode is more efficient.

**Chat mode** — no upfront planning:

- Fix a null pointer exception
- Add one or more logging statements
- Explore or explain unfamiliar code

**Plan mode** — plan first, then implement in one session:

- Add form validation to the signup page
- Refactor a module to use dependency injection

**CWF** — persistent plan, multi-session with review checkpoints:

- Build user authentication with OAuth, sessions, and role-based access
- Add a payment integration that touches API, database, and frontend
- Bootstrap and set up an initial version of a greenfield project
- Implement a new feature that requires design decisions and will take multiple sessions to complete

## Installation

Install as plugin in Claude Code:

1. `/plugin marketplace add tordks/claude-workflow` - adds repository to your marketplace
2. `/plugin install cwf@claude-workflow` - installs the plugin

To uninstall: `/plugin uninstall cwf@claude-workflow`

## Usage Guide

CWF uses slash commands to orchestrate the workflow and loads specialized knowledge (skills) on demand.

### Command Reference

| Command | When to Use | What It Does |
|---------|-------------|--------------|
| `/brainstorm [feature-name] [instructions]` | During planning | Structured exploration with guided questions, alternatives analysis, produces design summary |
| `/write-plan <feature-name> [instructions]` | After planning | Writes planning documents |
| `/implement-plan <feature-name> [instructions]` | Start/Resume implementation | Executes tasks task-by-task and phase-by-phase with quality checkpoints |
| `/amend-plan <feature-name> [instructions]` | Requirements changed or gaps identified | Updates plan/tasklist safely |

Arguments: `<feature-name>` is required (except for brainstorm). `[instructions]` are optional free-form text for additional context or constraints.

### Skill Reference

| Skill | Contains | How It's Used |
|-------|----------|---------------|
| `claude-workflow` | Planning structure, phase patterns, task format, amendment rules | Loaded by cwf commands |

### Planning

The planning phase is about solidifying the specifications for the feature we are about to implement, and make sure we have all the information for an agent to perform the implementation.

You can either:

- Have an informal planning discussion with the agent
- Use `/brainstorm` for structured exploration with guided questions and alternatives analysis
- Provide a written specification file

The `/brainstorm` command systematically extracts requirements, explores alternatives, and produces a design summary that can serve as input for `/write-plan`.

After solidifying the specification, run `/write-plan` to create the planning documents in `.cwf/{feature-name}/` at your project root:

- **Plan** `.cwf/{feature-name}/{feature-name}-plan.md`: Captures WHY/WHAT—architectural decisions, design rationale, alternatives considered
- **Tasklist** `.cwf/{feature-name}/{feature-name}-tasklist.md`: Defines WHEN/HOW—sequential phases with checkbox tracking `[x]`
- **Mockup** `.cwf/{feature-name}/{feature-name}-mockup.html` (optional): Visual reference for UI/frontend features

The plan divides work into phases that each produce runnable code. Each phase ends with quality checkpoints and human review before proceeding (see Implementation below).

**Tips:**

- Be specific about requirements, components, and technologies
- Set clear scope (what's IN and OUT of this feature)
- Before writing the plan, ask the agent to write svg or mermaid diagrams. Especially useful for webapps to confirm layout understanding, or for database schemas.
- For UI/frontend features, request an HTML mockup to verify layout understanding before implementation. The agent will create a single HTML file with inline CSS that you can open in a browser.
- For multi-session planning, save discussion to file and reload when resuming
- Use plan mode to get an initial plan draft that can be fed into `/write-plan`
- You can focus on specific parts of a discussion/spec and provide file inputs: `/write-plan user-auth only make a plan for the authentication layer described in my-spec-file.md`
- Create `.claude/rules/` files for project-specific coding standards when CLAUDE.md grows large. See <https://code.claude.com/docs/en/memory#modular-rules-with-claude/rules/>.

### Implementation

Run `/implement-plan` to start implementing the feature. The agent continues from the next incomplete task in the tasklist, allowing you to resume with clear context.

At the end of each phase, the agent runs **checkpoints**—validation operations that ensure code quality before proceeding:

- **Self-review:** Agent reviews implementation against phase deliverable
- **Code quality checks:** Linting, formatting, type checking—runs whatever tools the project already uses (e.g., eslint, prettier, mypy, ruff)
- **Complexity checks:** Code complexity analysis—runs if project has complexity tools configured

These checkpoints catch issues early before they accumulate (ie. ever-increasing function- or file size). After checkpoints pass, implementation stops for human review before proceeding to the next phase.

**Tips:**

- Review at phase boundaries before approving
- Run `/clear` often to maintain fresh context
- If context allows, write "continue to next phase" instead of clearing to speed up development
- You can add instructions to `/implement-plan`: `/implement-plan user-auth phase 1, 2 and 3, then stop`
- Use `/amend-plan` when requirements change (don't work around the plan)
- Use CLAUDE.md in subfolders to help facilitate discovery
- Use subagents to run independent phases/tasks in parallel or to preserve main instance context: `/implement-plan user-auth use subagents to implement phase 1 and 2 in parallel, enforce phase 2 for second subagent`

### Amending Plans

If requirements change during implementation or you discover a gap in the plan, use `/amend-plan` to update the plan and tasklist safely.

**Tips:**

- For complex amendments, `/clear` and discuss changes first, you might even want to use `/brainstorm <initial-description-of-change>`
- Add change description for amendments that might not need discussion: `/amend-plan my-cli-tool the cli needs an --output option`
- Keep the plan updated—it's the agent's source of truth
- **Warning:** Changing implementation without amending the plan causes confusion after `/clear` and will likely result in an erroneous implementation.

### Project Rules (Optional)

Claude Code supports modular rules in `.claude/rules/` for principles and standards that apply to the repository. All `.md` files in this directory are automatically loaded with the same priority as CLAUDE.md.

Rules accept a yaml frontmatter that specify conditions for when the rules are to be loaded into context. For example:

```yaml
paths: **/*.py
```

Specifies a rule that should only be loaded when considering python files.

Read more here: <https://code.claude.com/docs/en/memory#modular-rules-with-claude/rules/>

**You don't need separate rules files.** It's a convenience to avoid long, unwieldy CLAUDE.md files. When your CLAUDE.md grows large with coding standards and principles, move that content to `.claude/rules/` files instead.

**What goes where:**

- **CLAUDE.md** - Repository context, structure, navigation
- **`.claude/rules/`** - Coding principles, standards, guidelines

Example rules files (see `claude-rules-example/`):

- **Software Engineering Principles:** DRY, YAGNI, orthogonality, separation of concerns
- **Testing Philosophy:** Test coverage expectations, testing patterns
- **Language Standards:** Python-specific conventions and best practices

## Alternatives & Resources

Below are related projects and resources. Not thoroughly reviewed.

**Development Workflows:**

- [superpowers](https://github.com/obra/superpowers) - Comprehensive skills library with techniques and patterns that auto-activate through Claude Code's plugin system
- [spec-kit](https://github.com/github/spec-kit) - Spec-Driven Development toolkit where detailed specifications become executable artifacts that directly generate implementations
- [superclaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Meta-programming framework with 16 specialized agents and 7 behavioral modes for systematic workflow automation
- [BMAD-method](https://github.com/bmad-code-org/BMAD-METHOD) - Human-AI collaboration framework with 19+ specialized agents for software development, creativity, and problem-solving
- [claude-orchestration](https://github.com/mbruhler/claude-orchestration) - Multi-agent workflow orchestration enabling sequential, parallel, and conditional chaining of AI agents with manual checkpoints
- [VibeCoder (VC)](https://github.com/steveyegge/vc) - VC orchestrates multiple coding agents (Amp, Claude Code, etc.) to work on small, well-defined tasks, guided by AI supervision
- [moai-adk](https://github.com/modu-ai/moai-adk/tree/main/) - SPEC-First framework with 19 specialized agents for requirements, TDD, and documentation automation

**Resources:**

- [superpowers-marketplace](https://github.com/obra/superpowers-marketplace/tree/main) - Marketplace for plugins related to superpowers
- [superpowers-developing-for-claude-code](https://github.com/obra/superpowers-developing-for-claude-code/tree/main) - A Claude Code plugin providing skills and comprehensive documentation for building plugins, skills, MCP servers, and other Claude Code extensions.
- [episodic-memory](https://github.com/obra/episodic-memory) - Semantic search for Claude Code conversations. Remember past discussions, decisions, and patterns.
- [beads](https://github.com/steveyegge/beads) -  lightweight memory system for coding agents, using a graph-based issue tracker
  - <https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a>
  - <https://steve-yegge.medium.com/the-beads-revolution-how-i-built-the-todo-system-that-ai-agents-actually-want-to-use-228a5f9be2a9>
- [awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) - Curated list of Claude Skills organized by category (document handling, development, data analysis, scientific research, etc.)
- [claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) - PAtterns for auto-activating skills, modular organization, and scaling AI-assisted development
- [Martin Fowler on Spec-Driven Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) - Conceptual overview of specification-driven AI development approaches
- [claude-code-prompt-improver](https://github.com/severity1/claude-code-prompt-improver) - Prompt enhancement tool that intercepts and enriches vague prompts with targeted clarifying questions
- [armchr](https://github.com/armchr/armchr) - Toolkit with Splitter and Reviewer agents for helping AI better analyze and understand code through logical commit chunking
- [claude-code-switch](https://github.com/foreveryh/claude-code-switch) - Model switching tool supporting multiple AI providers (Claude, Deepseek, KIMI, GLM, Qwen) with intelligent fallback
- [claude-context](https://github.com/zilliztech/claude-context) - MCP plugin that adds semantic code search to Claude Code
- [sourcegraph-amp](https://sourcegraph.com/amp) - Agentic coding platform with autonomous reasoning and task execution

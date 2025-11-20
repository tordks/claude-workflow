# Claude Workflow

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/tordks/claude-workflow/releases)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-purple.svg)](https://claude.com/claude-code)

Claude Workflow (CWF) defines a plan-driven development workflow for Claude Code with phase-based implementation.

CWF is my personal exploration of agent development workflows. Other frameworks vary in rigor and documentation requirements, but most share the core concept of persisting specifications to maintain context between session. See links to other resources below.

## What Problem Does CWF Solve?

AI-assisted development often faces these challenges:

1. **Lost Implementation Context:** When context clears, gets compacted, or sessions end, implementation details vanish. Architectural decisions, component relationships, and technical rationale all disappear, forcing agents to re-derive or guess.

2. **Inconsistent Quality:** Without documented standards or quality control, implementation quality varies unpredictably. One session produces well-structured code with proper error handling; the next produces a 500-line function that mixes concerns.

3. **Plan Evolution Lost:** When implementation reveals gaps and needed changes, amended requirements remain buried in conversation. New sessions start with the original flawed plan, repeating the same discovery process.

4. **Loss of Control:** Agents can make dozens of changes at once, and without oversight mechanisms, developers lose control of what is being built. Instructions are often underspecified, so agents guess at developer intent and implementations quickly go off the rails—either building the wrong thing entirely or taking opaque approaches that require investigation to understand. Without checkpoints for human review and quality control, problems compound before they're caught.

## The Workflow

```text
  /brainstorm (optional)
         ↓
  Design Summary
         ↓
     /write-plan
         ↓
   Plan + Tasklist
         ↓
   /implement-plan
         ↓
  Phase 1 → Checkpoints → Review → ✓ → /clear
         ↓
 Phase 2 → Checkpoints → Review → ✓ → /clear
  [Changes?] → /amend-plan ──┐
         ↓                   │
  Continue development ←─────┘
         ↓
  Feature Complete ✓
```

## When to use CWF

Claude Code has different modes for different types of work. CWF is a workflow framework that adds structure for complex, multi-session development.

**Use regular chat mode when:**

- Single-session work
- Quick fixes or simple features
- No architectural decisions needed
- Informal exploration

**Use plan mode when:**

- Starting more complex features
- You want to review the work before implementation starts

Plan mode lets Claude read and analyze without editing or executing. Great for careful deliberation before implementation.

**Use CWF when:**

- Work spans multiple sessions
- Need to adjust plans during implementation
- Need reviewable checkpoints with runnable code

CWF adds persistent plan documents you can review and safely modify during implementation. In plan mode, evolving requirements and discovered gaps remain implicit and it can be hard to know that the agent applies amendments as intended.

## Installation

Install as plugin in claude code:

1. `/plugin marketplace add tordks/claude-workflow`
2. `/plugin install cwf@claude-workflow`

## How It Works

CWF preserves context across sessions by storing planning and progress in structured documents. It uses two key mechanisms:

**Skills** provide specialized knowledge to Claude as self-contained packages. The `claude-workflow` skill contains all CWF workflow knowledge (plan structure, tasklist format, amendment rules, etc.) that agents need to execute the workflow. Skills are loaded on-demand to keep context focused.

**Commands** are called by users to orchestrate the workflow. They provide instructions that guide agents through each stage and automatically load relevant skills.

### Command Reference

| Command | When to Use | Inputs | What It Does |
|---------|-------------|--------|--------------|
| `/brainstorm` | During planning | Feature name (optional) | Structured exploration with guided questions, alternatives analysis, produces design summary |
| `/write-plan` | After planning | Feature name, optional additional instructions | Writes planning documents |
| `/implement-plan` | Start/Resume implementation | Feature name, optional additional instructions | Executes tasks task-by-task and phase-by-phase with quality checkpoints |
| `/amend-plan` | Requirements changed or gaps identified | Feature name, optional additional instructions | Updates plan/tasklist safely |
| `/read-constitution` | When in need of coding principles | None | Loads  constitution files into context |

### Skill Reference

| Skill | Contains | How It's Used |
|-------|----------|---------------|
| `claude-workflow` | Planning structure, phase patterns, task format, amendment rules | Loaded by cwf commands |
| `read-constitution` | Engineering fundamentals (DRY, YAGNI, orthogonality), testing philosophy | Manually at the start of a planning session or by cwf commands automatically|

### Planning

The planning phase is about solidifying the specifications for the feature we are about to implement, and make sure we have all the information for an agent to perform the implementation.

You can either:

- Have an informal planning discussion with the agent
- Use `/brainstorm` for structured exploration with guided questions and alternatives analysis
- Provide a written specification file

The `/brainstorm` command systematically extracts requirements, explores alternatives, and produces a design summary that can serve as input for `/write-plan`.

After solidifying the specification, run `/write-plan` to create the planning documents:

- **Plan** `{feature.name}-plan.md`: Captures WHY/WHAT—architectural decisions, design rationale, alternatives considered
- **Tasklist** `{feature-name}-tasklist.md`: Defines WHEN/HOW—sequential phases with checkbox tracking `[x]`

The plan divides work into phases that each produce runnable code. Each phase ends with **checkpoints**—validation operations that ensure code quality before proceeding:

- **Self-review:** Agent reviews implementation against phase deliverable
- **Code quality checks:** Linting, formatting, type checking (only if project uses these tools)
- **Complexity checks:** Code complexity analysis (only if project uses these tools)

These checkpoints provide quality control, catching issues early before they accumulate (ie. ever-increasing function- or file size). After checkpoints pass, implementation stops for human review before proceeding to the next phase.

**Tips:**

- Be specific about requirements, components, and technologies
- Set clear scope (what's IN and OUT of this feature)
- Define success criteria
- For multi-session planning, save discussion to file and reload when resuming
- Use plan mode to get an initial plan draft that can be fed into `/write-plan`
- You can focus on specific parts of a discussion/spec and provide file inputs: `/write-plan user-auth only make a plan for the authentication layer described in my-spec-file.md`
- Create `.constitution/` files for project-specific coding standards when claude.md grows large.

### Implementation

Run `/implement-plan` to start implementing the feature. The agent continues from the next incomplete task in the tasklist, allowing you to resume with clear context.

**Tips:**

- Review at phase boundaries before approving
- Run `/clear` often to maintain fresh context
- If context allows, write "continue to next phase" instead of clearing to speed up development
- You can add instructions to `/implement-plan`: `/implement-plan user-auth phase 1, 2 and 3, then stop`
- Use `/amend-plan` when requirements change (don't work around the plan)
- Use CLAUDE.md in subfolders to help facilitate discovery

### Amending Plans

If requirements change during implementation or you discover a gap in the plan, use `/amend-plan` to update the plan and tasklist safely.

**Tips:**

- For complex amendments, `/clear` and discuss changes first, you might even want to use `/brainstorm <initial-description-of-change>`
- Add change description for amendments that might not need discussion: `/amend-plan my-cli-tool the cli needs an --output option`
- Keep the plan updated—it's the agent's source of truth
- **Warning:** Changing implementation without amending the plan causes confusion after `/clear` and will likely result in an erroneous implementation.

### Coding Constitution (Optional)

CWF supports a constitution (`.constitution/` directory) to guide implementation quality and consistency. When present, constitution files are automatically loaded by workflow commands (`/write-plan`, `/implement-plan`, `/amend-plan`) and can be manually loaded with `/read-constitution`.

Example constitution files:

- **Software Engineering Principles:** DRY, YAGNI, orthogonality, separation of concerns
- **Testing Philosophy:** Test coverage expectations, testing patterns, when to test
- **Language Standards:** Python-specific conventions and best practices

When configured, the constitution helps agents maintain consistent conventions and quality standards across implementations. Create `.constitution/` files for project-specific standards, or use CWF without them.

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

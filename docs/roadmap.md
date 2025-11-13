# CWF Roadmap

## High Priority (Core Workflow Improvements)

### Optimize implement-plan Context Loading

**What:** Reduce context consumption by making implement-plan infer structure from planning documents rather than loading full cfw-planning skill

**Why Needed:** Currently implement-plan loads extensive skill documentation. Plans should be as self-contained as possible with needed context embedded.

**Features:**
- Write-plan embeds essential structure info into plan document
- Implement-plan reads structure from plan itself
- Reduces token usage during implementation
- Makes plans more portable and self-documenting

---

### Feature-Based Directory Organization

**What:** Organize plan documents in feature-specific subdirectories instead of flat `plans/` directory

**Why Needed:** Plans directory becomes cluttered as project grows, making navigation difficult

**Features:**
- Create `plans/feature-name/` subdirectories
- Store plan.md and tasklist.md in feature directory
- Group related artifacts (diagrams, specs) with feature
- Maintain cleaner project structure

---

### Checkpoint Validation System

**What:** Automated validation and quality checks at phase boundaries

**Why Needed:** Ensure code quality, completeness, and architectural integrity before proceeding to next phase

**Features:**
- Post-phase validation: verify all tasks complete
- Code quality checks: linting, formatting
- Complexity analysis: detect refactoring needs using Radon
- Dynamic checkpoint adjustment based on complexity metrics

- Split complex phases, combine simple ones
- Balance implementation effort

**Reference:** Original notes line 119-131 (checkpoint concept) and 133-145 (dynamic checkpoints)

---

### Tracer Bullets Implementation Strategy

**What:** Optional workflow mode that creates minimal working examples before full implementation

**Why Needed:** Full layer/feature implementations in Phase 1 make it hard for users to test and understand incremental progress

**Features:**
- Create end-to-end minimal working example first
- Build incrementally on working foundation
- Enable early testing and feedback
- Reduce integration risk

---

## Medium Priority (Enhanced Features)

### Amendment Enhancements

**What:** Changelog tracking and strikethrough formatting for amended content

**Why Needed:** Maintain historical record of changes and why they were made

**Features:**
- Changelog section in amended documents
- Strikethrough for replaced content
- Amendment timestamps
- Rationale documentation

---

### Plan Settings / Front Matter

**What:** YAML front matter in plan documents for configuration

**Why Needed:** Allow plans to specify preferences like testing framework, language version, architectural style

**Example:**
```yaml
---
testing_framework: pytest
python_version: "3.11"
architecture: layered
implementation-strategy: tracer bullet
---
```

---

### Constitution File Reorganization

**What:** Move constitution files from `.constitution/` to plugin-specific location

**Why Needed:** Separate project-specific coding standards from CWF plugin defaults

**Features:**
- Move plugin constitution to plugin directory
- Support project-local constitution overrides
- Clear separation of plugin vs project standards
- Enable per-project coding conventions

**Reference:** Original note line 152-154

---

## Low Priority (Advanced/Future)

### Ambiguity Detection System

**What:** Automated detection of ambiguous requirements in planning discussions

**Why Needed:** Help identify unclear specifications before implementation begins

**Features:**
- Scan conversation for vague terms
- Flag missing technical details
- Prompt for clarification
- Suggest specific questions

**Reference:** `plans/skills-draft.md` lines 76-77

---

### Hooks System for Event-Driven Automation

**What:** Event hooks for automated actions during workflow

**Why Needed:** Automate repetitive tasks and enforce policies

**Features:**
- Pre-plan hooks (validate naming, check dependencies)
- Post-plan hooks (create issues, notify team)
- Pre-phase hooks (setup environment, run checks)
- Post-phase hooks (run tests, commit code)

**Reference:** `plans/skills-draft.md` line 84

---

### Refactor Skill with Ruff/Radon

**What:** Dedicated skill for code quality analysis and refactoring guidance

**Why Needed:** Systematic approach to improving existing code

**Features:**
- Integrate Ruff for linting
- Integrate Radon for complexity analysis
- Provide refactoring recommendations
- Generate refactoring tasks

**Reference:** `plans/skills-draft.md` line 81

---

### PM-Subagent Coordination Mode

**What:** Project manager agent that coordinates multiple implementation agents

**Why Needed:** Handle complex features requiring parallel work streams

**Features:**
- Coordinate multiple agents
- Manage dependencies
- Track overall progress
- Resolve conflicts

**Reference:** `plans/skills-draft.md` line 83

---

### Split cfw-planning into Separate Plugin

**What:** Extract cfw-planning skill into its own independent plugin

**Why Needed:** Better skill information hit-rate and independent versioning

**Features:**
- Separate cfw-planning plugin
- Independent updates and releases
- Improved discoverability
- Reduced main plugin complexity

**Reference:** Original note line 101-103

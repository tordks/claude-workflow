# Future Phases

## Phase 0 Scope

Phase 0 focused exclusively on architectural restructuring while maintaining v1 functionality parity:

**What Was Included:**
- Created `.claude-plugin/plugin.json` manifest (REQUIRED)
- Created 2 core skills with SKILL.md + YAML frontmatter
- Updated commands to invoke skills instead of inline logic
- Removed `/prime-planning-commands` command
- Kept `/read-constitution` command (now invokes skill)
- Created comprehensive documentation in `docs/`
- Updated README to reflect skills-first architecture
- Maintained exact v1 behavior and outputs

**Why This Scope:**
- Validates skills architecture before building on it
- Reduces risk by limiting changes
- Allows testing that behavior matches v1 exactly
- Establishes clean foundation for Phase 1+ features
- Proves plugin system works correctly

**Success Criteria Met:**
- All commands work identically to v1
- Skills load on-demand without duplication
- Constitution files remain in `.constitution/` (not duplicated)
- Documentation clearly explains three-layer architecture
- Plugin installs and functions correctly

## Excluded Features (Phase 1+)

The following features were explicitly excluded from Phase 0 to maintain focus on architectural foundation:

### Plan Settings / Front Matter

**What:** YAML front matter in plan documents for configuration

**Why Needed:** Allow plans to specify preferences like testing framework, language version, architectural style

**Example:**
```yaml
---
testing_framework: pytest
python_version: "3.11"
architecture: layered
---
```

**Reference:** `plans/skills-draft.md` line 76

**Phase:** 1

### Ambiguity Detection System

**What:** Automated detection of ambiguous requirements in planning discussions

**Why Needed:** Help identify unclear specifications before implementation begins

**Features:**
- Scan conversation for vague terms
- Flag missing technical details
- Prompt for clarification
- Suggest specific questions

**Reference:** `plans/skills-draft.md` lines 76-77

**Phase:** 1

### Amendment Enhancements

**What:** Changelog tracking and strikethrough formatting for amended content

**Why Needed:** Maintain historical record of changes and why they were made

**Features:**
- Changelog section in amended documents
- Strikethrough for replaced content
- Amendment timestamps
- Rationale documentation

**Reference:** `plans/skills-draft.md` lines 76-79

**Phase:** 1

### Refactor Skill with Ruff/Radon

**What:** Dedicated skill for code quality analysis and refactoring guidance

**Why Needed:** Systematic approach to improving existing code

**Features:**
- Integrate Ruff for linting
- Integrate Radon for complexity analysis
- Provide refactoring recommendations
- Generate refactoring tasks

**Reference:** `plans/skills-draft.md` line 81

**Phase:** 2

### Dynamic Checkpoints Based on Complexity

**What:** Adjust phase boundaries dynamically based on code complexity metrics

**Why Needed:** Optimize phase size for different complexity levels

**Features:**
- Analyze task complexity
- Suggest phase splits for complex work
- Combine simple phases
- Balance implementation effort

**Reference:** `plans/skills-draft.md` line 82

**Phase:** 2

### PM-Subagent Coordination Mode

**What:** Project manager agent that coordinates multiple implementation agents

**Why Needed:** Handle complex features requiring parallel work streams

**Features:**
- Coordinate multiple agents
- Manage dependencies
- Track overall progress
- Resolve conflicts

**Reference:** `plans/skills-draft.md` line 83

**Phase:** 3

### Hooks System for Event-Driven Automation

**What:** Event hooks for automated actions during workflow

**Why Needed:** Automate repetitive tasks and enforce policies

**Features:**
- Pre-plan hooks (validate naming, check dependencies)
- Post-plan hooks (create issues, notify team)
- Pre-phase hooks (setup environment, run checks)
- Post-phase hooks (run tests, commit code)

**Reference:** `plans/skills-draft.md` line 84

**Phase:** 2-3

### Full Progressive Disclosure

**What:** Complete skill structure with templates/, examples/, scripts/, references/

**Why Needed:** Provide rich resources without bloating core content

**Current State:**
- Documented in `docs/skill-structure.md`
- Framework ready for implementation
- Skills currently use Level 1+2 only (metadata + core content)

**Future Implementation:**
- Add templates/ to cfw-planning (plan/tasklist templates)
- Add examples/ to cfw-planning (sample plans)
- Add scripts/ to read-constitution (validation scripts)
- Add references/ as needed for detailed docs

**Reference:** `docs/skill-structure.md`, `plans/skills-draft.md` lines 119-140

**Phase:** Incremental across Phase 1-3

## v2 Vision Reference

For the complete v2 architecture vision, see `plans/skills-draft.md`.

**Key Target Outcomes:**

1. **Amendment-First Design**
   - Plans are living documents
   - Easy to modify during implementation
   - Historical tracking of changes
   - Clear rationale for amendments

2. **Complexity-Aware Planning**
   - Automatic complexity analysis
   - Dynamic phase boundaries
   - Intelligent task sizing
   - Risk identification

3. **Team Collaboration**
   - Multiple agents coordinating
   - Shared context management
   - Parallel work streams
   - Conflict resolution

4. **Automation Integration**
   - Event-driven hooks
   - Automated quality checks
   - CI/CD integration
   - Policy enforcement

5. **Rich Skill Ecosystem**
   - Domain-specific skills
   - Reusable templates
   - Executable scripts
   - Progressive disclosure

## Implementation Priorities

**Phase 1 (Next):**
- Plan settings/front matter
- Ambiguity detection
- Amendment enhancements (changelog, strikethrough)
- Begin progressive disclosure (templates/)

**Phase 2 (Medium-term):**
- Refactor skill with Ruff/Radon
- Dynamic checkpoints
- Hooks system (basic)
- Expand progressive disclosure (examples/, scripts/)

**Phase 3 (Long-term):**
- PM-subagent coordination
- Advanced hooks
- Full progressive disclosure
- Team collaboration features

## Migration Path

**From Phase 0 to Phase 1:**
- Existing plans work unchanged
- New features opt-in via front matter
- Commands backward compatible
- Skills extended, not replaced

**General Principles:**
- No breaking changes to existing workflows
- New features additive
- Backward compatibility maintained
- Incremental adoption

## Where to Learn More

**Planning Documents:**
- `plans/skills-draft.md` - Complete v2 vision with detailed feature descriptions
- `plans/skills-plan.md` - Phase 0 implementation plan (completed)
- `plans/skills-tasklist.md` - Phase 0 tasks (completed)

**Documentation:**
- `docs/concepts.md` - General skills/commands/agents pattern
- `docs/cwf-concepts.md` - CWF concepts, workflow, and architecture
- `docs/workflow-guide.md` - End-to-end usage guide with examples
- `docs/commands-reference.md` - Complete command API reference

**Plugin Resources:**
- `.claude-plugin/plugin.json` - Plugin manifest
- `skills/` - Current skill implementations
- `commands/` - Command implementations
- `.constitution/` - Coding principles

## Contributing

**To Add Phase 1 Features:**
1. Review `plans/skills-draft.md` for feature specs
2. Create feature-specific plan and tasklist
3. Follow Phase 0 patterns (skills-first, three-layer)
4. Maintain backward compatibility
5. Update documentation
6. Test with existing workflows

**To Create New Skills:**
1. Follow `docs/skill-structure.md` guidelines
2. Start with SKILL.md + frontmatter only
3. Test with real workflows
4. Add resources progressively
5. Document in README
6. Share with community

**To Propose New Features:**
1. Open issue describing use case
2. Reference existing patterns
3. Consider backward compatibility
4. Provide examples
5. Discuss with maintainers

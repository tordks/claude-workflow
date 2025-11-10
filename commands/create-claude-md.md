# Create CLAUDE.md Command

Generate a CLAUDE.md project context file for Claude Code.

## Purpose

This command creates a CLAUDE.md file in your project root that provides Claude with essential project context. The file helps Claude understand your project's architecture, conventions, and requirements.

## When to Use

- Starting a new project that will use Claude Code
- Adding Claude Code workflow to an existing project
- Updating project context documentation

## Instructions

1. **Check for existing CLAUDE.md:**
   - Use the Read tool to check if CLAUDE.md exists in the current directory
   - If the file doesn't exist, proceed to step 3
   - If the file exists, proceed to step 2

2. **Handle existing file conflict:**
   - If CLAUDE.md already exists, use the AskUserQuestion tool to ask how to proceed:
     - **Replace**: Backup existing file to CLAUDE.md.backup and create new file
     - **Append**: Add template sections to the end of existing file
     - **Skip**: Exit without making changes
   - Based on user choice, proceed accordingly

3. **Generate CLAUDE.md file:**
   - Use the Write tool (for new file) or Edit tool (for append) to create/update the file
   - Use the template below, replacing placeholders with project-specific information if available

4. **Confirm completion:**
   - Show success message confirming file creation/update
   - List the location of the file
   - Provide next steps for the user

## CLAUDE.md Template

````markdown
# Project Context

> This file provides Claude with essential context about your project.
> Update this file as your project evolves to maintain accurate context.

## Project Overview

**Name:** [Project Name]

**Description:** [Brief description of what this project does]

**Primary Goal:** [Main objective or problem this project solves]

## Tech Stack

**Language:** [e.g., Python 3.11, TypeScript, Go]

**Framework:** [e.g., FastAPI, React, Django, None]

**Key Dependencies:**
- [Dependency 1]: [Purpose]
- [Dependency 2]: [Purpose]
- [Dependency 3]: [Purpose]

**Development Tools:**
- Build system: [e.g., uv, npm, make]
- Testing: [e.g., pytest, jest, go test]
- Linting: [e.g., ruff, eslint, golangci-lint]
- Type checking: [e.g., mypy, TypeScript]

## Project Structure

```
project-root/
├── src/                 # [Description]
├── tests/               # [Description]
├── docs/                # [Description]
└── [other-directories]  # [Description]
```

**Key Directories:**
- `[directory]`: [Purpose and contents]
- `[directory]`: [Purpose and contents]

## Architecture

**Pattern:** [e.g., MVC, Microservices, Layered, Hexagonal]

**Key Components:**
1. **[Component Name]**: [Responsibility and location]
2. **[Component Name]**: [Responsibility and location]
3. **[Component Name]**: [Responsibility and location]

**Data Flow:**
[Brief description of how data flows through the system]

## Development Workflow

**Setup:**
```bash
# Commands to set up the development environment
[command 1]
[command 2]
```

**Running the Project:**
```bash
# Commands to run the project locally
[command]
```

**Testing:**
```bash
# Commands to run tests
[command]
```

**Building:**
```bash
# Commands to build for production
[command]
```

## Coding Standards

**Style Guide:** [e.g., PEP 8, Airbnb Style Guide, Go standard]

**Key Conventions:**
- [Convention 1]
- [Convention 2]
- [Convention 3]

**File Naming:**
- [Pattern for file names]

**Code Organization:**
- [Guidelines for organizing code]

## Common Tasks

**Adding a New Feature:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Debugging:**
- [Tools and approaches used]

**Updating Dependencies:**
- [Process for updating dependencies]

## Important Constraints

**Performance Requirements:**
- [Requirement 1]
- [Requirement 2]

**Security Considerations:**
- [Consideration 1]
- [Consideration 2]

**Compatibility:**
- [Platform/version requirements]

## Resources

**Documentation:**
- [Link to main docs]
- [Link to API docs]

**Related Projects:**
- [Link/description]

**Design Decisions:**
- See [ADR directory / design doc]

## Current Focus

**Active Development:**
[What's currently being worked on]

**Known Issues:**
[Any known issues or technical debt to be aware of]

**Upcoming Changes:**
[Planned changes or refactoring]
````

## Example Usage

**Creating new file:**
```
User: /create-claude-md
Assistant: CLAUDE.md does not exist in the current directory.
Assistant: [Generates CLAUDE.md with template]
Assistant: ✓ CLAUDE.md created successfully at /path/to/project/CLAUDE.md
```

**Handling existing file:**
```
User: /create-claude-md
Assistant: CLAUDE.md already exists in the current directory.
Assistant: [Uses AskUserQuestion to ask: Replace, Append, or Skip?]
User: [Selects "Replace"]
Assistant: [Backs up existing file]
Assistant: [Creates new CLAUDE.md with template]
Assistant: ✓ CLAUDE.md replaced. Previous version backed up to CLAUDE.md.backup
```

## Success Message Template

After creating/updating the file, show:

```
✓ CLAUDE.md [created/updated] successfully!

Location: [absolute path to file]

Next steps:
1. Open CLAUDE.md and replace placeholders with your project details
2. Update the tech stack, architecture, and structure sections
3. Document your coding standards and conventions
4. Run /read-constitution to load the software engineering principles
5. Start using claude-workflow commands like /write-plan

Tip: Keep CLAUDE.md updated as your project evolves to maintain accurate context for Claude.
```

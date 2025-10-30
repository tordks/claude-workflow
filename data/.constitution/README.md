# Code Constitution

Coding standards, principles, and tool guides for this project.

## Contents

### Principles

- **[Software Engineering Principles](principles/software-engineering.md)**: DRY, Orthogonality, YAGNI, Fail Fast, and universal guidelines
- **[Python Standards](principles/python-standards.md)**: Pythonic code, type safety, error handling, modern idioms

### Workflow

- **[Development Workflow](workflow.md)**: Protocols for before writing, while writing, reviewing, and when stuck
## Quick Reference

| Principle | Core Idea |
|-----------|-----------|
| DRY | Each piece of knowledge in exactly one place |
| Orthogonality | Change one thing without affecting unrelated things |
| YAGNI | Build what's needed now, not what might be needed |
| Fail Fast | Detect errors at the earliest possible point |

## Structure

```text
.constitution/
├── principles/               # Universal and language-specific principles
├── workflow.md               # Development protocols
└── README.md                 # This file
```

When making decisions, explicitly reference which principle guides your choice.

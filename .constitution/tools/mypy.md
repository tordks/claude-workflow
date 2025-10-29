# Mypy - Static Type Checker for Python

Mypy verifies type hints at development time, catching type-related bugs before runtime.

## Overview

Mypy analyzes Python code to:

- Verify type annotations are correct
- Detect type mismatches
- Catch attribute access errors
- Ensure function calls match signatures

## Command Reference

| Command | Purpose |
|---------|---------|
| `mypy .` | Check all Python files |
| `mypy <file>` | Check specific file |
| `mypy --strict .` | Use strict mode |
| `mypy --show-error-codes .` | Show error codes |

## Best Practices

**Do**:

- Annotate all public functions
- Use modern type syntax (`list[str]`)
- Prefer abstract types for parameters
- Use pydantic or dataclasses for data models

**Avoid**:

- Using `Any` unnecessarily
- Skipping return type annotations
- Using bare `type: ignore` comments

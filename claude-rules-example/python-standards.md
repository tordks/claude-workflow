---
paths: **/*.py
---

# Python-Specific Principles

## Pythonic Code

- Follow PEP 8 and PEP 20 (Zen of Python)
- Use language features idiomatically (comprehensions, context managers, decorators)
- Use type hints

## Type Safety

- Annotate function signatures
- Use modern syntax: `list[str]`, `dict[str, int]`
- Use `collections.abc` for parameters, concrete types for returns

## Error Handling

- Create domain-specific exception classes
- Never use bare `except:` clauses
- Use `try/except/else/finally` structure appropriately
- Log with full context and tracebacks

## Modern Python Idioms

- Use dataclasses or Pydantic for structured data
- Prefer pathlib over `os.path`
- Use f-strings for formatting

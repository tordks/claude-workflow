# Python Development Standards

Apply Python standards from `.constitution/python-standards.md`.

## Pythonic Code

Follow established Python conventions and idioms:

- Follow PEP 8 (style guide) and PEP 20 (Zen of Python)
- Use language features idiomatically (comprehensions, context managers, decorators)
- Use type hints consistently throughout codebase

## Type Safety

Python type hints improve code clarity and catch errors early:

- Annotate all function signatures with types
- Use modern syntax: `list[str]`, `dict[str, int]` (Python 3.9+)
- Use `collections.abc` for parameters, concrete types for returns
- Example:
  ```python
  from collections.abc import Sequence

  def process_items(items: Sequence[str]) -> list[str]:
      return [item.upper() for item in items]
  ```

## Error Handling

Handle errors explicitly and meaningfully:

- Create domain-specific exception classes for your application
- Never use bare `except:` clauses (always specify exception types)
- Use `try/except/else/finally` structure appropriately
- Log exceptions with full context and tracebacks

## Modern Python Idioms

Use current Python best practices:

- **Structured Data:** Use dataclasses or Pydantic for structured data
  ```python
  from dataclasses import dataclass

  @dataclass
  class User:
      name: str
      email: str
      age: int
  ```

- **File Paths:** Prefer pathlib over `os.path`
  ```python
  from pathlib import Path

  config_file = Path("config") / "settings.json"
  ```

- **String Formatting:** Use f-strings for clarity and performance
  ```python
  message = f"User {name} logged in at {timestamp}"
  ```

---

For complete details and examples, read `.constitution/python-standards.md`.

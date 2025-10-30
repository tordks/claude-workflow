# uv - Modern Python Package Management

uv is a Python package manager written in Rust. It manages dependencies, virtual environments, and tool execution.

## Execution Model

Three execution modes:

1. **Project Scripts**: Commands defined in `[project.scripts]`
2. **Project Environment**: Run tools/scripts with `uv run <command>`
3. **Temporary Execution**: One-off tools with `uvx <tool>`

No manual virtual environment activation needed.

## Command Reference

### Dependency Management

| Command | Purpose |
|---------|---------|
| `uv add <package>` | Add production dependency |
| `uv add --dev <package>` | Add development dependency |
| `uv remove <package>` | Remove dependency |
| `uv sync` | Install/sync all dependencies |
| `uv sync --frozen` | Install exact locked versions (CI) |
| `uv lock` | Update lock file |
| `uv lock --upgrade` | Upgrade all dependencies |

### Tool Management

| Command | Purpose |
|---------|---------|
| `uv tool install <tool>` | Install global tool |
| `uv tool uninstall <tool>` | Remove global tool |
| `uvx <tool> <args>` | Run tool without installing |

### Execution

| Command | Purpose |
|---------|---------|
| `uv run <script>` | Execute script in project environment |
| `uv run python script.py` | Run Python file |
| `uv run <tool>` | Run project tool |

## Constraints

### NEVER

- Use `pip` directly
- Create `requirements.txt` files
- Manually activate virtual environments

### ALWAYS

- Use `uv sync` after dependency changes
- Use `uv run` for executing commands
- Use `uv add` when adding dependencies

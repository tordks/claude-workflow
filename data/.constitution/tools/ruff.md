# Ruff - Fast Python Linter and Formatter

Ruff is a Python linter and formatter written in Rust. It replaces black, isort, flake8, and pyupgrade.

## Overview

Two main functions:

1. **Linting** (`ruff check`): Identifies code quality issues and potential bugs
2. **Formatting** (`ruff format`): Applies consistent code style

## Command Reference

### Formatting

| Command | Purpose |
|---------|---------|
| `ruff format .` | Format all files |
| `ruff format <file>` | Format specific file |
| `ruff format --check .` | Check without modifying |
| `ruff format --diff .` | Show changes without applying |

### Linting

| Command | Purpose |
|---------|---------|
| `ruff check .` | Check for issues |
| `ruff check --fix .` | Auto-fix safe issues |
| `ruff check --unsafe-fixes .` | Apply all fixes |
| `ruff check --select E .` | Check specific rule set |

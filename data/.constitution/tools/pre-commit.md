# Pre-commit - Git Hook Management

Pre-commit manages and runs code quality checks automatically before commits are allowed.

**Philosophy**: Catch issues early, enforce standards automatically.

## Command Reference

### Setup

| Command | Purpose |
|---------|---------|
| `pre-commit install` | Install git hooks |
| `pre-commit uninstall` | Remove git hooks |
| `pre-commit autoupdate` | Update hook versions |

### Running Hooks

| Command | Purpose |
|---------|---------|
| `pre-commit run --all-files` | Run all hooks on entire codebase |
| `pre-commit run <hook-id> --all-files` | Run specific hook |
| `pre-commit run --files <file>` | Run on specific file |
| `git commit` | Run hooks automatically |
| `git commit --no-verify` | Skip hooks (emergency only) |

### Maintenance

| Command | Purpose |
|---------|---------|
| `pre-commit validate-config` | Verify config syntax |
| `pre-commit clean` | Remove cached environments |

## Configuration

Configure in `.pre-commit-config.yaml` at repository root.

Each hook specifies:

- Repository URL and version
- Hook ID and arguments
- File patterns to match
- Additional dependencies

## How It Works

**On Commit**:

1. Git starts commit process
2. Pre-commit runs configured hooks on staged files
3. Auto-fixable issues corrected (formatting, import sorting)
4. Non-fixable issues reported
5. If all pass: commit succeeds
6. If any fail: commit blocked

**When Hooks Fail**:

1. Review error output
2. Check for auto-fixed files
3. Re-stage modified files: `git add .`
4. Fix remaining issues manually
5. Retry commit

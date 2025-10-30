"""Repository fetching functionality for claude-workflow CLI."""

import shutil
import subprocess
import tempfile
from pathlib import Path

from rich.console import Console

from .config import REPO_URL, DATA_DIR

console = Console()


class FetchError(Exception):
    """Raised when fetching the repository fails."""

    pass


def _check_git_available() -> bool:
    """Check if git is available on the system.

    Returns:
        True if git is available, False otherwise
    """
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def fetch_latest() -> Path:
    """Fetch the latest workflow files from the repository.

    Returns:
        Path to the data directory containing the fetched workflow files

    Raises:
        FetchError: If fetching fails
    """
    # Check if git is available
    if not _check_git_available():
        raise FetchError(
            "git is not installed or not available in PATH. "
            "Please install git to use claude-workflow."
        )

    # Create temporary directory for cloning
    temp_dir = Path(tempfile.mkdtemp(prefix="claude-workflow-"))

    try:
        with console.status("[bold green]Fetching latest workflow files from repository..."):
            # Clone the repository
            result = subprocess.run(
                ["git", "clone", "--depth", "1", REPO_URL, str(temp_dir / "repo")],
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode != 0:
                error_msg = result.stderr.strip()
                if "could not resolve host" in error_msg.lower() or "network" in error_msg.lower():
                    raise FetchError(
                        "Network error: Unable to connect to repository. "
                        "Please check your internet connection."
                    )
                else:
                    raise FetchError(f"Failed to clone repository: {error_msg}")

        console.print("[green]✓[/green] Repository fetched successfully")

        # Extract the data directory
        data_path = temp_dir / "repo" / DATA_DIR
        if not data_path.exists():
            raise FetchError(
                f"Data directory '{DATA_DIR}' not found in repository. "
                "The repository structure may have changed."
            )

        return data_path

    except subprocess.TimeoutExpired:
        # Clean up on timeout
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise FetchError("Repository clone timed out. Please try again.")
    except FetchError:
        # Clean up on fetch error and re-raise
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise
    except Exception as e:
        # Clean up on unexpected error
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise FetchError(f"Unexpected error while fetching repository: {e}")

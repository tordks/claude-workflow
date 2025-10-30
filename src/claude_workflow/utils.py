"""Utility functions for claude-workflow CLI."""

import hashlib
from pathlib import Path


def calculate_checksum(file_path: Path) -> str:
    """Calculate SHA256 checksum of a file.

    Args:
        file_path: Path to the file

    Returns:
        Hexadecimal digest of the file's SHA256 checksum
    """
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def ensure_directory(path: Path) -> None:
    """Ensure a directory exists, creating it and parents if necessary.

    Args:
        path: Directory path to ensure exists
    """
    path.mkdir(parents=True, exist_ok=True)


def get_relative_path(file_path: Path, base_path: Path) -> Path:
    """Get the relative path of a file from a base path.

    Args:
        file_path: The file path
        base_path: The base path to calculate relative to

    Returns:
        Relative path from base_path to file_path
    """
    return file_path.relative_to(base_path)

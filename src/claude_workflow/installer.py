"""Installation functionality for claude-workflow CLI."""

from dataclasses import dataclass
from pathlib import Path
from typing import List

from .utils import calculate_checksum, get_relative_path


@dataclass
class FileStatus:
    """Status of a file during installation analysis."""

    path: Path
    status: str  # 'new', 'identical', 'modified', 'updated'
    source_checksum: str
    target_checksum: str | None


@dataclass
class InstallationAnalysis:
    """Analysis of what will be installed."""

    new_files: List[FileStatus]
    identical_files: List[FileStatus]
    modified_files: List[FileStatus]
    updated_files: List[FileStatus]


@dataclass
class InstallationResult:
    """Result of an installation operation."""

    files_added: List[Path]
    files_skipped: List[Path]
    files_updated: List[Path]
    conflicts: List[Path]


def _get_all_files(directory: Path) -> List[Path]:
    """Get all files in a directory recursively.

    Args:
        directory: Directory to scan

    Returns:
        List of all file paths in the directory
    """
    files = []
    for item in directory.rglob("*"):
        if item.is_file():
            files.append(item)
    return files


def analyze_installation(source_dir: Path, target_dir: Path) -> InstallationAnalysis:
    """Analyze what files will be installed and their status.

    Args:
        source_dir: Directory containing source files to install
        target_dir: Target directory for installation

    Returns:
        Analysis of installation with file statuses
    """
    new_files: List[FileStatus] = []
    identical_files: List[FileStatus] = []
    modified_files: List[FileStatus] = []
    updated_files: List[FileStatus] = []

    # Get all source files
    source_files = _get_all_files(source_dir)

    for source_file in source_files:
        # Calculate relative path from source_dir
        relative_path = get_relative_path(source_file, source_dir)
        target_file = target_dir / relative_path

        # Calculate source checksum
        source_checksum = calculate_checksum(source_file)

        if not target_file.exists():
            # File doesn't exist in target - it's new
            new_files.append(
                FileStatus(
                    path=relative_path,
                    status="new",
                    source_checksum=source_checksum,
                    target_checksum=None,
                )
            )
        else:
            # File exists - compare checksums
            target_checksum = calculate_checksum(target_file)

            if source_checksum == target_checksum:
                # Files are identical
                identical_files.append(
                    FileStatus(
                        path=relative_path,
                        status="identical",
                        source_checksum=source_checksum,
                        target_checksum=target_checksum,
                    )
                )
            else:
                # Files differ - user may have modified it
                # We treat this as "modified" (user changed) which will trigger a warning
                modified_files.append(
                    FileStatus(
                        path=relative_path,
                        status="modified",
                        source_checksum=source_checksum,
                        target_checksum=target_checksum,
                    )
                )

    return InstallationAnalysis(
        new_files=new_files,
        identical_files=identical_files,
        modified_files=modified_files,
        updated_files=updated_files,  # Currently empty - could be used for version tracking
    )


def install_files(
    source_dir: Path,
    target_dir: Path,
    analysis: InstallationAnalysis,
    force: bool = False,
    dry_run: bool = False,
) -> InstallationResult:
    """Install files from source to target directory.

    Args:
        source_dir: Directory containing source files
        target_dir: Target directory for installation
        analysis: Pre-computed analysis of installation
        force: If True, overwrite modified files
        dry_run: If True, don't actually copy files

    Returns:
        Result of installation operation
    """
    import shutil
    from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn

    from .utils import ensure_directory

    files_added: List[Path] = []
    files_skipped: List[Path] = []
    files_updated: List[Path] = []
    conflicts: List[Path] = []

    # Calculate total files to process
    files_to_copy = analysis.new_files.copy()

    # Add modified files to copy list if force is enabled
    if force:
        files_to_copy.extend(analysis.modified_files)
    else:
        # Modified files are conflicts when force is not enabled
        conflicts.extend([f.path for f in analysis.modified_files])

    total_files = len(files_to_copy)

    if total_files > 0 and not dry_run:
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
        ) as progress:
            task = progress.add_task("[green]Installing files...", total=total_files)

            for file_status in files_to_copy:
                source_file = source_dir / file_status.path
                target_file = target_dir / file_status.path

                # Ensure target directory exists
                ensure_directory(target_file.parent)

                # Copy the file
                shutil.copy2(source_file, target_file)

                # Track the result
                if file_status.status == "new":
                    files_added.append(file_status.path)
                elif file_status.status == "modified":
                    files_updated.append(file_status.path)

                progress.advance(task)
    elif dry_run:
        # In dry-run mode, just track what would happen
        for file_status in files_to_copy:
            if file_status.status == "new":
                files_added.append(file_status.path)
            elif file_status.status == "modified":
                files_updated.append(file_status.path)

    # Identical files are always skipped
    files_skipped.extend([f.path for f in analysis.identical_files])

    # Modified files without force are skipped (and added to conflicts)
    if not force:
        files_skipped.extend([f.path for f in analysis.modified_files])

    return InstallationResult(
        files_added=files_added,
        files_skipped=files_skipped,
        files_updated=files_updated,
        conflicts=conflicts,
    )

"""CLI interface for claude-workflow."""

import shutil
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from .fetcher import fetch_latest, FetchError
from .installer import analyze_installation, install_files
from .utils import ensure_directory

console = Console()


@click.group()
def main():
    """Claude Workflow - Install Claude Code workflow files into your projects."""
    pass


@main.command()
@click.argument("target", type=click.Path(), default=".")
@click.option("--force", is_flag=True, help="Overwrite modified files")
@click.option("--dry-run", is_flag=True, help="Show what would be installed without making changes")
def install(target: str, force: bool, dry_run: bool):
    """Install workflow files to TARGET directory.

    Args:
        target: Target directory for installation (default: current directory)
        force: Overwrite modified files
        dry_run: Show what would be installed without making changes
    """
    target_path = Path(target).resolve()

    # Validate and create target directory
    try:
        ensure_directory(target_path)
    except Exception as e:
        console.print(f"[red]Error:[/red] Cannot create target directory: {e}")
        sys.exit(1)

    # Check if target is writable
    if not target_path.exists() or not target_path.is_dir():
        console.print(f"[red]Error:[/red] Target path is not a directory: {target_path}")
        sys.exit(1)

    # Fetch latest files
    try:
        data_dir = fetch_latest()
    except FetchError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

    # Analyze installation
    try:
        analysis = analyze_installation(data_dir, target_path)
    except Exception as e:
        console.print(f"[red]Error:[/red] Failed to analyze installation: {e}")
        sys.exit(1)

    # Show what will be done
    if dry_run:
        console.print("\n[bold]Dry run - no files will be modified[/bold]\n")

    # Create summary table
    table = Table(title="Installation Summary")
    table.add_column("Status", style="bold")
    table.add_column("Count", justify="right")
    table.add_column("Description")

    table.add_row("New", str(len(analysis.new_files)), "[green]Files to be added[/green]")
    table.add_row("Identical", str(len(analysis.identical_files)), "[dim]Files already up-to-date[/dim]")
    table.add_row("Modified", str(len(analysis.modified_files)),
                  "[yellow]Files changed by user[/yellow]" if not force else "[yellow]Files to be overwritten[/yellow]")

    console.print(table)

    # Show conflicts if any
    if analysis.modified_files and not force:
        console.print("\n[yellow]Warning:[/yellow] The following files have been modified:")
        for file_status in analysis.modified_files:
            console.print(f"  • {file_status.path}")
        console.print("\nUse --force to overwrite these files.")

    # Perform installation
    if not dry_run:
        try:
            result = install_files(data_dir, target_path, analysis, force=force, dry_run=False)
        except Exception as e:
            console.print(f"\n[red]Error:[/red] Installation failed: {e}")
            sys.exit(1)
        finally:
            # Clean up temporary directory
            temp_root = data_dir.parent.parent
            if temp_root.exists() and "claude-workflow-" in str(temp_root):
                shutil.rmtree(temp_root, ignore_errors=True)

        # Show results
        console.print("\n[bold green]✓ Installation complete![/bold green]")

        if result.files_added:
            console.print(f"\n[green]Added {len(result.files_added)} files[/green]")
        if result.files_updated:
            console.print(f"[yellow]Updated {len(result.files_updated)} files[/yellow]")
        if result.files_skipped:
            console.print(f"[dim]Skipped {len(result.files_skipped)} files[/dim]")

        # Show next steps
        console.print("\n[bold]Next steps:[/bold]")
        console.print("  1. Edit CLAUDE.md with your project-specific details")
        console.print("  2. Review the workflow documentation in .constitution/")
        console.print("  3. Start using /write-plan, /implement-plan, and /amend-plan commands")
    else:
        # Clean up in dry-run mode too
        temp_root = data_dir.parent.parent
        if temp_root.exists() and "claude-workflow-" in str(temp_root):
            shutil.rmtree(temp_root, ignore_errors=True)


@main.command()
@click.argument("target", type=click.Path(), default=".")
@click.option("--force", is_flag=True, help="Overwrite modified files")
@click.option("--dry-run", is_flag=True, help="Show what would be installed without making changes")
def update(target: str, force: bool, dry_run: bool):
    """Update workflow files in TARGET directory.

    Args:
        target: Target directory containing existing workflow files (default: current directory)
        force: Overwrite modified files
        dry_run: Show what would be updated without making changes
    """
    target_path = Path(target).resolve()

    # Validate target directory exists
    if not target_path.exists() or not target_path.is_dir():
        console.print(f"[red]Error:[/red] Target path does not exist or is not a directory: {target_path}")
        sys.exit(1)

    # Check if .claude directory exists (indicates previous installation)
    claude_dir = target_path / ".claude"
    if not claude_dir.exists():
        console.print(f"[red]Error:[/red] No existing workflow installation found in {target_path}")
        console.print("Use 'install' command for first-time installation.")
        sys.exit(1)

    # Fetch latest files
    try:
        data_dir = fetch_latest()
    except FetchError as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)

    # Analyze installation
    try:
        analysis = analyze_installation(data_dir, target_path)
    except Exception as e:
        console.print(f"[red]Error:[/red] Failed to analyze update: {e}")
        sys.exit(1)

    # Show what will be done
    if dry_run:
        console.print("\n[bold]Dry run - no files will be modified[/bold]\n")

    # Create summary table
    table = Table(title="Update Summary")
    table.add_column("Status", style="bold")
    table.add_column("Count", justify="right")
    table.add_column("Description")

    table.add_row("New", str(len(analysis.new_files)), "[green]New files to be added[/green]")
    table.add_row("Up-to-date", str(len(analysis.identical_files)), "[dim]Files already current[/dim]")
    table.add_row("Modified", str(len(analysis.modified_files)),
                  "[yellow]Files changed by user[/yellow]" if not force else "[yellow]Files to be overwritten[/yellow]")

    console.print(table)

    # Show conflicts if any
    if analysis.modified_files and not force:
        console.print("\n[yellow]Warning:[/yellow] The following files have been modified:")
        for file_status in analysis.modified_files:
            console.print(f"  • {file_status.path}")
        console.print("\nUse --force to overwrite these files.")

    # Perform update
    if not dry_run:
        try:
            result = install_files(data_dir, target_path, analysis, force=force, dry_run=False)
        except Exception as e:
            console.print(f"\n[red]Error:[/red] Update failed: {e}")
            sys.exit(1)
        finally:
            # Clean up temporary directory
            temp_root = data_dir.parent.parent
            if temp_root.exists() and "claude-workflow-" in str(temp_root):
                shutil.rmtree(temp_root, ignore_errors=True)

        # Show results
        console.print("\n[bold green]✓ Update complete![/bold green]")

        if result.files_added:
            console.print(f"\n[green]Added {len(result.files_added)} new files[/green]")
        if result.files_updated:
            console.print(f"[yellow]Updated {len(result.files_updated)} files[/yellow]")
        if result.files_skipped:
            console.print(f"[dim]Skipped {len(result.files_skipped)} files (unchanged or user-modified)[/dim]")

        # Show notice about modified files
        if result.conflicts and not force:
            console.print(f"\n[yellow]Note: {len(result.conflicts)} user-modified files were not updated.[/yellow]")
            console.print("Use --force to overwrite these files if needed.")
    else:
        # Clean up in dry-run mode too
        temp_root = data_dir.parent.parent
        if temp_root.exists() and "claude-workflow-" in str(temp_root):
            shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    main()

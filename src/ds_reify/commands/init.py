import os
from pathlib import Path
from shutil import rmtree

import rich_click as rclick

from .. import CONTEXT_SETTINGS
from ..utils.prompt import confirm, prompt


def overwrite_contents(project_dir: str) -> None:
    """Overwrite the contents of the project directory"""
    try:
        for path in Path(project_dir).iterdir():
            if path.is_file():
                path.unlink()
            if path.is_dir():
                rmtree(path)
    except Exception as e:  # pragma: no cover
        rclick.ClickException(f"Failed to delete {path}. Reason: {e}")


def create_project_dir(project_dir: str) -> None:
    """Create the project directory"""
    if os.path.exists(project_dir):
        overwrite = confirm(
            "Project directory already exists. Overwrite?", default=False
        )
        if overwrite:
            overwrite_contents(project_dir)
        else:
            raise rclick.Abort
    else:
        os.makedirs(project_dir)


def prompt_project_dir(project_name: str) -> str:
    """Get the project directory"""
    default_location = f"{os.getcwd()}/{project_name.lower().replace(' ', '_')}"
    location = prompt("Project Location", default=default_location)
    return location


@rclick.command(context_settings=CONTEXT_SETTINGS)
def init() -> None:
    """Initialize a new project"""
    project_name = prompt("Project Name")
    project_dir = prompt_project_dir(project_name)
    create_project_dir(project_dir)

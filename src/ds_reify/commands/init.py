import os

from rich import print as rprint
import rich_click as rclick

from .. import CONTEXT_SETTINGS
from ..styles import DS_GREEN
from ..utils.prompt import prompt


def get_project_dir(settings: dict) -> str:
    """Get the project directory"""
    default_location = f'{os.getcwd()}/{settings["project_name"]}'
    rprint(
        f'[{DS_GREEN}]Hello {settings["project_name"]} at {default_location}[/]',
        ":vampire:",
    )
    return default_location


@rclick.command(context_settings=CONTEXT_SETTINGS)
def init() -> None:
    """Initialize a new project"""
    settings = {}
    settings["project_name"] = prompt("Project Name")
    settings["project_dir"] = get_project_dir(settings)

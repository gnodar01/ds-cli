from typing import List, Optional

from rich.prompt import Confirm, Prompt
import rich_click as rclick

from ..styles import DS_PURPLE_LIGHT


def prompt(
    prompt: str, choices: Optional[List[str]] = None, default: Optional[str] = None
) -> str:
    """Prompt the user for input"""
    res = Prompt.ask(
        f"[{DS_PURPLE_LIGHT}]{prompt}[/]", choices=choices, default=default
    )
    if res is None or res == "":
        raise rclick.ClickException(f"You must provide a value for {prompt!r}")
    return res


def confirm(prompt: str, default: Optional[bool] = None) -> bool:
    """Prompt the user for a yes/no answer"""
    return Confirm.ask(f"[{DS_PURPLE_LIGHT}]{prompt}[/]", default=default)

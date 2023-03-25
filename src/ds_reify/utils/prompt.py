from typing import Optional

from rich.prompt import Prompt

from ..styles import DS_PURPLE_LIGHT


def prompt(prompt: str, default: Optional[str] = None) -> str:
    """Prompt the user for input"""
    return Prompt.ask(f"[{DS_PURPLE_LIGHT}]{prompt}[/]", default=default)

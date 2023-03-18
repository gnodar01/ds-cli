from rich import print as rprint
import rich_click as rclick

from . import __version__, CONTEXT_SETTINGS
from .styles import DS_GREEN


@rclick.command(context_settings=CONTEXT_SETTINGS)
def hello():
    """Say Hello to the world"""
    rprint(f"[{DS_GREEN}]Hello[/], [bold magenta]World[/]!", ":vampire:")
    rclick.secho(f"Hello, [bold magenta]World[/bold magenta]! :vampire:")

@rclick.version_option(__version__, '-v', '--version')
@rclick.group(context_settings=CONTEXT_SETTINGS)
def main():
    """
    Command Line Interface for [bold #59559E link=https://distributedscience.github.io/Distributed-Something]Distributed-Something[/]
    """
    pass

main.add_command(hello)

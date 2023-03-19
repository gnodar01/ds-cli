from rich import print as rprint
import rich_click as rclick

from .. import CONTEXT_SETTINGS
from ..styles import DS_GREEN


@rclick.command(context_settings=CONTEXT_SETTINGS)
def hello():
    '''Say Hello to the world'''
    rprint(f'[{DS_GREEN}]Hello[/], [bold magenta]World[/]!', ':vampire:')
    rclick.secho(f'Hello, [bold magenta]World[/bold magenta]! :vampire:')

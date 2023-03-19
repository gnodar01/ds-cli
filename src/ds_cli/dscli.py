import rich_click as rclick

from . import __version__, CONTEXT_SETTINGS

from .commands.hello import hello


@rclick.version_option(__version__, '-v', '--version')
@rclick.group(context_settings=CONTEXT_SETTINGS)
def main():
    '''
    Command Line Interface for [bold #59559E link=https://distributedscience.github.io/Distributed-Something]Distributed-Something[/]
    '''
    ...

main.add_command(hello)

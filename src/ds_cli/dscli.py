import click

from . import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def main():
    """Distributed-Something Command Line Interface"""
    click.echo("Hello, World!")


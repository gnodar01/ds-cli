import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """DistributedSomething Command Line Interface"""
    click.echo("Hello, World!")


import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern cookbook of Claudio Jolowicz's hypermodern python article and repo"""
    click.echo("Hello, world!")

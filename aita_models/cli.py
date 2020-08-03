# _*_ coding: utf-8 _*_

"""Console script for aita_models."""
import sys
import click
from aita_models.aita_models import func1


@click.command()
def main(args=None):
    """console script for aita_models."""
    click.echo("Hello, what would you like to search for?")
    return 0


if __name__ == "__main__":
    sys.exit(main()) # pragma: no cover

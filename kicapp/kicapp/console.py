"""Command line interface for kicapp."""

import click


@click.group()
def cli() -> None:
    """Entrypoint for invocation as command line program."""


def run() -> None:
    """Entrypoint for invocation as module."""
    cli()


if __name__ == "__main__":
    run()

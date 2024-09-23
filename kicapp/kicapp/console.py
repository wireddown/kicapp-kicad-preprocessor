"""Command line interface for kicapp."""

import click


@click.group()
def cli() -> None:
    """Run a command to prepare EDA files for importing into KiCad."""


def run() -> None:
    """Entrypoint for invocation as module."""
    cli()


if __name__ == "__main__":
    run()

"""Command line interface for kicapp."""

import logging

import click

import kicapp.click_logging

logger = logging.getLogger(__name__)


@click.group(invoke_without_command=True)
@click.help_option()
@click.option("-q", "--quiet", is_flag=True, default=False, help="Suppress warning messages.")
@click.option("-v", "--verbose", is_flag=True, default=False, help="Enable verbose messages.")
@click.version_option()
@click.option("--logging-demo", is_flag=True, default=False, hidden=True)
def cli(quiet: bool, verbose: bool, logging_demo: bool) -> None:  # noqa: FBT001
    """Run a command to prepare EDA files for importing into KiCad."""
    log_level = get_logging_level(quiet, verbose)

    kicapp.click_logging.initialize(log_level)

    if logging_demo:
        kicapp.click_logging.show_logging_demo(logger)
    else:
        cli(["--help"])


def run() -> None:
    """Entrypoint for invocation as module."""
    cli()


def get_logging_level(quiet: bool, verbose: bool) -> int:  # noqa: FBT001
    """Get the logging level for the specified quiet and verbose options."""
    log_level = logging.INFO
    if verbose:
        log_level = logging.DEBUG
    if quiet:
        log_level = logging.ERROR
    return log_level


if __name__ == "__main__":
    run()

"""Tests for the kicapp command line interface."""

import logging

from click.testing import CliRunner

from kicapp import console


def test_console():  # noqa: ANN201
    """Does it invoke the base command group?"""
    runner = CliRunner()
    result = runner.invoke(console.cli)
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_default_verbosity():  # noqa: ANN201
    """Does it use INFO as the default verbosity?"""
    log_level = console.get_logging_level(quiet=False, verbose=False)
    assert log_level == logging.INFO, "Default logging level should be 'logging.INFO' but it isn't"


def test_quiet_verbosity():  # noqa: ANN201
    """Does it use ERROR as the verbosity for --quiet?"""
    log_level = console.get_logging_level(quiet=True, verbose=False)
    assert log_level == logging.ERROR, "Quiet logging level should be 'logging.ERROR' but it isn't"


def test_verbose_verbosity():  # noqa: ANN201
    """Does it use DEBUG as the verbosity for --verbose?"""
    log_level = console.get_logging_level(quiet=False, verbose=True)
    assert log_level == logging.DEBUG, "Verbose logging level should be 'logging.DEBUG' but it isn't"


def test_quiet_velocity_wins():  # noqa: ANN201
    """Does --quiet win over --verbose?"""
    log_level = console.get_logging_level(quiet=True, verbose=True)
    assert log_level == logging.ERROR, "--quiet should override --verbose but it didn't"

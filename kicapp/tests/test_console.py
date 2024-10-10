"""Tests for the kicapp command line interface."""

import logging

import pytest
from click.testing import CliRunner

from kicapp import console


def test_console():  # noqa: ANN201
    """Does it invoke the base command group?"""
    runner = CliRunner()
    result = runner.invoke(console.cli)
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


@pytest.mark.parametrize(
    ("quiet", "verbose", "expected_log_level", "assert_message"),
    [
        (False, False, logging.INFO, "Default logging level should be 'logging.INFO'"),
        (True, False, logging.ERROR, "Quiet logging level should be 'logging.ERROR'"),
        (False, True, logging.DEBUG, "Verbose logging level should be 'logging.DEBUG'"),
        (True, True, logging.ERROR, "--quiet should override --verbose"),
    ],
)
def test_verbosity_truth_table(quiet, verbose, expected_log_level, assert_message):  # noqa: ANN001 ANN201
    """Validate all combinations of --quiet and --verbose."""
    log_level = console.get_logging_level(quiet, verbose)
    assert log_level == expected_log_level, assert_message

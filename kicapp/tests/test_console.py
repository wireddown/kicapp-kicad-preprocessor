"""Tests for the kicapp command line interface."""

from click.testing import CliRunner

from kicapp import console


def test_console() -> None:
    """Does it invoke the base command group?"""
    runner = CliRunner()
    result = runner.invoke(console.cli)
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output

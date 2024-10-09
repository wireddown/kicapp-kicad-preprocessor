"""Tests for the logging extensions."""

import logging

from kicapp import click_logging

TEST_LOGGER = logging.getLogger(__name__)


def test_default_logging_demo(capsys, caplog):  # noqa: ANN001 ANN201
    """Does it emit the correct log messages for default verbosity?"""
    log_level = logging.INFO
    with caplog.at_level(log_level):
        click_logging.initialize(log_level, TEST_LOGGER)
        click_logging.show_logging_demo(TEST_LOGGER)

    output_messages = capsys.readouterr()
    stderr_messages = output_messages.err.strip()

    assert stderr_messages.startswith("INFO     info world")
    assert stderr_messages.endswith("WARNING  exception handled")


def test_quiet_logging_demo(capsys, caplog):  # noqa: ANN001 ANN201
    """Does it emit the correct log messages for quiet verbosity?"""
    log_level = logging.ERROR
    with caplog.at_level(log_level):
        click_logging.initialize(log_level, TEST_LOGGER)
        click_logging.show_logging_demo(TEST_LOGGER)

    output_messages = capsys.readouterr()
    stderr_messages = output_messages.err.strip()

    assert stderr_messages.startswith("ERROR    error world")
    assert stderr_messages.endswith("ERROR    NameError: name error world")


def test_verbose_logging_demo(capsys, caplog):  # noqa: ANN001 ANN201
    """Does it emit the correct log messages for verbose verbosity?"""
    log_level = logging.DEBUG
    with caplog.at_level(log_level):
        click_logging.initialize(log_level, TEST_LOGGER)
        click_logging.show_logging_demo(TEST_LOGGER)

    output_messages = capsys.readouterr()
    stderr_messages = output_messages.err.strip()

    now = logging.time.localtime()
    year_month_day = logging.time.strftime("%Y.%m.%d", now)
    first_message = stderr_messages.splitlines()[0]
    last_message = stderr_messages.splitlines()[-1]

    assert first_message.startswith(f"{year_month_day} ")
    assert " DEBUG " in first_message
    assert last_message.startswith(f"{year_month_day} ")
    assert " WARNING " in last_message

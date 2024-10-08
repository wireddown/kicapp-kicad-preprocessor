"""Logging handler and formatter with click colors."""

import logging

import click


class ClickHandler(logging.Handler):
    _use_stderr = True

    def emit(self, record):
        try:
            formatted_entry = self.format(record)
            click.echo(formatted_entry, err=self._use_stderr)
        except Exception:
            self.handleError(record)


class ColorFormatter(logging.Formatter):
    colors = {
        'critical': dict(fg='bright_magenta'),
        'exception': dict(fg='red'),
        'error': dict(fg='red'),
        'warning': dict(fg='yellow'),
        'info': dict(fg='cyan'),
        'debug': dict(fg='white'),
    }

    def __init__(self, level=logging.NOTSET):
        self.level = self._checkLevel(level)

    def _checkLevel(self, level):
        if isinstance(level, int):
            valid_level = level
        elif str(level) == level:
            valid_levels = logging.getLevelNamesMapping()
            if level not in valid_levels:
                raise ValueError("Unknown level: %r" % level)
            valid_level = valid_levels[level]
        else:
            raise TypeError("Level not an integer or a valid string: %r"
                            % (level,))
        return valid_level

    def setLevel(self, level):
        self.level = self._checkLevel(level)

    def format(self, record):
        if record.exc_info:
            default_formatter = logging.Formatter()
            formatted_message = default_formatter.format(record)
        else:
            formatted_message = record.getMessage()

        level = record.levelname.lower()
        color_style = self.colors.get(level, dict(fg="bright_white"))

        time_string = ""
        location_string = ""
        if self.level < logging.WARNING:
            timestamp = logging.time.localtime(record.created)
            time_string = click.style(f"{logging.time.strftime('%Y.%m.%d %H:%M:%S', timestamp)}.{record.msecs:03.0f}", **color_style)
            location_string = click.style(f"{record.name:>30}::{record.funcName} L{record.lineno:>4}", **color_style)

        severity_string = click.style(f"{record.levelname:<8}", **color_style)
        message_strings = [click.style(line, fg="bright_white") for line in formatted_message.splitlines()]

        entry_prefix = f"{time_string} {location_string} {severity_string}"
        formatted_entry = '\n'.join(f"{entry_prefix} {line}".strip() for line in message_strings)

        return formatted_entry


def buildClickHandler(log_level) -> ClickHandler:
    """Create a logging Handler with click and color support."""
    click_handler = ClickHandler()
    click_handler.setLevel(log_level)
    color_formatter = ColorFormatter()
    color_formatter.setLevel(log_level)
    click_handler.setFormatter(color_formatter)
    return click_handler


def setLoggingLevel(level):
    """Set the specified level on the underlying handler and formatter."""


def show_logging_demo(logger: logging.Logger):
    """Show the different kinds of messages for the specified logger."""
    logger.debug("debug world")
    logger.info("info world")
    logger.warning("warning world")
    logger.error("error world")
    logger.critical("critical world")
    try:
        raise NameError("name error world")
    except NameError as err:
        logger.exception(err)
    logger.warning("exception handled")

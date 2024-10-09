"""Logging handler and formatter with click colors on stderr."""

import logging

import click


class ClickHandler(logging.Handler):
    """A logging.Handler that uses click.echo() to emit records."""

    _use_stderr = True

    def emit(self: "ClickHandler", record: logging.LogRecord) -> None:
        """Log the specified logging record with click.echo()."""
        try:
            formatted_entry = self.format(record)
            click.echo(formatted_entry, err=self._use_stderr)
        except Exception:  # noqa: BLE001
            self.handleError(record)


class ColorFormatter(logging.Formatter):
    """A logging.Formatter that uses click.style() to format records."""

    COLORS = {
        "critical": {"fg": "bright_magenta"},
        "exception": {"fg": "red"},
        "error": {"fg": "red"},
        "warning": {"fg": "yellow"},
        "info": {"fg": "cyan"},
        "debug": {"fg": "white"},
    }

    def __init__(self: "ColorFormatter", level: int | str = logging.NOTSET) -> None:
        """Create a new ColorFormatter with the specific logging level."""
        self.level = self._check_level(level)

    def _check_level(self: "ColorFormatter", level: int | str) -> int:
        if isinstance(level, int):
            valid_level = level
        elif str(level) == level:
            valid_levels = logging.getLevelNamesMapping()
            if level not in valid_levels:
                exception_message = f"Unknown level: {level}"
                raise ValueError(exception_message)
            valid_level = valid_levels[level]
        else:
            exception_message = f"Level not an integer or a valid string: {level}"
            raise TypeError(exception_message)
        return valid_level

    def set_level(self: "ColorFormatter", level: int | str) -> None:
        """Set the logging verbosity level."""
        self.level = self._check_level(level)

    def format(self: "ColorFormatter", record: logging.LogRecord) -> str:
        """Format the specified record."""
        if record.exc_info:
            default_formatter = logging.Formatter()
            formatted_message = default_formatter.format(record)
        else:
            formatted_message = record.getMessage()

        level = record.levelname.lower()
        color = self.COLORS.get(level, "bright_white")

        time_string = ""
        location_string = ""
        if self.level < logging.INFO:
            timestamp = logging.time.localtime(record.created)
            time_string = click.style(
                f"{logging.time.strftime('%Y.%m.%d %H:%M:%S', timestamp)}.{record.msecs:03.0f}", **color_style
            )
            location_string = click.style(f"{record.name:>30}::{record.funcName} {record.lineno:>4}", **color_style)

        severity_string = click.style(f"{record.levelname:<8}", **color_style)
        message_strings = [click.style(line, fg="bright_white") for line in formatted_message.splitlines()]

        entry_prefix = f"{time_string} {location_string} {severity_string}"
        return "\n".join(f"{entry_prefix} {line}".strip() for line in message_strings)


def initialize(log_level: int | str, logger: logging.Logger | None = None) -> None:
    """Configure the logging system to use colors."""
    click_handler = build_click_handler(log_level)

    logging.basicConfig(
        handlers=[click_handler],
        level=log_level,
    )

    if logger:
        logger.addHandler(click_handler)


def build_click_handler(log_level: int | str) -> ClickHandler:
    """Create a logging Handler with click and color support."""
    click_handler = ClickHandler()
    click_handler.setLevel(log_level)
    color_formatter = ColorFormatter()
    color_formatter.set_level(log_level)
    click_handler.setFormatter(color_formatter)
    return click_handler


def show_logging_demo(logger: logging.Logger) -> None:
    """Show the different kinds of messages for the specified logger."""
    logger.debug("debug world")
    logger.info("info world")
    logger.warning("warning world")
    logger.error("error world")
    logger.critical("critical world")
    try:
        exception_message = "name error world"
        raise NameError(exception_message)
    except NameError as err:
        logger.exception(err)
    logger.warning("exception handled")

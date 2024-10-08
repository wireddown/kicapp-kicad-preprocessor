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

    def format(self, record):
        if not record.exc_info:
            formatted_message = record.getMessage()
            level = record.levelname.lower()
            color_style = self.colors.get(level, dict(fg="bright_white"))
            time_string = ""
            location_string = ""
            if logger.level < logging.WARNING:
                timestamp = logging.time.localtime(record.created)
                time_string = click.style(f"{logging.time.strftime('%Y.%m.%d %H:%M:%S', timestamp)}.{record.msecs:03.0f}", **color_style)
                location_string = click.style(f"{record.name:>30}::{record.funcName} L{record.lineno:>4}", **color_style)
            severity_string = click.style(f"{record.levelname:<8}", **color_style)
            message_strings = [click.style(line, fg="bright_white") for line in formatted_message.splitlines()]
            entry_prefix = f"{time_string} {location_string} {severity_string}"
            formatted_entry = '\n'.join(f"{entry_prefix} {line}".strip() for line in message_strings)
            return formatted_entry
        return logging.Formatter.format(self, record)

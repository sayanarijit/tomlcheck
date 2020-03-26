import logging
from argparse import Namespace
from enum import Enum

import toml


class LogLevels(Enum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    critical = "CRITICAL"


def check(filepath: str) -> bool:
    """Check a single file."""

    logging.debug(filepath, extra=dict(status="checking"))

    try:
        with open(filepath) as f:
            toml.load(f)
    except toml.TomlDecodeError as err:
        logging.error(filepath, extra=dict(status=err.msg))
        return False

    logging.info(filepath, extra=dict(status="ok"))
    return True


def main(args: Namespace) -> int:
    return 0 if all(list(map(check, args.files))) else 1

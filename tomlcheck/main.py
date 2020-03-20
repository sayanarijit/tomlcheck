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


def check(filepath: str) -> None:
    """Check a single file."""

    logging.debug(f"Checking {filepath}...")

    with open(filepath) as f:
        toml.load(f)

    logging.info(f"{filepath}: OK")


def main(args: Namespace) -> int:
    list(map(check, args.files))
    return 0

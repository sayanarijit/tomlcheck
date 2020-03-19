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


def check_multi_thread(*files: str, max_workers: int = 0):
    from concurrent.futures import ThreadPoolExecutor, as_completed

    pool = ThreadPoolExecutor(max_workers=max_workers)
    for task in as_completed([pool.submit(check, x) for x in files]):
        task.result()


def check_single_thread(*files: str):
    list(map(check, files))


def main(args: Namespace) -> int:
    if args.force_single_thread or len(args.files) < 10:
        check_single_thread(*args.files)
    else:
        check_multi_thread(*args.files, max_workers=args.max_workers)
    return 0

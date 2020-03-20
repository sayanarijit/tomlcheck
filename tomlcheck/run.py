import logging
import sys
from argparse import ArgumentParser

from tomlcheck import __description__, __version__
from tomlcheck.main import LogLevels, main


def run() -> None:
    parser = ArgumentParser("tomlcheck", description=__description__)
    parser.add_argument("files", nargs="*")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "--log-level",
        choices=[x.value for x in LogLevels],
        default=LogLevels.warning.value,
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    sys.exit(main(args=args))


if __name__ == "__main__":
    run()

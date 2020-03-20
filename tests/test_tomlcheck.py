from argparse import Namespace

import pytest
from toml.decoder import TomlDecodeError
from tomlcheck.main import main
from subprocess import run, CalledProcessError
from unittest import mock

TOML_FILES = ["pyproject.toml", "poetry.toml"] * 10
NON_TOML_FILES = ["README.rst", "poetry.lock"] * 10


def test_main_pass():
    args = Namespace(files=TOML_FILES, log_level="info")
    with mock.patch("tomlcheck.main.logging") as mock_logging:
        main(args=args)
    mock_logging.debug.assert_called_with(f"Checking {TOML_FILES[-1]}...")
    mock_logging.info.assert_called_with(f"{TOML_FILES[-1]}: OK")


def check_main_fail():
    args = Namespace(files=NON_TOML_FILES, log_level="info")
    with pytest.raises(TomlDecodeError):
        with mock.patch("tomlcheck.main.logging") as mock_logging:
            main(args=args)
    mock_logging.debug.assert_called_with(f"Checking {TOML_FILES[0]}...")
    assert not mock_logging.info.called


def test_command_line_pass():
    run(["python", "-m", "tomlcheck.run", *TOML_FILES]).check_returncode()


def test_command_line_fail():
    with pytest.raises(CalledProcessError):
        run(["python", "-m", "tomlcheck.run", *NON_TOML_FILES]).check_returncode()

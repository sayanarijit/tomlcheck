from argparse import Namespace

import pytest
from tomlcheck.main import main
from subprocess import run
from unittest import mock

TOML_FILES = ["pyproject.toml", "poetry.toml", "poetry.lock"] * 10
NON_TOML_FILES = ["README.rst", ".travis.yml"]


def test_main_pass():
    args = Namespace(files=TOML_FILES, log_level="INFO")
    with mock.patch("tomlcheck.main.logging") as mock_logging:
        assert main(args=args) == 0
    mock_logging.debug.assert_called_with(TOML_FILES[-1], extra=dict(status="checking"))
    mock_logging.info.assert_called_with(TOML_FILES[-1], extra=dict(status="ok"))
    assert not mock_logging.error.called


def test_main_fail():
    args = Namespace(files=NON_TOML_FILES, log_level="INFO")
    with mock.patch("tomlcheck.main.logging") as mock_logging:
        assert main(args=args) == 1
    mock_logging.error.assert_has_calls(
        [
            mock.call(
                NON_TOML_FILES[0],
                extra=dict(status="Key name found without value. Reached end of line."),
            ),
            mock.call(
                NON_TOML_FILES[1],
                extra=dict(
                    status="Found invalid character in key name: ':'. Try quoting the key name."
                ),
            ),
        ]
    )

    assert not mock_logging.info.called


def test_command_line_pass():
    run(["python", "-m", "tomlcheck.run", *TOML_FILES]).check_returncode()
    run(
        ["python", "-m", "tomlcheck.run", "-"], input=("\n".join(TOML_FILES).encode())
    ).check_returncode()


def test_command_line_fail():
    assert run(["python", "-m", "tomlcheck.run", *NON_TOML_FILES]).returncode == 1
    assert (
        run(
            ["python", "-m", "tomlcheck.run", "-"],
            input=("\n".join(NON_TOML_FILES).encode()),
        ).returncode
        == 1
    )


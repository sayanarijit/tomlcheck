from argparse import Namespace

import pytest
from toml.decoder import TomlDecodeError


def test_main_single_thread_unforced():

    from tomlcheck.main import main

    files = ["pyproject.toml", "poetry.toml"]

    args = Namespace(files=files, log_level="info", force_single_thread=False)
    main(args=args)

    with pytest.raises(TomlDecodeError):
        args.files = ["README.rst"]
        main(args=args)


def test_main_single_thread_forced():

    from tomlcheck.main import main

    files = ["pyproject.toml", "poetry.toml"] * 10

    args = Namespace(files=files, log_level="info", force_single_thread=True)
    main(args=args)

    with pytest.raises(TomlDecodeError):
        args.files = ["README.rst"] * 20
        main(args=args)


def test_main_multithread_thread():

    from tomlcheck.main import main

    files = ["pyproject.toml", "poetry.toml"] * 10

    args = Namespace(
        files=files, log_level="info", force_single_thread=False, max_workers=10,
    )
    main(args=args)

    with pytest.raises(TomlDecodeError):
        args.files = ["README.rst"] * 20
        main(args=args)

tomlcheck
==========

.. image:: https://img.shields.io/pypi/v/tomlcheck.svg
    :target: https://pypi.org/project/tomlcheck
    :alt:

.. image:: https://img.shields.io/pypi/pyversions/tomlcheck.svg
    :target: https://pypi.org/project/tomlcheck
    :alt:

.. image:: https://travis-ci.com/sayanarijit/tomlcheck.svg?branch=master
    :target: https://travis-ci.com/sayanarijit/tomlcheck
    :alt:

.. image:: https://codecov.io/gh/sayanarijit/tomlcheck/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sayanarijit/tomlcheck
    :alt:

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black
    :alt:


A simple toml syntax checker.

Designed to be used by `pre-commit <https://github.com/pre-commit/pre-commit>`_ hooks.


Installation
------------

.. code-block:: bash

    pip install -U tomlcheck


Usage
-----

Check files:

.. code-block:: bash

    tomlcheck $(find . -type f -name "*.toml")

    # Or read from stdin

    find . -type f -name "*.toml" | tomlcheck -


With logging:

.. code-block:: bash

    tomlcheck --log-level DEBUG $(find . -type f -name "*.toml")
    
    # Or read from stdin

    find . -type f -name "*.toml" | tomlcheck --log-level DEBUG -

In `pre-commit <https://github.com/pre-commit/pre-commit>`_ config:

.. code-block:: yaml

    # .pre-commit-config.yaml

    - repo: local
      hooks:
      - id: tomlcheck
        name: Check TOML Syntax
        description: Checks TOML files for valid syntax.
        entry: tomlcheck
        language: system
        files: \**/*.toml$
        stages: [commit, push, manual]


Help Menu
---------

.. code-block:: bash

    tomlcheck --help

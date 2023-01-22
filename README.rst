========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |appveyor| |circleci| |requires|
        | |codecov|
        | |codeclimate|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/pyfuckery/badge/?style=flat
    :target: https://readthedocs.org/projects/pyfuckery
    :alt: Documentation Status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/williamgibb/pyFuckery?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/williamgibb/pyFuckery

.. |circleci| image:: https://circleci.com/gh/williamgibb/pyFuckery.svg?style=svg
    :alt: CircleCI Build Status
    :target: https://circleci.com/gh/williamgibb/pyFuckery

.. |requires| image:: https://requires.io/github/williamgibb/pyFuckery/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/williamgibb/pyFuckery/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/williamgibb/pyFuckery/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/williamgibb/pyFuckery

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/c983cdddacfb3eab3f86/maintainability
   :target: https://codeclimate.com/github/williamgibb/pyFuckery/maintainability
   :alt: Maintainability

.. |version| image:: https://img.shields.io/pypi/v/fuckery.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/fuckery

.. |commits-since| image:: https://img.shields.io/github/commits-since/williamgibb/pyFuckery/v0.6.0.svg
    :alt: Commits since latest release
    :target: https://github.com/williamgibb/pyFuckery/compare/v0.6.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/fuckery.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/fuckery

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/fuckery.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/fuckery

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/fuckery.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/fuckery


.. end-badges

Python Brainfuck implemention.

* Free software: BSD license

Installation
============

::

    pip install fuckery

Documentation
=============

https://pyFuckery.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

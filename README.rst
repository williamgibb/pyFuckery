========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/pyfuckery/badge/?style=flat
    :target: https://readthedocs.org/projects/pyfuckery
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/williamgibb/pyFuckery.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/williamgibb/pyFuckery

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/williamgibb/pyFuckery?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/williamgibb/pyFuckery

.. |requires| image:: https://requires.io/github/williamgibb/pyFuckery/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/williamgibb/pyFuckery/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/williamgibb/pyFuckery/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/williamgibb/pyFuckery

.. |landscape| image:: https://landscape.io/github/williamgibb/pyFuckery/master/landscape.svg?style=flat
    :target: https://landscape.io/github/williamgibb/pyFuckery/master
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/pyfuckery.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pyfuckery

.. |commits-since| image:: https://img.shields.io/github/commits-since/williamgibb/pyFuckery/v0.2.1.svg
    :alt: Commits since latest release
    :target: https://github.com/williamgibb/pyFuckery/compare/v0.2.1...master

.. |downloads| image:: https://img.shields.io/pypi/dm/pyfuckery.svg
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pyfuckery

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyfuckery.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pyfuckery

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyfuckery.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pyfuckery

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyfuckery.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pyfuckery


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

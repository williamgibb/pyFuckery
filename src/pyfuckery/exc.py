#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyFuckery - exc.py
Created on 2/12/17.

Exception definitions
"""


class FuckeryError(Exception):
    """
    Base exception for pyFuckery errors.
    """


class MemoryError(FuckeryError):
    """
    Error doing a memory operation.
    """


class AddressError(MemoryError):
    """
    Error related to address violations.
    """

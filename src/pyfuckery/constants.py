#!/usr/bin/env python
# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
pyFuckery - constants.py
Created on 2/12/17.


"""
# Stdlib
import logging
import re
# Third Party Code
# Custom Code
log = logging.getLogger(__name__)


# Brainfuck tokens
SYM_PTR_INC = '>'
SYM_PTR_DEC = '<'
SYM_DATA_INC = '+'
SYM_DATA_DEC = '-'
SYM_IO_OUTPUT = '.'
SYM_IO_INPUT = ','
SYM_JMP_FWD = '['
SYM_JMP_BACKWARD = ']'


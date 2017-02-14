#!/usr/bin/env python
# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
pyFuckery - vm.py
Created on 2/12/17.


"""
# Stdlib
import argparse
import json
import logging
import os
import sys

# Third Party Code
# Custom Code
from pyfuckery.constants import DEFAULT_MEMORY_SIZE
from pyfuckery.memory import Storage
from pyfuckery.exc import VMError

log = logging.getLogger(__name__)


class VirtualMachine(object):
    def __init__(self, memory_size=DEFAULT_MEMORY_SIZE,  *args, **kwargs):
        self.data_pointer = 0
        self._memory_size = memory_size
        self.memory = Storage(n=memory_size)
        self.stream_in = sys.stdin
        self.stream_out = sys.stdout

    def inc_data_ptr(self):
        temp = self.data_pointer + 1
        if temp not in self.memory:
            raise VMError('Invalid memory address: {}'.format(temp))
        self.data_pointer = temp

    def dec_data_ptr(self):
        temp = self.data_pointer - 1
        if temp not in self.memory:
            raise VMError('Invalid memory address: {}'.format(temp))
        self.data_pointer = temp

    def inc_data_value(self):
        v = self.memory.get(self.data_pointer)
        v = (v + 1) % 256
        self.memory.set(addr=self.data_pointer, value=v)

    def dec_data_value(self):
        v = self.memory.get(self.data_pointer)
        v = (v - 1) % 256
        self.memory.set(addr=self.data_pointer, value=v)

    def io_output(self):
        v = self.memory.get(self.data_pointer)
        s = chr(v)
        try:
            buf = s.encode('ascii')
        except UnicodeEncodeError:
            buf = repr(s).encode('ascii')
        self.stream_out.write(buf)

    # XXX Finish IO handlings
    def io_input(self):
        raise NotImplementedError('Input not implmented yet.')


# noinspection PyMissingOrEmptyDocstring
def main(options):  # pragma: no cover
    if not options.verbose:
        logging.disable(logging.DEBUG)

    sys.exit(0)


# noinspection PyMissingOrEmptyDocstring
def makeargpaser():  # pragma: no cover
    # XXX Fill in description
    parser = argparse.ArgumentParser(description="Description.")
    parser.add_argument('-i', '--input', dest='input', required=True, type=str, action='store',
                        help='Input file to process')
    parser.add_argument('-v', '--verbose', dest='verbose', default=False, action='store_true',
                        help='Enable verbose output')
    return parser


def _main():  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
    p = makeargpaser()
    opts = p.parse_args()
    main(opts)


if __name__ == '__main__':  # pragma: no cover
    _main()

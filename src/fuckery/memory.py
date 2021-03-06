#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyFuckery - memory.py
Created on 2/12/17.

Memory object implementation.  Provides memory bounds checking, as well as value enforcement.
"""
# Stdlib
import argparse
import hashlib
import json
import logging
import sys

# Third Party Code
import msgpack

# Custom Code
from fuckery.constants import DEFAULT_MEMORY_SIZE
from fuckery.constants import MEMORY_MAX_VALUE
from fuckery.constants import MEMORY_MIN_VALUE
from fuckery.exc import AddressError
from fuckery.exc import StorageError

log = logging.getLogger(__name__)


class Storage(object):
    """
    Provides an interface for storing memory values for the Brainfuck VM.

    This provides for type safety &  memory access checking.
    """

    def __init__(self, n=DEFAULT_MEMORY_SIZE):
        """
        Init function for Storage.

        :param n: Number of memory cells to create.
        """
        self.n = n
        self.min = MEMORY_MIN_VALUE
        self.max = MEMORY_MAX_VALUE
        self.mem = {i: 0x00 for i in range(self.n)}

    @property
    def mem_hash(self):
        """
        Returns a hash of the state of the memory.

        Note - Computing this frequently can be expensive to do as the memory section is
        serialized via msgpack.dumps() prior to hashing.

        :return:
        """
        # We're abusing the python 3.6 ordereddict behavior which
        # became a part of the cpython spec in 3.7 for this
        # to work.  It really only works since we pre-initialize
        # the self.mem dictionary on startup.
        ret = hashlib.md5(msgpack.dumps(self.mem)).hexdigest()
        return ret

    def __contains__(self, item):
        return item in self.mem

    def __len__(self):
        return len(self.mem)

    def get(self, addr):
        """
        Get the value of the memory at a location.

        :param addr: Memory address to retrieve.
        :return:
        """
        if addr not in self:
            raise AddressError(f'Address is invalid: {addr}')
        return self.mem.get(addr)

    def set(self, addr, value):
        """
        Set the value of the memory at a locaiton.

        :param addr: Memory address to set.
        :param value: Value to set.
        :return:
        """
        if addr not in self:
            raise AddressError(f'Address is invalid: {addr}')
        if not isinstance(value, int):
            raise StorageError(f'Value is not an int: {type(value)}')
        if value < self.min or value > self.max:
            raise StorageError(f'Value is out of size bounds: {value}')
        self.mem[addr] = value


# noinspection PyMissingOrEmptyDocstring
def main(options):  # pragma: no cover
    if not options.verbose:
        logging.disable(logging.DEBUG)

    m = Storage(n=25)
    v = m.get(0)
    log.info(f'm[0] is {v}')
    m.set(24, 1)
    v = m.get(0)
    log.info(f'm[24] is {v}')
    sys.exit(0)


# noinspection PyMissingOrEmptyDocstring
def makeargpaser():  # pragma: no cover
    parser = argparse.ArgumentParser(description="Memory / Storage runner.")
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

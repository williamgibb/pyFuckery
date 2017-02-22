#!/usr/bin/env python
# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
pyFuckery - vm.py
Created on 2/12/17.


"""
# Stdlib
import argparse
import logging
import sys

# Third Party Code
from lark import Tree
# Custom Code
from pyfuckery.constants import DEFAULT_MEMORY_SIZE
from pyfuckery.constants import SYM_DATA_DEC
from pyfuckery.constants import SYM_DATA_INC
from pyfuckery.constants import SYM_PTR_DEC
from pyfuckery.constants import SYM_PTR_INC
from pyfuckery.constants import SYM_IO_INPUT
from pyfuckery.constants import SYM_IO_OUTPUT
from pyfuckery.constants import SYM_LOOP
from pyfuckery.constants import SYM_ACTIONS
from pyfuckery.constants import SYM_PROGRAM
from pyfuckery.constants import SYM_EXPRESSIONS
from pyfuckery.exc import VMError
from pyfuckery.memory import Storage

log = logging.getLogger(__name__)


class VirtualMachine(object):
    def __init__(self, memory_size=DEFAULT_MEMORY_SIZE,  *args, **kwargs):
        self.data_pointer = 0
        self._memory_size = memory_size
        self.memory = Storage(n=memory_size)
        self.loop_detection = True
        self.stream_in = sys.stdin
        self.stream_out = sys.stdout
        self.sym2func = {SYM_DATA_DEC: self.dec_data_value,
                         SYM_DATA_INC: self.inc_data_value,
                         SYM_IO_INPUT: self.io_input,
                         SYM_IO_OUTPUT: self.io_output,
                         SYM_PTR_DEC: self.dec_data_ptr,
                         SYM_PTR_INC: self.inc_data_ptr,
                         }

    @property
    def current_value(self):
        return self.memory.get(self.data_pointer)

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

    def run(self, tree: Tree):
        # XXX This is a manual tree parsing.  Can we do better with a lark Transformer?
        if tree.data == SYM_PROGRAM:
            log.debug('Program entry point.')
            for t in tree.children:
                self.run(t)
            return
        if tree.data == SYM_ACTIONS:
            token = tree.children[0]
            func = self.sym2func.get(token)
            func()
            return
        if tree.data == SYM_EXPRESSIONS:
            for i, t in enumerate(tree.children):
                # log.debug('Executing command #{} - {}'.format(i, repr(t)))
                self.run(tree=t)
            return
        if tree.data == SYM_LOOP:
            sh = self.memory.state_hash
            while self.current_value != 0:
                for t in tree.children:
                    if isinstance(t, Tree):
                        self.run(tree=t)
                if self.loop_detection and self.memory.state_hash == sh:
                    raise VMError('Infinite loop detected - no change in memory during loop execution!')
                sh = self.memory.state_hash
            return
        raise NotImplementedError('Unknown tree type seen: {}'.format(tree.data))  # pragma: no cover

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

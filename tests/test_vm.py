# -*- coding: utf-8 -*-
# XXX Update Docstring
"""
pyFuckery - test_vm.py
Created on 2/12/17.


"""
# Stdlib
import logging

# Third party code
import pytest

# Custom code
from pyfuckery.exc import VMError
from pyfuckery.vm import VirtualMachine

# Logging config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s [%(filename)s:%(funcName)s]')
log = logging.getLogger(__name__)

# Assets Configuration
# ASSETS = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'assets')
# assert os.path.isdir(ASSETS)

@pytest.fixture()
def test_vm():
    vm = VirtualMachine()
    assert vm.data_pointer == 0
    return vm


class TestVm:

    def test_simple_vm(self):
        n = 20
        vm = VirtualMachine(memory_size=n)
        assert isinstance(vm, VirtualMachine)
        assert len(vm.memory) == n
        assert vm.data_pointer == 0

    def test_data_inc(self, test_vm: VirtualMachine):
        e = 1
        test_vm.inc_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == e

        test_vm.inc_data_value()
        test_vm.inc_data_value()
        test_vm.inc_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 4

        # Make sure things roll over
        test_vm.data_pointer = 1
        for _ in range(255):
            test_vm.inc_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 255
        test_vm.inc_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 0
        test_vm.inc_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 1

    def test_data_dec(self, test_vm: VirtualMachine):
        e = 255
        test_vm.dec_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == e

        test_vm.dec_data_value()
        test_vm.dec_data_value()
        test_vm.dec_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 252

        # Make sure things roll over
        test_vm.data_pointer = 1
        for _ in range(255):
            test_vm.dec_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 1
        test_vm.dec_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 0
        test_vm.dec_data_value()
        r = test_vm.memory.get(test_vm.data_pointer)
        assert r == 255

    def test_ptr_inc(self, test_vm: VirtualMachine):
        e = 1
        current_v = test_vm.data_pointer
        test_vm.inc_data_ptr()
        assert test_vm.data_pointer == e
        assert test_vm.data_pointer != current_v
        assert test_vm.data_pointer > current_v
        test_vm.inc_data_ptr()
        assert test_vm.data_pointer == e + 1
        test_vm.data_pointer = 0
        for i in range(test_vm._memory_size - 1):
            test_vm.inc_data_ptr()
        assert test_vm.data_pointer in test_vm.memory
        assert test_vm.data_pointer+1 not in test_vm.memory

        with pytest.raises(VMError) as cm:
            test_vm.inc_data_ptr()
        assert 'Invalid memory address' in str(cm.value)

    def test_ptr_dec(self, test_vm: VirtualMachine):
        with pytest.raises(VMError) as cm:
            test_vm.dec_data_ptr()
        assert 'Invalid memory address' in str(cm.value)

        test_vm.data_pointer = test_vm._memory_size - 1
        current_v = test_vm.data_pointer
        test_vm.dec_data_ptr()
        assert test_vm.data_pointer == (test_vm._memory_size - 2)
        assert test_vm.data_pointer != current_v
        assert test_vm.data_pointer < current_v

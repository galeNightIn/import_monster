import types

import numpy
import math
import pytest

from src.import_monster import methods_importer
from tests.modules_test import test1

def callable_test():
    assert isinstance(test1, types.ModuleType)
    isok = methods_importer(
        method_name='callable_method',
        modules_test=[test1])
    assert isok == [test1.test_callable]

def non_callable_test_const():
    assert isinstance(test1, types.ModuleType)
    isok = methods_importer(method_name='const', modules=[test1])
    assert isok == []

def non_callable_test_method():
    assert isinstance(test1, types.ModuleType)
    isok = methods_importer(method_name='non_collable_method', modules=[test1])
    assert isok == []

def incorrect_type():
    with pytest.raises(TypeError):
        methods_importer(method_name='callable_test', modules=[test1])

def str_module_test():
    isok = methods_importer(method_name='sum', modules=['numpy'])
    assert isok == [numpy.sum]

def two_modules_collable_test():
    isok = methods_importer(method_name='sin', modules=['numpy', 'math'])
    assert isok == [numpy.sin, math.sin]

def two_modules_non_collable_test():
    isok = methods_importer(method_name='pi', modules=['numpy', 'math'])
    assert isok == []

def test_methods_importer_other_module():
    isok = methods_importer(method_name='my_sum', modules=[test1, 'other'])
    assert isok == [test1.my_sum]
import types
import numpy
import math
import pytest

from src.import_monster import methods_importer
from tests.test_modules import test_1

def test_callable():
    assert isinstance(test_1, types.ModuleType)
    isok = methods_importer(
        method_name='callable_method',
        modules_test=(test_1, 
    assert isok == [(test_1, .callable_method]

def test_non_callable_const():
    assert isinstance(test_1, types.ModuleType)
    isok = methods_importer(method_name='const', modules=[test1])
    assert isok == []

def test_non_callable_method():
    assert isinstance(test_1, types.ModuleType)
    isok = methods_importer(method_name='non_collable_method', modules=[test1])
    assert isok == []

def test_incorrect_type():
    with pytest.raises(TypeError):
        methods_importer(method_name='callable_test', modules=[test1])

def test_str_modul():
    isok = methods_importer(method_name='sum', modules=['numpy'])
    assert isok == [numpy.sum]

def test_two_modules_collable():
    isok = methods_importer(method_name='sin', modules=['numpy', 'math'])
    assert isok == [numpy.sin, math.sin]

def two_modules_non_collable_test():
    isok = methods_importer(method_name='pi', modules=['numpy', 'math'])
    assert isok == []

def test_methods_importer_other_module():
    isok = methods_importer(method_name='my_sum', modules=[test1, 'other'])
    assert isok == [test1.my_sum]
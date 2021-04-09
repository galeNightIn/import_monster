import types

import numpy as np
import pandas as pd
import pytest

from src.import_monster import methods_importer

def callable_test():
    assert isinstance(test1, types.ModuleType)
    result = methods_importer(
        method_name='callable_method',
        modules_test=[test1])
    assert result == [module_1.test_callable]

def non_callable_test_const():
    assert isinstance(test1, types.ModuleType)
    result = methods_importer(
        method_name='const',
        modules=[test1])
    assert result == []

def non_callable_test_method():
    assert isinstance(test1, types.ModuleType)
    result = methods_importer(
        method_name='non_collable_method',
        modules=[test1])
    assert result == []

def incorrect_type():
    with pytest.raises(TypeError):
        methods_importer(
            method_name='callable_method',
            modules=[test2])


def string_module_test():
    result = methods_importer(
        method_name='sum',
        modules=['numpy'])
    assert result == [np.sum]

def two_modules_collable_test():
    result = methods_importer(
        method_name='sin',
        modules=['numpy', 'math'])
    assert result == [numpy.sin, math.sin]

def two_modules_non_collable_test():
    result = methods_importer(
        method_name='pi',
        modules=['numpy', 'math'])
    assert result == []

def test_methods_importer_nonexistant_module():
    result = methods_importer(
        method_name='array',
        modules=[module_1, 'nonexistant']
    )

    assert result == [module_1.array]
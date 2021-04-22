# -*- coding: utf-8 -*-
import math
import types

import numpy
import pytest
from import_monster.src.import_monster import methods_importer

from tests.test_modules import test_1


def test_callable_method():
    assert isinstance(test_1, types.ModuleType)
    isok = methods_importer(method_name="test_callable", modules=[test_1])
    assert isok == [test_1.test_callable_method]


def test_const():
    assert isinstance(test_1, types.ModuleType)
    isok = methods_importer(method_name="const", modules=[test_1])
    assert isok == []


def test_non_callable_method():
    assert isinstance(test_1, types.ModuleType)
    isok = methods_importer(method_name="test_non_callable", modules=[test_1])
    assert isok == []


def test_incorrect_type():
    with pytest.raises(TypeError):
        methods_importer(method_name="test_callable", modules=[test_1])


def test_str_module():
    isok = methods_importer(method_name="mean", modules=["numpy"])
    assert isok == [numpy.mean]


def test_two_modules_collable():
    isok = methods_importer(method_name="sin", modules=["numpy", "math"])
    assert isok == [numpy.sin, math.sin]


def test_two_more_modules_collable():
    isok = methods_importer(method_name="mean", modules=["numpy", test_1])
    assert isok == [numpy.mean, test_1.mean]


def two_modules_non_collable_test():
    isok = methods_importer(method_name="pi", modules=["numpy", "math"])
    assert isok == []


def test_methods_importer_other_module():
    isok = methods_importer(method_name="mean", modules=[test_1, "other"])
    assert isok == [test_1.mean]

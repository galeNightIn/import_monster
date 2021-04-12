# -*- coding: utf-8 -*-
"""Const is non callable, this tests intends showing that."""
const = 1


def test_callable_method():
    """
    Call callable method.
    Test_callable_method is callable,
    this tests intends showing that.
    """
    return


@property
def test_non_collable_method():
    """Decorator makes it non callable,
    that can be a good check.
    """
    return


def mean(x=1, y=1):
    """Callable function, available in numpy."""
    return (x + y) / 2

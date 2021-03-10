#!/usr/bin/env python3
import pytest
import inspect
import types
import typing
from codoc.service.parsing.utils import is_an_instance


def test_is_an_instance__positive(instance):
    assert is_an_instance(instance)


def test_is_an_instance__negative(non_instance):
    assert not is_an_instance(non_instance)


class TestClass:
    ...


def test_function():
    ...


@pytest.fixture(
    params=[
        inspect.getdoc,
        typing.Optional,
        types.ModuleType,
        inspect,
        pytest,
        TestClass,
        test_function,
    ]
)
def non_instance(request):
    return request.param


@pytest.fixture(params=["", TestClass(), 2])
def instance(request):
    return request.param

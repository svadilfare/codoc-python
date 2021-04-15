#!/usr/bin/env python3
import pytest
import logging

from codoc.service.parsing.node import get_identifier_of_object
from codoc.service.parsing.dependency import (
    get_dependency_edges,
    get_dependency_nodes_with_parents,
    get_dependency_nodes,
    DependencyNotFound,
)


def test_get_dependency_edges_match_snapshot(examples, assert_match_snap, kwargs):
    assert_match_snap(get_dependency_edges(**kwargs))


def test_get_dependency_nodes_with_parents_match_snapshot(
    examples, assert_match_snap, kwargs
):
    assert_match_snap(get_dependency_nodes_with_parents(**kwargs))


def test_get_dependency_nodes_match_snapshot(examples, assert_match_snap, kwargs):
    assert_match_snap(get_dependency_nodes(**kwargs))


def test_get_dependencies_raises_error_in_strictmode():
    with pytest.raises(DependencyNotFound):
        get_dependency_nodes(function_that_fails_under_strict_mode)


def test_get_dependencies_shows_warning_in_strictmode(caplog):
    caplog.set_level(logging.WARNING)
    get_dependency_nodes(function_that_fails_under_strict_mode, strict_mode=False)
    assert "UndefinedThing" in caplog.text


@pytest.fixture(
    params=(False, True), ids=["Without external nodes", "With external nodes"]
)
def kwargs(request, obj, create_node):
    return {
        "obj": obj,
        "include_external_dependencies": request.param,
        "create_node": lambda obj: create_node(
            identifier=get_identifier_of_object(obj)
        ),
    }


@pytest.fixture(params=(1, 2, 3), ids=["Class", "Function", "Module"])
def obj(request, examples):
    if request.param == 1:
        return examples.Animal
    if request.param == 2:
        return examples.random_function
    if request.param == 3:
        return examples


def function_that_fails_under_strict_mode():
    # This will fail in strict mode as it cannot find `UndefinedThing`
    return pytest.UndefinedThing()

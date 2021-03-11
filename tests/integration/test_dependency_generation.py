#!/usr/bin/env python3
import pytest

from codoc.service.parsing.node import get_identifier_of_object
from codoc.service.parsing.dependency import (
    get_dependency_edges,
    get_dependency_nodes_with_parents,
    get_dependency_nodes,
)


def test_get_dependency_edges_match_snapshot(examples, assert_match_snap, kwargs):
    assert_match_snap(get_dependency_edges(**kwargs))


def test_get_dependency_nodes_with_parents_match_snapshot(
    examples, assert_match_snap, kwargs
):
    assert_match_snap(get_dependency_nodes_with_parents(**kwargs))


def test_get_dependency_nodes_match_snapshot(examples, assert_match_snap, kwargs):
    assert_match_snap(get_dependency_nodes(**kwargs))


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

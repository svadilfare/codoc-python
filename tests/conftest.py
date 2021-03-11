#!/usr/bin/env python3
import pytest
from codoc.domain.model import Graph, Node, Dependency, NodeType
import examples as exampleModule


@pytest.fixture
def create_graph():
    def _func(**kwargs):
        kwargs.setdefault("nodes", [])
        kwargs.setdefault("edges", [])

        return Graph(**kwargs)

    return _func


@pytest.fixture
def create_edge():
    def _func(from_node: Node, to_node: Node):
        return Dependency(from_node=from_node.identifier, to_node=to_node.identifier)

    return _func


@pytest.fixture
def assert_match_snap(snapshot):
    def _to_snap(obj: object):
        if isinstance(obj, Node):
            return obj.identifier
        if isinstance(obj, Dependency):
            return (obj.from_node, obj.to_node)
        if isinstance(obj, (list, set, frozenset)):
            return list(sorted(_to_snap(elm) for elm in obj))
        if isinstance(obj, Graph):
            return (_to_snap(obj.nodes), _to_snap(obj.edges))

        return obj

    return lambda obj: snapshot.assert_match(_to_snap(obj))


@pytest.fixture
def create_node():
    def _func(**kwargs):
        kwargs.setdefault("name", "test")
        kwargs.setdefault("description", "test")
        kwargs.setdefault("path", None)
        kwargs.setdefault("args", None)
        kwargs.setdefault("lines", None)
        kwargs.setdefault("of_type", NodeType.CLASS)
        kwargs.setdefault("parent_identifier", None)
        return Node(**kwargs)

    return _func


@pytest.fixture
def examples():
    return exampleModule

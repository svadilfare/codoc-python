#!/usr/bin/env python3
import pytest

from codoc.domain.model import Graph, Node, NodeType


@pytest.fixture
def graph_with_children(child_node, parent_node):
    return create_graph(nodes=[child_node, parent_node])


@pytest.fixture
def graph_without_children(parent_node):
    return create_graph(nodes=[parent_node], edges=[])


@pytest.fixture
def child_node(parent_identifier):
    return create_node(identifier="ABCD", parent_identifier=parent_identifier)


@pytest.fixture
def parent_node(parent_identifier):
    return create_node(identifier=parent_identifier)


@pytest.fixture
def parent_identifier():
    return "ABCD"


def create_graph(**kwargs):
    kwargs.setdefault("nodes", [])
    kwargs.setdefault("edges", [])

    return Graph(**kwargs)


def create_node(**kwargs):
    kwargs.setdefault("name", "test")
    kwargs.setdefault("description", "test")
    kwargs.setdefault("path", None)
    kwargs.setdefault("args", None)
    kwargs.setdefault("lines", None)
    kwargs.setdefault("of_type", NodeType.CLASS)
    kwargs.setdefault("parent_identifier", None)
    return Node(**kwargs)

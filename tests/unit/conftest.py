#!/usr/bin/env python3
import pytest


@pytest.fixture
def graph_with_children(create_graph, child_node, parent_node):
    return create_graph(nodes=[child_node, parent_node])


@pytest.fixture
def graph_without_children(create_graph, parent_node):
    return create_graph(nodes=[parent_node], edges=[])


@pytest.fixture
def child_node(create_node, parent_identifier):
    return create_node(identifier="ABCD", parent_identifier=parent_identifier)


@pytest.fixture
def parent_node(create_node, parent_identifier):
    return create_node(identifier=parent_identifier)


@pytest.fixture
def parent_identifier():
    return "ABCD"

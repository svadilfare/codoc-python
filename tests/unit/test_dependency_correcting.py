#!/usr/bin/env python3


import pytest
from codoc.domain.model import Graph, Dependency
from codoc.service.dependency_correcting import (
    create_bubbled_dependencies,
    remove_non_connected_edges,
)


class TestBubbleDependencies:
    def test_returns_graph(self, new_graph):
        assert type(new_graph) is Graph

    def test_has_all_edges(self, has_edge_between, node_a, node_b, node_a_a, node_b_a):
        assert (
            has_edge_between(node_a, node_b)
            and has_edge_between(node_a, node_b_a)
            and has_edge_between(node_a_a, node_b)
        )

    def test_doesnt_go_downwards(self, has_edge_between, node_a_a_a, node_b_a):

        assert not (has_edge_between(node_a_a_a, node_b_a))

    @pytest.fixture()
    def has_edge_between(self, new_graph):
        def fun(node1, node2):
            return any(
                edge.from_node == node1.identifier and edge.to_node == node2.identifier
                for edge in new_graph.edges
            )

        return fun

    @pytest.fixture()
    def new_graph(self, graph):
        return create_bubbled_dependencies(graph)

    @pytest.fixture()
    def graph(
        self, create_graph, create_edge, node_a, node_a_a, node_a_a_a, node_b, node_b_a
    ):
        return create_graph(
            nodes={
                node_a,
                node_a_a,
                node_a_a_a,
                node_b,
                node_b_a,
            },
            edges={create_edge(node_a_a, node_b_a)},
        )

    @pytest.fixture()
    def node_b_a(self, create_node, node_b):
        return create_node(parent=node_b, identifier="b_a")

    @pytest.fixture()
    def node_b(self, create_node):
        return create_node(identifier="b")

    @pytest.fixture()
    def node_a_a_a(self, create_node, node_a):
        return create_node(parent=node_a, identifier="a_a_a")

    @pytest.fixture()
    def node_a_a(self, create_node, node_a):
        return create_node(parent=node_a, identifier="a_a")

    @pytest.fixture()
    def node_a(self, create_node):
        return create_node(identifier="a")


class TestRemoveNonConnectedEdges:
    def test_removes_non_connected_edges(self, create_edge, create_graph):

        graph = create_graph(edges={Dependency(from_node="A", to_node="B")})

        assert remove_non_connected_edges(graph).edges == set()

    def test_removes_partly_connected_edges(
        self, create_edge, create_graph, create_node
    ):

        node = create_node(identifier="A")
        graph = create_graph(
            nodes={node}, edges={Dependency(from_node=node.identifier, to_node="B")}
        )

        assert remove_non_connected_edges(graph).edges == set()

    def test_doesnt_remove_connected_edges(
        self, create_edge, create_graph, create_node
    ):

        node = create_node(identifier="A")
        graph = create_graph(
            nodes={node}, edges={Dependency(from_node=node.identifier, to_node="B")}
        )

        assert remove_non_connected_edges(graph).edges == set()

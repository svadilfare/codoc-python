#!/usr/bin/env python3

from codoc.service.graph import create_graph_of_module


def test_happy_path_create_graph(examples, snapshot):
    graph = create_graph_of_module(examples)

    snapshot.assert_match((graph.nodes, graph.edges))

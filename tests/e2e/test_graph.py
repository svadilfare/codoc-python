#!/usr/bin/env python3

from codoc.service.graph import create_graph_of_module


def test_happy_path_create_graph(
    examples,
    assert_match_snap,
):
    graph = create_graph_of_module(examples, include_external_dependencies=False)

    assert_match_snap(graph)

#!/usr/bin/env python3

import codoc.domain
from codoc.service import create_graph_of_module


def test_happy_path_dogfood_creates_graph(snapshot):
    graph = create_graph_of_module(codoc.domain)

    snapshot.assert_match((graph.nodes, graph.edges))

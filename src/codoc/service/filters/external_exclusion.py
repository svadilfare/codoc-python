#!/usr/bin/env python3

from codoc.domain.model import Graph

from .helpers import get_edges_where_both_ends_are_in_nodes


# TODO this fails if you do an OR on two graphs.
def exclude_external(graph: Graph) -> Graph:
    nodes = {node for node in graph.nodes if not node.external}
    edges = get_edges_where_both_ends_are_in_nodes(graph.edges, nodes)

    return Graph(nodes=nodes, edges=edges)

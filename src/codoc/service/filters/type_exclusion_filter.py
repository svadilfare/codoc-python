#!/usr/bin/env python3
"""
Filters that excludes a given node based on the type it is.
It will also remove all dependencies (edges) that reach a node that should be excluded


i.e exclude_modules will return a new graph with all module nodes have been removed.
"""
from codoc.domain.model import Graph, Node, NodeType, Dependency
from codoc.domain.helpers import get_node
from .helpers import node_without_parent


def include_only_modules(graph: Graph) -> Graph:
    """
    Returns a graph that only has modules
    """
    return TypeBasedFilter(NodeType.MODULE, exclusive=False).exclude(graph)


def include_only_functions(graph: Graph) -> Graph:
    """
    Returns a graph that only has functions
    """
    return TypeBasedFilter(NodeType.FUNCTION, exclusive=False).exclude(graph)


def include_only_classes(graph: Graph) -> Graph:
    """
    Returns a graph that only has classes
    """
    return TypeBasedFilter(NodeType.CLASS, exclusive=False).exclude(graph)


def include_only_exceptions(graph: Graph) -> Graph:
    """
    Returns a graph that only has exceptions
    """
    return TypeBasedFilter(NodeType.EXCEPTION, exclusive=False).exclude(graph)


def exclude_modules(graph: Graph) -> Graph:
    """
    Returns a graph that doesn't have any modules
    """
    return TypeBasedFilter(NodeType.MODULE).exclude(graph)


def exclude_functions(graph: Graph) -> Graph:
    """
    Returns a graph that doesn't have any functions
    """
    return TypeBasedFilter(NodeType.FUNCTION).exclude(graph)


def exclude_classes(graph: Graph) -> Graph:
    """
    Returns a graph that doesn't have any classes
    """
    return TypeBasedFilter(NodeType.CLASS).exclude(graph)


def exclude_exceptions(graph: Graph) -> Graph:
    """
    Returns a graph that doesn't have any exceptions
    """
    return TypeBasedFilter(NodeType.EXCEPTION).exclude(graph)


class TypeBasedFilter:
    """
    Filte
    """

    # TODO make this inclusive too

    def __init__(self, based_on_type: NodeType, exclusive: bool = True):
        self._type = based_on_type
        self._exclusive = exclusive

    def exclude(self, graph: Graph) -> Graph:
        return Graph(
            edges=set(edge for edge in graph.edges if self.edge_permitted(edge, graph)),
            nodes=set(
                self.node_without_parent_of_type(node, graph)
                for node in graph.nodes
                if self.permitted(node)
            ),
        )

    def edge_permitted(self, edge: Dependency, graph: Graph) -> bool:
        return self.identifier_is_permitted(
            edge.to_node, graph
        ) and self.identifier_is_permitted(edge.from_node, graph)

    def node_without_parent_of_type(self, node: Node, graph) -> Node:
        if node.parent_identifier and self.identifier_is_permitted(
            node.parent_identifier, graph
        ):
            return node_without_parent(node)
        return node

    def identifier_is_permitted(self, identifier: str, graph) -> bool:
        return self.permitted(get_node(identifier, graph))

    def permitted(self, node: Node) -> bool:
        return (node.of_type is self._type) ^ self._exclusive

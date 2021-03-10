#!/usr/bin/env python3
from typing import Callable
from codoc.domain.model import Graph, Node, NodeType, Dependency
from codoc.domain.helpers import get_node
from .helpers import node_without_parent

FilterType = Callable[[Graph], Graph]


def exclude_modules(graph: Graph) -> FilterType:
    return TypeExclusionFilter(NodeType.MODULE).exclude(graph)


def exclude_functions(graph: Graph) -> FilterType:
    return TypeExclusionFilter(NodeType.FUNCTION).exclude(graph)


def exclude_classes(graph: Graph) -> FilterType:
    return TypeExclusionFilter(NodeType.CLASS).exclude(graph)


class TypeExclusionFilter:
    def __init__(self, exclude_type: NodeType):
        self._excluded_type = exclude_type

    def exclude(self, graph: Graph) -> Graph:
        return Graph(
            edges=set(
                edge
                for edge in graph.edges
                if not self.edge_is_attached_to_type(edge, graph)
            ),
            nodes=set(
                self.node_without_parent_of_type(node, graph)
                for node in graph.nodes
                if not self.is_type(node)
            ),
        )

    def edge_is_attached_to_type(self, edge: Dependency, graph: Graph) -> bool:
        return self.identifier_is_type(edge.to_node, graph) or self.identifier_is_type(
            edge.from_node, graph
        )

    def node_without_parent_of_type(self, node: Node, graph) -> Node:
        if node.parent_identifier and self.identifier_is_type(
            node.parent_identifier, graph
        ):
            return node_without_parent(node)
        return node

    def identifier_is_type(self, identifier: str, graph) -> bool:
        return self.is_type(get_node(identifier, graph))

    def is_type(self, node: Node) -> bool:
        return node.of_type is self._excluded_type
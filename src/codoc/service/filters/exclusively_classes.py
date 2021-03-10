#!/usr/bin/env python3
from codoc.domain.model import Graph, Node, NodeType, Dependency
from codoc.domain.helpers import get_node
from .helpers import node_without_parent


def include_only_classes(graph: Graph) -> Graph:
    return Graph(
        edges=set(
            edge
            for edge in graph.edges
            if edge_is_attached_only_to_classes(edge, graph)
        ),
        nodes=set(
            node_with_non_class_parent(node, graph)
            for node in graph.nodes
            if is_class(node)
        ),
    )


def node_with_non_class_parent(node: Node, graph) -> Node:
    if node.parent_identifier and not identifier_is_class(
        node.parent_identifier, graph
    ):
        return node_without_parent(node)
    return node


def edge_is_attached_only_to_classes(edge: Dependency, graph: Graph) -> bool:
    return identifier_is_class(edge.to_node, graph) and identifier_is_class(
        edge.from_node, graph
    )


def identifier_is_class(identifier: str, graph) -> bool:
    return is_class(get_node(identifier, graph))


def is_class(node: Node) -> bool:
    return node.of_type is NodeType.CLASS

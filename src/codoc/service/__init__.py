import types
from codoc.domain.model import Graph, Dependency, Node

from .parsing.node import create_node_from_object, get_identifier_of_object
from .parsing.dependency import (
    get_dependency_edges,
    get_dependency_nodes_with_parents,
    get_dependency_nodes,
)

from .object_unpacker import recursively_get_all_subobjects_in_object


def create_graph_of_module(module: types.ModuleType) -> Graph:
    all_objects = frozenset(recursively_get_all_subobjects_in_object(module))
    nodes = set(
        node
        for obj in all_objects
        for node in {create_node_from_object(obj)}
        | get_dependency_nodes_with_parents(obj)
    )
    edges = set(
        Dependency(
            # TODO use `get_identifier_from_object` instead
            from_node=get_identifier_of_object(obj),
            to_node=dependency.identifier,
        )
        for obj in all_objects
        for dependency in get_dependency_nodes(obj)
    )
    return Graph(nodes=nodes, edges=edges)

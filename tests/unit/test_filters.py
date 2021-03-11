#!/usr/bin/env python3
import pytest

from codoc.service import filters
from codoc.domain.model import NodeType
from codoc.domain.helpers import contains_node, contains_dependency_between


@pytest.mark.parametrize(
    "filter_function",
    [
        filters.include_only_classes,
        filters.exclude_classes,
        filters.exclude_functions,
        filters.exclude_modules,
    ],
)
def test_matches_snapshot(filter_function, test_graph, snapshot):
    filtered_graph = filter_function(test_graph)
    snapshot.assert_match((filtered_graph.nodes, filtered_graph.edges))


class TestFilterOnlyClasses:
    def test_keeps_class_to_class_edges(self, filtered_graph, node_class, node_class_b):
        assert contains_dependency_between(
            node_class.identifier, node_class_b.identifier, filtered_graph
        )

    def test_removes_non_class_to_class_edges(
        self, filtered_graph, node_class, node_function, node_module
    ):
        assert not contains_dependency_between(
            node_class.identifier, node_function.identifier, filtered_graph
        ) and not contains_dependency_between(
            node_module.identifier, node_function.identifier, filtered_graph
        )

    def test_keeps_class_nodes(self, filtered_graph, any_node_class):
        assert contains_node(any_node_class.identifier, filtered_graph)

    def test_removes_non_class_nodes(self, filtered_graph, any_non_node_class):
        assert not contains_node(any_non_node_class.identifier, filtered_graph)

    @pytest.fixture
    def filtered_graph(self, test_graph):
        return filters.include_only_classes(test_graph)


@pytest.fixture(params=[0, 1])
def any_node_class(request, node_class, node_class_b):
    return [node_class, node_class_b][request.param]


@pytest.fixture(params=[0, 1])
def any_non_node_class(
    request,
    node_function,
    node_module,
):
    return [node_function, node_module][request.param]


@pytest.fixture
def test_graph(
    create_graph,
    node_class,
    node_class_b,
    node_function,
    node_function_b,
    node_module,
    node_module_b,
    create_edge,
):
    return create_graph(
        nodes=[
            node_class,
            node_class_b,
            node_function,
            node_module,
            node_function_b,
            node_module_b,
        ],
        edges=[
            create_edge(node_class, node_class_b),
            create_edge(node_class_b, node_class),
            create_edge(node_class, node_function),
            create_edge(node_class, node_module),
            create_edge(node_module, node_function),
            create_edge(node_function, node_module),
            create_edge(node_function, node_function_b),
            create_edge(node_module, node_module_b),
        ],
    )


@pytest.fixture
def node_class(create_node):
    return create_node(identifier="ClassA", of_type=NodeType.CLASS)


@pytest.fixture
def node_class_b(create_node, node_module_b):
    return create_node(
        identifier="ClassB",
        parent_identifier=node_module_b.identifier,
        of_type=NodeType.CLASS,
    )


@pytest.fixture
def node_function(create_node, node_class):
    return create_node(
        identifier="FuncA",
        parent_identifier=node_class.identifier,
        of_type=NodeType.FUNCTION,
    )


@pytest.fixture
def node_function_b(create_node):
    return create_node(identifier="FuncB", of_type=NodeType.FUNCTION)


@pytest.fixture
def node_module(create_node):
    return create_node(identifier="ModuleA", of_type=NodeType.MODULE)


@pytest.fixture
def node_module_b(create_node, node_module):
    return create_node(
        identifier="ModuleB",
        parent_identifier=node_module.identifier,
        of_type=NodeType.MODULE,
    )

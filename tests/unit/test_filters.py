#!/usr/bin/env python3
import pytest

from codoc.service import filters
from codoc.domain.model import NodeType
from codoc.domain.helpers import contains_node, contains_dependency_between


@pytest.mark.parametrize(
    "filter_function",
    [
        filters.class_diagram_filter,
        filters.exclude_classes,
        filters.exclude_functions,
        filters.exclude_modules,
    ],
)
def test_matches_snapshot(filter_function, test_graph, assert_match_snap):
    filtered_graph = filter_function(test_graph)
    assert_match_snap(filtered_graph)


class TestGetChildrenOfFilter:
    def test_matches_snapshot(self, assert_match_snap, filtered_graph):
        assert_match_snap(filtered_graph)

    def test_includes_filtered_elm(self, filtered_graph, obj_to_filter):
        assert obj_to_filter in filtered_graph.nodes

    class TestExcludeExternalParent:
        def test_removes_parent(self, parent, filtered_graph):
            assert parent not in filtered_graph.nodes

        def test_keeps_child(self, child, filtered_graph):
            assert child in filtered_graph.nodes

        def test_removes_childs_parent_attribute(self, filtered_graph):
            # there should only be the one node
            assert len(filtered_graph.nodes) == 1
            child = list(filtered_graph.nodes)[0]
            assert child.parent_identifier is None

        @pytest.fixture()
        def filtered_graph(self, parent, child, graph):
            return filters.get_children_of(child.identifier)(graph)

        @pytest.fixture()
        def graph(self, create_graph, child, parent):
            return create_graph(nodes=[child, parent])

        @pytest.fixture()
        def child(self, create_node, parent):
            return create_node(parent=parent, identifier="child")

        @pytest.fixture()
        def parent(self, create_node):
            return create_node(identifier="parent")

    @pytest.fixture(
        params=[False, True], ids=["Exclude dependencies", "Include dependencies"]
    )
    def filtered_graph(self, request, test_graph, obj_to_filter):
        return filters.get_children_of(
            obj_to_filter.identifier, keep_external_nodes=request.param
        )(test_graph)

    @pytest.fixture()
    def obj_to_filter(self, node_module_b):
        return node_module_b


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
        return filters.class_diagram_filter(test_graph)


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
            create_edge(node_class_b, node_function),
            create_edge(node_function, node_class_b),
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
def node_function(create_node, node_class_b):
    return create_node(
        identifier="FuncA",
        parent_identifier=node_class_b.identifier,
        of_type=NodeType.FUNCTION,
    )


@pytest.fixture
def node_function_b(create_node, node_module_b):
    return create_node(
        identifier="FuncB",
        of_type=NodeType.FUNCTION,
    )


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

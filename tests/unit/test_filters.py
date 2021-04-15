#!/usr/bin/env python3
import pytest

from codoc.service import filters
from codoc.service.filters import depth_based
from codoc.domain.model import NodeType, Graph
from codoc.domain.helpers import contains_node, contains_dependency_between


@pytest.mark.parametrize(
    "filter_function",
    [
        filters.class_diagram_filter,
        filters.exclude_classes,
        filters.exclude_functions,
        filters.exclude_modules,
        filters.exclude_exceptions,
        filters.include_only_modules,
        filters.include_only_functions,
        filters.include_only_classes,
        filters.include_only_exceptions,
    ],
)
def test_matches_snapshot(filter_function, test_graph, assert_match_snap):
    filtered_graph = filter_function(test_graph)
    assert_match_snap(filtered_graph)


class TestExcludeExternals:
    def test_remove_external(self, create_graph, create_node):
        node = create_node(external=True)
        graph = create_graph(nodes={node})
        assert filters.exclude_external(graph).nodes == set()

    def test_keep_internals(self, create_graph, create_node):
        node = create_node(external=False)
        graph = create_graph(nodes={node})
        assert filters.exclude_external(graph).nodes == {node}

    def test_only_keeps_internal_dependency(
        self, create_graph, create_node, create_edge
    ):
        node_a = create_node(identifier="a", external=True)
        node_b = create_node(identifier="b", external=False)
        node_c = create_node(identifier="c", external=False)
        edge_ab = create_edge(node_a, node_b)
        edge_bc = create_edge(node_b, node_c)
        graph = create_graph(nodes={node_a, node_b, node_c}, edges={edge_ab, edge_bc})
        assert filters.exclude_external(graph).edges == {edge_bc}


class TestDepthBasedFilter:
    def test_returns_filter(self, graph):
        assert type(filters.get_depth_based_filter(1)(graph)) is Graph

    def test_depth_zero_is_empty(self, graph, parent):
        filtered_graph = filters.get_depth_based_filter(0)(graph)
        assert len(filtered_graph.nodes) == 0 and len(filtered_graph.edges) == 0

    def test_depth_one_only_has_root(self, graph, parent):
        assert filters.get_depth_based_filter(1)(graph).nodes == {parent}

    class TestGetDepthOfNode:
        def test_depth_of_parent(self, parent, get_depth_of):
            assert get_depth_of(parent) == 1

        def test_depth_of_child(self, child, get_depth_of):
            assert get_depth_of(child) == 2

        def test_depth_of_child_2(self, child_2, get_depth_of):
            assert get_depth_of(child_2) == 2

        @pytest.fixture()
        def get_depth_of(self, graph):
            return lambda node: depth_based.get_depth_of_node(node, graph)

    def test_depth_zero_has_no_edges(self, graph, parent):
        assert len(filters.get_depth_based_filter(0)(graph).edges) == 0

    def test_keep_only_relevant_edges(self, create_graph, create_edge, create_node):
        nodeA = create_node(identifier="A")
        nodeB = create_node(identifier="B")
        nodeC = create_node(identifier="C", parent=nodeB)
        edge1 = create_edge(nodeA, nodeB)
        edge2 = create_edge(nodeA, nodeC)
        graph = create_graph(nodes={nodeA, nodeB, nodeC}, edges={edge1, edge2})
        assert filters.get_depth_based_filter(1)(graph).edges == {edge1}

    @pytest.fixture()
    def graph(self, create_graph, child, child_2, parent):
        return create_graph(nodes={child_2, child, parent})

    @pytest.fixture()
    def child_2(self, create_node, parent):
        return create_node(parent=parent, identifier="child")

    @pytest.fixture()
    def child(self, create_node, parent):
        return create_node(parent=parent, identifier="child")

    @pytest.fixture()
    def parent(self, create_node):
        return create_node(identifier="parent")


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
            return create_graph(nodes={child, parent})

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
    node_exception,
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
            node_exception,
        ],
        edges=[
            create_edge(node_class, node_class_b),
            create_edge(node_class_b, node_class),
            create_edge(node_class, node_function),
            create_edge(node_class, node_exception),
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
def node_exception(create_node, node_module):
    return create_node(
        identifier="Exception",
        parent_identifier=node_module.identifier,
        of_type=NodeType.EXCEPTION,
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

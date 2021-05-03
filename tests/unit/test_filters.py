#!/usr/bin/env python3
import pytest
from codoc.domain.helpers import contains_node
from codoc.domain.model import Graph, NodeType
from codoc.service import filters
from codoc.service.filters import depth_based


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


class TestExcludeRegexFilter:
    def test_remove_match(self, create_graph, create_node):
        node = create_node(name="test")
        graph = create_graph(nodes={node})
        assert filters.exclude_by_regex("abc")(graph).nodes == {node}

    def test_remove_non_match(self, create_graph, create_node):
        node = create_node(name="abc")
        graph = create_graph(nodes={node})
        assert filters.exclude_by_regex("abc")(graph).nodes == set()


class TestRegexFilter:
    def test_remove_not_match(self, create_graph, create_node):
        node = create_node(name="test")
        graph = create_graph(nodes={node})
        assert filters.filter_by_regex("abc")(graph).nodes == set()

    def test_keep_match(self, create_graph, create_node):
        node = create_node(name="abc")
        graph = create_graph(nodes={node})
        assert filters.filter_by_regex("abc")(graph).nodes == {node}


class TestExcludeExternals:
    def test_remove_external(self, create_graph, create_node):
        node = create_node(external=True)
        graph = create_graph(nodes={node})
        assert filters.exclude_external(graph).nodes == set()

    def test_keep_internals(self, create_graph, create_node):
        node = create_node(external=False)
        graph = create_graph(nodes={node})
        assert filters.exclude_external(graph).nodes == {node}


class TestDepthBasedFilter:
    def test_returns_filter(self, graph):
        assert type(filters.get_depth_based_filter(1)(graph)) is Graph

    def test_depth_zero_is_empty(self, graph, parent):
        filtered_graph = filters.get_depth_based_filter(0)(graph)
        assert len(filtered_graph.nodes) == 0

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

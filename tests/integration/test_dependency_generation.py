#!/usr/bin/env python3
import pytest

from codoc.service.parsing.dependency import (
    get_dependency_edges,
    get_dependency_nodes_with_parents,
    get_dependency_nodes,
)


class TestGetDependencyEdges:
    def test_class_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_edges(examples.Animal))

    def test_function_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_edges(examples.random_function))

    def test_module_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_edges(examples))

    def test_dogfood_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_edges(get_dependency_edges))


class TestGetDependencyNodesAndParents:
    def test_class_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_nodes_with_parents(examples.Animal))

    def test_function_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(
            get_dependency_nodes_with_parents(examples.random_function)
        )

    def test_module_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_nodes_with_parents(examples))

    def test_dogfood_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(
            get_dependency_nodes_with_parents(get_dependency_nodes_with_parents)
        )


class TestGetDependencyNodes:
    def test_class_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_nodes(examples.Animal))

    def test_function_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_nodes(examples.random_function))

    def test_module_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_nodes(examples))

    def test_dogfood_match_snapshot(self, examples, snapshot):
        snapshot.assert_match(get_dependency_nodes(get_dependency_nodes))

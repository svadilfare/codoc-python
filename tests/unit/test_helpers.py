#!/usr/bin/env python3
from codoc.domain.helpers import has_children, get_children, set_parent


def test_has_children__positive(parent_identifier, graph_with_children):
    assert has_children(parent_identifier, graph_with_children) is True


def test_has_children__negative(parent_identifier, graph_without_children):
    assert has_children(parent_identifier, graph_without_children) is False


def test_get_children__not_empty(parent_identifier, child_node, graph_with_children):
    assert child_node in get_children(parent_identifier, graph_with_children)


def test_get_children__empty(parent_identifier, graph_without_children):
    assert len(get_children(parent_identifier, graph_without_children)) == 0


def test_set_parent__doesnt_change_instance(parent_identifier, child_node):
    set_parent(child_node, "asdasda")
    assert child_node.parent_identifier == parent_identifier


def test_set_parent(parent_identifier, child_node):
    new_id = "ASDASDA"
    new_node = set_parent(child_node, new_id)
    assert new_node.parent_identifier == new_id

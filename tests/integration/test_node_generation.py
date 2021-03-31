#!/usr/bin/env python3

from codoc.service.parsing.node import create_node_from_object


def test_class_match_snapshot(examples, snapshot):
    node = create_node_from_object(examples.Animal)
    snapshot.assert_match(node)


def test_function_match_snapshot(examples, snapshot):
    node = create_node_from_object(examples.random_function)
    snapshot.assert_match(node)


def test_exception_match_snapshot(examples, snapshot):
    node = create_node_from_object(examples.RandomError)
    snapshot.assert_match(node)


def test_module_match_snapshot(examples, snapshot):
    node = create_node_from_object(examples)
    snapshot.assert_match(node)


def test_dogfood_match_snapshot(examples, snapshot):
    node = create_node_from_object(create_node_from_object)
    snapshot.assert_match(node)

# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_class_match_snapshot 1"] = GenericRepr(
    "Node(identifier='Animal/NodeType.CLASS/examples', name='Animal', of_type=<NodeType.CLASS: 1>, path='tests/examples/__init__.py', args=('self', 'kind', 'name'), lines=None, external=True, description='Animal(kind: examples.AnimalType, name: str)', parent_identifier='examples/NodeType.MODULE/')"
)

snapshots["test_dogfood_match_snapshot 1"] = GenericRepr(
    "Node(identifier='create_node_from_object/NodeType.FUNCTION/codoc.service.parsing.node', name='create_node_from_object', of_type=<NodeType.FUNCTION: 2>, path='src/codoc/service/parsing/node.py', args=('obj', 'external'), lines=None, external=True, description='', parent_identifier='codoc.service.parsing.node/NodeType.MODULE/codoc.service.parsing')"
)

snapshots["test_exception_match_snapshot 1"] = GenericRepr(
    "Node(identifier='RandomError/NodeType.EXCEPTION/examples', name='RandomError', of_type=<NodeType.EXCEPTION: 4>, path='tests/examples/__init__.py', args=None, lines=None, external=True, description='Common base class for all non-exit exceptions.', parent_identifier='examples/NodeType.MODULE/')"
)

snapshots["test_function_match_snapshot 1"] = GenericRepr(
    "Node(identifier='random_function/NodeType.FUNCTION/examples', name='random_function', of_type=<NodeType.FUNCTION: 2>, path='tests/examples/__init__.py', args=(), lines=None, external=True, description='Will output something COMPLETLY random', parent_identifier='examples/NodeType.MODULE/')"
)

snapshots["test_module_match_snapshot 1"] = GenericRepr(
    "Node(identifier='examples/NodeType.MODULE/', name='examples', of_type=<NodeType.MODULE: 3>, path='tests/examples/__init__.py', args=None, lines=None, external=True, description='', parent_identifier=None)"
)

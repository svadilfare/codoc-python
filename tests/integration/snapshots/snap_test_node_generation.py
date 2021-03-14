# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_class_match_snapshot 1"] = GenericRepr(
    "Node(identifier='Animal/NodeType.CLASS/examples', name='Animal', description='Animal(kind: examples.AnimalType, name: str)', of_type=<NodeType.CLASS: 1>, parent_identifier='examples/NodeType.MODULE/', path=None, args=('self', 'kind', 'name'), lines=None)"
)

snapshots["test_dogfood_match_snapshot 1"] = GenericRepr(
    "Node(identifier='create_node_from_object/NodeType.FUNCTION/codoc.service.parsing.node', name='create_node_from_object', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.service.parsing.node/NodeType.MODULE/codoc.service.parsing', path=None, args=('obj',), lines=None)"
)

snapshots["test_function_match_snapshot 1"] = GenericRepr(
    "Node(identifier='random_function/NodeType.FUNCTION/examples', name='random_function', description='Will output something COMPLETLY random', of_type=<NodeType.FUNCTION: 2>, parent_identifier='examples/NodeType.MODULE/', path=None, args=(), lines=None)"
)

snapshots["test_module_match_snapshot 1"] = GenericRepr(
    "Node(identifier='examples/NodeType.MODULE/', name='examples', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
)

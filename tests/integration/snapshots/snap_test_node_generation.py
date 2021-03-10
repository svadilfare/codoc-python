# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_class_match_snapshot 1"] = GenericRepr(
    "Node(identifier='examples.AnimalNodeType.CLASS', name='Animal', description='Animal(kind: examples.AnimalType, name: str)', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('self', 'kind', 'name'), lines=(97, 106))"
)

snapshots["test_dogfood_match_snapshot 1"] = GenericRepr(
    "Node(identifier='codoc.service.parsing.node.create_node_from_objectNodeType.FUNCTION', name='create_node_from_object', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.service.parsing.codoc.service.parsing.nodeNodeType.MODULE', path=None, args=('obj',), lines=(14, 16))"
)

snapshots["test_function_match_snapshot 1"] = GenericRepr(
    "Node(identifier='examples.random_functionNodeType.FUNCTION', name='random_function', description='Will output something COMPLETLY random', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=(), lines=(55, 60))"
)

snapshots["test_module_match_snapshot 1"] = GenericRepr(
    "Node(identifier='None.examplesNodeType.MODULE', name='examples', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=(1, 106))"
)

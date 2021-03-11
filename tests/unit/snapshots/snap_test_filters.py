# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_matches_snapshot[exclude_classes] 1"] = (
    set(
        [
            GenericRepr(
                "Node(identifier='ModuleA', name='test', description='test', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='FuncA', name='test', description='test', of_type=<NodeType.FUNCTION: 2>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ModuleB', name='test', description='test', of_type=<NodeType.MODULE: 3>, parent_identifier='ModuleA', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='FuncB', name='test', description='test', of_type=<NodeType.FUNCTION: 2>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
        ]
    ),
    set(
        [
            GenericRepr("Dependency(from_node='FuncA', to_node='FuncB')"),
            GenericRepr("Dependency(from_node='FuncA', to_node='ModuleA')"),
            GenericRepr("Dependency(from_node='ModuleA', to_node='FuncA')"),
            GenericRepr("Dependency(from_node='ModuleA', to_node='ModuleB')"),
        ]
    ),
)

snapshots["test_matches_snapshot[exclude_functions] 1"] = (
    set(
        [
            GenericRepr(
                "Node(identifier='ModuleA', name='test', description='test', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ClassA', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ClassB', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier='ModuleB', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ModuleB', name='test', description='test', of_type=<NodeType.MODULE: 3>, parent_identifier='ModuleA', path=None, args=None, lines=None)"
            ),
        ]
    ),
    set(
        [
            GenericRepr("Dependency(from_node='ClassA', to_node='ModuleA')"),
            GenericRepr("Dependency(from_node='ClassB', to_node='ClassA')"),
            GenericRepr("Dependency(from_node='ClassA', to_node='ClassB')"),
            GenericRepr("Dependency(from_node='ModuleA', to_node='ModuleB')"),
        ]
    ),
)

snapshots["test_matches_snapshot[exclude_modules] 1"] = (
    set(
        [
            GenericRepr(
                "Node(identifier='FuncA', name='test', description='test', of_type=<NodeType.FUNCTION: 2>, parent_identifier='ClassA', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ClassA', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ClassB', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='FuncB', name='test', description='test', of_type=<NodeType.FUNCTION: 2>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
        ]
    ),
    set(
        [
            GenericRepr("Dependency(from_node='FuncA', to_node='FuncB')"),
            GenericRepr("Dependency(from_node='ClassA', to_node='FuncA')"),
            GenericRepr("Dependency(from_node='ClassB', to_node='ClassA')"),
            GenericRepr("Dependency(from_node='ClassA', to_node='ClassB')"),
        ]
    ),
)

snapshots["test_matches_snapshot[include_only_classes] 1"] = (
    set(
        [
            GenericRepr(
                "Node(identifier='ClassA', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='ClassB', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
        ]
    ),
    set(
        [
            GenericRepr("Dependency(from_node='ClassB', to_node='ClassA')"),
            GenericRepr("Dependency(from_node='ClassA', to_node='ClassB')"),
        ]
    ),
)

# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_views_are_runable 1"] = (
    (),
    {
        "api_key": "ABCD",
        "description": "",
        "graph": GenericRepr(
            "Graph(edges={Dependency(from_node='A', to_node='B')}, nodes={Node(identifier='A', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None), Node(identifier='B', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)})"
        ),
        "graph_id": "view_domain_classes",
        "label": "My Graph",
    },
)

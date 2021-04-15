# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_view_calls_publish 1"] = (
    (),
    {
        "api_key": "ABCD",
        "description": "",
        "graph": GenericRepr(
            "Graph(edges=[Dependency(from_node='A', to_node='B')], nodes=[Node(identifier='A', name='test', of_type=<NodeType.CLASS: 1>, path=None, args=None, lines=None, external=False, description='test', parent_identifier=None), Node(identifier='B', name='test', of_type=<NodeType.CLASS: 1>, path=None, args=None, lines=None, external=False, description='test', parent_identifier=None)])"
        ),
        "graph_id": "test_codoc_view.codoc_identity_view",
        "label": "My Graph",
    },
)

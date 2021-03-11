# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_can_publish_graph 1"] = (
    (),
    {
        "headers": {
            "Authorization": "OrgToken ABCD",
            "Content-Type": "application/json",
        },
        "json": {
            "commit_hash": None,
            "description": "some description",
            "edges": [{"from_node": "A", "to_node": "B"}],
            "graph_id": "my-graph",
            "label": "My Label",
            "nodes": [
                {
                    "description": "test",
                    "identifier": "A",
                    "name": "test",
                    "of_type": "CLASS",
                },
                {
                    "description": "test",
                    "identifier": "B",
                    "name": "test",
                    "of_type": "CLASS",
                },
            ],
        },
    },
)

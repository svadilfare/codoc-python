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
            "commit_hash": "",
            "description": "some description",
            "edges": [{"from_node": "A", "to_node": "B"}],
            "graph_id": "my-graph",
            "label": "My Label",
            "nodes": [
                {
                    "description": "test",
                    "identifier": "B",
                    "name": "test",
                    "of_type": "CLASS",
                    "parent_node": None,
                },
                {
                    "description": "test",
                    "identifier": "A",
                    "name": "test",
                    "of_type": "CLASS",
                    "parent_node": None,
                },
            ],
        },
        "url": "https://api.codoc.org/graphs/",
    },
)

#!/usr/bin/env python3
import pytest

from codoc.service.export import publish


def test_can_publish_graph(mocker, snapshot, generic_graph, api_key):
    label = "My Label"
    graph_id = "my-graph"
    description = "some description"

    mock_post = mocker.patch("requests.post")

    publish(
        graph=generic_graph,
        label=label,
        graph_id=graph_id,
        description=description,
        api_key=api_key,
    )

    snapshot.assert_match(mock_post.call_args)


@pytest.fixture
def api_key():
    return "ABCD"


@pytest.fixture
def generic_graph(create_graph, create_node, create_edge):
    nodeA = create_node(identifier="A")
    nodeB = create_node(identifier="B")
    edge = create_edge(from_node=nodeA, to_node=nodeB)

    return create_graph(nodes=[nodeA, nodeB], edges=[edge])

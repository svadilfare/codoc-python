#!/usr/bin/env python3
import pytest

# from codoc.service_layer.publishing import GraphPublisher


def test_can_publish_graph(generic_graph, api_key):

    publisher = GraphPublisher(api_key)

    publisher.publish(generic_graph)


@pytest.fixture
def api_key():
    return "ABCD"


@pytest.fixture
def generic_graph(create_graph, create_node, create_edge):
    nodeA = create_node(identifier="A")
    nodeB = create_node(identifier="B")
    edge = create_edge(from_node_id="A", to_node_id="B")

    return create_graph(nodes=[nodeA, nodeB], edges=[edge])

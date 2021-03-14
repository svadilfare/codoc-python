#!/usr/bin/env python3
import pytest
from codoc.service.export.codoc_view import view, get_id
from codoc.domain.model import Graph

TEST_LABEL = "My Graph"


def test_get_id_from_func(examples):
    assert get_id(examples.random_function) == "examples.random_function"


def test_view_calls_publish(mocker, snapshot, generic_graph):
    mock_publish = mocker.Mock()

    api_key = "ABCD"
    codoc_identity_view(generic_graph, api_key=api_key, publish_func=mock_publish)

    snapshot.assert_match(mock_publish.call_args)


def test_view_uses_returned_graph(
    mocker, api_key, snapshot, generic_graph, generic_graph_2
):
    mock_publish = mocker.Mock()

    @view(label=TEST_LABEL)
    def codoc_static_graph_view(graph):
        return generic_graph_2

    codoc_static_graph_view(generic_graph, api_key=api_key, publish_func=mock_publish)

    arg_graph = mock_publish.call_args[1]["graph"]

    assert arg_graph is generic_graph_2


@view(label=TEST_LABEL)
def codoc_identity_view(graph):
    return graph


@pytest.fixture
def generic_graph_2(create_graph, create_node, create_edge):
    return Graph(nodes=[create_node(identifier="C")], edges=[])

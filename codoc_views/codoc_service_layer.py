#!/usr/bin/env python3

from codoc.service.parsing.node import get_description
from codoc import filters, view

import codoc
import codoc.service
import codoc.service.export


@view(
    label="Parsing in Codoc Python",
    description="""
This graph showcases the inter dependencies of the parsing,
as well as the direct dependencies of
the internal aspects.
\n\n
"""
    + get_description(codoc.service),
)
def view_parsing(graph):
    return filters.get_children_of(codoc.service.parsing)(graph)


@view(
    label="Graph Generation in Codoc Python",
)
def view_graph_rendering(graph):
    """
    This graph showcases the inter dependencies of the graph,
    as well as the direct dependencies of
    the internal aspects.
    """
    # TODO makes sure the order of filters doesn't matter when looking at children.
    return filters.get_children_of(codoc.service.graph, keep_external_nodes=True)(
        filters.get_children_of(codoc)(graph)
    )


@view(
    label="Overview of the Service layer",
    description=get_description(codoc.service),
)
def service_layer_view(graph):
    return filters.get_depth_based_filter(2)(
        filters.get_children_of(codoc.service, keep_external_nodes=True)(graph)
    )


@view(
    label="Dependencies of the CLI",
)
def view_cli_dependencies(graph):
    """
    Here we show the dependencies of the CLI.
    """
    return filters.get_children_of(codoc.entrypoints, keep_external_nodes=True)(graph)


@view(
    label="Dependencies of the View decorator",
)
def depdencies_of_view_decorator(graph):
    """
    To minimize the bootstrapping of each view, we chose to create view
    decorators that make it easy to add relevant details to the specific
    view function but also make it easy for the Codoc Python framework
    to find any defined view function.

    The current version of the view decorator is closely knitted to the
    Codoc API, however, we plan to refactor this to make it simply
    return a view, rather than publish a view.

    The view decorator overrides the __name__, __docs__ attributes but also sets label,
    description, and graph_id on the function before returning it.

    It also changes the return type to simply return a success or failure regarding
    whether the publishing step succeeded. Lastly, it creates a __is_codoc_view attribute,
    with the True value. This can then be used when Codoc Python searches for
    views by checking objects whether it has that attribute.

        def is_a_codoc_view(obj: object) -> bool:
            return getattr(obj, "__is_codoc_view", False)
    """

    return filters.get_children_of(
        codoc.service.export.codoc_view, keep_external_nodes=True
    )(filters.get_children_of(codoc)(graph))


@view(
    label="Context of codoc.service.finder",
)
def view_context_of_finder_module(graph):
    """
    This graph showcases the inter dependencies of the graph,
    as well as the direct dependencies of
    the internal aspects.
    """
    finder_graph = filters.get_children_of(
        codoc.service.finder, keep_external_nodes=True
    )(filters.get_children_of(codoc)(graph))
    service_layer_graph = filters.get_depth_based_filter(2)(
        filters.get_children_of(codoc.service, keep_external_nodes=True)(graph)
    )

    return finder_graph | service_layer_graph

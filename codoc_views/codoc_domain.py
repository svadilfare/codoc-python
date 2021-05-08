#!/usr/bin/env python3
import codoc.domain.model
import codoc.domain
import codoc.domain.helpers
from codoc import filters, view


@view(
    label="Domain Model",
)
def domain_model(graph):
    """
    This view presents the basic domain model of the
    Codoc Python system.

    It shows the core models.

    To actually utilize the classes, look at the service layer.
    """
    graph = filters.get_children_of(codoc.domain.model)(graph)

    return filters.include_only_classes(graph)


@view(
    label="Domain",
)
def domain(graph):
    graph = filters.get_children_of(codoc.domain)(graph)

    return graph

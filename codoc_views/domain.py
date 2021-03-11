#!/usr/bin/env python3
from codoc.service import filters

import codoc.domain.model


@codoc.export.view(
    label="Domain Model",
)
def domain_model_view(graph):
    """
    This view presents the basic domain model of the
    [Codoc](https://codoc.org/) system.

    It shows the core models.

    To actually utilize the classes, look at the service layer.
    """

    domain_model_filter = filters.include_only_children_of_obj(codoc.domain.model)

    graph = domain_model_filter(graph)
    graph = filters.include_only_classes(graph)

    return graph

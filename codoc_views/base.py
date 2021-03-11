#!/usr/bin/env python3
import os

from codoc.service.graph import create_graph_of_module
from codoc.service.export import publish
from codoc.service import filters

import codoc.domain.model


def modules():
    # TODO this needs dependencies between modules if on children, to work.
    graph = create_graph_of_module(codoc, include_external_dependencies=False)

    graph = filters.exclude_functions(filters.exclude_classes(graph))

    description = """
This view contains all the modules that our system contain.
    """
    publish(
        graph=graph,
        graph_id="module_view",
        label="Module View of the Codoc SDK",
        description=description,
        api_key=os.getenv("CODOC_API_KEY"),
    )

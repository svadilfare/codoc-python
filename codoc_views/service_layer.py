#!/usr/bin/env python3
import os

from codoc.service.graph import create_graph_of_module
from codoc.service.parsing.node import get_description
from codoc.service.export import publish
from codoc.service import filters

import codoc.service


def parsing():
    graph = create_graph_of_module(
        codoc.service.parsing, include_external_dependencies=False
    )

    graph = filters.exclude_modules(graph)

    description = """
This graph showcases the inter dependencies of the parsing,
as well as the direct dependencies of
the internal aspects.
\n\n
""" + get_description(
        codoc.service
    )

    publish(
        graph=graph,
        graph_id="service_layer-parsing",
        label="Parsing in Codoc Python",
        description=description,
        api_key=os.getenv("CODOC_API_KEY"),
    )

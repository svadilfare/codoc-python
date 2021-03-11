#!/usr/bin/env python3
import os

from codoc.service.graph import create_graph_of_module
from codoc.service.export import publish
from codoc.service import filters

import codoc.domain.model


def domain_model_view_function():
    graph = create_graph_of_module(codoc.domain.model)

    class_graph = filters.include_only_classes(graph)

    publish(
        graph=class_graph,
        graph_id="domain_model",
        label="Domain Model",
        description="""
        This view presents the basic domain model of the
        [Codoc](https://codoc.org/) system.

        It shows the core models.

        To actually utilize the classes, look at the service layer.
        """,
        api_key=os.getenv("CODOC_API_KEY"),
    )

#!/usr/bin/env python3

from codoc.service.parsing.node import get_name, get_parent_of_object, get_description

from codoc.domain.model import Graph
from typing import Optional, Callable
from codoc.service.export import publish


def view(
    label: str,
    graph_id: str = None,
    description: str = None,
):
    def decorator(func):
        nonlocal description
        nonlocal graph_id

        if description is None:
            description = get_description(func)
        if graph_id is None:
            graph_id = get_id(func)

        def decorated_function(
            graph: Graph,
            api_key: str,
            publish_func: Optional[Callable] = None,
        ):
            filtered_graph = func(graph)
            if not publish_func:
                publish_func = publish

            if not filtered_graph.nodes:
                raise ValueError(f"Graph '{label}' has no nodes")

            return publish_func(
                graph=filtered_graph,
                label=label,
                graph_id=graph_id,
                description=get_description(func),
                api_key=api_key,
            )

        decorated_function.__name__ = graph_id
        decorated_function.__docs__ = description

        # Attributes for logging etc
        decorated_function.graph_id = graph_id
        decorated_function.label = label
        decorated_function.description = description

        return decorated_function

    return decorator


def get_id(func) -> str:
    parent = get_parent_of_object(func)
    if parent:
        prefix = get_id(parent) + "."
    else:
        prefix = ""

    return prefix + get_name(func)

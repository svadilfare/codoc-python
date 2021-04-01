#!/usr/bin/env python3
from codoc.service.parsing.node import get_identifier_of_object

from codoc.service import filters
from codoc.service.export.codoc_view import view

import codoc


@view(
    label="Module View of the Codoc SDK",
)
def view_modules(graph):
    """
    This view contains all the modules that our system contain.
    """
    return filters.exclude_functions(filters.exclude_classes(graph))


@view(
    label="Internal Module View of the Codoc SDK",
)
def view_modules_internal(graph):
    """
    This view contains all the modules that our system contain.
    """
    graph = filters.get_children_of(
        get_identifier_of_object(codoc), keep_external_nodes=False
    )(graph)
    return filters.exclude_functions(filters.exclude_classes(graph))

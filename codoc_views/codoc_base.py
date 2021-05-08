#!/usr/bin/env python3

from codoc import filters, view

import codoc


@view(
    label="Module View of the Codoc SDK",
)
def view_modules(graph):
    """

    This diagram can be a bit verbose, but shows all external dependencies
    and where we and how we depend on them.

    It is good to get an overview of the whole system and how it connects
    with the outside world.
    """
    graph = filters.get_depth_based_filter(2)(graph)
    return filters.include_only_modules(graph)


@view(
    label="Internal Module View of the Codoc SDK",
)
def view_modules_internal(graph):
    """
    This view displays the internal structure of the Codoc Python
    system.

    The main purpose is to see how different elements are inter-dependent.

    The service layer is created to expose pure functionality of the framework.

    We try to develop things in a pure functional fashion without side effects, and
    general adhere to immutable data types.

    We utilize a service layer with the intent of separating
    the domain model from usage.

    The top level of the service layer should expose a bunch of functions
    that can  be used by a given entry point
    (be it the CLI or when used as a functional framework)

    Our usage of a service layer is heavily inspired by
    [Architectural Patterns In Python](https://cosmicpython.com).

    We also have a data model. These are pure dataclasses,
    and are the basis of the overall system.

    """
    return filters.get_depth_based_filter(2)(filters.get_children_of(codoc)(graph))


@view(
    label="Internal(detailed) Module View of the Codoc SDK",
    description=view_modules_internal.__docs__,
)
def view_modules_internal_detailed(graph):
    return filters.include_only_modules(
        filters.get_depth_based_filter(3)(filters.get_children_of(codoc)(graph))
    )

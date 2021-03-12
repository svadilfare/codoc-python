"""
This module contains various filters that can be used to filter a graph.

This is used to create a more special and specific view, making it more
viewer friendly.

An example giving a class diagram:

```python
graph = create_graph_of_module(examples)

class_graph = filter_only_classes(graph)
````
"""
from .exclusively_classes import include_only_classes
from .children_based import get_children_of
from .type_exclusion_filter import exclude_classes, exclude_functions, exclude_modules


__all__ = [
    "include_only_classes",
    "exclude_classes",
    "exclude_functions",
    "exclude_modules",
    "get_children_of",
]

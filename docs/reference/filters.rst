
.. _reference-filters:
.. _reference-filter:
.. _filter:
.. _filters:

Filters
================

.. automodule:: codoc.service.filters


.. _type_ex_filter:

Type exclusion Filters
----------------------
.. automodule:: codoc.service.filters.type_exclusion_filter


.. _class_ex_filter:

Class based
`````````````````

.. autofunction:: exclude_classes

.. _function_ex_filter:

Function based
`````````````````

.. autofunction:: exclude_functions


.. _module_ex_filter:

Module based
`````````````````

.. autofunction:: exclude_modules


.. _child_filter:

Child Based Filters
----------------------

.. autofunction:: codoc.service.filters.get_children_of


.. _class_diagram:

Class Diagram filter
----------------------

.. autofunction:: codoc.service.filters.class_diagram_filter


Customization
-------------
Filters are, from a implementation perspective, simply a function that
takes a graph and returns a new graph, making it very easy to implement custom
filters.

An example where one creates a filter that removes all edges:


.. code-block:: python


   def remove_edges(graph):
        return Graph(
                nodes=graph.nodes,
                edges=set()
        )

We recommend you put all your custom filters in your `codoc_views` folder, in a
file called `custom_filters` or similar, however this is completly optional.

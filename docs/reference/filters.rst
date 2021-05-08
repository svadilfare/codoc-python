
.. _reference-filters:
.. _reference-filter:
.. _filter:
.. _filters:

Filters
================

.. automodule:: codoc.service.filters


.. _type_ex_filter:

Type based
----------------------
.. automodule:: codoc.service.filters.type_exclusion_filter


.. _class_ex_filter:

Exclude classes
`````````````````

.. autofunction:: exclude_classes

.. _function_ex_filter:

Exclude functions
`````````````````

.. autofunction:: exclude_functions


.. _module_ex_filter:

Exclude modules
`````````````````

.. autofunction:: exclude_modules

Exclude exceptions
````````````````````

.. autofunction:: exclude_exceptions

Only classes
`````````````````

.. autofunction:: include_only_classes

Only functions
`````````````````

.. autofunction:: include_only_functions


Only modules
`````````````````

.. autofunction:: include_only_modules

Only exceptions
````````````````````

.. autofunction:: include_only_exceptions

.. _child_filter:

Child Based
----------------------

.. autofunction:: codoc.service.filters.get_children_of

Depth based
----------------------

.. autofunction:: codoc.service.filters.get_depth_based_filter

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

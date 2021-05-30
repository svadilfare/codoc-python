
.. _reference-filters:
.. _reference-filter:
.. _filter:
.. _filters:

Filters
================

list of all filters
--------------------

.. automodule:: codoc.service.filters


.. _type_ex_filter:

.. _class_ex_filter:

.. autofunction:: exclude_classes

.. _function_ex_filter:

.. autofunction:: exclude_functions

.. _module_ex_filter:

.. autofunction:: exclude_modules

.. autofunction:: exclude_exceptions

.. autofunction:: include_only_classes

.. autofunction:: include_only_functions

.. autofunction:: include_only_modules

.. autofunction:: include_only_exceptions

.. _child_filter:

.. autofunction:: content_of

.. autofunction:: get_depth_based_filter

.. _class_diagram:

.. autofunction:: class_diagram_filter


.. autofunction:: filter_by_regex
.. autofunction:: exclude_by_regex


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

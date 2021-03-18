.. _views:

Views
================
A view is a graph with a label and a description, which can be viewed in our
`web app <https://codoc.org/app/?utm_source=readthedocs&utm_medium=post&utm_campaign=info>`_

They can compared to `Architectural
views <https://www.sciencedirect.com/topics/computer-science/architecture-view>`_,
however we aim to make them interactive and contain more and better information.

The cool thing about having architectural views in your CI pipeline, is that you
have historical information, and that they are constantly up to date.

This is what you can use the
`codoc app <https://codoc.org/app/?utm_source=readthedocs&utm_medium=post&utm_campaign=info>`_
for. You can see all prior versions, and how your system evolves from a
structural perspective. It's super cool in our humble opinion.

In our framework, we define a view as consisting of:

- A graph
- A label
- A unique id
- A project that (which *owns* the view)
- An optional commit hash


.. _view_functions:

View Functions
--------------
Views functions are functions that are used to generate views.

They should reside in files prefixed with `views_` and reside inside
a `codoc_views` folder in your root directory.

A simple example can be found in :ref:`simpleview`.

A view is simply a function that takes a graph as input and returns the graph
that you want to view. Here you add a label and a description and any related
data that is relevant to you. The label is supplied in the `view` decorator, and
the description is simply the docstring of the view function.

The label you supply to the decorator is the one that will be visualized on the webapp.

Advanced Usage
******************************

By default the view

Dynamic Descriptions
`````````````````````````````````
The `view` function can also take a string as input if you want a dynamic
description, i.e based on the docstring of something else. This can make
documentation more `DRY <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_:

.. code-block:: python

    from codoc.service import filters
    from codoc.service.export import view
    from codoc.service.parsing.node import get_description

    import myproject

    @view(
        label="Module View",
        description=get_description(myproject)
    )
    def view_modules(graph):
        return filters.exclude_functions(filters.exclude_classes(graph)


Custom ID
`````````````````````````````````
The way we identify whether two views are the same, but different versions, is
by using a unique graph_id. We generate this based on the function and file
name, which is a combination we hope is unique. You can, however, set this
yourself, if you have concrete reasons for it. Don't do this if you don't know
what you are doing, because it my create collisions, and make your documentation unusable.

.. code-block:: python

    from codoc.service import filters
    from codoc.service.export import view

    import myproject

    @view(
        label="Module View",
        graph_id="my_very_long_and_unique_id"
    )
    def view_modules(graph):
        return filters.exclude_functions(filters.exclude_classes(graph)

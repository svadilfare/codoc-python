.. _`examples`:

==========================
Examples of view functions
==========================

This file contains examples of different views, explain what they do and why you
might want them. They are merely examples and might need tweaking to work within
your project

Domain Model
-------------
Model diagram, class diagram or something else. People call it different
things.

To quote `Cosmic Python
<https://www.cosmicpython.com/book/chapter_01_domain_model.html#_what_is_a_domain_model>`_,
a highly recommended book:

    The domain is a fancy way of saying the problem you’re trying to solve. Your
    authors currently work for an online retailer of furniture. Depending on
    which system you’re talking about, the domain might be purchasing and
    procurement, or product design, or logistics and delivery. Most programmers
    spend their days trying to improve or automate business processes; the
    domain is the set of activities that those processes support.

The following view function will show all the classes of your domain model,
given that it's defined in ``myproject.domain``.

.. code-block:: python

    from codoc import filters, view

    import myproject


    @view(
        label="Domain model (Classes)",
    )
    def domain_model(graph):
        graph = filters.get_children_of(myproject.domain, keep_external_nodes=False)(graph)

        return filters.include_only_classes(graph)

Django models
---------------------------
In django you define your dataclasses by inheriting the *Model* class.
Our filters currently do not support filtering based on inheritance, however by
concatinating

.. code-block:: python

    from codoc import filters, view

    import accounts.models
    import billing.models

    @view(
        label="Domain Model (API)",
    )
    def all_models(graph):
        graph = filters.include_only_classes(graph) | filters.include_only_modules(graph)

        return (
            filters.get_children_of(accounts.models)(graph)
            | filters.get_children_of(billing.models)(graph)
        )


Clean Django module diagram
---------------------------
Django includes a few files that you might not be that interested in, like the
``migrations`` file or ``tests`` of each app. We personally like to get a bit
cleaner diagrams. We also don't always need external dependencies.
The following custom made filter can help you here, and is
utilized in the below example:

.. code-block:: python

    from codoc import view, filters

    import accounts, billing

    @view(
        label="Internal modules",
    )
    def internal_modules(graph):
        return remove_django_bloat(
            remove_external_nodes(
                filters.include_only_modules(graph)
            )
        )

    def remove_external_nodes(graph):
        return (
            filters.get_children_of(accounts)(graph)
            filters.get_children_of(accounts)(graph)
            | filters.get_children_of(billing)(graph)
        )

    def remove_django_bloat(graph):
        graph = filters.exclude_by_regex(r".migration")(graph)
        graph = filters.exclude_by_regex(r".test")(graph)
        graph = filters.exclude_by_regex(r".apps")(graph)
        graph = filters.exclude_by_regex(r".snapshots")(graph)

        return graph

.. seealso::

   - :ref:`filters`
   - :ref:`how`

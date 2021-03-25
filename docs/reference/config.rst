
.. _config:
.. _configuration:

Configuration
============================
Some times you want more control of your view generation - maybe you want to
apply a filter on *all* views for what ever reason, or maybe you want to add
annotations to each graph.

This is all possible in the configuration file.

file
---------
The file needs to be located in your `codoc_views` folder and be called
`codoconf.py`.
The cool thing is that it is an executable python file, making it easy to write
custom setup functions based on your environment.

.. _bootstrap:

Bootstrap
---------
The graph given to each view function is generated with the ``bootstrap``
function.

One can find simple version in :ref:`simple_config`, however more advanced
versions could be by utilizing :ref:`filters`, i.e:

.. code-block:: python

    from codoc.service.graph import create_graph_of_module
    from codoc.service import filters

    import myproject

    def bootstrap():
        graph = create_graph_of_module(myproject)
        return filters.exclude_functions(graph**


.. _prep_env:

Prepping your environment
-------------------------

One neat reason to use the :ref:`bootstrap` function, is that you can use it to
prepare your environment. If you are using a framework of sorts, there might be
a need to bootstrap your code before it can run.

.. _dotenv:

Python dotenv
---------

We personally like `python-dotenv <https://pypi.org/project/python-dotenv/>`_,
and it can easily be used for, for instance, your CODOC API key. Simply add it like so:

.. code-block:: python

    import os
    from dotenv import load_dotenv

    import myproj


    def bootstrap():
        load_dotenv()
        return create_graph_of_module(myproj)
.. _django:

Django
---------

Django needs you to bootstrap and import settings prior to importing any
modules.

The following config will do this, which is taken from our own
backend, which is also written in django:

.. code-block:: python

    import os
    from codoc.service.graph import create_graph_of_module


    def bootstrap():

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codoc_api.settings")
        import django

        django.setup()
        import organizations

        return create_graph_of_module(organizations)


An important note with django is that you don't, in the same fashion, have a
singular module, but rather multiple. A cool thing here, however, is that graphs
can be combined. We do something like this, in our application:

.. code-block:: python

    import os
    from codoc.service.graph import create_graph_of_module


    def bootstrap():

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codoc_api.settings")
        import django

        django.setup()
        import organizations
        import graphs


        return create_graph_of_module(organizations) + create_graph_of_module(graphs)

And you can then add all the modules you have that are relevant.

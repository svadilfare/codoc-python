
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
.. _create_system_graph:
.. _setup_function:

Setup
--------------------

The graph given to each view function is generated with the ``setup``
function.

One can utilize the simple version in :ref:`simple_config`, however more advanced
versions could be by utilizing :ref:`filters`, i.e:

.. code-block:: python

    # codoc_views/config.py
    from codoc import new_graph, filters

    import myproject

    def setup(**kwargs):
        graph = new_graph(myproject)
        return filters.exclude_functions(graph, **kwargs)


However the function exposes a variety of other possibilities too.

.. _prep_env:

Prepping your environment
.........................

One neat reason to use the :ref:`create_system_graph` function, is that you can use it to
prepare your environment. If you are using a framework of sorts, there might be
a need to bootstrap your code before it can run.

.. _dotenv:

Python dotenv
.............

We personally like `python-dotenv <https://pypi.org/project/python-dotenv/>`_,
and it can easily be used for, for instance, your CODOC API key. Simply add it like so:

.. code-block:: python

    # codoc_views/config.py
    from codoc import new_graph
    from dotenv import load_dotenv

    import myproject


    def setup(**kwargs):
        load_dotenv()
        return new_graph(myproject, **kwargs)

.. _multi_mods:

Multiple modules
................
Some Python codebases exposes multiple packages. If this is the case, then you
need to generate graphs for all of these too. Luckily you can use a variety of
binary operators to group graphs together. Using the OR (``|``) operation you
can get nodes that exist in either of two graphs. The following configuration
file does precisely this to include tests as well as dependencies of the views themselves:

.. code-block:: python

    # codoc_views/config.py
    from codoc import new_graph

    import myproject, tests, codoc_views

    def setup(**kwargs):
        return (
            new_graph(sample, **kwargs)
            | new_graph(tests, **kwargs)
            | new_graph(codoc_views, **kwargs)
        )


.. _django:

Django
.........

Django needs you to bootstrap and import settings prior to importing any
modules.

The following configuration does this, and creates a graph for two different
django apps (Which is what they name their modules). Replace ``app_one`` and
``app_two`` with the modules of your system, and add more if applicable.

.. code-block:: python

    # codoc_views/config.py
    from codoc import new_graph
    import os

    def setup(**kwargs):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codoc_api.settings")
        import django
        django.setup()

        import app_one, app_two
        return (
            new_graph(app_one, **kwargs) |
            new_graph(app_two, **kwargs)
        )

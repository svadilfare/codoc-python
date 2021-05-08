.. _get-started:

===============
Getting started
===============

``codocpy`` requires: Python 3.6, 3.7, 3.8, 3.9.

.. _`getstarted`:
.. _`installation`:

Install ``codoc-python``
----------------------------------------


1. Install the package by running:

.. code-block:: bash

    pip install codoc-python

2. Check that it's installed correctly:

.. code-block:: bash

    $ codocpy

Create a config
-----------------------
Everything Codoc related should be located inside a folder
called ``codoc_views`` located at the root directory of your project.

Start by creating a configuration file:

You will also need a basic config file in the same folder, called ``config.py``.
This file mainly needs a function called ``bootstrap`` to return a
graph of the system in question. The example below returns a graph containing
the ``myproject`` module, and it's direct dependencies:

.. warning:: Using django? Please see :ref:`django` to bootstrap that correctly.
             Please see :ref:`multi_mods` if your code exposes multiple packages.

.. code-block:: python

    # codoc_views/config.py
    from codoc import new_graph

    import myproject

    def bootstrap(**kwargs):
        return new_graph(myproject, **kwargs)

.. _`simpleviews`:
.. _`simpleview`:
.. _`simple_view`:
.. _`firstview`:

Your first *view function*
--------------------------

Inside the ``codoc_views`` folder, create a new python file, the name of which can be anything
you choose. This file will include your first *view function*, which generates a view
of the modules of your system.

.. code-block:: python

    # codoc_views/module_views.py
    from codoc import filters, view
    @view(
        label="Module View",
    )
    def modules(graph):
        """
        This view contains all the top level modules that our project contains.
        """
        module_graph = filters.include_only_modules(graph)
        top_module_graph = filters.get_depth_based_filter(2)(module_graph)
        return top_module_graph

You can verify that codoc can find your views:

.. code-block:: bash

    $ codocpy list_views
    - module_views.modules

.. warning:: Please make sure you are in the root directory of the project.

This should be your filename appended with the name of each view function.

.. _`simple_config`:
.. _`first_config`:


Publishing your view
----------------------------------------------------------

.. warning:: Codoc will load all your code, and by effect execute all
             side-effects! Make sure you don't have files that execute critical
             code on import! see :ref:`side_effects` for more info.

By now we hope you are already `signed up
<https://codoc.org/signup/?utm_source=readthedocs&utm_medium=post&utm_campaign=info>`_
and a registered user.

You'll have to fetch the API key for the project you are currently working on.

Go to your `codoc project
<https://codoc.org/app/org/?utm_source=readthedocs&utm_medium=post&utm_campaign=info>`_
and scroll to the bottom and fetch your API key of choice.

This has to be set as an environmental variable called ``CODOC_API_KEY``. One
way of doing is simply by writing:

.. code-block:: bash

    $ export CODOC_API_KEY="f5f9c07f4ce96aeee3aeb32faf35c0e821b8c831"

You can now publish your views:

.. code-block:: bash

    $ codocpy publish
    Publishing Module View...
    published at https://codoc.org/app/view/181

.. note:: Did it failed? Codoc is a bit sensitive, sadly. Read :ref:`it_crashed`
          for what to do.

Your view is now published, and you can view it at the URL shown in your console
(in our example https://codoc.org/app/graph/181) which offers a public example
from our `sample project <https://github.com/svadilfare/codoc-python-example>`_

.. seealso::

   - :ref:`examples`
   - :ref:`how`
   - :ref:`filters`
   - :ref:`views`
   - :ref:`configuration`

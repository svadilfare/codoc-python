.. _get-started:

===============
Getting started
===============

This guide will go through setting up Codoc with Python, creating a config and a
few simple architectural views with the supplied framework. Finally you will
publish them, and see the diagrams of your system. Very neat!

Don't know what views are? A *view*, or *architectural view* is, according to
`opengroup.org
<https://pubs.opengroup.org/architecture/togaf8-doc/arch/chap31.html>`_ is:

    Architecture views are representations of the overall architecture that are
    meaningful to one or more stakeholders in the system. The architect chooses
    and develops a set of views that will enable the architecture to be
    communicated to, and understood by, all the stakeholders, and enable them to
    verify that the system will address their concerns.

We have an indepth motivation and explanation on https://codoc.org - it also has examples!

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
This file mainly needs a function called ``setup`` to return a
graph of the system in question. The function takes ``**kwargs``, to pass along
any flags. The example below returns a graph containing the ``myproject``
module, and it's direct dependencies - please replace ``myproject`` with the
module you want to document:

.. warning:: Using django? Please see :ref:`django` to bootstrap that correctly.
             Please see :ref:`multi_mods` if your code exposes multiple packages.

.. code-block:: python

    # codoc_views/config.py
    from codoc import new_graph

    import myproject

    def setup(**kwargs):
        return new_graph(myproject, **kwargs)

.. _`simpleviews`:
.. _`simpleview`:
.. _`simple_view`:
.. _`firstview`:

Your first *view function*
--------------------------
You'll be creating what we call a *view function* now. This is a function that
takes, as input, a graph that details the whole python codebase, and as output
returns a new graph. This makes it possible for you to

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
        This view contains all the modules that your project contains.
        """
        return filters.include_only_modules(graph)

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

    $ export CODOC_API_KEY=f5f9c07f4ce96aeee3aeb32faf35c0e821b8c831

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


Your second *view function*
---------------------------
This prior view might be very verbose, depending on the system you have.
It also shows all external dependencies too, which might not be ideal.

If you feel confident and want to play around, you can look at
either :ref:`examples` for examples of views we created or :ref:`filters` for a
complete lists of possible views.

Otherwise read on! We will go into how you can use these filters for more
complex needs.

As mentioned, filters are simply functions that remove nodes from your graph,
however by combining them one can express rather complex needs.

For instance by chaining them (i.e using one on the result of another) one can
use the possibilities of both. The following examples uses a
``depth_based_filter`` to only get the top modules and any direct content of those.

Any important thing to note is that the function has a different name. Otherwise
one would override the other.

.. code-block:: python

    # codoc_views/module_views.py
    from codoc import filters, view

    @view(
        label="Top level Module View",
    )
    def top_level_modules(graph):
        """
        This view contains all the modules that your project contains.
        """
        graph = filters.include_only_modules(graph)
        # we only want the outer most modules and their direct content
        depth_based_filter = filters.get_depth_based_filter(2)
        return depth_based_filter(graph)

If you run ``codocpy publish`` again, you'll see two views being generated, and
if you click on the new one, you'll see a simpler graph.

Another great filter is the ``get_children_of``, which makes the graph "zoom in"
on a subsection (subgraph) of the graph/system. So if you are analyzing a
project called ``myproject`` but only want to view the content of a submodule,
i.e ``myproject.submodule`` the following view would help:


.. code-block:: python

    # codoc_views/module_views.py
    from codoc import filters, view
    import myproject.submodule

    @view(
        label="Content of Submodule",
    )
    def content_of_submodule(graph):
        return filters.get_children_of(myproject.submodule)(graph)

You could also use the ``|`` (OR) operator to get the union of two graphs, i.e
both modules AND classes. We increase depth here, to make sure we get more
content.

.. code-block:: python

    # codoc_views/module_views.py
    from codoc import filters, view
    import myproject.submodule

    @view(
        label="Classes & Module View",
    )
    def modules_and_classes(graph):
        graph = (
                filters.include_only_modules(graph)
                | filters.include_only_classes(graph)
        )
        return filters.get_children_of(myproject.submodule)(graph)

Want more? There are a bunch of examples and reference documentation etc that
you can consult. I hope it made sense - otherwise please contact us.

.. seealso::

   - :ref:`examples`
   - :ref:`how`
   - :ref:`filters`
   - :ref:`views`
   - :ref:`configuration`

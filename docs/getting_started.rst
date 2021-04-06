.. _get-started:

===============
Getting started
===============

.. _`getstarted`:
.. _`installation`:

``codocpy`` requires: Python 3.6, 3.7, 3.8, 3.9.

Install ``codoc-python``
----------------------------------------


1. Install the package by running:

.. code-block:: bash

    pip install codoc-python

2. Check that it's installed correctly:

.. code-block:: bash

    $ codocpy

.. _`simpleviews`:
.. _`simpleview`:
.. _`simple_view`:
.. _`firstview`:

Create your first View
-----------------------

We suggest to group your views into a single folder called ``codoc_views``. This
is the default folder that ``codocpy`` will look for.

Inside this folder, create a new file called ``codoc_sample.py``:

.. code-block:: python

    from codoc.service import filters
    from codoc.service.export import view

    @view(
        label="Module View",
    )
    def modules(graph):
        """
        This view contains all the modules that our project contain.
        """
        return filters.exclude_functions(filters.exclude_classes(graph))


.. note:: All codoc view files have to be prefixed with ``codoc_``

.. _`simple_config`:
.. _`first_config`:

Create a config
-----------------------

You will also need a basic config file in the same folder, called
``conf.py`` in your views folder, so codocpy knows what project you want to analyze:

.. code-block:: python

    from codoc.service.graph import create_graph_of_module

    import myproject

    def bootstrap():
        return create_graph_of_module(myproject)

.. note:: Using django? Please see :ref:`django` to bootstrap that correctly.

You can verify that codoc can find your views:

.. code-block:: bash

    $ codocpy list_views
    - view_modules




Publishing your view
----------------------------------------------------------

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



Your view is now published, and you can view at the returned domain (in our
example https://codoc.org/app/graph/181) which shows a public example from our
`sample project <https://github.com/svadilfare/codoc-python-example>`_

.. seealso::
   - :ref:`how`
   - :ref:`filters`
   - :ref:`views`
   - :ref:`configuration`

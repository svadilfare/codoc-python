.. Codocpy documentation master file, created by
   sphinx-quickstart on Thu Mar 18 10:21:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Turn your python code into architectural views
=============================================================

Codoc is the first Continuous Documentation tool.
It provides a revolutionary graph based interface,
that gives a powerful overview of any software system.

For more information about codoc, please visit `our website <https://codoc.org/?utm_source=readthedocs&utm_medium=post&utm_campaign=info>`_.

**Codocpy** is used to publish your graphical documentation & architectural views from a command-line
or CI solution, by writing simple Python scripts.

.. warning:: Codoc is still very early beta, and incomplete.
   We are currently looking for `beta testers <https://codoc.org/signup/?utm_source=readthedocs&utm_medium=post&utm_campaign=betatest>`_.

A quick example
---------------


.. code-block:: python

    @view(
        label="Module View",
    )
    def view_modules(graph):
        """
        This view contains all the modules that our system contain.
        """
        return filters.exclude_classes(graph)

Features
---------------

- Always-up-to-date architectural views
- A simple framework integrated in your favorite language
- Variety of filters to show only the relevant information
- Historical information about prior views
- **COMING SOON** See graphical representation of test coverage, contributors etc.
- **COMING SOON** Get live monitoring data on your views
- **COMING SOON** A git bot that provide context for pull requests
- **COMING SOON** A variety of export possibilities
- **COMING SOON** Sphinx (and other) integrations

Content
---------------
.. toctree::
   :maxdepth: 3

   getting_started
   reference/index
   faq


Bugs/Requests
-------------

Please use the `GitHub issue tracker <https://github.com/svadilfare/codoc-python/issues>`_ to submit bugs or request features.





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

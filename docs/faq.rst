
.. _faq:

Frequently Asked Questions
============================


.. _dynamic_analysis:
.. _dynanal:
.. _how:
.. _how_works:

How does codocpy work?
----------------------
You might be wondering how it all works.

codocpy utilizes `Dyanmic Analysis
<https://totalview.io/blog/what-dynamic-analysis#what>`_ to examine your code.

This is done because we get a greater insight into exactly how and what your
system does in the current environment with the external dependencies you have.
This provides a few cool features, one of which making it easy to fully
understand all dependencies, but also understand code with unexpected side
effects.
In the future, it will also make it possible to include information regarding
the path your code takes when running tests.



It crashed!
---------------------------

That isn't really a question but okay.

Codocpy relies on dynamic analysis (see :ref:`dynamic_analysis`), which means
that if your code crashes, then codoc crashes. There can be a bunch of different
reasons. We recommend you read :ref:`prep_env` and make sure it is setup correctly.

Another possible problem is side-effects in your code base. This can happen if
codocpy imports a file that doesn't `define a __main__ function <https://realpython.com/python-main-function/>`_  correctly, and then
either exits or something similar. This can happen if you have a python file
which executes python code on import. Don't do that :)

If you have circular dependencies, that will make codocpy crash too, due to
python not handling it.

We try our best at providing meaningful messages, where possible, however it
might be difficult at times. Codoc is a sensitive framework, but it will help
you forever if you treat it right.

Is it secure?
----------------------
You might fear losing your data. You shouldnt! Codoc doesn't access data and
only reads your sourcecode. It also only exports what you want, and you can
always delete your data again. It's as safe as using Github, Sonarcloud or other
tools.

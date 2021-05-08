
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

codocpy utilizes `Dynamic Analysis
<https://totalview.io/blog/what-dynamic-analysis#what>`_ to examine your code.

This is done because we get a greater insight into exactly how and what your
system does in the current environment with the external dependencies you have.
This provides a few cool features, one of which making it easy to fully
understand all dependencies, but also understand code with unexpected side
effects.
In the future, it will also make it possible to include information regarding
the path your code takes when running tests.


.. _side_effects:

Dangerous side effects!
---------------------------

Codocpy relies on dynamic analysis (see :ref:`dynamic_analysis`), which is both
good and bad. We strongly advise that you don't have any production api keys or
anything set up, in the environment you run codoc in. Codoc is much like
automated tests. If your automated tests execute code that sends emails, then codoc might
do it too. It's a bit different, but codoc will import all your files into
memory, and if your code is written improperly, then that means side effects.

This can happen if codocpy imports a file that doesn't
`define a __main__ function <https://realpython.com/python-main-function/>`_  correctly, and then
either exits or something similar. Essentially, if you have a python file
that executes python code on import, then don't run codoc. Rewrite your code.
It's bad practice.

**TL;DR**
Do this
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # scripts/myfile.py
    if __name__ == "__main__":
        users = get_users()
        for user in users
            send_spam_email(user)

Not this
~~~~~~~~~~~~~~~~~~~~~~~
.. warning:: DONT DO THE FOLLOWING
.. code-block:: bash

    # scripts/myfile.py
    users = get_users()
    for user in users
        send_spam_email(user)

.. _it_crashed:

It crashed!
---------------------------
This might be due to the quality of your code, and I mean that in the nicest way
possible.

Codocpy relies on dynamic analysis (see :ref:`dynamic_analysis`), which means
that if your code crashes, then codoc crashes. There can be a bunch of different
reasons. We recommend you read :ref:`prep_env` and make sure it is set up correctly.

You can run codocpy with the ``raise_errors`` for more information if the error
message isn't helpful. (``codocpy publish --raise_errors``).

Another possible problem is side-effects in your codebase. See :ref:`side_effects`.

If you have circular dependencies, that will make codocpy crash some times, due to python crashing.

If you are using Django, then it might be due to a `known bug <https://github.com/svadilfare/codoc-python/issues/4>`_ with ``admin.py``.

We try our best at providing meaningful messages, where possible, however, it
might be difficult at times. Codoc is a sensitive framework, but it will help
you forever if you treat it right.

Is it secure?
----------------------
You might fear losing your data. You shouldn't! Codoc doesn't access data and
only reads your source code. It also only exports what you want, and you can
always delete your data again. We, however, do not currently offer any
self-hosted solutions, so if you want total control over your data, you are out
of luck. Please contact us, if this is a big issue for you, and we might be able
to help, and/or prioritize it higher.

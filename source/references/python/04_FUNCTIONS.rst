.. _python_functions:

=========
Functions
=========

This page details **Python** functions we will frequently need to use.

The arguments of functions are specified as between angular brackets ``<>``, with the name of the argument on the left hand side and the type of argument on the right hand side. For example, the definition,

    my_function(<this_argument : required>, <that_argument : optional>)

Says the function ``my_function`` has a *required* argument named ``this_argument`` and an *optional* argument named ``that_argument``. 

.. _python_builtin_functions:

Built-In Functions
==================

``len(<list : required>)``
    The *length* function is used to find how many elements are in a list.

.. code:: python

    data = [ 1, 2, 3, 4, 5 ]
    n = len(data)

``sum(<list : required>)``
    The sum function totals all the elements in a list.

.. code:: python

    data = [ 2, 2, 2, 2 ]
    total = sum(data)
    print(data)

``range(<start : optional>, <stop : required>, <step : optional>)``
    The *range* generates an *iterable* sequence of numbers. 

Note only the ``stop`` argument is required. If only one argument is passed to the *range* function, then it is assumed to represent the ``stop`` argument. 

The *range* function is typically used with :ref:`python_list_comprehension` to generate large lists of data quickly. For example, the following code snippet will create and print the list ``[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]``,

.. code:: python

    data = [ i for i in range(10) ]

Notice the output does not include the endpoint *10*. The *range* function is exclusive with respect to the ``stop`` endpoint. This is so we can use the length function and get a result that makes sense,

.. code:: python

    data = [ i for i in range(10) ]
    n = length(data)
    print(n)

In other words, the *range* function excludes the endpoint so the length of the returned list will equal whatever number was originally passed into the *range* function.

You can use the ``start`` and ``step`` arguments to generate arbitrary lists of data according to a rule. The following code snippet will create and print the list ``[2, 4, 6, 8, 10, 12, 14, 16, 18]``

.. code:: python 

    data = [ i for i range(2, 20, 2) ]

.. _python_creating_functions:

Creating Functions
==================

TODO
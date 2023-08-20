.. _python_basics:

======
Basics 
======

**Python** is made up of *functions* and *variables*. Everything in **Python** is either one or the other. 

.. tip:: 

    As you read through this page, open an :ref:`IDLE shell<python_idle>` and try out the commands yourself.

Variables
=========

A variable is a stored piece of data. A variable has a *type* that is determined by the form of the data, called the *data type*. 

Every varible must be *assigned* a value in order to be used. A value assignment occurs when you type an expression of the form,

    x = y

The left hand side, *x*, is the *name* of the variable. The right hand side, *y*, is the *value* of the variable. The order in which the *name* and *value* appear is important: the *name* of the variable always occurs on the left hand side and the *value* of the variable always occurs on the right hand side. The equals sign in between them is the *assignment operator*; it assigns the value of *y* to *x*. 

.. warning:: 
    The assignment operator ``=`` is not *exactly* the same as the equals signs from **Algebra**, but it is similar. With an assignment, we are not *equating* two expressions. Instead, we are *assigning* the value of the right hand side to the left hand side.

.. _python_strings:

Strings 
    Data that represents text are called *strings*. A string is enclosed by double quotes "" or single quotes '',

.. code:: python

    var = "hello world"
    another_var = 'this is a sentence'
    print("these are strings: ", var, " & ", another_var)

.. _python_integers:

Integers
    Data that represents whole numbered quantities are called *integers*.

.. code:: python

    a_number = 5
    another_number = 15
    print("these are integers: ", a number, another_number)

.. _python_floats:

Floats
    Data that represents numerical quantities with decimals are called *floats*. 

.. code:: python

    n = 100.00000001
    m = 25.76
    print("these are floats: ", n, m)

.. _python_lists:

Tuples
    Tuples are *ordered pairs* of variables. 

    .. code:: python

        pair = (1, 2)

        another_pair = ("dog", "cat")

    Note the variables in the *tuple* do not have to be numbers.
    
Lists 
    Lists are ordered collections of variables. 
    
.. code:: python 

    example_list = [ "Led Zeppelin", "Pink Floyd", "The Beatles" ]

The *index* of an element in a list is the order that it appears, starting at 0. In other words, the first element in a list is *indexed* at 0, the second element at 1, the third element at 2, ... , the n :sup:`th` element at *n-1*. You can access the value of an element by using ``[]`` brackets and the element's index,

.. code:: python

    print("this is a whole list: ", example_list)
    print("this is the first element of a list: ", example_list[0])
    print("this is the second element of a list: ", example_list[1])
    print("this is the last element of a list: ", example_list[2])

The variables in a list need not be the same type,

.. code:: python

    unlike_list = [ "red", 5.67, "blue", "green" ]
    print("lists can have different types of elements: ", unlike_list[0], unlike_list[1])

You can determine the *length* of a list, i.e. how many elements are in it, using the ``len()`` function,

.. code:: python

    my_list = [ 1, 2, 3, 4, 5, 6, 7 ]
    print(my_list)

Arithmetical Operations
=======================

Most of the arithmetical operations in **Python** are exactly what you would expect them to be. The only operation whose symbol may be surprising is :ref:`python_exponentiation`.

.. _python_addition:

Addition
--------

.. code:: python
    
    7 + 3 

.. _python_subtraction:

Subtraction
-----------

.. code:: python
    
    10.45 - 3.2

.. _python_multiplication:

Multiplication
--------------

.. code:: python
    
    5 * 76

.. _python_division:

Division 
--------

.. code:: python

    68 / 5

.. _python_exponentiation:

Exponentiation
--------------

.. code::

    5 ** 2

.. _python_list_operations:

List Operations
===============

The operations in the previous section dealt with :ref:`python_floats` and :ref:`python_integers`. In other words, the operations in the last section applied to numbers. **Python** has many operations that can be applied to :ref:`python_lists`.

.. _python_list_slicing:

Slicing
-------

Slicing a list is **Python**'s way of accessing multiple elements in a list at once. The general syntax of slicing is given below,

    list[<start index : optional> : <end index : optional>]

Where ``<end index>`` is always *exclusive*, i.e. is **not** included in the slice. For example, 

.. code:: python

    data = [ "a", "b", "c", "d"]
    sliced_data = data[1:3]
    print(sliced_data)
    
The commands above will print to screen the elements starting at the second index up to, but not including, the fourth index. In other words, if you execute the given commands, you will see the list `["b", "c"]` print to screen. 

Try to figure out what the next example will print to screen before pasting it into an :ref:`IDLE notebook <python_idle>`,

.. code:: python 

    data = [ "A", "B", "C" , "D"]
    sliced_data = data[0:2]
    print(sliced_data)

If you leave out the ``<start index>``, it is understood to be ``0``, 

.. code:: python

    data = [ "dog", "cat", "fish" ]
    sliced_data = data[:2]
    print(sliced_data)

Likewise, if you leave out ``<end index>``, it is understood to be the (last index + 1),

.. code:: python

    data = [ "dog", "cat", "fish", "hamster", "bearded goat"]
    sliced_data = data[1:]
    print(sliced_data)

We can use slicing in conjunction with the ``len()`` function to remove data from the start and end of a data set, 

.. code:: python

    data = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    length = len(data)
    trimmed_data = data[2:length - 2]
    print(trimmed_data)

Special Slicing Techniques
**************************

There is another type of slicing that allows you extract elements from a list according to a rule. First we give the syntax and then go through a few examples,

    list[ <start_index : optional> :: <step : required>]

This command tells **Python** to look at the ``<start index>`` and then *iterate* through the list in steps of ``<step>``, grabbing each element it lands on along way,        

.. code:: python

    data = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    even_data = data[0::2]
    print(even_data)

The code snippet above will print to screen the list ``[ 0, 2, 4, 6, 8, 10]``. If instead we started at a different index,

.. code:: python 

    data = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    even_data = data[1::2]
    print(even_data)

This would print to screen the list ``[1, 3, 5, 7, 9]``

.. _python_list_comprehension:

Comprehension
-------------

*List comprehension* is a way of applying an algebraic expression to every element in a list. In other words, *list comprehension* allows us to generate a list of data according to a formula. For this reason, *list comprehension* is sometimes called *list generation*. The general syntax is given below, 

    list = [ <expr> for <element> in <list> ]

For example, the following code snippets uses the list ``[1, 2, 3, 4, 5]`` to generate a new list that squares each element of the first list and then prints it to screen,

.. code:: python

    data = [1, 2, 3, 4, 5]
    squared_data = [ x ** 2 for x in data ]
    print(squared_data)

*List comprehension* is usually used in conjunction with the `range() built-in function <python_builtin_functions>`. Hop over to that section, take a look at ``range()`` to see more examples.
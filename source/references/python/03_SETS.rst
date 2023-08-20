.. _python_sets:

====
Sets
====

.. _python_set_variables:

Set Variables
=============

A set is an *unordered* collection of variables. By *unordered* it is meant a set that contains *a* and *b* is considered the same as a set that contains *b* and *a*. 

A set is defined in **Python** using the familiar :math:`\{ \}` :ref:`list_notation`,

.. code:: python

    pets = { "dog", "cat", "fish", "hamster", "snake" }

    four_legs = { "dog", "cat", "hamster" }

    swims = { "dog", "fish", "snake" }

    warm_blooded = { "dog", "cat", "fish" }

    poets = { "byron", "shakespeare", "eliot" }


.. _python_set_operations: 

Set Operations
==============

.. note:: 
    Before executing these commands, try working them out by hand first and see if your work agrees!

.. _python_set_cardinality:

Cardinality
-----------

The :ref:`cardinality` of a set is found by calculating its :ref:`length <python_builtin_functions>`,

.. code:: python 

    total_pets = len(pets)

.. _python_set_union:

Union
-----

The :ref:`union` of two sets is found by,

.. code:: python

    pets_or_poets = pets.union(poets)

.. _python_set_intersection:

Intersection
------------

The :ref:`intersection` of two sets is found by,

.. code:: python 

    four_legs_and_swims = four_legs.intersect(swims)




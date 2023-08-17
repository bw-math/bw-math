====
Sets
====

Set Variables
=============

A set is an *unordered* collection of variables. By *unordered* it is meant a set that contains *a* and *b* is considered the same as a set that contains *b* and *a*. 

A set is defined in **Python** using the familiar :math:`\{ \}` :ref:`list_notation`,

    pets = { "dog", "cat", "fish", "hamster", "snake" }

    four_legs = { "dog", "cat", "hamster" }

    swims = { "dog", "fish", "snake" }

    warm_blooded = { "dog", "cat", "fish" }

    poets = { "byron", "shakespeare", "eliot" }

Set Operations
==============

.. note:: 
    Before executing these commands, try working them out by hand first and see if your work agrees!

The :ref:`cardinality` of a set is found by calculating its *length*,

    total_pets = len(pets)

The :ref:`union` of two sets is found by,

    pets_or_poets = pets.union(poets)

The :ref:`intersection` of two sets is found by,

    four_legs_and_swims = four_legs.intersect(swims)




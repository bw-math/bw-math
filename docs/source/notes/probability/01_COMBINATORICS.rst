.. _combinatorics:

=============
Combinatorics
=============

**Combinatorics** is the study of sequences and the order in which they occur.

.. _fundamental_counting_principles:

Definitions
=============

.. glossary::
    Power Set
        The *Power Set* of a set **A**, denoted :math:`PS(A)`, is the set of all subsets of **A**.

        .. warning::
            :math:`\forall B: B \subseteq A \implies B \in PS(A)`

    Sequences
        An ordered set of numerical elements. The i:sup:`th` element of a sequence is called the i:sup:`th` term of the sequence

        .. warning::
            :math:`G = \{ \forall x \in E, y \in F: xy \}` 


Fundamental Counting Principles
===============================

Motivation
----------

Suppose you live in the aptly named *Town A* and are planing a road trip to the similarly uninspired *Town C*. You plan on stopping at *Town B* to fill up your gas tank before proceeding to *Town C*.

Suppose further there are two routes from *Town A* to *Town B*, and there are four routes from *Town B* to *Town C*, depicted below.

INSERT PICTURE HERE

How many routes can you take from *Town A* to *Town B*, and then from *Town B* to *Town C*?

.. collapse:: Try It Yourself 
    The answer becomes obvious if we label the graphic pictured above appropriately. Use a *directed arrow* starting from each point to show each route taken. 

    INSERT PICTURE HERE

    The number of possible routes is equal to the number of endpoints in graph pictured above. In this case, 8. 
    
    These types of graphs are called `tree diagrams <tree_diagrams>` and they are very useful for visualizing the sample spaces of experiments that are composed successive, independent choices, as in this example. 

.. _counting_principle:

The Counting Principle
----------------------

We now generalize the example in the previous section into the *Counting Principle*, using the language of `Set Theory</notes/SET_THEORY>.

Proposition

    Let the sets **E** and **F** have cardinalities *n* and *m*. Let **G** of sequences *xy* formed by first selecting an element from **E**

.. note:: Example
    TODO

.. note:: Try It Yourself
    TODO

.. collapse:: Solution
    TODO

.. warning::

    We state the Counting Principle rigorously below

        :math:`n(E) = n \and n(F) = m`
        :math:``

.. _tree_diagrams:

Tree Diagrams
-------------

.. _generalized_counting_principle:

Generalized Counting Principle
------------------------------

Permutations
============

Motivation
----------
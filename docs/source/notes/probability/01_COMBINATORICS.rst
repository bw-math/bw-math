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
        The *Power Set* of a set **A**, or more simply the *Power Set of A*, denoted :math:`\mathcal{P}(A)`, is the set of all subsets of **A**.

        .. note::
            If :math:`A = \{ a, b \}`

            Then :math:`\mathcal{P}(A) = \{ \{\}, \{a\}, \{b\}, \{a, b\} \}`

        .. warning::

            We can define the *Power Set* of a set **A** formally by quantifying over all sets in the :ref:`Sample Space<sample_space>` (:ref:`Universal Set <universal_set>`) and imposing the condition we only look at subsets of a given set **A**

            :math:`\forall B: B \subseteq A \implies B \in \mathcal{P}(A)`

            In English, "for all *B*, if *B* is a subset of *A*, then *B* belongs to the *Power Set of A*"


Counting Principles
===============================

Motivation
----------

Suppose you live in the aptly named *Town A* and are planing a road trip to the similarly uninspired *Town C*. You plan on stopping at *Town B* to fill up your gas tank before proceeding to *Town C*.

Suppose further there are two routes from *Town A* to *Town B*, and there are three routes from *Town B* to *Town C*. Let us call the routes from *Town A* to *Town B* *a* :sub:`1` and *a* :sub:`2`, respectively. Let us call the routes from *Town B* to *Town C* *b* :sub:`1`, *b* :sub:`2`, and *b* :sub:`3`, respectively. This setup is depicted in the following diagram,

.. image:: ../../imgs/combinatorics_road_trip.png
   :width: 60%
   :align: center

How many different routes can you take from *Town A* to *Town C*, by way of *Town B*?

Before toggling the solution below, try and figure out the answer by drawing arrows from *Town A* to *Town B*, and then from *Town B* to *Town C* that represent the possible routes you can take and then count up each distinct route. In other worlds, generate a :ref:`Sample Space<sample_space>` for this "experiment".

.. collapse:: Solution

    We start by breaking down the problem into the choices we are making at each stage of the road trip. Starting in *Town A*, we have two possible routes from which we can choose to get to *Town B*. Once we arrive in *Town B*, regardless of the route we took to get there, we then have three possible routes to choose from that lead from *Town B* to *Town C*. To put it a different way, for each route from *Town A* to *Town B*, there are three routes from *Town B* to *Town C*.

    Each choice represents a branch. Every time we make a choice, we are narrowing down the set of possible outcomes. With that in mind, we can represent each choice as a *branch* in a tree, as in the following diagram,

    .. image:: ../../imgs/combinatorics_tree_diagram.png
        :width: 60%
        :align: center

    The number of possible routes is equal to the number of endpoints in this graph. In this case, there are 6 possible routes we can take, where each route is represented by a particular branch of the tree. These types of graphs are called :ref:`tree diagrams <tree_diagrams>`, for this reason. They are very useful for visualizing the sample spaces of experiments that are composed of successive, independent choices, as in this example. 

    We may also see the solution by enumerating every possible choice in :ref:`list_notation`,

    .. math::
        
        G = \{ {a_1}{b_1}, {a_1}{b_2}, {a_1}{b_3}, {a_2}{b_1}, {a_2}{b_2}, {a_2}{b_3} \}

    .. math::

        \implies n(G) = 6

.. _counting_principle:

The Fundamental Counting Principle
----------------------------------

We now generalize the example in the previous section into the *Counting Principle* in three steps: first, we give an intuitive explanation fo the *Counting Principle*, then we state it in :ref:`propositional <proposition>` form using the language of :ref:`Set Theory<set_theory>` and finally, we state it entirely symbolically.

**Heuristic**

    If the object **E** may be chosen in *n* ways, and thereafter the object **F** may be chosen in *m* ways, **E** and **F** may be chosen, in that order, :math:`n \cdot m` ways.
 
**Proposition**

    Let the sets **E** and **F** have cardinalities *n* and *m*, respectively. Let **G** be the set of sequences *xy* formed by first selecting an element *x* from **E** and then an element *y* from **F**. If these two conditions are met, then the cardinality of **G** is :math:`n \cdot m`

.. note:: Careful! 

    The element :math:`xy \in G` is **not** the product of *x* and *y*, i.e the number *x* times the number *y*. It is a *sequence* of the characters *xy*. 
    
    This becomes more obvious if we let :math:`E = \{ a, b, c \}` and :math:`F=\{d, e , f\}`; then **G** is the set of sequences :math:`G = \{ ad, ae, af, bd, be, bf, cd, ce, cf \}`. 
    
    Take note that :math:`n(E)=3`, :math:`n(F)=3`, so therefore :math:`n(G) = n(E) \cdot n(F) = 3 \cdot 3 = 9`

Before stating the *Counting Principle* formally, we will take a look at one more example.

**Example**
    
You are trying to figure out what to outfit to wear. In your closet, you have a red, green, blue and orange shirt. In your dresser, you have a pair of blue jeans, a pair of khakis and a pair of sweat pants. How many possible choices do you have for your outfit?

.. collapse:: Solution
    
    We have two sets in this problem: the set of shirts in our closet, and the set of pants in our dresser. 

    .. image:: ../../imgs/combinatorics_example.png
        :width: 60%
        :align: center

    The outfits we can pick are formed by first picking a shirt from the set of shirts, and then picking a pair of pants from the set of pants. The first set contains four elements and the second set contains three elements. Therefore, by the **Counting Principle**, the total number of outfits is the product of the two cardinalities, :math:`4 \cdot 3 = 12`.

.. warning::

    We state the hypothesis and conclusion of the **Counting Principle** in precise symbols below,

        .. math::
            n(E) = n \land n(F) = m
        .. math::
            G = \{ \forall x \in E \land y \in F: xy \}
        .. math::
            \implies n(G) = n(E) \cdot n(F)

.. _tree_diagrams:

Tree Diagrams
-------------

TODO 

.. _generalized_counting_principle:

Generalized Counting Principle
------------------------------

TODO 

Permutations
============

Motivation
----------

Three of your friends, Aletheia, Bertha and Cornelius, are running a foot race to determine who is the fastest. As a diligent statistician, rather than participate in the festitivities, you decide to turn into a bookie and take bets from your other friends on who is going to win the race. In order to assign odds to each outcome, you first have to know *how many ways* the race can finish.   

*Well*, my fellow statistician, how many ways *can* this race between Aletheia, Bertha and Cornelius finish? Before toggling the solution below, try and figure out the answer by listing each possible outcome and then totaling the number of results.

.. collapse:: Solution

    TODO

**Example**

.. collapse:: Solution 

    TODO 

Combinations
============

Motivation
----------

TODO



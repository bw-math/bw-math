.. _combinatorics:

=============
Combinatorics
=============

**Combinatorics** is the study of sequences and the order in which they occur.

Definitions
=============

.. _power_set:

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

Corollaries 
-----------

Before stating the first important corollary that follows from the *Generalized Counting Principle*, we look at an instructive example.

**Example**
    A pizza shop lets their customers make any kind of pizza they want from the following ingredients: pepperoni, sausage, green peppers, mushrooms and onions. 

    How many different pizzas can you order from this restaurant? Try listing out every possible sequence of toppings a customer could order. Once you think you have the answer, toggle the solution below and review the solution in detail.

.. :collapse:: Solution

    Let us represent the set of pizza topping as :math:`A = \{ s, p, g, m, o \}`, where *s = sausage*, *p = pepperoni*, *g = green peppers*, *m = mushroom* and *o = onions*.

    Notice the customer ordering pizza does not have to include *every* topping nor does the customer have to include *any* topping, if they so choose. For example, one customer might get a pepperoni, mushrooms and onions pizza (corresponding to the set :math:`\{ p, m, o \}`), while another customer might get a sausage, green peppers, mushrooms and onions pizza (corresponding to the set :math:`\{s, g, m, o \}`), while another still might get a pizza with *no* toppings at all (corresponding to the *empty set* :math:`\varnothing = \{\}`). 

    The choices being made in this problem consist of whether or not to include each ingredient. There are five ingredients, therefore there are five choices. For each ingredient and therefore for each choice, we have two options: include it or exclude it. A tree diagram helps visualize this,

    (INSERT PICTURE HERE)

    Thus, from inspection of tree diagram, we see solution is given by,

    :math:`2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^5 = 32`

    Notice the power of 2 on the left hand side of the equation is equal to the *cardinality of* **A**, :math:`n(A)`. 
    
    This example can be rephrased in a more general way using the language of :ref:`Set Theory<set_theory>`: *how many subsets can be formed from the set* **A**? 
    
    In other words, what is the *cardinality* of the *Power Set of A*?

    This leads directly to the first corollary of Combinatorics.

**Power Set Theorem**
    :math:`n(A)=n \implies n(\mathcal{P}(A))=2^n`


Permutations
============

Permutation
    An *r*-element permutation of *n* things is an ordered selection or arrangement of *r* of them.

Motivation
----------

Three friends, Aletheia, Bertha and Cornelius, are running a foot race to determine who is the fastest. As a diligent statistician, rather than participate in the festitivities, you decide to turn bookie and take bets from your other friends on who is going to win the race. In order to assign odds to each outcome, you first have to know *how many ways* the race can finish.   

*Well*, my fellow statistician, how many ways *can* this race between Aletheia, Bertha and Cornelius finish? Before toggling the solution below, try and figure out the answer by listing each possible outcome and then totaling the number of results.

.. collapse:: Solution

    TODO

**Example**

.. collapse:: Solution 

    TODO 

Formula
-------

TODO 

Combinations
============

Combination
    An *r*-element combination of *n* things is an unordered selection of *r* of them.

Motivation
----------

The same three friends from the permutation section, Aletheia, Bertha and Cornelius, have tossed their sneakers aside and decided their talents would be better served enriching the school culture. They each put their names into the running for Prom Committee. Unfortunately, there are only two open positions on the committee. How many ways can these open positions be filled by the three friends?

.. collapse:: Solution

    TODO

**Example**

.. collapse:: Solution 

    TODO 

The Connection Between Permutations and Combinations
----------------------------------------------------

Combined Permutations
*********************

Let **O** be the set of objects,

    .. math::
        O = \{ a, b, c \}

and consider all the two-element permutations that can be formed from this set, that is to say, all the possible ways two objects can be selected from this set, where the order of elements is important,

    ab ac bc ba ca cb 

If the condition that order is important is removed, then the permutation *ab* and *ba* are considered the same *combination*. Likewise for *ac* and *ca*, and then again for *bc* and *cb*. The number of distinct sequences becomes,

    ab ac bc

Permuted Combinations
*********************

Suppose now a similar set of objects **P** is given as,

    .. math::
        P = \{ a, b, c, d \}

and all two-element *combinations* (not *permutations*) are required, that is to say, all the possible ways two objects can be selected from this set, where order is important. Careful enumeration of every possibility yields the list of combination as follows,

    ab ac ad bc bd cd 



.. image:: ../../imgs/combinatorics_connection.png
        :width: 60%
        :align: center
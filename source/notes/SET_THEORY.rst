.. _set_theory: 

==========
Set Theory
==========

Preliminaries
=============

.. _symbolic_logic:

Logic
-----

In order to develop the theory of sets precisely, we will first need a few concepts from *logic*. 

.. _proposition:

Proposition
    :math:`p, q, r`

A sentence that can be judged either *true* or *false*.

.. _implication:

Implication
    :math:`p \implies q`

A symbolic representation of a *conditional* relationship between two *propositions*. This type of proposition can be translated into English in the following ways,
    1. "if *p*, then *q*"
    2. "whenever *p*, then *q*"
    3. "*p* implies *q*"
    4. "*q* follows from *p*"

Universal Quantification
    :math:`\forall p: q`

A symbolic representation of a universal proposition. This type of proposition can be translated into English in the following ways,
    1. "for all *p*, *q*"
    2. "for every *p*, *q*"
    3. "for each *p*, *q*"

Definitions
===========

.. _domain_of_discourse:

Domain of Discourse
    The *domain of discourse* is subject matter we are treating. 

.. _elements:

Elements
    :math:`x,y,x` (*lowercase letters*)
    
    :math:`x_1, x_2, ... , x_n` (*lowercase letters with subscripts*)
    
The individuals, or objects, in the *domain of discourse*; The "*things*" being counted.

.. _sets:

Sets
    :math:`A,B,C` (*upper case letters*)

    :math:`A_1, A_2, ... , A_n` (*uppercase letters with subscripts*)

Groups of elements that share a common property. *Sets* are sometimes referred to as *classes* or *collections*.

.. _cardinality:

Cardinality
    :math:`n(A)`

The number of *distinct* elements in a set.

.. _universal_set:

Universal Set 
    :math:`S`

The universal set *S* is set of all elements in the *domain of discourse*. 

.. _null_set:

Null Set
    :math:`\varnothing`

The unique set which contains nothing. 

Notation
========

.. _list_notation:

List Notation
-------------

.. math:: 

    A = \{ a, b, c, ... \}

In *list notation*, all of the elements that belong to **A** are *explicitly* written between a pair of brackets with commas separating each element. 

.. _quantifier_notation:

Quantifier Notation 
-------------------

.. math:: 
    
    A = \{ \forall x: F(x) \}

In *quantifier notation*, all of the elements that belong to **A** are *implicitly* written between a pair of brackets with a formula that specifies the conditions for membership.

*Quantifier notation* is sometimes referred to as *set builder notation*.

Corollaries
===========

:math:`n(\varnothing)=0`
    The number of elements in the *null set* (the *cardinality* of the *null set*) is 0.

:math:`\forall x: x \notin \varnothing`
    Nothing belongs to the *null set*

:math:`\forall x: x \in S`
    Everything belongs to the *unverisal set*

.. _venn_diagrams:

Venn Diagrams
=============

A *Venn Diagram* is a visual representation of sets. The universal set is represent as rectangle and sets are represented as circles within this rectangle. The simplest *Venn Diagram* is a graphic of a single set **A** shown against the universal set **S**, 

.. image:: ../assets/imgs/sets/sets_simple.jpg
    :align: center

You will sometimes set *Venn Diagrams* with the elements of the sets written in, as in the following picture,

.. image:: ../assets/imgs/sets/sets_simple_with_elements.jpg
    :align: center

*Venn Diagrams* are useful for visualizing :ref:`set_relations`. For this reason, we will see more complex examples of *Venn Diagrams* in the next section.

.. _set_relations:

Relations
=========

.. _subset:

Subset
******
 
Symbolic Expression
    .. math::
     
        A \subseteq B

**A** is a subset of **B** if all of **A**'s elements are contained in **B**. 

To say the same thing in a different way, if the element *x* belongs to **A**, then the element *x* also belongs to **B**

.. math::
    
    \forall x : x \in A \implies x \in B

The relation of *subset* can be seen in the following *Venn Diagram*, 

.. image:: ../assets/imgs/sets/sets_subset.jpg

This diagram represents the relationship :math:`A \subseteq B`.

.. _proper_subset:

Proper Subset 
*************

Symbolic Expression
    .. math:: 
        A \subset B

**A** is a subset of **B** and :math:`A \neq B`. To say the same thing in a different way, **A** is wholly contained in **B**.

.. math::
    \forall x: x \in A \implies x \in B \text{ and } A \neq B 

An equivalent way of defining a *proper subset* is given by,

.. math::
    \forall x: x \in A \implies x \in B \text{ and } n(A) < n(B)

This is an equivalent formulation between saying the cardinality of **A** is less than the cardinality of **B** is logically equivalent to saying **A** is not identical to **B**.

.. _set_equivalence:

Equivalence
***********

Symbolic Expression
    .. math::
    
        A \equiv B
    
Two sets **A** and **B** are *equivalent* if the number of elements in **A** is equal to the number of elements **B**.

.. _set_equality:

Equality
********

Symbolic Expression 
    .. math::

        A = B

Two sets **A** and **B** are *equal* if they contain the same elements. In other words, two sets are equal if they are the same set.

.. math:: 

    \forall x: x \in A \implies x \in B \text{ and } x \in B \implies x \in A

An equivalent way of defining the equality of sets is given by,

.. math:: 

    A \subseteq B \text { and } B \subseteq A 

In other words, if **A** is wholly contained in **B** and **B** is wholly contained in **A**, then the only way this can occur is if :math:`A = B`.

.. _set_operations:

Operations
==========

.. _complement:

Complement
**********

Symbolic Expression 
    .. math::

        A^c

    .. math::

        \sim  A

The set containing elements that do not belong to the set **A**. 

.. math:: 

    A^c = \{ \forall x: x \not in A \}

The complement can be visualized with the following *Venn Diagram*,

.. image:: ../assets/imgs/sets/sets_complement.jpg

.. tip:: 

    The complement of a set correspond to the English "*not*". To see this, let **S** be the set of animals and let **A** be the set of dogs. Then :math:`A^c` is the set of animals that are *not* dogs.

.. _union:

Union
*****

Symbolic Expression 
    .. math::

        A \cup B

The set containing elements that belong to either the set **A** or the set **B**.

.. math:: 

    A \cup B = \{ \forall x: x \in A \text{ or } x \in B \}

We have to be careful with *Venn Diagrams* that represent unions, because the two sets **A** and **B** might have elements in common, or they may not have elements in common. 

The first case, where the two sets have no elements in common is shown below,

.. image:: ../assets/imgs/sets/sets_union_disjoint.jpg

The union would be represented by *both* circles. Notice the circles do not touch. Sets that have no elements in common are called *disjoint*. 

The second case, where the two sets have elements in common is shown in the next diagram,

.. image:: ../assets/imgs/sets/sets_union_overlapping.jpg

The union would be represented by the entire area of both circles. Notices the circles share some elements in this case. Sets that have elements in common, but are not subsets in either direction (i.e. neither :math:`A \subseteq B` nor :math:`B \subseteq A`, are called *overlapping*.

.. tip:: 
    
    The union of two sets corresponds to the English "*or*". To see this, let **A** be the set of calculators. Let **B** represent the set of *pencils*. Then :math:`A \cup B` represents the set of *calculators* or *pencils*.

.. _intersection:

Intersection
************

Symbolic Expression
    .. math::
        
        A \cap B

The set containing elements that to both the set **A** and the set **B**. 

.. math:: 

    A \cap B = \{ \forall x: x \in A \text{ and } x \in B \}

As in the union, there are two cases we need to consider when representing the interesection of two sets with a *Venn Diagram*. Either the sets have elements in common, or they do not. 

The first case, where the two sets have elements in common is shown in the next diagram,

.. image:: ../assets/imgs/sets/sets_union_overlapping.jpg

The intersection is represented by where the circles meet. In the case of *overlapping* sets, this is non-empty,

.. math:: 

    A \cap B \neq \varnothing

The second case, where the two sets have no elements in common is shown below,

.. image:: ../assets/imgs/sets/sets_union_disjoint.jpg

The intersection is represented by where the circles meet. In the case of *disjoint sets*, the circles do not meet. Thus, 

.. math:: 

    A \cap B = \varnothing

.. tip:: 

    The intersection of two sets corresponds to the English "*and*". To see this, let **A** be the set of United States Senators. Let **B** the set of people over the age of 70. Then, :math:`A \cap B` represents the set of people who are both United States Senators and over the age of 70.

.. _set_theorems:

Theorems
========

Almost all of the theorems of Set Theory can be proven by referring to a :ref:`Venn Diagram<venn_diagrams>`. As you read through the following theorems, try to justify each one to yourself by drawing a picture of what it is saying. 

We will go through each of these theorems in more detail in class.

.. _identity_theorems:

Identity Theorems
-----------------

.. _identity_theorem_one:

Theorem 1
*********

.. math:: 

    A \cap \varnothing = \varnothing

.. note:: 

    Notice the resemblance to *zero property of multiplication*,

    .. math:: 
        
        a \cdot 0 = 0

.. _identity_theorem_two:

Theorem 2
*********

.. math:: 

    A \cup \varnothing = A

.. note:: 

    Notice the resembalnce to the *identity property of addition*,

    .. math::

        a + 0 = a

.. _identity_theorem_three:

Theorem 3
*********

.. math:: 

    A \cap S = A 

.. note:: 

    Notice the resemblance to the *identity property of multiplication*,

    .. math::

        a \cdot 1 = a

.. _identity_theorem_four:

Theorem 4
*********

.. math:: 

    A \cup S = S 

.. note:: 

    This theorem does not have an analogous algebraic property. This is where *set theory* starts to diverge from ordinary algebra. 

.. _identity_theorem_five:

Theorem 5
*********

.. math:: 

    A \cup A = A 

.. _identity_theorem_six:

Theorem 6
*********

.. math:: 

    A \cap A = A

Subset Theorems
---------------

.. _subset_theorem_one:

Theorem 1
*********
    .. math::

        A \cap B \subseteq A 

The intersection of **A** and **B** is a subset of **A**.

.. _subset_theorem_two:

Theorem 2
*********
    .. math::
        
        A \subseteq A \cup B

**A** is a subset of the union of **A** and **B**.

.. _subset_theorem_three:

Theorem 3
*********
    .. math::

        A \cap B \subseteq A \cup B

The intersection of two sets **A** and **B** is a subset of the union of those same two sets.

.. _subset_theorem_four:

Theorem 4
*********
    .. math::

        A \subseteq B \implies A \cap B = A

If **A** is a subset of **B**, then the intersection of **A** and **B** is equal to **A**. 

.. _subset_theorem_five:

Theorem 5
*********
    .. math::

        A \subseteq B \implies A \cup B = B

If **A** is a subset of **B**, then the union of **A** and **B** is equal to **B**

.. _subset_theorem_six:

Theorem 6
*********
    .. math:: 
    
        A \subseteq B \text{ and } B \subset C \implies A \subseteq C

If **A** is a subset of **B** and **B** is a subset of **C**, then **A** is a subset of **C**. 

.. note::
    
    This theorem is a type of `syllogism <https://en.wikipedia.org/wiki/Syllogism>`_. Refer to the :ref:`knowledge` section for more details on *syllogisms*.

.. _square_of_opposition:

Aristotle's Square of Opposition
================================
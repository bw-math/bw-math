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
    
    TODO

.. _sets:

Sets
    :math:`A,B,C` (*upper case letters*)

    :math:`A_1, A_2, ... , A_n` (*uppercase letters with subscripts*)

    TODO

.. _universal_set:

Universal Set 
    :math:`S`

    The universal set *S* is set of all elements in the *domain of discourse*. 

.. _null_set:

Null Set
    :math:`\varnothing`

Notation
========

.. _list_notation:

List Notation
    TODO

.. _quantifier_notation:

Quantifier Notation 
    TODO 

Corollaries
===========

:math:`n(\varnothing)=0`
    The number of elements in the *null set* (the *cardinality* of the *null set*) is 0.

:math:`\forall x: x \notin \varnothing`
    Nothing belongs to the *null set*

:math:`\forall x: x \in S`
    Everything belongs to the *unverisal set*

Relations
=========

.. _subset:

Subset 
    .. math::
        A \subseteq B

    All of **A**'s elements are contained in **B**. To say the same thing in a different way, if the element *x* belongs to **A**, then the element *x* also belongs to **B**

    .. math::
        
        x \in A \implies x \in B

.. _proper_subset:

Proper Subset 
    .. math:: 
        A \subset B

    **A** is a subset of **B** and :math:`A \neq B`. To say the same thing in a different way, **A** is wholly contained in **B**.

    .. math::
        x \in A \implies x \in B \land A \neq B 

    An equivalent way of defining a *proper subset* is given by,

    .. math::
        x \in A \implies x \in B \land n(A) < n(B)

    This is an equivalent formulation between saying the cardinality of **A** is less than the cardinality of **B** is logically equivalent to saying **A** is no the same as **B**.


.. _set_theorems:

Theorems
========

TODO
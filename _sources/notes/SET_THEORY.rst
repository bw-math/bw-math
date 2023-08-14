.. _set_theory: 

==========
Set Theory
==========

Preliminaries
=============

In order to develop the theory of sets precisely, we will need to use a few concepts from *logic*. 

.. glossary:: 

    .. _proposition::

    Proposition
        :math:`p, q, r`

        A sentence that can be judged either *true* or *false*.

    Implication
       A symbolic representation of a *conditional* relationship

Definitions
===========

.. _universal_set:

Universal Set 

    TODO

Null Set

    TODO

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

Subset 

    .. math::
        A \subseteq B

    All of **A**'s elements are contained in **B**. To say the same thing in a different way, if the element *x* belongs to **A**, then the element *x* also belongs to **B**

    .. math::
        
        x \in A \implies x \in B

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
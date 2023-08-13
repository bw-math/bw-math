Introduction
============

Probability is the study of the properties of random events.

Preliminaries
-------------

Extended Union 
    A symbol that represents the union of a sequence of sets.

    .. math:: 
        \bigcup\limits_{i=1}^{n} A_{i} = A_1 \cup A_2 \cup ... \cup A_{n-1} \cup A_n 

Summation
    A symbol that represents the sum of the elements :sub:`i`\ *x*

    .. math::
        \sum_{i=0}^n x_i = x_1 + x_2 + ... x_{n-1} + x_n

Definitions
-----------

Experiment
    An *uncertain* event.    

Mutual Exclusivity
    :math:`A \cap B = \varnothing \implies` **A** and **B** are mutually exclusive. 
        Two sets, **A** and **B**, are *mutually exclusive* if they are disjoint.

Outcomes 
    :math:`x, y, z` (*lower case letters*)
        A possible way an experiment might occur.
    
Sample Space 
    :math:`S`
        The set of all possible outcomes for an experiment.

Events 
    :math:`A, B, C` (*upper-case letters*)
    :math:`A_1, A_2, A_3, ..., A_{n-1}, A_n` (*upper-case letters with subscripts*)
        
    A subset of the sample space, i.e. a set of outcomes. 

    :math:`A \subseteq S \implies` **A** is an event

Probability
    :math:`P(A)`
        A numerical measure of the *likelihood*, or *chance*, that event **A** occurs.

.. _axioms_of_probability:

Axioms of Probability
---------------------

*Axiom 1*: :math:`P(A)>=A`
    All probabilities are positive; No probabilities are negative.

*Axiom 2*: :math:`P(S)=1`
    The probability of *some* outcome from the sample space **S** occuring is equal to 1.

*Axiom 3*: :math:`\forall i <> j: A_i \cap A_j = \varnothing \implies P(\bigcup\limits_{i=1}^{n} A_i) = \sum_{i=1}^n P(A_i)`
    If each event :sub:`i` **A** in the sample space **S** is *mutually exclusive* with every other event :math:`\forall i<>j: A_i`, then the probability of the union of all of these events is equal to the sum of the probabilities of each individual event.

Corollaries
-----------

**The Law of Complements** :math:`P(A) + P(A^C) = 1` 

Proof

By Complement Theorem 12 (Put Link), the union of complements is the sample space **S**.
        
    .. math::
        A \cup A^C = S

    .. math::
        \implies P(A \cup A^C) = P(S)

By Axiom 2, the probability of the entire sample space **S** is 1.
        
    .. math:: 
        \implies P(A \cup A^C) = 1

By Complement Theorem 13 (Put Link), the intersection of complements is the empty set.

    .. math::
        A \cap A^C = \varnothing

By Axiom 3, if the intersection of two sets is empty, the probability of their union is equal to the sum of the individual probabilities,

    .. math::
        A \cap A^C = \varnothing \implies P(A \cup A^C) = P(A) + P(A^C)

Therefore, putting the results together,

    .. math::
        P(A \cup A^C) = 1

    .. math::
        P(A \cup A^C) = P(A) + P(A^C)
        
    .. math::
        \implies P(A) + P(A^C) = 1
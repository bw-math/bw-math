============
Introduction
============

Probability is the study of the properties of random events.

Preliminaries
=============

Compound Union 
    A symbol that represents the union of a sequence of sets.

    .. math:: 
        \bigcup\limits_{i=1}^{n} A_{i} = A_1 \cup A_2 \cup ... \cup A_{n-1} \cup A_n 

Summation
    A symbol that represents the sum of the elements :sub:`i`\ *x*

    .. math::
        \sum_{i=0}^n x_i = x_1 + x_2 + ... x_{n-1} + x_n

Definitions
===========

.. _experiment:

Experiment
    An *uncertain* event.    

.. _mutual_exclusion:

Mutual Exclusivity
    :math:`A \cap B = \varnothing \implies` **A** and **B** are mutually exclusive. 
        Two sets, **A** and **B**, are *mutually exclusive* if they are disjoint.

.. _outcome:

Outcomes 
    :math:`x, y, z` (*lower case letters*)
        A possible way an experiment might occur.
    
.. _sample_space: 

Sample Space 
    :math:`S`
        The set of all possible outcomes for an experiment.

.. _event:

Events 
    :math:`A, B, C` (*upper-case letters*)

    :math:`A_1, A_2, A_3, ..., A_{n-1}, A_n` (*upper-case letters with subscripts*)
        
    A subset of the sample space, i.e. a set of outcomes. 

    :math:`A \subseteq S \implies` **A** is an event

Probability
    :math:`P(A)`
        A numerical measure of the *likelihood*, or *chance*, that event **A** occurs.

.. _sample_spaces:

Sample Spaces and Events
========================

The *sample space* for an experiment is the set of everything that could possibly happen.

Motivation
----------

.. note:: 
    By "*fair*", we mean the probability of either outcome, heads or tails, is *equally likely*.

Consider flipping a fair, two-sided coin. The only possible outcomes to this experiment are heads or tails. If we let *h* represent the outcome of a head for a single flip and *t* represent the outcome of a tail for a single flip, then the sample space is given by the set **S**,

.. math:: 
    S = \{ h, t \}

Events can be defined as :ref:`subsets` of the sample space. If we let **H** represent the event of a head and if we let **T** represent the event of a tail, then clearly,

.. math:: 
    H = \{ h \}
    
.. math:: 
    T = \{ t \}

Be careful not to confuse the outcome *h* with the event **H**, and likewise the outcome *t* with the event **T**. They have different, but related, meanings. The outcomes *h* and *t* are individual observables; they are physically measured by flipping a coin and observing on which side it lands. An event, on the other hand, is a :ref:`set <sets>`, and *sets* are abstract collections of individual. In this case, the sets are *singletons*, i.e. the sets **H** and **T** only contain one element each, which can lead to confusion. Let us extend this example further, to put a finer point on this subtlety.   

Consider now flipping the same fair, two-sided coin twice. A :ref:`tree diagram <tree_diagrams>` can help visualize the sample space for this experiment,

.. image:: ../../imgs/sample_space_coin_flip.png
    :width: 60%
    :align: center

The outcomes of the sample space are found by tracing each possible path of the :ref:`tree diagram <tree_diagrams>` and then collecting them into a set,

.. math::
    S = \{ hh, ht, th, tt \}

In this example, there is no simple correspondence between the events defined on the sample space and the outcomes within those events, as in the previous example. Take note, the sequence of outcomes *ht* is different than the sequence of outcomes *th*. In the first case, we get a head and *then* we get a tail. In the second case, we get a head and *then* we get a tail. Therefore, *ht* and *th* represent two different *outcomes* that correspond to the same *event*. Let us call that event the set **HT**. **HT** represents event of getting one head and one tail, regardless of order. Then, **HT** has exactly two outcomes (elements), for the reasons just discussed,

.. math:: 
    HT = \{ ht, th \}

Classical Definition of Probability
-----------------------------------

.. math:: 
    P(A) = \frac{n(A)}/{n(S)}

.. _axioms_of_probability:

Axioms of Probability
=====================

**Axiom 1**: :math:`P(A)>=A`
    All probabilities are positive; No probabilities are negative.

**Axiom 2**: :math:`P(S)=1`
    The probability of *some* outcome from the sample space **S** occuring is equal to 1.

**Axiom 3**: :math:`\forall i \neg j: A_i \cap A_j = \varnothing \implies P(\bigcup\limits_{i=1}^{n} A_i) = \sum_{i=1}^n P(A_i)`
    If each event :sub:`i` **A** in the sample space **S** is *mutually exclusive* with every other event :math:`\forall i \neg j: A_i`, then the probability of the union of all of these events is equal to the sum of the probabilities of each individual event.

Corollaries
===========

**The Law of Complements** :math:`P(A) + P(A^C) = 1` 

Example

.. warning::
    Proof

    By Complement Theorem 12 (Put Link), the union of complements is the sample space **S**. Therefore, the *probability* of the union is equal to the probability of the entire sample space **S**.
            
        .. math::
            A \cup A^C = S

        .. math::
            \implies P(A \cup A^C) = P(S)

    By Axiom 2, the probability of the entire sample space **S** is 1.
        
        .. math:: 
            \implies P(A \cup A^C) = 1

    By Complement Theorem 13 (Put Link), the intersection of complements is the empty set.
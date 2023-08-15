Conditional Probability
=======================

Motivation
----------

TODO 

Reduction of Sample Space
-------------------------

TODO

Multiplication Rule
-------------------

TODO 

The following example illustrates the simplification affected by the introduction of *conditional probability* into combinatorial problems. This example can be solved in one of two ways. The first solution uses the techniques from the :ref:`Combinatorics section<combinatorics>`. The second solution uses the techniques of the *Multiplication Rule* and *Reduction of the Sample Space* just discussed. The reader will observe, while both methods yield the same answer, the second method is substantially easier, both from a calculation perpsective and from a conceptual perspective (i.e., it's easier to understand).


Example
    Two cards are drawn without replacement from a standard deck of 52 playing cards. What is the probability both cards are red? 

.. collapse:: Solution 1: Combinatorics
    
    A hand of two cards dealt from a deck of 52 cards is equivalent to one of the combinations of 52 distinct objects taken 2 at a time. To find the total number of such combinations, :ref:`combination_formula` is used,

    .. math::
        C_2^{52} = \frac{52!}{2! \cdot 50!} = \frac{52 \cdot 51}{2} = 1326

    Therefore, there are a total of *1326* hands that can be dealt. 

    The same logic can be used to find the number of ways to pick two red cards. Note there are :math:`\frac{52}/{2}=26` red cards in a standard deck of playing cards. Therefore, the number of combinations of 26 distinct objects taken 2 at a time is,

    .. math::
        C_2^{26} = \frac{26!}{2! \cdot 24!} = \frac{26 \cdot 25}{2} = 325
    
    Therefore, the desired probability can be found using the :ref:`classical_definition`,

    .. math::
        P("two red cards") = \frac{325}{1326} \approx 0.2451

.. collapse:: Solution #2: Conditional Probability

    Let **R** :sub:`1` represent the event the first card drawn is red. Let **R** :sub:`2` represent the event the second card drawn is red. Then the event :math:`R_1 \cap R_2` represents the event the first card is red *and* the second card is red. The *Multiplication Rule* states the probability of an intersection can be expressed as,

    .. math::
        P(R_1 \cap R_2) = P(R_2 \mid R_1 ) \cdot P(R_1)

    The term :math:`P(R_1)` is the probability of selecting a red card on the first draw. This can be calculated easily with the :ref:`classical_definition`,
    
    .. math::
        P(R_1) = \frac{26}{52}

    The term :math:`P(R_2 \mid R_1)` can likewise be quickly decomposed by noticing the event **R** :sub:`1` *reduces the sample space* to *51* cards, *25* of which are red. Using the :ref:`classical_definition` once again, the conditional probability of **R** :sub:`2` given the occurrence of **R** :sub:`1` is,

    .. math::
        P(R_2 \mid R_1) = \frac{25}{51}

    Therefore, 

    .. math::
        P(R_1 \cap R_2) = \frac{26}{52} \cdot \frac{25}{51} = \frac{26 \cdot 25}{52 \cdot 51}

    .. math::
        P(R_1 \cap R_2) = \frac{650}{2652} \approx 0.2451

    
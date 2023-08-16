Conditional Probability
=======================

Motivation
----------

TODO 

.. _conditional_probability_formula:

Condtional Probability Formula
------------------------------

TODO 

.. math::
    P(A \mid B) = \frac{P(A \cap B)}{P(B)}

TODO

Reduction of Sample Space
-------------------------

Probability is merely a guess. It tells us the chance of some event occuring. If new information is given about the sample space that was unavailabiity when probabilities were initially assigned to the events of the sample space, then those probabilities must be updated to include this new information. Conditional probability is the tool by which new information is used to update our prior assumptions about the state of the world.

TODO 

Formula
*******

.. math::
    P(A \mid B) = \frac{n(A \mid B)}{n(S \mid B)}

The following example and its accompanying solutions serve to illustrate how conditional probability and the reduction of the sample space can be used to solve problems involving probability.

Example
    A fair, two-sided coin with heads and tails on either side is placed into a box alongside a double-sided coin that has heads on both sides. You select a coin at random from the box and, without looking at which coin you picked, flip it. If the coin lands on heads, what is the probability you selected the two sided coin?

.. collapse:: Solution #1

    Before solving the problem, first set up the :ref:`sample space <sample_space>` and define the events that correspond to its various outcomes. 

    Let :math:`h^{F}` denote the outcome of getting a head from the flip of the fair, two-sided coin. Let :math:`t^{F}` denote the outcome of getting a tail from the flip of the fair, two sided coin. Let :math:`h^{D}_1` denote the outcome of getting the first head from the flip of the double-sided coin. Finally, let :math:`h^{D}_2` denote the outcome of getting the second head from the flip of the double-sided coin. The sample space for this experiment is then given by the set **S**,

    .. math::
        S = \{ h^{F}, t^{F}, h^{D}_1, h^{D}_2 \}

    .. math::
        n(S) = 4 

    The event of selecting the fair coin, :math:`F`, is made up of the outcomes,

    .. math::
        F = \{ h^{F}, t^{F} \}

    .. math::
        n(F) = 2

    Likewise, the event of selecting the double-sided coin, :math:`D`, is made up of the outcomes,

    .. math:: 
        D = \{ h^{D}_1, h^{D}_2 \}
    
    .. math::
        n(D) = 2

    The event of getting a head, :math:`H`, is made up of the outcomes,

    .. math:: 
        H = \{ h^{F}, h^{D}_1, h^{D}_2 \}
    
    .. math::
        n(H) = 3

    The problem can then be expressed in terms of the :ref:`conditional_probability_formula`,

    .. math::
        P(D \mid H) = \frac{P(D \cap H)}{P(H)}

    The denominator of this expression can be found by straight-forward application of the :ref:`classical_definition`,

    .. math::
        P(H) = \frac{3}{4}

    Whereas the numerator first requires calculating the intersection of **D** and **H**,

    .. math::
        D \cap H = \{ h^{D}_1, h^{D}_2 \}

    .. math::
        n(D \cap H) = 2

    Whereupon the :ref:`classical_definition` can be applied again,

    .. math::
        P(D \cap H) = \frac{2}{4} = \frac{1}{2}

    The conditional probability of **D** given the occurrence of **H** is then calculated from the previously mentioned :ref:`conditional_probability_formula`,

    .. math::
        P(D \mid H) = \frac{\frac{1}{2}}{\frac{3}{4}} = \frac{1}{2} \cdot \frac{4}{3} = \frac{2}{3}

.. collapse:: Solution #2

    There is another way of looking at this problem. The fact that it is known the outcome of the coin flip was heads effectively *reduces* the sample space **S** from,

    .. math::
        S = \{ h^{F}, t^{F}, h^{D}_1, h^{D}_2 \}

    To a truncated set :math:S \mid H, the sample space *given the occurence of event* **H**, 

    .. math::
        S \mid H = \{ h^{F}, h^{D}_1, h^{D}_2 \}

    .. math::
        n(S \mid H) = 3

    In other words, the outcome of tails is removed as a possibility by the additional information a head has been obtained. Then, the event :math:`D` of selecting the two-sided coin conditioned on the event of getting a head remains,

    .. math::
        D \mid H= \{ h^{D}_1, h^{D}_2 \}
    
    .. math::
        n(D \mid H) = 2

    Therefore, by the *reduction of sample space* formula,

    .. math::
        P(D \mid H) = \frac{n(D \mid H)}{n(S \mid H)}

    .. math::
        P(D \mid H) = \frac{2}{3}

Monty Hall Problem
******************

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

    
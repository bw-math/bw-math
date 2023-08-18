.. _probability_introduction_classwork:

============
Introduction
============

Sample Spaces and Events
========================

1. Describe the sample spaces of the following experiments with a set using :ref:`list_notation`

    a. Flipping a two-sided coin three times
    b. Rolling a six-sided die
    c. Rolling two six-sided dice
    d. Flipping a two-sided coin and if it lands on heads rolling a six-sided die.

2. Two dice are rolled. Let **E** be the event the sum of the outcomes is odd. Let **F** be the event of at least one *1* appearing on one of the die. Describe the elements of the following evnets in :ref:`list_notation` and interpret the meaning of each event.

    a. :math:`E \cap F`
    b. :math:`E^C \cap F`
    c. :math:`E^C \cap F^C`
    d. :math:`E \cup F`
    e. :math:`E \cup F^C`

3. Three red balls and one green ball are placed into a box. Describe the samples of the following experiments with a set using *List Notation*.

    .. note:: 
        *Hint*: Let *r* :sub:`1`, *r* :sub:`2` and *r* :sub:`3` represent the *outcome* of drawing each of the respective red balls. 

    a. Selecting one ball at random.
    b. Selecting two balls at random and :ref:`with_replacement` (i.e. putting the ball you drew back into the back after you draw it).
    c. Selecting two balls at random and :ref:`without_replacement` (i.e. *not* putting the ball back after you draw it)

4. A deck of six cards consists of three black cards numbered *1*, *2*, *3* and three red cards numbered *1*, *2*, *3*. You draw two cards :ref:`without_replacement`. Let **A** be the event the second card has a larger number than the first card. Let **B** be the event the first card has a larger number than the second card.
   
    a. Are **A** and **B** mutually exclusive?
    b. Are **A** and **B** complements?

Applications
============

6. Let **S** be the sample space of flipping a fair, two-sided coin three times. LEt **A** be the event of at least two heads. Find :math:`P(A)`
   
7. You roll two dice. The find the probability of the following events. 
   
    a. The sum of the numbers rolled is 7.
    b. The sum of the numbers rolled on the dice is 3 or 5.
    c. The numbers rolled are both even. 
    d. One of the numbers rolled is even.
    e. Neither or the numbers rolled are even.
    f. Is part *e* the complement of part *c* or part *d*?

8. You have a standard deck of 52 playing cards. You shuffle the cards into a random order and deal yourself exactly one card. Find the probabilities of the following events,

    a. The card is a king.
    b. The card is a spade.
    c. The card is a king or spade.
    d. The card is a 4 or Jack.
    e. The card is black. 
    f. The card is black or a queen. 
    g. The card is neither nor a queen.

9. You select a number randomly between 1 and 1000. What is the probability the number selected is divisible by 5?

Probability Proofs
==================

10. Let **A** and **B** be two events, not necessarily mutually exclusive. Prove the following inequality

.. math:: 
    P(A \cap B) \geq P(A) + P(B) - 1

.. note:: 
    *Hint*: Use the :ref:`law_of_unions` and :ref:`axiom_1`

11. Let **A** and **B** be two events, not necessarily mutually exclusive. The event,
    
.. math:: 
    (A - B) \cap (B - A)

is called the *symmetric difference of* **A** *and* **B**. Prove the probability of the *symmetric difference of* **A** *and* **B** is equal to,

.. math:: 
    P(A) + P(B) - 2 \cdot P(A \cap B)

.. note:: 
    *Hint #1*: Draw a :ref:`Venn Diagram <venn_diagrams>` of **A** and **B**, assuming the events are *not* mutually exclusive. Label the area that correspodned to the *symmetric difference of* **A** *and* **B**. 

    *Hint #2*: Recall (TODO link) :math:`A - B = A \cap B^C`
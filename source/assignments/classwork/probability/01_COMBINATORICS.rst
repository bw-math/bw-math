.. _combinatorics_classwork:

=============
Combinatorics
=============

Counting
--------

1.

2.

3.

4.

5.

6.


TODO 

Probability
-----------

7. A bank PIN is selected at random from 4 digits.
   
   a. What is the probability all of the digits are the same?

   b. What is the probability no digits repeat?

   c. What is the probability the PIN starts with the number 7?

8. Let **S** be the sample space for flipping a fair, two-sided coin three times. Let **A** be the event of atleast one heads. Find :math:`P(A)`.

.. collapse:: Solution #8

    The word "*atleast*" is a red flag in problems involving probability. If you see the word "*atleast*", it is a fair bet you will need to find the complement of a set at some point. To see why, note the way this problem is phrase can be interpretted with the :ref:`square_of_opposition`. The *Square of Opposition* is pictured below for quick reference,

    .. image:: ../../assets/imgs/sets/square_of_opposition.jpg
        :align: center

    The *Square* tells us the complement of "*some are*" ("atleast one") is "*none are*". Therefore, we can express the probability this problem is seeking with the :ref:`law_of_complements`,

    .. math::

        P(A) = 1 - P(A^c)    
    
    Where :math:`A^c` corresponds to the event of getting *no heads*. 
    
    This is equivalent to getting all tails, which is a much simpler event to find, because it only has one outcome, namely ``ttt``. 

    To calculate the probability of this event, we apply the :ref:`counting_principle` to find the total number of ways the experiment can occur. Each flip has two outcomes, heads or tails. There are three flips in total. Thus,

    .. math::

        n(S) = 2 \cdot 2 \cdot 2 = 8

    The probability sought can then be calculated as,

    .. math::

        P(A) = 1 - \frac{1}{8} = \frac{7}{8}

2. A bag contains 4 red and 5 green balls. Two balls are drawn at random from the bag *with replacement*. 

    a. What is the probability all of them are red? 

    b. What is the probability exactly one of them is green?

    c. What is the probability of atleast one green ball? 

    d. Why does *part a + part c* equal 1?

.. hint:: 

    For part b, consider the outcomes,

        rg, gr 

    In both cases you would have exactly one green ball. 

.. hint:: 

    For part c, the event of getting two green balls is :ref:`mutually exclusive <mutual_exclusion>` with the event of getting exactly one green ball. 

3. A bag contains 4 red and 5 green balls. Two balls are drawn at random from the bag *without replacement*. 

    a. What is the probability all of them are red?

    b. What is the probability exactly one of them is red?

    c. What is the probability none of them are red?

    d. Why does *part a + part b + part c* equal 1?

4. **Lottery** In Maryland's state lottery, 48 balls numbered 1 through 48 are placed into a spinner and well mixed. Six of them are drawn at random, without replacement. There are three prizes awarded based on how many numbers a player is able to guess. 

    a. If the six numbers drawn match the numbers the player has chosen, the player wins the grand prize. Find the probability of winning the grand prize if a single lottery ticket is purchased.

    b. If five of the six numbers drawn match the numbers the player has chosen, the player wins the second place prize. Find the probability of winning the second place prize if a single lottery ticket is purchased.

    c. If four of the six numbers drawn match the numbers the player has chosen, the player wins the third place prize. Find the probability of winning the third place prize if a single lottery ticket is purchased.

    d. Find the probability of not winning the Maryland Lottery. 

.. hint:: 
    
    A player not winning is the complement of the event of the player winning the grand prize *or* the player winning the second place prize *or* the player winning the third place prize.

5. **The Birthday Problem**

    a. Suppose three people are in a room. What is the probability there is at least one shared birthday among these three people?

    b. Suppose ten people are in a room. What is the probability there is at least one shared birthday among these ten pople?

    c. Suppose thirty people are in a room. What is the probability there is at least one shared birthday among these thirty people?

    
6. **Five Card Poker** Find the probability of getting the following hands in 5-card poker. 

    a. Royal Flush. Recall a Royal Flush is a hand of cards all of the same suit given by the sequence of faces 10JQKA

    b. Straight Flush. Recall a Straight Flush is a hand of cards all of the same suit given by any sequential ordering of faces, e.q. 45678 or 78910J. Note: In five-card poker, a Royal Flush is *not* considered a Straight Flush. 

    c. Four of a Kind. Recall a Four of a Kind is a hand of cards where four cards all have the same face. 

    d. Full House. Recall a full house is a three of kind and a pair simultaneously. For example, Kings full of 8s is given by the sequence KKK88. 
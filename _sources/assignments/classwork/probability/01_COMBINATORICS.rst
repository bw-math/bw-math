.. _combinatorics_classwork:

=============
Combinatorics
=============

Counting Principle
==================

1. **A Matter of Outfits**

a. A man has 5 shirts and 3 ties. How many different outfits can he wear?

b. A woman has 5 blouses and 8 skirts. How many different outfits can she wear?
   
2. **Digits**

a. How many four-digit numbers can be formed using the digits *0, 1, 2, 3, 4, 5, 6, 7, 8* and *9* if the first digit cannot be a 0? Repeated digits are allowed.
	
b. How many five-digit numbers can be formed using the digits *0, 1, 2, 3, 4, 5, 6, 7, 8* and *9* if the first digit cannot be 0 or 1? Repeated digits are still allowed.

3. TODO

4. TODO

5. TODO

Permutations
============

1. **Definition**

a. Consider the set of objects,

.. math::

	\{ \text{Ry}, \text{Gage}, \text{Cora} \}
	
Use this set for the following problems.

	i. List all ordered arrangement these objects choosing 3 at a time without replacement. What is :math:`P^{3}_3`?
	
	ii. List all ordered arrangement these objects choosing 2 at a time without replacement. What is :math:`P^{3}_2`?

	iii. List all ordered arrangment of these objects choosing 1 at a time without replacement. What is math:`P^{3}_1`?

b. Consider the set of objects,

.. math::

	\{ \text{Rory}, \text{Lydia}, \text{Sejal}, \text{Rachael}, \text{Sophia} \}

Use this set for the following problems:

	i. List all ordered arrangement these objects choosing 5 at a time without replacement. What is :math:`P^{5}_5`?

	ii. List all ordered arrangment of these objects choosing 4 at a time without replacement. What is math:`P^{5}_4`?
	
	iii. List all ordered arrangement these objects choosing 3 at a time without replacement. What is :math:`P^{5}_3`?

	iv. List all ordered arrangment of these objects choosing 2 at a time without replacement. What is math:`P^{5}_2`?
	
	v. List all ordered arrangement these objects choosing 1 at a time without replacement. What is :math:`P^{5}_1`?
	
2. **Codes**

a. How many two-letter codes can be formed using the letters *A*, *B*, *C* and *D*? Repeated letters are allowed.

b. How many two-letter codes can be formed using the letters *A*, *B*, *C*, *D* and *E*? Repeated letters are allowed.

c. How many different three-letter codes are there if only the letters *A*, *B*, *C*, *D* and *E* can be used and no letter can be used more than once?

d. How many different four letter codes are there if only the letters *A*, *B*, *C*, *D*, *E* and *F* can be used and no letter can be used more than once?

3. **Words**


Combinations
============

1. **Definition**

a. Consider the set of objects,

.. math::

	\{ \text{Ry}, \text{Gage}, \text{Cora} \}
	
Use this set for the following problems.

	i. List all combinations of these objets taken 3 at a time.What is :math:`C^{3}_3`?
	
	ii. List all combinations of these objets taken 2 at a time. What is :math:`C^{3}_2`?

	iii. List all combinations of these objets taken 1 at a time. What is math:`C^{3}_1`?

b. Consider the set of objects,

.. math::

	\{ \text{Rory}, \text{Lydia}, \text{Sejal}, \text{Rachael}, \text{Sophia} \}

Use this set for the following problems:

	i. List all combinations of these objets taken 5 at a time. What is :math:`C^{5}_5`?

	ii. List all combinations of these objets taken 4 at a time. What is math:`C^{5}_4`?
	
	iii. List all combinations of these objets taken 3 at a time.What is :math:`C^{5}_3`?

	iv. List all combinations of these objets taken 2 at a time. What is math:`C^{5}_2`?
	
	v. List all combinations of these objets taken 1 at a time. What is :math:`C^{5}_1`?

2. **Committees**

a. In how many ways can a committee of 4 students be formed from a pool of 7 students?

b. In how many ways can a committee of 3 professors be formed from a department having 8 professors?

c. A student dance committee is to be formed consisting of 2 boys and 3 girls. If the memberships is be chosen from 4 boys and 8 girls, how many different committees are possible?

d. The student relations committee of a college consists of 2 administrators, 3 faculty members and 5 students. Four administrators, 8 faculty members and 20 students are eligible to serve. How many different committees are possible?

3. **Selecting Objects**

a. An urn contains 7 white balls and 3 red balls. Three balls are selected. In how many ways can the 3 balls be drawn from the total of 10 balls in each of the following cases:

	i. If 2 balls are white and 1 is red?
	
	ii. If all 3 balls are white?
	
	iii. If all 3 balls are red?
	
b. An urn contains 165 red balls and 10 white balls. Five balls are selected. In how many ways can the 5 balls be drawn from the total of 25 balls in each of the following cases:

	i. If all 5 balls are red?
	
	ii. If 3 balls are red and two balls are white?
	
	iii. If atleast 4 are red balls?
	
Probability
===========

1. A bank PIN is selected at random from 4 digits.
   
   a. What is the probability all of the digits are the same?

   b. What is the probability no digits repeat?

   c. What is the probability the PIN starts with the number 7?

2. Consider the experiment of flipping a fair, two-sided coin three times. Let **A** be the event of atleast one heads. Find :math:`P(A)`.

3. A bag contains 4 red and 5 green balls. Two balls are drawn at random from the bag *with replacement*. 

    a. What is the probability all of them are red? 

    b. What is the probability exactly one of them is green?

    c. What is the probability of atleast one green ball? 

    d. Why does *part a + part c* equal 1?

.. hint:: 

    For part b, consider the outcomes,

        rg, gr 

    In both cases you would have exactly one green ball, but each sequence would correspond to a different order of outcomes.

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

A.P. Exam Practice
==================

1. **2014, Free Response, #2**

Nine sales representatives, 6 men and 3 women, at a small company wanted to attend a national convention. There were only enough travel funds to send 3 people. The manager selected 3 people to attend and stated that the people were selected at random. The 3 people selected were women. There were concerns that no men were selected to attend the convention.

a. Calculate the probability that randomly selecting 3 people from a group of 6 men and 3 women will result in selecting 3 women.

b.  Based on your answer to part *#a*, is there reason to doubt the manager's claim that the 3 people were selected at random? Explain.

c. An alternative to calculating the exact probability is to conduct a simulation to estimate the probability. A proposed simulation process is described below.

    Each trial in the simulation consists of rolling three fair, six-sided dice, one die for each of the convention attendees. For each die, rolling a 1, 2, 3, or 4 represents selecting a man; rolling a 5 or 6 represents selecting a woman. After 1,000 trials, the number of times the dice indicate selecting 3 women is recorded.

Does the proposed process correctly simulate the random selection of 3 women from a group of 9 people consisting of 6 men and 3 women? Explain why or why not.

2. **2018, Free Response, #3**

Approximately 3.5 percent of all children born in a certain region are from multiple births (that is, twins, triplets, etc.). Of the children born in the region who are from multiple births, 22 percent are left-handed. Of the children
born in the region who are from single births, 11 percent are left-handed.

a. What is the probability that a randomly selected child born in the region is left-handed?

b. A random sample of 20 children born in the region will be selected. What is the probability that the sample will have at least 3 children who are left-handed?

Solutions
=========

Probability
-----------

2. The word "*atleast*" is a red flag in problems involving probability. If you see the word "*atleast*", it is a fair bet you will need to find the complement of a set at some point. To see why, note the way this problem is phrase can be interpretted with the :ref:`square_of_opposition`. The *Square of Opposition* is pictured below for quick reference,

.. image:: ../../../assets/imgs/sets/square_of_opposition.jpg
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

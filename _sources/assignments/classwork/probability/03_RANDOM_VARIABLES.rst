.. _random_variable_classwork:

================
Random Variables
================

Definition
==========

1. A random variable :math:`\mathcal{X}` is defined as the number of heads in three coin flips.

	a. List the elements of the sample space for this random variable.

	b. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=0` in set notation.

	c. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=1` in set notation.

	d. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=2` in set notation.

	e. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=3` in set notation.

	f. Find the probability distribution :math:`P(\mathcal{X}=x)` for all values of *x*. 

	g. Using the probability distribution derived in *part e*, find the expectation :math:`E(\mathcal{X})` of the sum of two die rolls.

	h. Using the probability distribution derived in *part e*, find the variance :math:`Var(\mathcal{X})` of the sum of two die rolls. 

	
2. A random variable :math:`\mathcal{X}` is defined as the sum of two six-sided die rolls. 

	a. List the elements of the sample space for this random variable.

	b. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=6` in set notation.

	c. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=7` in set notation.

	d. Write the elements of the sample space that belong to the event :math:`\mathcal{X}=8` in set notation.

	e. Find the probability distribution :math:`P(\mathcal{X}=x)` for all values of *x*.

	f. Using the probability distribution derived in *part e*, find the expectation :math:`E(\mathcal{X})` of the sum of two die rolls.

	g. Using the probability distribution derived in *part e*, find the variance :math:`Var(\mathcal{X})` of the sum of two die rolls. 

Examples
========

1. TODO

2. TODO 
 
Theorems
========

.. topic:: Linearity of Expectations

	Suppose :math:`\mathcal{Y}` and :math:`\mathcal{Z}` are random variables, not necessarily independent. If :math:`\mathcal{X} = \mathcal{Y} + \mathcal{Z}`, then
	
	.. math::
	
		E(\mathcal{X}) = E(\mathcal{Y}) + E(\mathcal{Z})
		
1. Use the linearity of expectations to solve the following problems.

	a. What is the expected number of heads in three coin flips?
	
	b. What is the expected sum of outcomes for two die rolls?
	
2. Clavius Hecklesnotz is playing a game of chance where he flips 10 fair coins. If Clavius Hecklesnotz gets 1 head, he will be paid $1. If Clavius Hecklesnotz gets 2 heads, he will be paid $2. In general, if Clavius Hecklesnotz gets *n* heads, he will be paid $*n*. What is the expected value of Clavius Hecklesnotz' payout? 

.. hint::

	This problem can be solved with a :ref:`binomial_distribution`, but it is much easier to understand through the :ref:`linearity_of_expectations`.
	
3. A box contains a yellow ball, an orange ball, a green ball, and a blue ball. Matilda Weierstrauss randomly selects 4 balls from the box (with replacement). What is the expected value for the number of distinct colored balls Matilda Weierstrauss will select?

4. Every time one of the AP Statistics students buys a Happy Meal from McDonalds, they receive a :ref:`Strawberry Shortcake <https://en.wikipedia.org/wiki/Strawberry_Shortcake>`_ plush doll. There are five dolls in total: Strawberry Shortcake, Cherry Jam, Raspberry Torte, Blueberry Muffin and Lemon Meringue. The toys in every Happy Meal are awarded at random. What is the expected number of Happy Meals an AP Statistics Students must buy in order to get all the *Strawberry Shortcake* plush dolls?

A.P. Exam Practice
==================

3. **2019, Free Response, #5**

A company that manufactures smartphones developed a new battery that has a longer life span than that of a traditional battery. From the date of purchase of a smartphone, the distribution of the life span of the new battery is approximately normal with mean 30 months and standard deviation 8 months. For the price of $50, the company offers a two-year warranty on the new battery for customers who purchase a smartphone. The warranty guarantees that the smartphone will be replaced at no cost to the customer if the battery no longer works within 24 months from the date of purchase.

a. In how many months from the date of purchase is it expected that 25 percent of the batteries will no longer work? Justify your answer.

b. Suppose one customer who purchases the warranty is selected at random. What is the probability that the customer selected will require a replacement within 24 months from the date of purchase because the battery no longer works?

c. The company has a gain of $50 for each customer who purchases a warranty but does not require a replacement. The company has a loss (negative gain) of $150 for each customer who purchases a warranty and does require a replacement. What is the expected value of the gain for the company for each warranty purchased?


2. **2015, Free Response, #3**

A shopping mall has three automated teller machines (ATMs). Because the machines receive heavy use, they sometimes stop working and need to be repaired. Let the random variable X represent the number of ATMs that are working when the mall opens on a randomly selected day. The table shows the probability distribution of X. Number of ATMs working when 

.. image:: ../../../assets/imgs/classwork/2015_apstats_frp_3.png
    :align: center

a. What is the probability that at least one ATM is working when the mall opens?

b. What is the expected value of the number of ATMs that are working when the mall opens?

c. What is the probability that all three ATMs are working when the mall opens, given that at least one ATM is working?

d. Given that at least one ATM is working when the mall opens, would the expected value of the number of ATMs that are working be less than, equal to, or greater than the expected value from part *b*? Explain.

3. **2014, Free Response, #3**

Schools in a certain state receive funding based on the number of students who attend the school. To determine the number of students who attend a school, one school day is selected at random and the number of students in attendance that day is counted and used for funding purposes. The daily number of absences at High School A in the state is approximately normally distributed with mean of 120 students and
standard deviation of 10.5 students.

a. If more than 140 students are absent on the day the attendance count is taken for funding purposes, the school will lose some of its state funding in the subsequent year. Approximately what is the probability that High School A will lose some state funding?

b. The principals’ association in the state suggests that instead of choosing one day at random, the state should choose 3 days at random. With the suggested plan, High School A would lose some of its state funding in the subsequent year if the mean number of students absent for the 3 days is greater than 140. Would High School A be more likely, less likely, or equally likely to lose funding using the suggested plan compared to the plan described in *part a*? Justify your choice.

c. A typical school week consists of the days Monday, Tuesday, Wednesday, Thursday, and Friday. The principal at High School A believes that the number of absences tends to be greater on Mondays and Fridays, and there is concern that the school will lose state funding if the attendance count occurs on a Monday or Friday. If one school day is chosen at random from each of 3 typical school weeks, what is the probability that none of the 3 days chosen is a Tuesday, Wednesday, or Thursday?

4. **2019, Free Response, #5**

A company that manufactures smartphones developed a new battery that has a longer life span than that of a traditional battery. From the date of purchase of a smartphone, the distribution of the life span of the new battery is approximately normal with mean 30 months and standard deviation 8 months. For the price of $50, the company offers a two-year warranty on the new battery for customers who purchase a smartphone. The warranty guarantees that the smartphone will be replaced at no cost to the customer if the battery no longer works within 24 months from the date of purchase.

a. In how many months from the date of purchase is it expected that 25 percent of the batteries will no longer work? Justify your answer.

b. Suppose one customer who purchases the warranty is selected at random. What is the probability that the customer selected will require a replacement within 24 months from the date of purchase because the battery no longer works?

c. The company has a gain of $50 for each customer who purchases a warranty but does not require a replacement. The company has a loss (negative gain) of $150 for each customer who purchases a warranty and does require a replacement. What is the expected value of the gain for the company for each warranty purchased?

5. **2003, Free Response Form B, #5**

TODO

6. **2005, Free Response Form B, #2**

TODO

7. **2008, Free Response Form B, #5**

TODO

8. **2008, Free Response, #3**

A local arcade is hosting a tournament in which contestants play an arcade game with possible scores ranging from 0 to 20. The arcade has set up multiple game tables so that all contestants can play the game at the same time; thus contestant scores are independent. Each contestant’s score will be recorded as he or she finishes, and the contestant with the highest score is the winner.

After practicing the game many times, Josephine, one of the contestants, has established the probability distribution of her scores, shown in the table below.

.. topic:: Josephine's Distribution

	+-------------+------+------+------+------+
	| Score       | 16   | 17   | 18   | 19   |
 	+-------------+------+------+------+------+
 	| Probability | 0.10 | 0.30 | 0.40 | 0.20 |
 	+-------------+------+------+------+------+
 	
Crystal, another contestant, has also practiced many times. The probability distribution for her scores is shown in the table below.

.. topic:: Crystal's Distribution

	+-------------+------+------+------+
	| Score       | 17   | 18   | 19   |
 	+-------------+------+------+------+
 	| Probability | 0.45 | 0.40 | 0.15 |
 	+-------------+------+------+------+
 	
a. Calculate the expected score for each player.

b. Suppose that Josephine scores 16 and Crystal scores 17. The difference (Josephine minus Crystal) of their scores is -1. List all combinations of possible scores for Josephine and Crystal that will produce a difference (Josephine minus Crystal) of -1, and calculate the probability for each combination.

c. Find the probability that the difference (Josephine minus Crystal) in their scores is -1.

d. The table below lists all the possible differences in the scores between Josephine and Crystal and some associated probabilities.


.. topic:: Distribution (Josephine minus Crystal)

	+-------------+-------+--------+--------+--------+-------+-------+
	| Difference  | -3    | -2     | -1     | 0      | 1     | 2     | 
	+-------------+-------+--------+--------+--------+-------+-------+
	| Probability | 0.015 |   ?    |   ?    | 0.325  | 0.260 | 0.090 |
	+-------------+-------+--------+--------+--------+-------+-------+
	
Complete the table and calculate the probability that Crystal’s score will be higher than Josephine’s score.

9. **2010, Free Response Form B, #3**

A test consisting of 25 multiple-choice questions with 5 answer choices for each question is administered. For each question, there is only 1 correct answer.

a. Let :math:`\mathcal{X}` be the number of correct answers if a student guesses randomly from the 5 choices for each of the 25 questions. What is the probability distribution of :math:`\mathcal{X}`?

This test, like many multiple-choice tests, is scored using a penalty for guessing. The test score is determined
by awarding 1 point for each question answered correctly, deducting 0.25 point for each question answered
incorrectly, and ignoring any question that is omitted. That is, the test score is calculated using the following
formula.

	Score = (1 x number of correct answers) – (0.25 x number of incorrect answers) + (0 x number of omits)

For example, the score for a student who answers 17 questions correctly, answers 3 questions incorrectly, and omits 5 questions is

	Score = (1 x 17) - (0.25 x 3) + (0 x 5) = 16.25.
	
b. Suppose a student knows the correct answers for 18 questions, answers those 18 questions correctly, and chooses randomly from the 5 choices for each of the other 7 questions. Show that the expected value of the student’s score is 18 when using the scoring formula above.

c. A score of at least 20 is needed to pass the test. Suppose a student knows the correct answers for 18 questions, answers those 18 questions correctly, and chooses randomly from the 5 choices for each of the other 7 questions. What is the probability that the student will pass the test?

10. **2012, Free Response, #2**

A charity fundraiser has a Spin the Pointer game that uses a spinner like the one illustrated in the figure below.

.. image:: ../../../assets/imgs/classwork/2012_apstats_frp_02.png
    :align: center

A donation of $2 is required to play the game. For each $2 donation, a player spins the pointer once and receives the amount of money indicated in the sector where the pointer lands on the wheel. The spinner has an equal probability of landing in each of the 10 sectors.

a. Let X represent the net contribution to the charity when one person plays the game once. Complete the table for the probability distribution of X.

+--------------+----+----+-----+
|   x          | $2 | $1 | -$8 |
+--------------+----+----+-----+
| :math:`P(x)` |    |    |     |
+--------------+----+----+-----+

b. What is the expected value of the net contribution to the charity for one play of the game?

c. The charity would like to receive a net contribution of $500 from this game. What is the fewest number of times the game must be played for the expected value of the net contribution to be at least $500 ?

d. Based on last year’s event, the charity anticipates that the Spin the Pointer game will be played 1,000 times. The charity would like to know the probability of obtaining a net contribution of at least $500 in 1,000 plays of the game. The mean and standard deviation of the net contribution to the charity in 1,000 plays of the game are $700 and $92.79, respectively. Use the normal distribution to approximate the probability that the charity would obtain a net contribution of at least $500 in 1,000 plays of the game.


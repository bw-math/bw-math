.. _geometric_distribution_classwork:

======================
Geometric Distribution 
======================

1. **Conditions**

.. topic:: Conditions for Geometric Random Variable

	1. The trials must be independent.
	
	2. Each trial must be either a success or failure.
	
	3. The probability of each trial must be the same across trials.

Determine whether each of the following experiments satisfy the conditions for a Geometric Random Variable.

	a. A basketball player takes shots from the foul line and the number of shots is counted until he misses a basket. 
	
	b. The number of cards drawn from a standard deck of 52 cards *without* replacement is counted until a Queen is drawn. 
	
	c. The number of cards drawn from a standard deck of 52 cards *with* replacement is counted until a Queen is drawn.
	
	d. You count the number of random people you have to survey before someone says *Yes* to the question, "Have you seen the science faction magnum opus from film autuer Ridley Scott, *Blade Runner*?"
	
	e. Suppose two chess players keep playing until one of them wins three games in a row. You count the number of games they have to play until the match is over.
	
2. **Density**

.. topic:: Geometric Probability Density
	
	.. math::

		P(\mathcal{X}=x) = (1-p)^{x-1} \cdot p

Use the Geometric Probability Density Function to answer the following questions.

	a. If :math:`p=0.1`, what is :math:`P(\mathcal{X}=1)`?
	
	b. If :math:`p=0.1`, what is :math:`P(\mathcal{X}=10)`?
	
	c. If :math:`p=0.9`, what is :math:`P(\mathcal{X}=1)`?
	
	d. If :math:`p=0.9`, what is :math:`P(\mathcal{X}=10)`?
	
	e. Write a few sentences in plain English that explains how changing the parameter *p* of the Geometric Distribution affects the probability of its outcomes.

3. **Histogram**

Let the probability of success for a Geometric Random Variable be :math:`p = 0.3`. Create a probability distribution (i.e. a table) for :math:`\mathcal{X}=0,1,2,...,10`. Use this table to create and label histogram. Describe the distribution of a Geometric Random Variable wth :math:`p = 0.3`. 

4. **Probability**

Use the properties of probability and the Geometric Distribution to solve the following problems.

	a. From an ordinary deck of 52 cards, you draw cards at random and with replacement, until the first ace is drawn. what is the probability that atleast five draws are needed?

	
	b. A certain basketball player makes a foul shot 45% of the time. Suppose this player stands on the foul line and continues shooting until he makes two baskets. What is the probability that (i) the first basket occurs on the sixth shot? (ii) the first and second baskets occur on the fourth and eighth shots, respectively?
	
	c. The probability is 0.8 that Marty hits target *M* when he fires at it. The probability is 0.45 that Alvie hits target *A* when he fires at it. Marty and Alvie fire one shot each at their targets. If both of them hit their targets, they stop; otherwise, they will continue. What is the probability that they stop after 3 tries? 

	
5. **Expectations**

Solve the following problems.

	a. Refer to *#4a*. What is the expected value for the number of cards drawn before an ace is drawn?
	
	b. Refer to *#4b*. How many shots on average will it take the basketball player before the shot goes in? 
	
	c. Refer to *#4c*. What is the expected number of times Marty and Alvie fire before stopping?
A.P. Exam Practice
==================

1. **2016, Free Response, #4**

A company manufactures model rockets that require igniters to launch. Once an igniter is used to launch a rocket, the igniter cannot be reused. Sometimes an igniter fails to operate correctly, and the rocket does not launch. The company estimates that the overall failure rate, defined as the percent of all igniters that fail to operate correctly, is 15 percent.

A company engineer develops a new igniter, called the super igniter, with the intent of lowering the failure rate.

To test the performance of the super igniters, the engineer uses the following process.

    Step 1: One super igniter is selected at random and used in a rocket.
    
    Step 2: If the rocket launches, another super igniter is selected at random and used in a rocket.

Step 2 is repeated until the process stops. The process stops when a super igniter fails to operate correctly or 32 super igniters have successfully launched rockets, whichever comes first. Assume that super igniter failures are independent.

	a. If the failure rate of the super igniters is 15 percent, what is the probability that the first 30 super igniters selected using the testing process successfully launch rockets?

	b. Given that the first 30 super igniters successfully launch rockets, what is the probability that the first failure occurs on the thirty-first or the thirty-second super igniter tested if the failure rate of the super igniters is 15 percent?

	c. Given that the first 30 super igniters successfully launch rockets, is it reasonable to believe that the failure rate of the super igniters is less than 15 percent? Explain.

2. **2011, Free Response, #3**

.. warning::

	The problem requires more than the Geometric Distribution to solve.
	
An airline claims that there is a 0.10 probability that a coach-class ticket holder who flies frequently will be upgraded to first class on any flight. This outcome is independent from flight to flight. Sam is a frequent flier who always purchases coach-class tickets.

	a. What is the probability that Sam’s first upgrade will occur after the third flight?

	b. What is the probability that Sam will be upgraded exactly 2 times in his next 20 flights?

	c. Sam will take 104 flights next year. Would you be surprised if Sam receives more than 20 upgrades to first class during the year? Justify your answer.

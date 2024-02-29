.. _simulation_activities:

===========
Simulations
===========

No statistician's tool belt is complete without an absurd number of Rubber Ducks! Rubber Ducks provide countless opportunities for statistics and probability demonstrations! 

.. topic:: Required Materials
	
	- Dice (6-sided, 12-sided, 24-sided, etc.)
	- Coins
	- Calculators
	- Tables of Random Digits
	- Skittles	
	
Skittles
========

TODO: explain

Foul Shot
=========

TODO: explain

Coin Flips
==========

Binomial
--------

TODO: explain

Geometric
---------

The following two demonstrations should be performed one after another. This will allow the students to see the differences in the two dot plots.

Coin Flip
*********

In this demonstrations, students will be flipping a coin and counting the number of flips it takes until they get their first head. A *success* in this experiment corresponds to the outcome of the coin landing on heads.

.. admonition:: Discussion Question

	What is the probability of success in this Geometric experiment?
	
1. Draw a dot plot on the board, as shown below. Note the horizontal axis should extend to 10 or more, to account for extreme outcomes.

(TODO: insert graph) 

2. Give each student a coin. 

3. Have each student flip the coin, counting the number of flips as they go. When it lands on heads the first time, the experiment is over. 

4. For each experiment they perform, have each student add a dot to the dot plot. The dot should be placed at the number corresponding to the total number of flips in the experiment. 

5. Repeat the process until the dot plot has 30 or more data points. 

6. Once the dot plot is constructed, have the students create a relative frequency distribution.

.. admonition:: Discussion Question

	How is the sample mean of the distribution related to the probability of success?

Die Roll
********

In this demonstrations, students will be rolling a die and counting the number of rolls it takes until they get their first 5. A *success* in this experiment corresponds to the outcome of rolling a 5.

.. admonition:: Discussion Question

	What is the probability of success in this Geometric experiment?
	
1. Draw a dot plots on the board, as shown below. Note the horizontal axis should extend to 20 or more, to account for extreme outcomes.

(TODO: insert graph) 

2. Give each student a six-sided die. 

3. Have each student flip the coin, counting the number of flips as they go. When it lands on heads the first time, the experiment is over. 

4. For each experiment they perform, have each student add a dot to the dot plot. The dot should be placed at the number corresponding to the total number of flips in the experiment. 

5. Repeat the process until the dot plot has 30 or more data points. 

6. After the dot plot is constructed, have the students create a relative frequency distribution.

.. admonition:: Discussion Question

	How is the sample mean of the distribution related to the probability of success?
	
Analysis
********

Have the students answer the following questions.

1. Compare and contrast the distribution of coin flips with the distribution of die rolls. How do measures of center compare? How do measures of variation of compare? 

2. Based on the answer to #1, what is the relationship between the probabiltiy of success, :math:`p`, and the standard deviation, :math:`\sigma`, of the distribution?

.. topic:: Geometric Expectation and Variance

	If :math:`\mathcal{X} \mid \text{Geom}(p)`, then,
	
	.. math::
	
		E(\mathcal{X}) = \frac{1}{p}
		
	.. math::
	
		Var(\mathcal{X}) = \frac{1-p}{p^2}
		
3. Using a graphing utility, plot the variance of a Geometric distribution as function of the probability of success, :math:`f(x)=\frac{1-x}{x^2}. Ensure the graping window is set to :math:`0 \leq x \leq 1` and :math:`0 \leq y \leq 100`.

	a. Why is it necessary to set the view window to :math:`0 \leq x \leq 1`? 
	
	b. What happens to the variance as the probability of success approaches 1? Interpret this result in context.
	
	c. What happens to the variance as the probability of success approaches 0? Interpret this result in context.

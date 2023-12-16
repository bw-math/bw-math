.. _project_six:

==========
Simulation
==========

.. epigraph:: 
	Your mind makes it real.

	-- Morpheus, The Matrix

**Python** allows us to simulate experiments that would otherwise be tedious to perform. In this lab, we will explore a few techniques for conducting *simulations* to model outcomes.

Instructions
============

1. Create a Python ``.py`` script named ``LASTNAME_FIRSTNAME_project_six.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``LASTNAME`` and ``FIRSTNAME`` with your last and first name, respectively.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_six_background` section.
6. Perform all exercises and answer all questions in the :ref:`project_six_project` section. Label your script with comments where appropriate.
7. When you are done, zip your script in a zip file named ``LASTNAME_FIRSTNAME_project_six.zip``
8. Upload the zip file to the Google Classroom Project Six Assignment.


.. _project_six_background:

Background
==========

Loops
-----

TODO: EXPLAIN LOOPS

Law of Large Numbers
--------------------

Definition
**********

Consider the experiment of flipping a fair coin ten times. We intuitively understand that, if the coin is truly fair, we should get an approximately even amount of heads and tails. However, the chances of getting exactly five heads and exactly five tails in one sequence of ten coin flips is incredibly small. Since each flip of the coin is :ref:`independent <independence>` of the previous coin flip, the fact we get a head on the first flip in no way influences the probability of getting a head on the second flip. The second coin flip has no responsibility to come out as tails if the first flip was heads.

The *Law of Large Numbers* gives a tool for understanding this result. First, we take the experiment of flipping a fair coin ten times and perform this experiment itself a large number of times, let us say 100 times. For each experiment of ten coin flips, we count the number of heads and the number of tails. If we then take the result of each repetition of the experiment and average them all together, the average value will be close to the true value. The more times we repeat the experiment, i.e. the more samples we create to pool into the average value, the closer and closer the overall average becomes. In the limit, as the number of repetitions becomes infinite, the average value of the experiment equals its true value. In other words, if we replicate our experiment enough times, the average result will approximate its true value. In this case, we should observe, after a large number of repetitions, the approximate proportion of heads to be 50% and the approximate proportion of tails to be 50%.

Python
******

Using :ref:`python_control_structures` and a few `python_builtin_functions`, we can simulate experiments involving uncertainty and see the *Law of Large Numbers* in action. The key idea is using random numbers to represent random draws from a population. If we think of a random number between 0 and 1 as an observation, then we can use logic to construct the experiment. 

For example, let the event of getting a random number less than 0.5 correspond to the event of getting heads in a coin flip. Let the event of getting number between 0.5 and 1 correspond to the event of getting a tail. Then, by simulating random numbers between 0 and 1 and interpretting the results as outcomes of flipping a coin, we can derive a 

The following code snippet simulates flipping a fair coin 10 times,

.. code:: python

	import random

	# simulation parameters
	no_simulations = 100
	no_coins = 10
	coin_prob = 0.5

	# simulation loop
	for i in range(no_simulations):
	    	# resetting simulation variables
		sim_heads = 0
		sim_tails = 0
		
		# start simulation
		for j in range(no_coins):
		
			# simulating a single coin flip
			flip = random.random()

			if flip >= coin_prob:
				sim_heads += 1
			else:
				sim_tails += 1 
		# end simulation
				
		print("simulation #", i)
		print("\t number of heads: ", sim_heads)
		print("\t number of tails: ", sim_tails)
		
		head_dist.append(sim_heads)
		tail_dist.append(sim_tails) 
	
	# do stuff with head_dist and tail_dist...

.. _project_six_project:

Project
=======

1. Using the :ref:`randint() function <python_random_function>` and :ref:`conditional control structure <python_control_structures>`, simulate drawing 10 random **integers** between 0 and 12. Perform the simulation 200 times. Save the results of each simulation in a :ref:`python_lists` variable. 

a. Plot the results using a histogram. Label the 

b. Describe the distribution. What value is the distribution centered around? What shape does the distribution have?

c. What would happen to the distribution if you increased the number of coins being flipped? 

.. hint::

	Test it out yourself by changing the number of coins!

d. What would happen to the shape of the distribution if you increased the number of simulations being performed? 
    
.. hint::

	Test it out yourself by changing the number of simulations!

TODO: keep editing

2. Using the :ref:`rand() function <python_random_function>`, simulate 100 random **floats** between 0 and 1.
    - What do you expect the shape of the distribution to be? 
    - Using five classes, plot the results using a histogram. Save the image and add it to your report. 
    - What are the class width and boundaries?
    - Comment on the shape of the distribution. Is the result consistent with what you expected? Explain any discrepancies.

3. Using a :ref:`conditional control structure <python_control_structures>`, simulate 10 flips of a fair coin. 
    - What do you expect the shape of the distribution to be? 
    - Plot the results using a histogram. Save the image and add it to your report.
    - Comment on the shape of the distribution. Is the result consistent with what you expected? Explain any discrepancies. 
    - Based on your simulation, what is the approximate probability of observing more than 8 heads in 10 flips of a fair coin?

4. Using a :ref:`conditional control structure <python_control_structures>`, simulate 10 flips of an **unfair** coin. Assume the probability of a head is 0.75. 
    - What do you expect the shape of the distribution to be? 
    - Plot the results using a histogram. Save the image and add it to your report.
    - Describe the shape of the distribution. What is value is the distribution centered around? Is the result consistent with what you expect? Explain any discrepancies. How does the result compare to simulation involving a fair coin?
    - Based on your simulation, what is the probability of observing less than 5 heads in 10 flips of an unfair coin? 

5. Using a :ref:`conditional control structure <python_control_structures>`, simulate 10 rolls of a six-sided die. Plot the results using a histogram. 
    - What do you expect the shape of the distribution to be? 
    - Plot the results using a histogram. Save the image and add it to your report.
    - Comment on the shape of the distribution. What is value is the distribution centered around? Is the result consistent with what you expect? Explain any discrepancies. 


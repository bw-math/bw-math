.. _project_three:

=========
Normality
=========

	All models are wrong, but some are useful.
	
	- George Box

*Normality* is an important phenomenon because of its far-reaching power. The concept of *normality* will allows us to draw *statistical inferences*. In this project, we will learn how to perform :ref:`normal_calculations` using **Python**. Using these techniques, we will compare theoretically determined population parameters to empirically determined sample statistics in order to see how the Normal Distribution is used to model populations. 

Instructions
============

1. Download **all three** *csv* datasets in the :ref:`project_three_dataset` section and place them in the ``Linux Files`` folder on your file system where you save your ``.py`` scripts.
2. Create a Python ``.py`` script named ``NAME_project_three.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``AME`` with your name.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_three_background` section.
5. Load in the data from the ``.csv`` files using the technique outlined in the :ref:`project_three_loading_data` section.
6. Perform all exercises and answer all questions in the :ref:`project_three_project` section. Label your script with comments as indicated in the instructions of each problem.
7. When you are done, zip your script **and** the *csv* file in a zip file named ``NAME_project_three.zip``
8. Upload the zip file to the Google Classroom Project Four Assignment.

.. _project_three_background:

Background 
==========

Normality arises when observations being randomly drawn from a population are *independent* and *identically distributed*. In other words, if a series of experiments are performed where each experiment is the same as the last in every respect, then the outcomes of all the experiments taken together should be approximately normal. 

.. hint::

	Recall our die roll experiment from class. The underlying population distribution was uniform (each face of the die is an *equally likely* outcome), but when the outcomes of each independent die roll were summed together, the resulting distribution became normal. 

A departure from normality can suggest several things: 

1. The selection process was not random.
2. The observations are not *independent*.
3. The observations are not being drawn from the exact same population.

Normal Distribution
-------------------

A Normal Distribution is *parameterized* by its mean, :math:`\mu`, and its standard deviation, :math:`\sigma`. If a single observation is being drawn from this Normal Distribution, we write,

.. math::

	\mathcal{X} \sim \mathcal{N}(\mu, \sigma)

Recall a sample of data can be :ref:`transformed <data_transformations>` by applying algebraic operations to each observations. For instance, we can :ref:`standardize <z_score>` each observation :math:`X` into a *z-score* by subtracting the mean of the distribution and dividing by the standard deviation of the distribution,

.. math::

	\mathcal{Z} = \frac{\mathcal{X} - \mu}{\sigma}


.. _project_three_loading_data:

Loading In Data
===============

The following code snippet will load in a *CSV* spreadsheet named ``example.csv``, parse it into a list and then print it to screen, assuming that *CSV* file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets in :ref:`project_two_dataset` section.

.. code:: python 

    import csv

    # read in data
    with open('example.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file and ensure it's a number (not a string)
    column_1 = [ float(row[0]) for row in columns ]

    print(column_1)
    
.. _project_three_normal_objects:

Normal Objects
==============

The following code snippet illustrates how to create and use a *Normal Distribution* ``object`` in **Python**,

.. code:: python

	import statistics
	
	# Create the Normal Distribution object
	mean = 100
	std_dev = 10
	dist = statistics.NormalDist(mean, std)
	
	# Use the Normal Distribution object to calculate probabilities
	prob = dist.cdf(120)
	rounded_prob = round(prob, 2)
	print("P(X <= 120) = ", rounded_prob)
	
	# Use the Normal Distribution object to calculate percentiles
	third_quartile = dist.inv_cdf(0.75)
	rounded_quartile = round(third_quartile,2)
	print("P(X <= ", rounded_quartile , ") = 0.75")
	
		
Output:
	P(X <= 120) = 0.98

	P(X <= 106.74) = 0.75

For a more comprehensive explanation of ``NormalDist()`` from the ``statistics`` package and its various uses, refer to the :ref:`Python Normal Distribution page <python_normal_distribution>`.
 
.. _project_three_qq_plots:

QQ Plots
========

TODO


.. _project_three_project:

Project
=======

Normal Calculations
-------------------

1. Create a Standard Normal Distribution ``object``. Use this ``object`` to answer the following questions.

a. :math:`P(Z \leq 1.751)`

b. :math:`P(Z \geq 0.888)`

c. :math:`P(-1.234 \leq Z \leq 0.545)`

d. TODO inverse

e. TODO inverse

f. TODO inverse

2. Create a Normal Distribution ``object`` with a mean of 50 and a standard deviation of 10. Use this object to answer the following questions.

a. TODO: cdf

b. TODO: cdf 

c. TODO: cdf

d. TODO: inverse

e. TODO: inverse

f. TODO: inverse


Measuring Normality
-------------------

Velocity of Light
*****************

1. Find the following percentiles in Michelson's Velocity of Light distribution.

a. 95 :sup:`th` percentile
b. 84 :sup:`th` percentile
c. 16 :sup:`th` percentile
d. 5 :sup:`th` percentile

2. Find the Z-score for each percentile found in the previous problem.

3. Create a Standard Normal Distribution ``object``. Use this object to find the theoretical percentile for each Z-score found in the previous problem.

4. How do the sample percentiles found in #1 compare to the theoretical percentiles found in #3? 

Old Faithful
************

1. Find the following percentiles in the Old Faithful eruption duration distribution.

a. 95 :sup:`th` percentile
b. 84 :sup:`th` percentile
c. 16 :sup:`th` percentile
d. 5 :sup:`th` percentile

2. Find the Z-score for each percentile found in the previous problem.

3. Create a Standard Normal Distribution ``object``. Use this object to find the theoretical percentile for each Z-score found in the previous problem.

4. How do the sample percentiles found in #1 compare to the theoretical percentiles found in #3? 

Velocity of Light
*****************

1. Find the following percentiles in the number of Celebrity Twitter followers distribution.

a. 95 :sup:`th` percentile
b. 84 :sup:`th` percentile
c. 16 :sup:`th` percentile
d. 5 :sup:`th` percentile

2. Find the Z-score for each percentile found in the previous problem.

3. Create a Standard Normal Distribution ``object``. Use this object to find the theoretical percentile for each Z-score found in the previous problem.

4. How do the sample percentiles found in #1 compare to the theoretical percentiles found in #3? 
Assessing Normality
-------------------

Velocity of Light
*****************

1. Create a QQ plot for Michelson's Velocity of Light distribution.

2. Based on the QQ plot, is Michelson's distribution approximately normal? Why or why not?

Old Faithful
************

1. Create a QQ plot for Old Faithful's eruption duration.

2. Based on the QQ plot, is Old Faithful's eruption duration approximately normal? Why or why not?

Celebrity Twitter
*****************

1. Create a QQ plot for the number of Celebrity Twitter followers.

2. Based on the QQ plot, is the number of Celebrity Twitter followers normal? Why or why not?
 
.. _project_three_dataset:

Datasets
========

Velocity of Light Data
----------------------

.. note::

	You may already have this dataset downloaded into your *Linux Files* directory from when we did :ref:`project_two`.

You can download the full dataset :download:`here <../../assets/datasets/velocity_of_light_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Michelson's Velocity of Light Data
   :file: ../../assets/datasets/previews/velocity_of_light_data_preview.csv

The meaning of the column is clear from the column header: each observation measures the speed of light in meters per second, :math:`\frac{km}{s}`.

Old Faithful
------------

You can download the full dataset :download:`here <../../assets/datasets/old_faithful_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Old Faithful Geyser Duration and Wait Time
   :file: ../../assets/datasets/previews/old_faithful_data_preview.csv

TODO

Celebrity Twitter
-----------------

TODO

.. _project_four:

=================
Linear Regression
=================

	Mathematicians do not study objects, but relations among objects; they are indifferent to the replacement of objects by others as long as relations do not change. Matter is not imporant, only form interests them.
	
	- Henri Poincare

TODO

Instructions
============

1. Download all **three** *csv* datasets in the :ref:`project_four_dataset` section and place them in the ``Linux Files`` folder on your folder system where you save your ``.py`` scripts.
2. Create a Python ``.py`` script named ``NAME_project_four.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``NAME`` with your name.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_four_background` section.
5. Read the :ref:`project_four_loading_data` section.
6. Read the :ref:`project_four_bivariate_analysis` section.
6. Load in the data from the ``.csv`` file using the technique outlined in the :ref:`project_four_loading_data` section.
7. Perform all exercises and answer all questions in the :ref:`project_four_project` section. Label your script with comments as indicated in the instructions of each problem.
8. When you are done, zip your script **and** the *csv* files in a zip file named ``NAME_project_four.zip``
9. Upload the zip file to the Google Classroom Project Four Assignment.

.. _project_four_background:

Background
==========

Linear Regression Model
-----------------------

The *Linear Regression Model* is a special statistical method for modelling the linear relationship that exists between correlated variables. A regression model (not necessarily *linear*) applies to a sample of bivariate data,

.. math::

	S = \{ (x_1, y_1), (x_2, y_2), ... , (x_n, y_n) \}
	
Where :math:`n` is the total number of samples. The :math:`x_i` variable is referred to as the **predictor** variable (or sometimes the **independent** variable); the :math:`y_i` variable is referred to as the **response** varaible (or sometimes the **dependent** variable). If a statistically significant *linear* correlation exists between the predictor and response variable, the *Linear Regression Model* can be used to *predict* a value of :math:`y_i` given a value of :math:`x_i`. The *model equation* for :math:`\hat{y_i}` is given by,

.. math::

    \hat{y_i} = \mathcal{B}_1 \cdot x_i + \mathcal{B}_0 + \varepsilon_i

Where the term :math:`\varepsilon_i` is a normally distributed error term centered around 0 with standard deviation equal to the **mean squared error** of the model,

.. math::

    \varepsilon \sim \mathcal{N}(0, \text{MSE})

The error term :`\varepsilon_i` is sometimes called a residual. The value of a residual for a given :math:`i` can be found by subtracing the actual value of :math:`y_i` from the *predicted value* :math:`\hat{y_i}`,

.. math::
	
	\varepsilon_i = \hat{y_i} - y_i


A crucial assumption of the *Linear Regression Model* is the normality of the residuals. If this assumption is violated, then there is evidence to suggest the model is incomplete, i.e. there is another variable influencing the *response* variable. Moreover, if the normality assumption is violated, the model can no longer be used to extrapolate outside of the range of the *predictor variable*. 

Datasets
--------
TODO 

Old Faithful
------------

TODO

Spice Girls Songs
-----------------

TODO 

Celebrity Twitter
-----------------

TODO


.. _project_four_loading_data:

Loading In Data
===============

The following code snippet will load in a *CSV* spreadsheet named ``example.csv``, parse it into a list and then print it to screen, assuming that *CSV* file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets in :ref:`project_two_dataset` section.

.. code-block:: python 

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


.. _project_four_bivariate_analysis:

Bivariate Analysis
==================

Before we begin, let's import all the appropriate libraries and create some dummy data to test out the bivariate functions Python's :ref:`statistics <python_stats_package>` package has available,

.. code:: python

	import matplotlib.pyplot as mpl
	import statistics as stat
	
	bivariate_data = [ (1,2), (3,6), (5,9), (7, 13), (9, 16), (11, 19) ]
	(fig, axes) = mpl.subplots()
	
The sections that follow assume you have these lines added to the top of your script.

Scatter Plots
-------------

.. plot:: assets/plots/plots/scatterplots/scatterplot_example.py

Correlation
-----------

Regression Model
----------------

TODO

.. _project_four_project:

Project
=======

TODO 

Old Faithful
------------

Scatter Plot
************

1. Construct a scatter plot for this dataset using the **Eruption Length** as the *indicator* variable and the **Waiting Time** as the *response* variable.

2. In your :ref:`python_docstring`, describe the correlation in this dataset. Is it positive, negative or neutral? Is it linear or non-linear? Is it strong or weak? 

3. In your :ref:`python_docstring`, answer the following question: Based on your answer to the previous question, would a linear regression model be a good fit for this dataset?

Correlation
***********

TODO 

Regression
**********

TODO

Residual Analysis
*****************

TODO 

Spice Girl Song Length
----------------------

Scatter Plot
************

1. Construct a scatter plot for this dataset using the **Track Number** as the *indicator variable* and the **Song Length** as the *response* variable.

.. note::

    This type of scatter plot, where the horizontal axis represents time, is known as a :ref:`time_series`.

2. In your :ref:`python_docstring`, describe the correlation in this dataset. Is it positive, negative or neutral? Is it linear or non-linear? Is it strong or weak? 

3. In your :ref:`python_docstring`, answer the following question: Based on your answer to the previous question, would a linear regression model be a good fit for this dataset?

Correlation
***********

TODO 

Regression
**********

TODO

Residual Analysis
*****************

TODO 

Celebrity Twitter
-----------------

Scatter Plot
************

1. Construct a scatter plot for this dataset using the **Tweet Count** as the *indicator* variable and the **Follower Count** as the *response* variable.

2. In your :ref:`python_docstring`, describe the correlation in this dataset. Is it positive, negative or neutral? Is it linear or non-linear? Is it strong or weak? 

3. In your :ref:`python_docstring`, answer the following question: Based on your answer to the previous question, would a linear regression model be a good fit for this dataset?

Correlation
***********

TODO 

Regression
**********

TODO

Residual Analysis
*****************

TODO 

.. _project_four_dataset:

Data Sets
=========

Celebrity Twitter
-----------------

You can download the full dataset :download:`here <../../assets/datasets/celebrity_twitter_data.csv>`

The following table is a preview of the data you will be using for this project.

.. csv-table:: Celebrity Twitter Followers and Tweet Count
    :file: ../../assets/datasets/previews/celebrity_twitter_data_preview.csv

The fifth column represents the number of followers for a given Twitter user. The sixth column represents the number of tweets for a given Twitter user.

Old Faithful
------------

You can download the full dataset :download:`here <../../assets/datasets/old_faithful_data.csv>`.

The following table is a preview of the data you will be using for this project. 

.. csv-table:: Old Faithful Eruption and Waiting Times
   :file: ../../assets/datasets/previews/old_faithful_data_preview.csv

The first column represents the length of the eruption in minutes. The second column represents the waiting time in minutes until the next eruption.

Spice Girls Song Length
-----------------------

You can download the full dataset :download:`here <../../assets/datasets/spice_girls_song_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Spice Girl Song Lengths
   :file: ../../assets/datasets/previews/spice_girls_song_data_preview.csv

The third column represents the song length in milliseconds. The fifth column represents the track number of the song on the studio album on which it was released.

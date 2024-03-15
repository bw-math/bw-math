.. _python_demos:

==============
Demonstrations
==============

Below you will find some **Python** scripts that demonstrate various statistical facts and theorems. We will go over them in class when the time comes. 

Conditional Distributions
-------------------------

This script will generate a random bivariate sample of categorical data and then construct a conditional distribution for one variable. A stacked bar chart is then created to visualize the association, or lack thereof, between the two conditional distributions. 

:download:`Stacked Bar Chart (Conditional Distribution) <../../assets/demos/conditional_distributions.py>`

Estimators
----------

This script contains many useful functions for young statisticians seeking to tame the wild beast of uncertainy.

:download:`Point Estimators <../../assets/demos/stats.py>`

Measuring Variation
-------------------

This script displays a dot plot of a sample of data and illustrates how the different measures of variation are affected by the slight alterations in the sample of data.

:download:`Measuring Variation <../../assets/demos/variation.py>`

The Effect of Outliers
----------------------

This script generates a distribution of grades and visualizes the distribution with a dot plot. It will then calculate the sample mean and sample median, and plot as vertical lines, red and green respectively. 

We will alter the distribution in class to see how it affects the sample mean and median.

:download:`The Effects of Outliers <../../assets/demos/outliers.py>`

Scatter Plot of Twitter Data 
----------------------------

This script shows how to parse a CSV file and then create a scatter plot with it. To execute this script, you will need to download the Twitter dataset from :ref:`datasets` section and place it in the same folder where you download this script.

This dataset is an example of :ref:`negative <negative_correlation>`, :ref:`non-linear <non_linear_correlation>` correlation. In other words, even though there is clearly a correlation in this dataset, we cannot use linear regression to fit a model.

:download:`Twitter Data Scatter Plot <../../assets/demos/scatter_plot.py>`

Die Roll Simulation
-------------------

This script will simulate rolling ``m`` die ``n`` times. The outcome of the ``m`` die rolls is then summed and a frequency distribution is created for the ``n`` experiments. The frequency distribution is visualized with a histogram. 

The intent is show how the random variation of :ref:`independent <independence>`, identically distributed :ref:`random variables <random_variables>` leads naturally to the normal distribution. This result is known as :ref:`central_limit_theorem`

:download:`Die Roll Simulations <../../assets/demos/die_rolls.py>`

Normal Distribution
-------------------

This script shows how to work with the normal distribution in **Python**. It demonstrates how to calculate percentiles and probabilities. It also demonstrates how the symmetry of the :ref:`normal_distribution` manifests numerically via the :ref:`law_of_complements`.

:download:`Normal Distribution <../../assets/demos/normal_probabilities.py>`

QQ Plot
-------

This script shows how to construct a QQ plot to assess the normality of a sample of data. 

:download:`QQ Plot <../../assets/demos/qq_plot.py>`

Least Squares Regression
------------------------

This script illustrates how the regression parameters for the slope and intercept of the line of best fit are estimated used least squares.

:download:`Least Squares <../../assets/demos/least_squares.py>`

.. plot:: assets/demos/least_squares.py

Sampling Distributions
----------------------

This script illustrates the difference between *biased* and *unbiased* estimators. It will simulate a sample from a Normal population and then calculate various statistics. The results of the simulation are shown in a histogram with the true value of the population parameter plotted as a vertical line.

:download:`Sampling Distributions <.../../assets/demos/sampling_simulations.py>`

.. _graphical_representations_of_data:

=================================
Graphical Representations of Data
=================================

Definitions
===========
.. _skew:

Skew
----

Definition
    A *skew* is a feature of sample where more data is *clustered* on one side of the sample. We say such data are "*skewed*", or that it exhibits "*skewness*". 

.. _frequency_distributions:

Frequency Distributions
=======================

.. _ungrouped_frequency_distributions:

Ungrouped Distributions
-----------------------

Suppose you ask 10 people their favorite color and the following data set represents their answers,

.. math:: 
    S = \{ r, b, g, g, r, r, y, o, r, b \}

Where 

    *b* = response of "blue"
    *g* = response of "green"
    *o* = response of "orange"
    *r* = response of "red"
    *y* = response of "yellow "

An *ungrouped frequency distribtion* is simply a table where each entry represents the :ref:`frequency` of every possible observation,

+-----+-------+
|  x  |  f(x) |
+=====+=======+
|  b  |   2   |
+-----+-------+
|  g  |   2   |
+-----+-------+
|  o  |   1   |
+-----+-------+
|  r  |   4   |
+-----+-------+
|  y  |   1   |
+-----+-------+

.. _grouped_frequency_distributions:

Grouped Distributions
---------------------

TODO 

The steps for constructing a *grouped* frequency distribution are given below. 

Steps
*****

If you are given a sample **S** of data points, then the steps for finding a *grouped* frequency distribution are as follows,

1. Find the range of the data set. 

.. math::

    R = max(\{ x_i \}) - min(\{ x_i \})

2. Choose a number of classes. Typically between 5  and 20, depending on the size and type of data.

3. Find the class width. Round up, if necessary.

.. math::
    
    w = \frac{R}{n}

.. note:: 

    Using the :ref:`ceiling_function` from a future section, we could simply write,

    .. math::

        w = \lceil \frac{R}{n} \rceil

    And the *rounding* would be implied. 

4. Find the lower and upper class limits **LL**:sub:`i` and **UL**:sub:`i` for each *i* up to *n*, i.e. for each class. 

.. math:: 
    
    LL_i = min(S) + (i-1) \cdot w

.. math::

    UL_i = min(s) + i \cdot w - 1

.. math::
    
    i = 1, 2, ... , n

.. note:: 

    The upper limit is subtracted by 1 so the lower limit of the next class doesn't overlap. 

5. Find the lower and upper class boundaries **LB**:sub:`i` and **UB**:sub:`i` for each *i* up to *n*, i.e. for each class, 

.. math::
    
    LB_i = LL_i - 0.5

.. math::
    
    UB_i = UL_i + 0.5

.. math::
    
    i = 1, 2, ... , n

.. important:: 
    
    This step is *only* really necessary for continuous data. In the previous step, we subtracted the upper limit of each class by 1, so there are now gaps in the interval. In other words, with a class width of *5* and starting a minimum :math:`min(S)=100`, we might end up with intervals like 100 - 104, 105 - 109, 110 - 114, etc. We need to ensure the classes actually meet so we divide up the 1 we subtracted and distributed it evenly on either side of the boundary. 

6. Sort the data set into classes and tally up the frequency of each class.

Example 
    Suppose you measure the height of everyone in your class and get the following sample of data, where each observation in the data set is measured in feet,

    .. math::

        S = \{ 5.7, 5.8, 5.5, 5.7, 5.9, 6.3, 5.3, 5.5, 5.4, 5.3, 5.7, 5.9 \}

    Find the grouped frequency distribution for this sample of data using :math:`n = 5` classes.

TODO 

.. _histograms:

Histograms
==========

A *histogram* is a graphical representation of a :ref:`frequency distribution <frequency_distributions>`. The *classes* or *bins* are plotted on the *x-axis* against the frequency of each *class* on the *y-axis*.

.. plot:: assets/plots/histograms/histogram_random.py

Variations
----------

A basic *histogram* can be modified to accomodate a variety of scenarios, depending on the specifics of the problem. In each case below, the sample's frequency distribution is used as the basis for constructing the graph.

.. _bar_charts:

Bar Charts
**********

Sometimes the frequency distribution has already been calculated for us. In cases like this, a simple bar chart is all that is required.

.. plot:: assets/plots/other/bar_chart.py

.. _stem_leaf_plots:

Stem-Leaf Plots
***************

TODO 

.. _relative_frequency_distribution:

Relative Frequency Plots
************************

*Relative frequency* histograms express the frequency of each class as a *percentage* of the total observations in the sample, 

.. math::
    f(x_i) = \frac{x_i}{n}


.. plot:: assets/plots/histograms/histogram_relative.py

Distribution Shapes
-------------------

TODO 

Uniform
*******

.. plot:: assets/plots/histograms/histogram_uniform.py

Normal
******

.. plot:: assets/plots/histograms/histogram_normal.py

Bimodal
*******

.. plot:: assets/plots/histograms/histogram_bimodal.py

Skewed
******

**Skewed Right**

.. plot:: assets/plots/histograms/histogram_skewed_right.py

**Skewed Left**

.. plot:: assets/plots/histograms/histogram_skewed_left.py

.. _ogives:

Ogives
======

TODO 

.. plot:: assets/plots/histograms/histogram_and_ogive.py


.. note:: 
    
    Your book's authors call these types of graphs *ogives*. Be aware, you will almost never see these graphs referred to by that term. In practice, they are almost always called *cumulative frequency distributions*.

Construction
------------

1. Find the :ref:`relative frequency distribution<frequency_distributions>`

.. _boxplots:


Distribution Shapes
-------------------

TODO 

Uniform
*******

.. plot:: assets/plots/ogives/ogive_uniform.py

Normal
******

.. plot:: assets/plots/ogives/ogive_normal.py

Bimodal
*******

.. plot:: assets/plots/ogives/ogive_bimodal.py

Skewed
******

Skewed Right
    .. plot:: assets/plots/ogives/ogive_skewed_right.py

Skewed Left
    .. plot:: assets/plots/ogives/ogive_skewed_left.py

Boxplots
========

While :ref:`histograms` and :ref:`ogives` provide a wealth of information about the sample distribution, they do not give us the whole picture. 

Construction
------------

1. Find the maximum observation.
2. Find the 75 :sup:`th` percentile (*third quartile*)
3. Find the 50 :sup:`th` percentile (*median*)
4. Find the 25 :sup:`th` percentile (*first quartile*)
5. Find the minimum observation.
   
Distribution Shapes
-------------------

TODO 

Uniform
*******

.. plot:: assets/plots/boxplots/boxplot_uniform.py

Normal
******

.. plot:: assets/plots/boxplots/boxplot_normal.py

Bimodal
*******

.. plot:: assets/plots/boxplots/boxplot_bimodal.py

Skewed
******

**Skewed Right**

.. plot:: assets/plots/boxplots/boxplot_skewed_right.py

**Skewed Left**

.. plot:: assets/plots/boxplots/boxplot_skewed_left.py

Scatter Plots
=============

**No Correlation**

.. plot:: assets/plots/scatterplots/scatterplot_no_correlation.py

**Positive Correlation**

.. plot:: assets/plots/scatterplots/scatterplot_positive_correlation.py

**Negative Correlation**

.. plot:: assets/plots/scatterplots/scatterplot_negative_correlation.py

Other Types of Graphs
=====================

TODO 

Pie Chart
---------

TODO 

Time Series
-----------

**Positive Trend**

.. plot:: assets/plots/timeseries/timeseries_positive_trend.py

**Negative Trend**

.. plot:: assets/plots/timeseries/timeseries_negative_trend.py

**No Trend**

.. plot:: assets/plots/timeseries/timeseries_no_trend.py
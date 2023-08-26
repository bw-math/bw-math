.. _graphical_representations_of_data:

=================================
Graphical Representations of Data
=================================

In this section we study various ways of representing data graphically. 

.. _frequency_distributions:

Frequency Distributions
=======================

A *frequency distribution* is a tabular summary (table) of a sample of data. It tells us how often each observation occurs. 

.. _ungrouped_frequency_distributions:

Ungrouped Distributions
-----------------------

The concept of an *ungrouped distribution* is intuitive and best seen by example.

Example
    Suppose you ask 10 people their favorite color and the following data set represents their answers,

    .. math:: 
        S = \{ r, b, g, g, r, r, y, o, r, b \}

    Where 

        *b* = response of "blue"

        *g* = response of "green"

        *o* = response of "orange"

        *r* = response of "red"

        *y* = response of "yellow "

    Describe the *distribution* of this sample with a an ungrouped frequency distribution.

An *ungrouped frequency distribtion* is simply a table where each entry represents the :ref:`frequency` of every possible observation,

+---------------+-------+
|  :math:`x_i`  |  f(x) |
+===============+=======+
|     b         |   2   |
+---------------+-------+
|     g         |   2   |
+---------------+-------+
|     o         |   1   |
+---------------+-------+
|     r         |   4   |
+---------------+-------+
|       y       |   1   |
+---------------+-------+

Notice the sum of the right hand column totals to the number of observations in the sample, :math:`n = 10`. We summarize this result below,

.. math:: 

    n = \sum_{x_i \in S} f(x_i)

Take note of the index in this sum. The :math:`x_i \in S` symbol can be read as "*for every* :math:`x_i` *in S*". This notation is used to take into account observations that may have the same value, as in this example where the observations ``b``, ``g`` and ``r`` occur multiple times. In other words, each term :math:`x_i` of the sum is a *unique value*. Its multiplicity derives from the frequency :math:`f(x_i)` by which it is multiplied.

Contrast this against the notation employed in the :ref:`sample_mean_formula`

.. math:: 

    \bar{x} = \frac{ sum^n_{i=1} x_i }{n}

In the :ref:`sample_mean_formula`, the index is over the observation order, i.e. from :math:`i = 1, 2, 3 ..., n`. In this case, it may happen that :math:`x_i = x_j` for some :math:`i \neq j`. In other words, in the sample mean formula, it is possible for terms in the summation to *repeat*. 

.. _grouped_frequency_distributions:

Grouped Distributions
---------------------

Ungrouped distributions can get cumbersome when the :ref:`range` of the data is very large or when there are a large number of unique observations drawn from a continuous population. For example, consider the following dataset which represents the eruption length and period between eruptions for the famous geyser `Old Faithful <https://en.wikipedia.org/wiki/Old_Faithful>`_ at Yellowstone National Park in Wymoing.

.. csv-table:: Old Faithful Eruption and Waiting Times
   :file: ../../assets/datasets/previews/old_faithful_data_preview.csv

Attempting to create an ungrouped distribution of this data would be a futile effort. Therefore, the standard approach with datasets like this is to create an *grouped* frequency distribution.

Steps
*****

If you are given a sample of *n* data points :math:`S = \{ x_1, x_2, ... , x_n \}`, then the steps for finding a *grouped* frequency distribution are as follows,

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

.. _histogram_variatians:

Variations
----------

A basic *histogram* can be modified to accomodate a variety of scenarios, depending on the specifics of the problem. In each case below, the sample's frequency distribution is used as the basis for constructing the graph.

.. _dot_plots:

Dot Plots
*********

Instead bars with differing heights, dot plots use *stacked dots* to represent the number of times each observation occurs, i.e. its frequency. 

.. _stem_leaf_plots:

Stem-Leaf Plots
***************

TODO 

.. _relative_frequency_distribution:

Relative Frequency Plots
************************

*Relative frequency* histograms express the frequency of each class as a *percentage* of the total observations in the sample, 

.. math::
    r(x_i) = \frac{f(x_i)}{n}

Recall that the sum of frequencies is *n*,

.. math:: 

    n = \sum_{x_i \in S} f(x_i)  \text{      Frequency Equation }

Therefore, the sum of *relative frequencies* is,

.. math::

    \sum_{x_i \in S} r(x_i) = \sum_{x_i \in S} \frac{f(x_i)}{n}

Since the sum does not depend on *n*, we can factor :math:`\frac{1}{n}` out of the denominator,

.. math::

     = \frac{1}{n} \cdot \sum_{x_i \in S} f(x_i)

Whence, we apply the *Frequency Equation* to get,

.. math::

    = \frac{1}{n} \cdot n = 1

In other words, the sum of *relative frequencies* is equal to 1, 

.. math::

    \sum_{x_i \in S} r(x_i) = 1  \text{     Relative Frequency Equation}

This intuitive result simply means the distribution must total to *100%*.

In other words, *relative frequency* histograms do not change the shape of the distribution; they scale (*normalize*) the distribution so that the sum of class frequencies is *100%*.

.. plot:: assets/plots/histograms/histogram_relative.py


Pie Charts
**********

*Pie charts* are a special type of relative frequency histogram. Since the relative frequencies sum to 1, we can represent the distribution as *one* circle and then express the proportion the distribtion that belongs to class by the proportion of area in a circular sector.

In other words, the size of each slice of the pie represents the relative frequency of that class. 

(TODO plot)

.. _distribution_shapes:

Distribution Shapes
-------------------

The shape of the histogram can tell us a lot about the distribution of the sample. 

.. _uniform_shape:

Uniform
*******

A histogram where each class is approximately level with every other class is known as *uniform*. 

.. plot:: assets/plots/histograms/histogram_uniform.py

A *uniform distribution* tells us each class is *equally likely*. In other words, if we were to randomly select an individual from this sample, there is an equal chance the selected individual will come from each class. 

(TODO find good uniform data set)

Normal
******

A histogram where the classes are symmetric and decreasing around a common point is known as *normal*.

.. plot:: assets/plots/histograms/histogram_normal.py

The line of symmetry in a perfectly symmetrical distribution is the :ref:`median`. The reason for this can seen by equating the *area* under the distribution with the proportion of the sample that belongs to that area. Since the *areas* on either side of a symmetric distribution are equal,

(TODO: fill between points)

It follows these areas both represent fifty percent of the distribution. 

A *normal distribution* tells us classes closer to the :ref:`median` are more likely to be observed.

Example
    :download:`here <../../assets/datasets/velocity_of_light.csv>`.

.. note::

    We will construct the histogram for this dataset in class using **Python3**.
    
Bimodal
*******

A histogram where two classes are more frequent than the other classes in the distribution is known as *bimodal*.

.. plot:: assets/plots/histograms/histogram_bimodal.py

Example
    :download:`here <../../assets/datasets/old_faithful_data.csv>`.

.. note::

    We will construct the histogram for this dataset in class using **Python3**.
    
Skewed
******

Definition
    A *skew* is a feature of sample where more data is *clustered* on one side of the sample. We say such data are "*skewed*", or that it exhibits "*skewness*". 

A *skewed* distribution has *tails*, indicating the distribution is not symmetric (*asymmetric*). Individuals drawn from a *skewed* distribution are more likely to have extreme values. By "*extreme*" we mean values outside of the intervals where the majority of the distribution lies. 

**Skewed Right**

.. plot:: assets/plots/histograms/histogram_skewed_right.py

Example
    :download:`here <../../assets/datasets/roman_emperors_data.csv>`.

.. note::

    We will construct the histogram for this dataset in class using **Python3**.

**Skewed Left**

.. plot:: assets/plots/histograms/histogram_skewed_left.py

Example
    :download:`here <../../assets/datasets/earth_density_data.csv>`.

.. note::

    We will construct the histogram for this dataset in class using **Python3**.
    
.. _ogives:

Ogives
======

TODO 

.. plot:: assets/plots/histograms/histogram_and_ogive.py


.. note:: 
    
    Your book's authors call these types of graphs *ogives*. Be aware, you will almost never see these graphs referred to by that term. In practice, they are almost always called *cumulative frequency distributions*.

Construction
------------

1. Find the :ref:`relative frequency distribution <frequency_distributions>`


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

Variations
----------

Stacked Bar Chart
*****************

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


.. note::

    The maximum observation, the third quartile, the median, the firsrt quartile and the minimum are sometimes collectively known as the *five-number summary*.

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

No Correlation
--------------

.. plot:: assets/plots/scatterplots/scatterplot_no_correlation.py

Positive Correlation
--------------------

.. plot:: assets/plots/scatterplots/scatterplot_positive_correlation.py

Negative Correlation
--------------------

.. plot:: assets/plots/scatterplots/scatterplot_negative_correlation.py

Time Series
===========

Positive Correlation
--------------------

**Positive Trend**

.. plot:: assets/plots/timeseries/timeseries_positive_trend.py

Negative Correlation
--------------------

**Negative Trend**

.. plot:: assets/plots/timeseries/timeseries_negative_trend.py

**No Trend**

.. plot:: assets/plots/timeseries/timeseries_no_trend.py
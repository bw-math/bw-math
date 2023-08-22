.. _point_estimation:

================
Point Estimation
================

A sample of data is characterized by *point estimates* of *sample statistics*.

Definitions
===========

.. _observation:

Observation
-----------

Symbolic Expression
    :math:`x_i`

Definition
    An :ref:`individual`; A single piece of data. 
    
The subscript *i* is called the *index* of the observation. If the sample is ordered, the *index* corresponds to the order in which the observation was made, i.e. :math:`x_1` is the first observation, :math:`x_2` is the second observation, etc. 

.. _sample:

Sample
------

Symbolic Expression 
    :math:`\{ x_1, x_2, ..., x_{n-1}, x_n \}`

Definition 
    A collection, or :ref:`set <set_theory>`, of observations. 
    
The number of samples, *n*, is called the *sample size*.

.. _frequency:

Frequency
---------

Symbolic Expression
    :math:`f(x_i)`

Definition
    The number of times a particular observation occurs in a sample of data.

.. _outlier:

Outlier
-------

Definition
    An unusual observation.

What we mean by "*unusual*" depends on the data. GEnerally speaking, we mean something that roughly approximates, "*a data that is far outside what is expected*".

If we are measuring :ref:`numerical data <quantitative_data>`, this might mean an observation that is much, much greater than or much, much less than the majority of the data. 

If we are measuring :ref:`categorical data <categorical_data>`, this might mean an observation is in infrequent.

.. _measures_of_location:

Measures of Location
====================

*Measures of location* describe *where* a sample of data can be found.

.. _arithmetic_mean:

Arithmetic Mean
---------------

The *arithmetic* mean is a sample statistic you have probably seen before; what you probably didn't know is it is not the *only* way of calculating the mean. You will see in the next few sections alternate ways of calculating a quantity that is meant to represent the *mean* of a sample.

Before getting to the good stuff, let's review the *arithmetic* mean. There are two equivalent ways of defining the *sample mean*. 

.. _sample_mean_formula:

Sample Formula
**************

If the sample of data is specified as a set or list of data as in the following, 

.. math:: 
    S = \{ x_1, x_2, ... , x_n \}

Then the sample arithmetic mean can be calculated with the formula,

.. math::
    \bar{x} = \frac{\sum_{i}^n x_i}{n}

This is known as the *sample mean formula* for the arithmetic mean.

Example
    Suppose you survey 10 people and ask them how many of the 11 full-length, major motion picture *Star Wars* movies they have seen. Suppose the sample **S** of their responses is given below,

    .. math::
        S = \{ 6, 7, 9, 0, 1, 0, 3, 6, 3, 9 \}

    Find the average number of *Star Wars* movies seen by this sample of people.

Applying the *sample mean formula*,
    
.. math::

    \bar{x} = \frac{6 + 7 + 9 + 0 + 1 + 0 + 3 + 6 + 3 + 9}{10} = 3.5 movies

.. note::
    
    Notice in this example the *sample mean* does **not** correspond to an observable value in the sample. 
    
    The *sample mean* is not even a *possible value* of an individual observation in this sample (unless we allow for people who stopped watching half-way through one of the movies).

Interlude
*********

Suppose in a sample of data **S**, some of the observations have identical values, such as in the following dataset that represents the age in years of an A.P Statistics student,

    S = \{ 16, 16, 17, 18, 16, 17, 17, 17 \}

Before moving on to calculate the sample mean, let us represent this sample **S** in an equivalent way using a table,

+--------------+----------------+
|  :math:`x_i` | :math:`f(x_i)` |
+--------------+----------------+
|      16      |       3        |
+--------------+----------------+
|      17      |       4        |
+--------------+----------------+
|      18      |       1        |
+--------------+----------------+

This way of representing a sample of data, where the first column stands for the value of the observation and the second column that stands for the frequency of that observation, is known as a :ref:`frequency_distribution`. 

(We will study *frequency distributions* in more detail in the :ref:`next section <_graphical_representations_of_data>`.)

Let us move on to the task at hand: calculating the sample mean. In this case, the formula for the arithmetic mean gives,

.. math:: 
    \bar{x} = \frac{16 + 16 + 17 + 18 + 16 + 17 + 17 + 17}{8}

If we collect all the terms in the numerator that are *like*, we may rewrite this as,

.. math::
    \bar{x} = \frac{3 \cdot 16 + 4 \cdot 17 + 1 \cdot 18}{8}

Notice the first factor of each term in the numerator is simply frequency of that observation in the *frequency distribution* table, whereas the second factor is the actual value of the observation. In other words, each term of the numerator is of the form,

.. math::
    x_i \cdot f(x_i)

This recognization leads the following formula that comes in handy when sample distributions are given in terms of :ref:`frequency distributions <frequency_distributions>`

.. _sample_mean_frequency_formula:

Frequency Formula
*****************

If the sample of data is specified as a frequency distribution as in the following,

+-------------+-------------------+
|     x       |      f(x)         |
+=============+===================+
|  x :sub:`0` |   f( x :sub:`0`)  |
+-------------+-------------------+
|  x :sub:`1` |   f( x :sub:`1`)  |
+-------------+-------------------+
|  ...        |  ...              |
+-------------+-------------------+
|  x :sub:`n` |   f( x :sub:`n`)  |
+-------------+-------------------+

Then the sample arithmetic mean can be calculated with the formula, 

.. math::
    \bar{x}_A = \sum_{i}^n x_i \cdot f(x_i)

Example
    TODO 

+--------------+----------------+
|  :math:`x_i` | :math:`f(x_i)` |
+--------------+----------------+
|      ??      |       ?        |
+--------------+----------------+
|      ??      |       ?        |
+--------------+----------------+
|      ??      |       ?        |
+--------------+----------------+

.. _geometric_mean:

Geometric Mean
--------------

The *geometric mean* is an alternate way of defining the *mean* of a sample data. 

The *geometric mean* is defined as,

.. math::
    \bar{x}_G = (x_1 \cdot x_2 \cdot ... \cdot x_{n-1} \cdot x_n )^(1/n)

TODO 

.. _geometric_vs_arithmetic_mean:

Geometric vs. Arithmetic Mean
*****************************

TODO

The Moral of the Story
**********************

There are other variants of the *mean* that sometimes appear in the literature. For example, when dealing with acoustic (sound) data, the `harmonic mean <https://en.wikipedia.org/wiki/Harmonic_mean>`_ is often the most appropriate measure for the *mean*. 

We talk about these other variants only to make you aware of them. In this class, we will exclusively be dealing with the *arithmetic mean*.

Nevertheless, before moving on, there is an important point to make: the mean is not an absolute measure of a sample; its value depends on the *way* we calculate it. 

This feature of statistics may be surprising. The amount of choice we have in *how* we go about measuing the population from a sample of data may seem as if it should not lead to a rigorous and well defined branch of mathematics.

It is true the choice we make between using the geometric mean and the arithmetic mean is to some extent arbitrary; there is not a particularly good reason for preferring one over the other, besides convention. It is not important which one we choose; it is only important *that* we choose one and stick with it.

One of the key idea of statistics is, not that we should *rid* ourselves of assumptions and biases (an impossible task), but that we should be *aware* of our assumptions and biases. Otherwise, without awareness, those assumptions and biases may show up and influence the data.

.. _mode:

Mode
----

TODO 

.. _percentiles:

Percentiles
-----------
    
TODO 

.. _median:

Median
------

TODO

.. _quartiles: 

Quartiles
---------

TODO 
        
.. _measures_of_variation:

Measures of Variation 
=====================

*Measures of variation* characterize the *spread* and *dispersion* of a sample of data.

Motivation
----------

Consider these two samples of data :math:`S_1` and :math:`S_2`,

.. math::

    S_1 = \{ 4, 5, 6 \}

.. math::

    S_2 = \{ 0, 5, 10 \}

If we apply the :ref:`Sample Mean Formula <sample_mean_formula>` to **S_1**, we get,

.. math::

    \bar{x_1} = \frac{4 + 5 + 6}{3} = 5

If we apply the :ref:`Sample Mean Formula <sample_mean_formula>` to **S_1**, we get,

.. math::

    \bar{x_2} = \frac{0 + 5 + 10}{3} = 5

In bothcases, we wind up with the same sample mean. If we summarizing these two samples of data to audience and the only information we gave them was the sample mean, they might erroneously conclude the samples were the same.

However, refering to the actual observations that make up either sample, it is clear the samples are **not** the same.

Clearly, we need some other type of :ref:`sample_statistic` to differentiate these two samples of data. 

In other words, the *sample mean* is *not enough* to completely describe a sample of data. In the language of mathematics, we say the sample mean is "*necessary, but not sufficient*" to determine a sample of data.

But what exactly is different about these two samples? If we plot the samples separately on a number line and compare, we can see what is going on more clearly,

(INSERT PICTURE)

Fom the picture, it is obvious that :math:`S_2` is more *spread out* around the mean than :math:`S_1`. To put it another way, :math:`S_1` is more tightly *clustered* around the mean than :math:`S_2`. This *spread* or *clustering* is referred to as *variation*.

The goal of the next few sections is to come up with a way of quantifying and measuring this *variation*.

.. _interquartile_range:

Interquartile Range
-------------------

First up, we have the *interquartile range*.

TODO

Rule of Thumb for Outliers
**************************

(TODO: three times IQR)

.. _absolute_variation:

Absolute Variation
------------------

TODO 

.. _sample_variance:

Variance
--------

Motivation
**********

Let us consider a rather contrived example that is nevertheless instructive. Suppose **S** a sample of data.represents 
TODO


.. _standard_deviation:

Standard Deviation
------------------

TODO

Measures of Comparision
=======================

Coefficient of Variation
------------------------

.. math:: 
    v = \frac{\bar{x}}{s} \cdot 100

Z Score
-------

.. math::
    z = \frac{x_i - \bar{x}}{s}


Outliers
========

TODO

Rule of Thumb
-------------

TODO

.. _chebyshevs_theorem:

Chebyshev's Theorem
===================

TODO
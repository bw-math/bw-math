
.. _data:

Data
====

Classifications
===============

The data we collect from an experiment is classified according to several factors.

.. _data_dimensionality:

Dimensionality
--------------

Definition

    The *dimension* of a dataset is the number of values associated with a single observation.

Univariate
    :math:`\{ x_1, x_2, x_3 \}`

*Univariate* data consists of observations that each contain a single value.

Example 
    Experimental data from Henri Cavendish's density of the Earth experiments. Density is expressed as a ratio of the density of water. See :ref:`project_one` for more information about this dataset.

.. csv-table:: Density of the Earth
   :file: ../../assets/datasets/previews/earth_density_data_preview.csv

Bivariate
    :math:`\{ (x_1, y_1), (x_2, y_2), ... , (x_n, y_n)\}`

*Bivariate* data consists of observations that each contain two values (i.e. an *pair*)

Example 
    Data from the Challenger space shuttle explosion showing the atmospheric temperature versus the erosion index of the O-ring seal. The failure of the O-ring seal at lower temperatures was not accounted for prior to launch.

.. csv-table:: Challenger Space Shuttle Erosion Data
   :file: ../../assets/datasets/previews/challenger_erosion_data_preview.csv


Multivariate 
    :math:`\{ (x_{1}^1, x_{2}^1, ... , x_{n}^1 ), (x_{1}^2, x_{2}^2, ... , x_{n}^2 ), ... ,(x_{1}^m, x_{2}^m, ... , x_{n}^m )`

*Multivariate* data consists of observations that each contain an arbitrary number of values (i.e. a *vector*)

Example
    Body measurements from a sample of grizzly bears.

.. csv-table:: Bear Measurements
    :file: ../../assets/datasets/previews/bear_measurements_data_preview.csv

.. _data_characteristic:

Characteristic
--------------

Definition
    The *characteristic* of a dataset is the *type* of data being observed.

Qualitative
    :math:`\{ \text{red}, \text{blue}, \text{yellow} \}`

Qualitative data are categorical.

Example
    - The favorite color of a sample of people. 
    - A group of people's answer to supporting a new tax reform law.
    - Movies that feature Kevin Bacon.
    - Words that appear in a novel.

Quantitative
    Quantitative data are numerical. 

These are two types of *quantitative* data, *discrete* and *continuous*.

Discrete Quantitative 
   :math:`\{ 1, 2, 3, 4, 5, ... \}`

*Discrete quantitative* data are countable.

Example
    - Students in a class.
    - Petals on a clover
    - The championships won by a football team.
    - M&M's in a bag.

Continuous Quantitative
    :math:`\{ 1.0, 1.01, 1.001, 1.0001, 1.00001, ... \}`

*Continuous quantitative* data are infinitely divisible 

Example
    - The temperature of a gallon of water under various pressures. 
    - The speed of a train. 
    - The weight of a coin.
    - The amount of rainfall in a region.

Scale 
-----

.. image:: ../../assets/imgs/statistics/measurement_scales.jpg
    :align: center

Nominal Level
    Unordered, categorical data. 

*Nominal data* is the simplest type of data. A *nominal scale* or *level* is a way of labelling and separating individuals in a sample into groups.

Example
    - The favorite color of each person in a sample of data.
    - The political party affiliation of each person in a sample of data.
    - The nationality of each person in a sample of data.

Ordinal Level
    Ordered, categorical data.

*Ordinal data* is a step above *nominal data*. It is *categorical*, but an order can be imposed on it.

Example
    - Answers to a customer satisfaction survey: ``DISSATISFIED``, ``NEUTRAL``, ``SATISIFED``
    - Grades on a quiz: ``A``, ``B``, ``C``, ``D``, ``E``, ``F``.

Interval Level
    Ordered, numerical data.

*Interval level* is a step above *ordinal data*. The data are ordered, but now the *difference* between observations is defined. In other words, with an *interval level*, the distance between two observation :math:`x_2` and :math:`x_1` can be defined as :math:`x_2 - x_1`

Example
    - A historical time series of the Consumer Price Index
    - The IQs of a random sample of people.
    - The SAT scores of the graduating class of seniors.

Ratio Level 
    Ordered, numerical data.

*Ratio level* is the final level of data. The data are ordered, the difference between two datapoints can be computed :math:`x_2 - x_1` and there is a *true zero*. With a *ratio level*, it makes sense to have an observation of *0*.

Example
    - Measurements from a scale, i.e. the weight of a mass.
    - Measurements from a thermometer, i.e the temperature of a body.
    - The amount of rainfall in a region over a period of a week. 

.. _statistics_defintions:

Types of Statistics
===================

.. _sample_statistic:

Sample Statistic
    A piece of information calculated from sample of data.

*Sample statistics* are used to summarize the features of a dataset. They are broken down into two main categories.

.. _descriptive_statistic:

Descriptive Statistic 
    A sample statisic used to visualize and approximate the shape and spread of a population.

.. _inferential_statistic:

Inferential Statistic
    A sample statistic used to make inferences about the population.

One of the most important *descriptive statistics* is the *sample mean*,

.. math:: 

    \bar{x} = \frac{ \sum^n_{i = 1} x_i } {n}

One of the most important *inferential statistics* is the *Z-score* of the *sample mean*,

.. math:: 

    Z = \frac{ \bar{x} - \mu }{ \frac{ \sigma }{\sqrt n} }

If these formulae make no sense yet, don't worry! That is to be expected. They are listed here, so you can start forming a picture of the things to come. By the end of this class, these two formulae will become your best friends.

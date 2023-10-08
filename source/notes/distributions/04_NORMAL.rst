.. _normal_distribution:

===================
Normal Distribution
===================


The **Normal Distribution** is the foundation of :ref:`inferential statistics <inferential_statistic>`. 

.. _normality:

Normality 
=========

.. _normality_introduction:

Introduction
------------

Normality arises when observations being randomly drawn from a :ref:`population` are *independent* and *identically distributed*. In other words, if a series of experiments are performed where each experiment is the same as the last in every respect, then the outcomes of all the experiments taken together should be approximately normal. 

.. important::

    *Independence* and *Identically Distributed* are mathematical concepts with precise defintions. We will talk more about them when we get to :ref:`probability <probability_introduction>` 

In order to explain the origin of normality, it is instructive to consider a simple example. 

Consider the experiment of rolling a single die. Think about what the *ideal* relative frequency distribution for this experiment should look like. 

A die has six sides and each one is equally likely. If we let :math:`\mathcal{X}` represent the outcome a rolling a single die, we can express the relation of all outcomes being equally likely with the following equation, 

.. math::

    P(\mathcal{X}=1) = P(\mathcal{X}=2) = P(\mathcal{X}=3) = P(\mathcal{X}=4) = P(\mathcal{X}=5) = P(\mathcal{X}=6)

To say the same thing in a different way, the :ref:`probability <probability_introduction>` of all outcomes should be the same,

.. math::

    P(\mathcal{X}=i) = p \text{   i = 1, 2, 3, 4, 5, 6 }

The *ideal* histogram (in other words, the distribution of the *population*) would look perfectly uniform,

.. plot:: assets/plots/examples/04_ex01_die_roll.py

Consider now the experiment of rolling 10 die. The *relative* frequency of each outcome in the *ideal distribution* will not change, since the new die being rolled consist of the same outcomes as the original die; Outcomes are added to the experiment in the same proportion. 

TODO

A departure from normality can suggest several things: 

1. The selection process was not random.
2. The observations are not *independent*.
3. The observations are not being drawn from the exact same population.


.. _normal_calculations:

Normal Calculations
-------------------

TODO

.. plot:: assets/plots/distributions/normal/normal_distribution_01.py

.. plot:: assets/plots/distributions/normal/normal_distribution_02.py

.. _normal_cdf:

Cumulative Distribution Function
********************************

TODO

.. _normal_inverse_cdf:

Inverse Cumulative Distribution Function
****************************************

TODO

Symmetry
--------

TODO 

Z-Tables
========

TODO 

Empirical Rule
==============

TODO 

.. image:: ../../assets/imgs/distributions/normal/normal_distribution_empirical_rule.png
    :align: center

Effects of Parameters
=====================

Varying the Mean
----------------

TODO 

Varying the Standard Deviation
------------------------------

By changing the :ref:`standard_deviation`, the shape of the distribution changes. As the :ref:`standard_deviation` increase, the graph spreads out. This is because :ref:`standard_deviation` is a :ref:`measure of variation<measures_of_variation>`. In other words, :ref:`standard_deviation` quantifies how the distribution is spread out along the *x*-axis.

.. plot:: assets/plots/distributions/normal/normal_distribution_03.py

To summarize,

.. note:: 
    1. By changing the mean of the *normal distribution*, the *location* of the distribution changes.
    2. By changing the standard deviation of the *normal distribution*, the *spread* of the distribution changes. 

.. _assessing_normality:

Assessing Normality
===================

TODO

.. _qq_plots: 

QQ Plots
--------

TODO

Relation To Other Distributions
===============================

The :ref:`normal_distribution` is deeply connected with many different areas of mathematics. It pops up everywhere, from `quantum mechanics <https://en.wikipedia.org/wiki/Wave_packet>`_ to `finance <https://www.investopedia.com/articles/investing/102014/lognormal-and-normal-distribution.asp#:~:text=When%20the%20investor%20continuously%20compounds,time%20in%20a%20normal%20distribution.>`_. The reach of the *normal distribution* is far and wide.

.. _normal_binomial_approximation:

Normal As An Approximation of the Binomial
------------------------------------------

TODO 

.. note:: 
    *Conditions*: 
    
    :math:`n \cdot p \geq 5`

    :math:`n \cdot (1 - p) \geq 5`

.. _normal_poisson_approximation:

Poisson As An Approximation of the Normal
-----------------------------------------

TODO

.. note:: 
    *Conditions*: 
        
    :math:`	\lambda \leq \leq 0`
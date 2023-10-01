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

TODO 


.. _normal_distribution:

Probability Distribution
------------------------

TODO

.. plot:: assets/plots/distributions/normal/normal_distribution_01.py

.. plot:: assets/plots/distributions/normal/normal_distribution_02.py

.. _normal_cdf:

Cumulative Distribution Function
********************************

TODO

.. _inverse_normal_cdf:

Inverse Cumulative Distribution Function
****************************************

TODO

.. _normal_outliers:

Outliers
--------

TODO 

.. _central_limit_theorem:


Symmetry
========

TODO 

Z-Tables
========

TODO 

Empirical Rule
==============

TODO 

.. image:: ../../assets/imgs/distributions/normal/normal_distribution_empirical_rule.png

Pearson Skew Index
==================

TODO 

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
        
    :math:`	\lambda >> 0`

.. _assessing_normality:

Assessing Normality
===================

TODO

.. _qq_plots: 

QQ Plots
--------
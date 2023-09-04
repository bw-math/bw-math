.. _geometric_distribution:

=======================
Geometric Distributions
=======================

TODO

.. _geometric_random_variable:

Geometric Random Variable
=========================

TODO 

.. _geometric_probability_density:

Probability Density
-------------------
.. math:: 

    P(X = x) = \sum_{i=1}^{x} (1-p)^{x-1} \cdot p

Distribution
------------

TODO

In order to show the geometric density represents a distribution, we must show the probability of all outcomes sums to 1. In order to do this, we must first talk about the *geometric series*.

.. _geometric_series:

Geometric Series
****************

A geometric series is defined as the sum of powers of ``r``,

.. math:: 

    \sum_{i=1}^{n} r^i = r + r^2 + r^3 + ... + r^n 

The reason it is called *geometric* can be easily seen if we give ``r`` a value. For instance, if :math:`r = \frac{1}{4}`, then the first few terms of the geometric series are given by,

.. math:: 

    \sum_{i=1}^{n} (\frac{1}{4})^i = \frac{1}{4} + \frac{1}{16} + \frac{1}{64} + ... + (\frac{1}{4})^n

Each term on the right hand side can be identified with the areas of successive squares in the following picture,

.. image:: ../../assets/imgs/context/geometric_series.png
    :align: center
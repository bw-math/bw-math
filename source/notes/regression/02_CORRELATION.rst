.. _correlation:

===========
Correlation
===========

Correlation is a measure of the strength of a relationship that exists between two observable variables.

.. _correlation_introduction:

Introduction
============

Preliminaries
-------------

Before we can begin our study of *correlation*, let's make some preliminary defintions that will help us keep everything clear and precise.

Univariate Statistics
*********************

In order to differentiate between the statistics relationing to the *x* and *y* variables, we introduce some notation.

:math:`\bar{x}` and :math:`\bar{y}` are defined as the *univariate* sample means of the :math:`x` and :math:`y` variables. In other words, :math:`\bar{y}` is the sample mean of the :math:`y` variable, as if we were observing the :math:`y` variable in isolation. Similarly for :math:`\bar{x}`.


:math:`s_x` and :math:`s_y` are defined as the *univariate* standard deviations of the :math:`x` and :math:`y` variables. In other words, :math:`s_x` is the standard deviation of the :math:`x` variable, as if we were observing the :math:`x` variable in isolation. Similarly, for :math:`s_y`. 

.. math::

	s_{x}^2 = \frac{1}{n-1} \cdot \sum_{i=1}^{n} (x_i - \bar{x})^2
	
.. math::
	
	s_{y}^2 = \frac{1}{n-1} \cdot \sum{i=1}^{n} (y_i - \bar{y})^2
	
Assessing Correlation
*********************


TODO

.. plot:: assets/plots/scatterplots/scatterplot_positive_correlation.py

TODO

.. plot:: assets/plots/scatterplots/scatterplot_negative_correlation.py

TODO

.. plot:: assets/plots/scatterplots/scatterplot_no_correlation.py

TODO


:math:`s_x` and :math:`s_y` are defined as the *univariate* standard deviations of the :math:`x` and :math:`y` variables. In other words, :math:`s_x` is the standard deviation of the :math:`x` variable, as if we were observing only :math:`x` alone. Similarly, for :math:`s_y`. 

.. math::

	s_{x}^2 = \frac{1}{n-1} \cdot \sum_{i=1}^{n} (x_i - \bar{x})^2
	
.. math::
	
	s_{y}^2 = \frac{1}{n-1} \cdot \sum{i=1}^{n} (y_i - \bar{y})^2
Definition
==========

Version 1
---------

TODO: justification. make some plots.

.. math::

Version 2
---------

Version 3
---------

TODO

.. math::

	r_{xy} = \frac{1}{n-1} \cdot \sum_{i=1}^{n} \frac{x_i - \bar{x}}{s_x} \frac{y_i - \bar{y}}{s_y}
	

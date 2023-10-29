.. _bivariate_introduction:

============
Introduction
============

Up to now we have been dealing with *univariate* data. In this section, we begin the study of *bivariate data*.

Definitions
===========

Bivariate Data
--------------

:math:`S = \{ (x_1, y_1), (x_2, y_2), ... , (x_n, y_n) \}`
	When two variables are measured on one individual, we call such data *bivariate*.
	
The :math:`x` variable is sometimes called the *independent* or *predictor* variable. The :math:`y` variable is sometimes called the *dependent* or *response* variable. It is important to understand this terminology is only used in the context of the :ref:`linear_regression` model introduced in the next section. Before the *statistical significance* of the relationship is established, this terminology is misleading, as it implies a relationship between the :math:`x` and `y` variable when none may exist. Correlation can be measured between variables that have no relationship whatsoever; in such instance we call the variables *uncorrelated*. 

.. important::

	Because we are dealing with randomness, *uncorrelated* variables will not necessarily have a correlation of 0. In fact, correlations of 0 are never observed in practice. There will always be a non-zero correlation between any given variables; the task of statistics is to determine whether or not this correlation is significant enough to use the outcome of one variable to make predictions about the outcome of the other variable.
	

.. _scatter_plots:

Scatter Plots
=============

A scatterplot is a very simple and easy to understand graphical representation of bivariate data. The :math:`x` variable is plotted on the horizontal axis versus the :math:`y` variable on the vertical axis. Graphs of *scatterplots* are classified based on the *direction* of the relationship observed, the *strength* of the relationship observed and the *linearity* of the relationship observed.

.. _correlation_direction:

Direction
---------

.. _no_correlation:

No Correlation
**************

A scatterplot with no correlation between the :math:`x` and :math:`y` variables should appear random,

.. plot:: assets/plots/scatterplots/scatterplot_no_correlation.py

.. _positive_correlation:

Positive Correlation
********************

A scatterplot with a positive correlation betwen the :math:`x` and :math:`y` variables should have a general upward trend,

.. plot:: assets/plots/scatterplots/scatterplot_positive_correlation.py

.. _negative_correlation:

Negative Correlation
********************

.. plot:: assets/plots/scatterplots/scatterplot_negative_correlation.py

.. _correlation_strength:

Strength
--------

.. _strong_correlation:

Strong
******

TODO

.. _weak_correlation:

Weak
****

TODO

.. _correlation_linearity:

Linearity
---------

.. _linear_correlation:

Linear
******

TODO 

.. _nonlinear_correlation:

Non-Linear
**********
 
TODO

.. _time_series:

Time Series
===========

A *time series* is similar to a *scatter plot* in almost all ways, except the *independent* variable in a *time series* is always a unit of time. A *correlation* for a *time series* is called a *trend*.

Positive Trend
--------------

.. plot:: assets/plots/timeseries/timeseries_positive_trend.py

Negative Trend
--------------

.. plot:: assets/plots/timeseries/timeseries_negative_trend.py

No Trend
--------

.. plot:: assets/plots/timeseries/timeseries_no_trend.py

.. _linear_regression:

=================
Linear Regression
=================

TODO

.. _regression_model:

Regression Model
================

TODO

.. math::

    \hat{y_i} = \mathcal{B}_1 \cdot x_i + \mathcal{B}_0 + \varepsilon

Where the term :math:`\varepsilon` is a normally distributed error term centered around 0 with standard deviation equal to the **mean squared error** of the model,

.. math::

    \varepsilon \sim \mathcal{N}(0, \text{MSE})

TODO

.. _mean_squared_error:

Mean Squared Error
==================

The term :math:`\hat{y}` is **not** the observed value of :math:`y` in the bivariate sample of data that was used to calibrate the model. It is the *predicted* value of :math:`y` given the *observed* value of :math:`x`. This is an *extremely* important point when talking about regression. The *model* equation is a *prediction*, and the prediction is not *exact*. Each *predicted value* of :math:`y`, :math:`\hat{y}`, will deviate from the *observed* value of :math:`y`. The deviation, if the model is a good fit, should be *normally distributed* around 0. 

TODO 

SSE: Sum Squared Error
----------------------

TODO 

.. math::

    \sum_{i=1}^{n} (\hat{y}_i - y_i)^2

TODO

MSE: Mean Squared Error
-----------------------

TODO 

.. math::

    \frac{\sum_{i=1}^n (\hat{y}_i - y_i)^2}{n-2}

TODO 

Model Coefficients
==================

The regression model coefficients can be estimated by finding the values of :math:`\mathcal{B}_0` and :math:`\mathcal{B}_1` that *minimize* the MSE of the model.

In other words,

    TODO: example. plug in various values of coefficients and demonstrate the MSE varies. Show there is a value that produces a minimum.

.. note::

    In order to derive an algebraic expression for the coefficients, differential calculus is required. If you want an extra credit assignment related to this, talk to me outside of class.

:math:`\mathcal{B}_0`

    TODO 

:math:`\mathcal{B}_1`

    TODO 

Line of Best Fit
================

TODO

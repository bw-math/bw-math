.. _graphical_representations_of_data:

=================================
Graphical Representations of Data
=================================

Definitions
===========

.. _frequency:

Frequency

    :math:`f(x)`

    The number of times an observation *x* occurs in a sample *S*.  

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

An *ungrouped frequency distribtion* is simply a table where each entry represents the frequency of every possible observation,

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

The steps for constructing a *grouped* frequency distribution are given below. 

Steps 
    1. Find the range of the data sets. 
 
        .. math::
            R = max(x_i) - min(x_i)
    
    2. Choose a number of classes. Typically between 5  and 20, depending on the size and type of data.
    3. Find the class width. Round up, if necessary.

        .. math::
            w = \frac{R}{n}

    4. Find the lower and upper class limits **LL**:sub:`i` and **UL**:sub:`i` for each *i* up to *n*, i.e. for each class. 

        .. math:: 
            LL_i = min(x_i) + (i-1) \cdot w
        
        .. math::
            UL_i = min(x_i) + i \cdot w
        
        .. math::
            i = 1, 2, ... , n

    5. Find the lower and upper class boundaries **LB**:sub:`i` and **UB**:sub:`i` for each *i* up to *n*, i.e. for each class, 

        .. math::
            LB_i = LL_i - 0.5
        
        .. math::
            UB_i = UL_i + 0.5

        .. math::
            i = 1, 2, ... , n

    6. Sort the data set into classes and tally up the frequency of each class.
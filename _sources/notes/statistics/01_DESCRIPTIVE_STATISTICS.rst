================
Point Estimation
================

A sample of data is characterized by *point estimates* of *sample statistics*.

Definitions
===========

Observation
    :math:`x_i`

    A single piece of data. The subscript is called the *index* of the observation. If the sample is ordered, the *index* corresponds to the order in which the observation was made, i.e. :math:`x_1` is the first observation, :math:`x_2` is the second observation, etc. 

Sample 
    :math:`\{ x_1, x_2, ..., x_{n-1}, x_n \}`

    A collection, or :ref:`set <set_theory>`, of observations. The number of samples, *n*, is called the *sample size*.

Frequency
    :math:`f(x_i)`

    The number of times a particular observation occurs in a sample of data.

Measures of Location
--------------------

*Measures of location* describe *where* a sample of data can be found.


Mean
    Arithmetic Mean

        The *arithmetic* mean can be defined in two equivalent ways. 

        Sample Formula 

            If the sample of data is specified as a set or list of data as in the following, 
            
            .. math:: 
                S = \{ x_1, x_2, ... , x_n \}

            Then the sample arithmetic mean can be calculated with the formula,

            .. math::
                \bar{x} = \frac{\sum_{i}^n x_i}{n}


        Suppose in the sample of data **S**, some of the observations have identical values, such as in the following dataset that represents the age in years of an A.P Statistics student,

            S = \{ 16, 16, 17, 18, 16, 17, 17, 17 \}

        In this case, the formula for the arithmetic mean gives,

            .. math:: 
                \bar{x} = \frac{16 + 16 + 17 + 18 + 16 + 17 + 17 + 17}{8}

            .. math::
                \bar{x} = \frac{2 \cdot 16 + 4 \cdot 17 + 1 \cdot 18}{8}

        Notice the first factor of each term in the numerator is simply frequency whereas the second factor is the value of the observation,

            .. math::
                x_i \cdot f(x_i)

        This recognization leads the following formula that comes in handy when sample distributions are given in terms of :ref:`frequency distributions <frequency_distributions>`

        Frequency Formula

            If the sample of data is specified as a frequency distribution as in the following,

            +-------------+-------------------+
            |     x       |      f(x)         |
            +=============+===================+
            |  x:sub:`0`  |   f( x:sub:`0`)   |
            +-------------+-------------------+
            |  x:sub:`1`  |   f( x:sub:`1`)   |
            +-------------+-------------------+
            |  ...        |  ...              |
            +-------------+-------------------+
            |  x:sub:`n`  |   f( x:sub:`n`)   |
            +-------------+-------------------+

            Then the sample arithmetic mean can be calculated with the formula, 

            .. math::
                \bar{x}_A = \sum_{i}^n x_i \cdot f(x_i)
    
    Geometric Mean

        The *geometric mean* is defined as,

        .. math::
            \bar{x}_G = (x_1 \cdot x_2 \cdot ... \cdot x_{n-1} \codt x_n )^(1/n)

    Geometric vs. Arithmetic Mean


Mode

    TODO 

Median

    TODO

Percentiles

    TODO

    Quartiles

        TODO 
        
Measures of Dispersion
----------------------

Interquartile Range
    
    TODO

Variance/Standard Deviation

    TODO 
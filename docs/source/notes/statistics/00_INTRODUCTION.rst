============
Introduction
============

Definitions
===========

Key
---

.. _population: 

Population
    The *population* is the set of all possible individuals that can be observed in a given experiment. 

.. _observation_methods:

Methods of Observation
----------------------

Census
    A *census* is a type of statistical study where each individual in the population is observed.

    A *census* may also refer to the entire population itself, rather than the method of observation. 

Sample 
    A *sample* is a type of statistical study where a subset of the population is observed *at random*.

    A *sample* may also refer to the subset of the population being observed, rather than the method of observation.

.. _sampling_techniques:

Sampling Techniques
-------------------

Random

    TODO

    Ex.

        TODO 

Systematic

    TODO 

    Ex.

        TODO

Stratified

    TODO

    Ex. 

        TODO

Cluster

    TODO

    Ex.

        TODO 

Statistical Fallacies
---------------------

.. _bias:

Bias 
    *Bias* is a type of systematic error that arises when the sample data that is used to draw conclusions about the population does not accurately represent a *random* sample. 

    Selection Bias
        *Selection bias* occurs when the sampling method is not representative of the entire population.
        
        As an extreme example, if you were interested in making assertions about the average height of a United States citizens, selecting a sample of 100 elementary schoolers would lead you to make wildly erroneous conclusions. 

    Response bias
        *Response bias* occurs when the sampling method is over-representative or under-representative of certain segments of the population.

        A typical example of this kind of bias can be found in cold-calling telephone surveys. Most people are likely to ignore to robo-calls for political polls, and the set of people who do answer the calls are likely not an accurate representation of the entire population. 

        A famous example of this kind of bias is the `1948 Election Between Thomas Dewey and Harry Truman <https://en.wikipedia.org/wiki/Dewey_Defeats_Truman>`. The polling data the Chicago Tribune relied on showed Dewey winning by a huge margin [DEWEY]_

        .. [DEWEY] The 1948 Presidential Election polls
            `source <https://www.randomservices.org/random/data/Election1948.html>`_

        ========= ======== ====== ===== ======
        Candidate Crossley Gallup Roper Actual
        ========= ======== ====== ===== ======
        Truman          45     44    38     50
        Dewey           50     50    53     45
        Other            5      6     9      5
        ========= ======== ====== ===== ======

        While polls will never agree 100% of the time with reality, the error in this case was extreme. The pollsters at the organizations of Crossley, Gallup and Roper were told to survey a certain number of people. Beyond that, they were free to choose who to include in the survey. This led to the data they collected being *biased*, leading to blunders such as,

        .. image:: ../../imgs/context/dewey_defeats_truman.jpg
            :width: 60%
            :align: center
    

    

.. _data_classification:

Classifications of Data
-----------------------

Dimensionality
    The *dimension* of a dataset is the number of values associated with a single observation.

    Univariate
        *Univariate* data consists of observations that each contain a single value.

        :math:`\{ x_1, x_2, x_3 \}`

    Bivariate
        *Bivariate* data consists of observations that each contain two values (i.e. an *pair*)

        :math:`\{ (x_1, y_1), (x_2, y_2), ... , (x_n, y_n)\}`

    Multivariate 
        *Multivariate* data consists of observations that each contain an arbitrary number of values (i.e. a *vector*)

        :math:`\{ (x_{1}^1, x_{2}^1, ... , x_{n}^1 ), (x_{1}^2, x_{2}^2, ... , x_{n}^2 ), ... ,(x_{1}^m, x_{2}^m, ... , x_{n}^m )`

Characteristic
    The *characteristic* of a dataset is the *type* of data being observed.

    Qualitative
        Qualitative data are categorical.

        Ex. 
            :math:`\{ "Red", "Blue", "Yellow"\}`

    Quantitative
        Quantitative data are numerical. 

        Discrete 
            Discrete quantitative data is countable.

            Ex.
                :math:`\{ 1, 2, 3, 4, 5, ... \}`

        Continuous
            Continuous quantitative data  is infinitely divisible 

            Ex.
                :math:`\{ 1.0, 1.01, 1.001, 1.0001, 1.00001, ... \}`

Scale 

    Nominal Level
        Unordered, categorical data.

        Ex.

            TODO

    Ordinal Level
        Ordered, categorical data.

        Ex. 

            TODO

    Interval/Ratio Level 
        Ordered, numerical data.

        Ex.

            TODO

.. _statistics_defintions:

Types of Statistics
-------------------

.. _sample_statistic:

Sample Statistic
    A piece of information that characterizes the shape and spread of a sample.

.. _descriptive_statistic:

Descriptive Statistic 
    A sample statisic used to visualize and approximate the shape and spread of a population.

.. _inferential_statistic:

Inferential Statistic
    A sample statistic used to make inferences about the population.

Other Terminology
-----------------

.. _with_replacement:

With Replacement
    An observation has been made *with replacement*, if after its selection, it is placed back into the population. 

        Consider drawing a single card from a deck of cards, shuffling it back into the deck and then selecting another card. The event of getting the same card on both draws is a possible event because the card selected on the first draw is returned to the population of possible observation before making the second draw.

.. _without_replacement:

Without Replacement 
    An observation has been made *without replacement*, if after its selection, it is removed from the population and is no longer a possible observation.

        Consider drawing a single card from a deck of cards, setting it aside and then selecting another card. The event of getting the same card on both draws is an impossible event because the card selected on the first draw is no longer in the population of possible observation, and therefore cannot possible be selected again. In other words, when we sample data *without replacement*, we affect the *sample space* of subsequent experiments.
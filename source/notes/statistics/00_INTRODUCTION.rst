============
Introduction
============

Statistics is the study of making general assertions from particular cases.

Motivation
==========


Definitions
===========

.. _individual:

Individual
----------

Definition
    A single observation.

*Individuals* will mean different things depending on the experiment being conducted. 

If we are measuring how hot it is over the course of a week in the summer, then the *individuals* in the experiment will be the temperature measurements made on a thermometer. The *experimental unit* of each *individual observation* would be degrees Kelvin.

.. note:: 

    When reading temperature data in most scientific literature, you will likely never see celsius or fahrenheit. Kelvin is the standard *experimental unit* for the fields of physics, chemistry and biology. The only times you will encounter other measurement scales is when the authors are trying to relate the data to human experience.

If we are measuring what percent of the country's population supports a government policy, then the *individuals* in the experiment will be the collection (:ref:`set_theory`) people's answers, Yes or No. The *experimental unit* of each *individual observation* would be the binary units, *Y* or *N*. 

.. _population: 

Population
----------

Definition
    The *population* is the set of all possible individuals that can be observed in a given experiment. 

.. _sample_definition:

Sample
------

Definition 
    A *sample* is a subset of individuals drawn from the population in a given experiment.


.. _population_subset_sample:

Population vs. Sample 
*********************

The relationship between the *population* and the *sample* can be visualized with the following :ref:`venn diagram <venn_diagrams>`. 

.. image:: ../../assets/imgs/statistics/sample_subset_population.jpg
    :align: center


The *sample* is contained in the *population*; it is the portion of the population we actually observe. The *sample* is the information we have available to us to draw conclusions about the population.

.. note:: 

    We will study :ref:`venn diagrams <venn_diagrams>` in more detail in later chapters. 

.. _observation_methods:

Methods of Observation
======================

In statistics, "*observation*" is the name of the game. Without first making observations, there is nothing else to be done. 

Conducting Census
    A *census* is a type of statistical study where each individual in the population is observed.

In practice, we are never able to see entire population at once. A *census* is an *ideal*, like a *vacuum* or a *frictionless surface*. If we had infinite time and resources, we should always like to conduct a *census*, rather than drawing a *sample*, because it would tell us conclusively how the population looked. 

A *census* is conducted every ten years in the United States to accurately measure the population size. Even a massive operation like this is likely to miss more than a few individuals in the population, whether due to undocumented citizens, errors in record-keeping or pure happenstance. The point being, a *census* is the *ideal* study, but *impossible* to obtain.

.. warning::
    
    A *census* may also refer to the entire population itself, rather than the method of observation. The use should always be clear from context.

Drawing A Sample
    A *sample* is a type of statistical study where a subset of the population is observed *at random*.

When a sample is drawn from a population, we say, "*the population has been sampled*" or that we are "*sampling the population*".

Because we are not able to conduct a *census* whenever we want, we have to make do with a sample. It is usually the case the sample is much, much smaller than the actual population. For this reason, it is very important the sample is *random* and *representative* of the population. 

We need a *random* sample because we do not want the data to have any features in it (e.g., patterns) that would obscure the population we are trying to observe.

At the same time, we need a *representative* sample because we do not want the data to give a false impression of the population we are trying to observe.

Often, these two goals are at odds with one another. In order to make a sample *representative*, you must impose some sort of order on the way you sample the population, but doing so then affects the *randomness* of the sample. Finding the right balance between these two directives is the topic of the next section.

.. _sampling_techniques:

Sampling Techniques
-------------------

.. _random_sampling:

Random
******

Definition
    A *random* sample is selected from a population without any pre-determined method. 

Examples

    - Mixing names in a hat and picking three names without looking.
    - Going through the phone book and flipping a coin to determine who to include in the sample and who to exclude. 
    - Assign every name a number and then draw random numbers.

The last item in the list above is the most common technique in practice. A standard method in statistics for generating a random sample from a population is to *associate an index* to each *individual*. Consider the following table of names,

+-------+---------------------+
| Index | Individual          |
+-------+---------------------+
| 1     | Jean-Paul Sartre    |
+-------+---------------------+
| 2     | Martin Heidegger    |
+-------+---------------------+
| 3     | Edmund Husserl      |
+-------+---------------------+
| 4     | Bertrand Russel     |
+-------+---------------------+
| 5     | Kurt Godel          |
+-------+---------------------+
| 6     | Gottlob Frege       |
+-------+---------------------+
| 7     | Immanuel Kant       |
+-------+---------------------+
| 8     | Rene Descarates     |
+-------+---------------------+
| 9     | Ludwig Wittgenstein |
+-------+---------------------+
| 10    | Alain Badiou        |
+-------+---------------------+

Once each individual in the population is associated with an *index*, random numbers are generated; the indices that are selected by the random number generator then tell us what individuals to select for the sample.

.. _systematic_sampling:

Systematic
**********

Definition
    A *systematic* sample is selected from a population according to some fixed rule.

Examples

    - Asking every 10 :sup:`th` person who they are voting for in the next election.
    - Selecting ten people from every zipcode.
    - Sending out surveys and using every 5 :sup:`th` one that is returned.

.. _stratifed_sampling:

Stratified
**********

Definition
    To get *stratified* samples, the population is broken up by demographics. Then a *random* sample from every demographic is taken. Finally, the results are put back together. 

Example
        

.. _cluster_sampling:

Cluster
*******

    TODO

Example

    TODO 

Statistical Inference
---------------------

Once we have data to analyze, we apply the *statistical inference* to see what it tells us. 

*Statistical inference* is the process of using a sample of data to reach new conclusions about the population from which it was drawn. 

Null and Alternate Hypotheses
*****************************

Usually in statistics we are concerned with *hypotheses* and whether or not, based on the available data, there is sufficient evidence to reject one hypothesis in favor of another.

For example, we might like to know whether a new type of fuel is cleaner and more efficient than standard gasoline. In this case, we would start by assuming the *null hypothesis* that the efficiency of the new fuel is the same as standard gasoline. We would then establish an experiment designed to test this hypothesis against the *alternate hypothesis* that the new fuel is more efficient than standard gasoline.

.. topic:: Null Hypothesis

    .. math::

        H_{ \varnothing }

    The *null hypothesis* is the prior assumption we bring to the *experiment*. It represents the "*status quo*". 

    The term "*Null*" (as in :ref:`null_set`) means "*none*" or "*empty*", as in nothing has been accomplished with the *null hypothesis*. It represents "*no change to the state of our knowledge about the world*"

.. topic:: Alternate Hypothesis

    .. math::

        H_a

    The *alternate hypothesis* is the theory we would like to test with the experiment. It represents "*overturning of the status quo*" in favor of a new explanation. 

We assume the *null hypothesis* in order to test the validity of the *alternate hypothesis*. If we find sufficient evidence the *null hypothesis* is not true, we reject it in favor of the *alternate hypothesis*.

.. important::

    We never *prove* the null hypothesis true. It is always *assumed* true in order to determine whether there is evidence to conclude it is false.

In the example of testing the efficiency of a new type of fuel against standard gasoline, notice we are asking a question about two different populations: the population of cars that use the new type of fuel and the population of cars that use standard gasoline. Specifically, we are asking if there is a *statistical significance* difference between the efficiency of either groups. 

The first group is referred to as the *test* group, the sample to which a *treatment* has been applied and whose efficacy we would like to test.

The second group is referred to as the *control group*, the sample to which no *treatments* have been applied. 

Confounding Variables
*********************

Let us continue  to consider the example experiment of testing the efficiency of a new type of fuel against standard gasoline. 

To truly isolate the experiment from any *confounding variables*, we should restrict our populations to certain *makes* and *models* of cars. Otherwise, we would not be sure if the results of our experiments were due to the efficiency of the new fuel, or variations in the engine running the fuel. 

A *confounding variable* is a variable that affects the experiment, but is not measured, whether due to poor experimental design or due to the nature of the interaction. 

To see what is meant by "*due to the nature of the interaction*", suppose the new type of fuel whose efficiency is being tested loses some of its potency at higher elevations (due to the effects of gravity on its chemical composition, let's say). If some of the data we collect from the cars using the new fuel type is collected from high altitude locations, then the data will show the effects of this dependence, without our being aware. We might then erroneously conclude the new fuel does not possess the anticipated efficiency gains. 

For this reason, we must be very careful to always consider what variables for which we haven't accounted might influencing the samples we observe. In other words, we must always be mindful of *confounding variables*. 

Statistical Fallacies
=====================

.. _bias:

Bias 
-----

*Bias* is a type of systematic error that arises when the sample data that is used to draw conclusions about the population does not accurately reflect the population. 

Selection Bias
**************

Definition 
    *Selection bias* occurs when the sampling method is not representative of the entire population.
        
As an extreme example, if you were interested in making assertions about the average height of a United States citizens, selecting a sample of 100 elementary schoolers would lead you to make wildly erroneous conclusions. 

Response bias
*************

Definition
    *Response bias* occurs when the sampling method is over-representative or under-representative of certain segments of the population.

A typical example of this kind of bias can be found in cold-calling telephone surveys. Most people are likely to ignore robo-calls for political polls, and the set of people who do answer the calls are likely not an accurate representation of the entire population. 

A famous example of this kind of bias is the `1948 Election Between Thomas Dewey and Harry Truman <https://en.wikipedia.org/wiki/Dewey_Defeats_Truman>`_. The polling data the Chicago Tribune relied on showed Dewey winning by a huge margin [*]_

The results of the polls versus the actual result of the election are shown below,

.. [*] The 1948 Presidential Election polls `source <https://www.randomservices.org/random/data/Election1948.html>`_

========= ======== ====== ===== ======
Candidate Crossley Gallup Roper Actual
========= ======== ====== ===== ======
Truman          45     44    38     50
Dewey           50     50    53     45
Other            5      6     9      5
========= ======== ====== ===== ======

While polls will never agree 100% of the time with reality, the error in this case was extreme. Upon investigating what went wrong, it was discovered the pollsters at the organizations of Crossley, Gallup and Roper were told to survey a certain number of people. Beyond that, they were free to choose who to include in the survey. They ended up calling their friends, family and close relatives. This led to the data they collected being *biased*, resulting in an infamous photograph,

.. image:: ../../assets/imgs/context/dewey_defeats_truman.jpg
    :align: center

Observer Bias
*************

Definition
    *Observer Bias* occurs when the act of observation changes that which is being observed. 
        
Examples of this type of bias can crop up when pollsters ask leading questions, such as, "Do you *still* drink coffee?" versus the more neutral phrasing, "Do you drink coffee?". Depending on how the question is phrased, a different answer might be given.

A more famous example of this type of bias is the `Milgram Experiment <https://en.wikipedia.org/wiki/Milgram_experiment>`_ conducted by Dr. Stanley Milgrim at Yale University. The *Milford Experiment* was a psychological study wherein participants were told they were testing the effects of phyiscal punishment in form of an electric shock on the memory. Participants were to be paired off as *teacher* and *learner*. The *learner* would be asked to memorize a series of words, and then asked to recite them. If they got the words wrong in the recitation, the *teacher* would administer an electric shock to the *learner*. Each time a wrong answer was given, the voltage of the electric shock was increased.

Unbeknownst to the participants of the study, this wasn't the actual experiment. In reality, the *learner* in every experiment was a paid actor and the electric shocks weren't real. The actor would intentionally get answers wrong and then pretend to be in pain when the teacher was administering the fake electric shocks. The *teacher* was the real object of study. Dr. Milgram was trying to see how much pain a randomly selected individual would inflict on someone else simply because they were told to do it. 

When participants expressed unease or concern, the researchers running the study, intentionally dressed in white lab coats to give the appearance of authority, would give one of the following responses,

    - Please continue.
    - The experiment requires that you continue.
    - It is absolutely essential that you continue.
    - You have no other choice; you must go on.
    
The actor would get many questions wrong, forcing the *teacher* to increase the voltage of the shock. Most, but not all, participants would quit before reaching the maximum voltage. Dr. Milgrim found 14 of the 40 participants in the original study would increase the voltage of the shock all the way up to the maximum amount, as long as a researcher was there to instruct him or her to continue. 

Subsequent variations of this experiment have shown the *way* the researcher responds to the participant's concern after hearing the actor cry out in pain significantly affects the results. In Dr. Milgram's original experiment, the responses were phrased in such a way as to imply the actor's pain was for the "*good of the experiment*". If instead of saying,
        
    The experiment requires that you continue.

Researchers instead said,

    You are ordered to continue.

The results were vastly different. With this slight change, the results were nowhere near as large as in Dr. Milgrim's original experiment; Fewer people were more likely to quit before reaching the maximum shock threshold.

In other words, *how* you make the observation may change *what* you are observing.

.. _data_classification:

Classifications of Data
-----------------------

.. _data_dimensionality:

Dimensionality
**************

Definition

    The *dimension* of a dataset is the number of values associated with a single observation.

Univariate
    :math:`\{ x_1, x_2, x_3 \}`

*Univariate* data consists of observations that each contain a single value.

Bivariate
    :math:`\{ (x_1, y_1), (x_2, y_2), ... , (x_n, y_n)\}`

*Bivariate* data consists of observations that each contain two values (i.e. an *pair*)

Multivariate 
    :math:`\{ (x_{1}^1, x_{2}^1, ... , x_{n}^1 ), (x_{1}^2, x_{2}^2, ... , x_{n}^2 ), ... ,(x_{1}^m, x_{2}^m, ... , x_{n}^m )`

*Multivariate* data consists of observations that each contain an arbitrary number of values (i.e. a *vector*)

.. _data_characteristic:

Characteristic
**************

Definition
    The *characteristic* of a dataset is the *type* of data being observed.

Qualitative
    :math:`\{ "Red", "Blue", "Yellow"\}`

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

Nominal Level
    Unordered, categorical data.

TODO 

Example

    TODO

Ordinal Level
    Ordered, categorical data.

Example

    TODO

Interval/Ratio Level 
    Ordered, numerical data.

TODO

Example

    TODO

.. _statistics_defintions:

Types of Statistics
-------------------

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

Other Terminology
-----------------

.. _with_replacement:

With Replacement
    An observation has been made *with replacement*, if after its selection, it is placed back into the population. 

Example 

    Consider drawing a single card from a deck of cards, shuffling it back into the deck and then selecting another card. The event of getting the same card on both draws is a possible event because the card selected on the first draw is returned to the population of possible observation before making the second draw.

.. _without_replacement:

Without Replacement 
    An observation has been made *without replacement*, if after its selection, it is removed from the population and is no longer a possible observation.

Example

    Consider drawing a single card from a deck of cards, setting it aside and then selecting another card. The event of getting the same card on both draws is an impossible event because the card selected on the first draw is no longer in the population of possible observation, and therefore cannot possible be selected again. In other words, when we sample data *without replacement*, we affect the *sample space* of subsequent experiments.
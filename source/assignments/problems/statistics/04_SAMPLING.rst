.. _sampling_distribution_classwork:

======================
Sampling Distributions
======================

Sample Proportion
=================

.. topic:: Sample Proportion Sampling Distribution

	If :math:`\mathcal{X}_i \sim \text{Bern}(p)` for :math:`i = 1, 2, ..., n` and the following conditions are met,
	
	1. :math:`n cdot p \geq 10`
	2. :math:`n cdot (1 - p) \geq 10`
	
	The random variable, :math:`\hat{p} = \frac{\mathcal{X}_1 + \mathcal{X}_2 + ... + \mathcal{X}_n}{n}` has the following distribution,
	
	.. math::
	
		\hat{p} \sim \mathcal{N}(n \cdot p, \sqrt{n \cdot p \cdot (1 - p)) 
	
TODO

Difference of Proportions
-------------------------

.. topic:: Difference of Sample Proportions Sampling Distribution

	TODO
	
TODO

Sample Mean
===========

.. topic:: Sampling Distribution for the Sample Mean

	If :math:`\mathcal{X}_i \sim \mathcal{N}(\mu, \sigma)` for :math:`i = 1, 2, ..., n` **and** :math:`n \geq 30`, then the random variable :math:`\bar{\mathcal{X}} = \frac{\mathcal{X}_1 + \mathcal{X}_2 + ... + \mathcal{X}_n}{n}` has the following distribution, 
	
	.. math::
	
		\bar{\mathcal{X}} \sim \mathcal{N}(\mu, \frac{\sigma}{\sqrt{n}})
	
TODO

Difference of Means
-------------------

.. topic:: Sampling Distribution for Difference of Sample Means

	TODO
	
TODO

A.P. Exam Practice
==================

1. **2006, Free Response, #3**

The depth from the surface of Earth to a refracting layer beneath the surface can be estimated using methods developed by seismologists. One method is based on the time required for vibrations to travel from a distant explosion to a receiving point. The depth measurement **M** is the sum of the true depth **D** and the random measurement error **E**. That is, :math:`M = D + E`. The measurement error **E** is assumed to be normally distributed with mean 0 feet and standard deviation 1.5 feet.

	a. If the true depth at a certain point is 2 feet, what is the probability that the depth measurement will be negative?

	b. Suppose three independent depth measurements are taken at the point where the true depth is 2 feet. What is the probability that at least one of these measurements will be negative?

	c. What is the probability that the mean of the three independent depth measurements taken at the point where the true depth is 2 feet will be negative?

2. **2004, Free Response Form B, #3**

Trains carry bauxite ore from a mine in Canada to an aluminum processing plant in northern New York state in hopper cars. Filling equipment is used to load ore into the hopper cars. When functioning properly, the actual weights of ore loaded into each car by the filling equipment at the mine are approximately normally distributed with a mean of 70 tons and a standard deviation of 0.9 ton. If the mean is greater than 70 tons, the loading mechanism is overfilling.

	a. If the filling equipment is functioning properly, what is the probability that the weight of the ore in a randomly selected car will be 70.7 tons or more? Show your work.

	b. Suppose that the weight of ore in a randomly selected car is 70.7 tons. Would that fact make you suspect that the loading mechanism is overfilling the cars? Justify your answer.

	c. If the filling equipment is functioning properly, what is the probability that a random sample of 10 cars will have a mean ore weight of 70.7 tons or more? Show your work.

	d. Based on your answer in part (c), if a random sample of 10 cars had a mean ore weight of 70.7 tons, would you suspect that the loading mechanism was overfilling the cars? Justify your answer.

3. **2007, Free Response, #3**

Big Town Fisheries recently stocked a new lake in a city park with 2,000 fish of various sizes. The distribution of the lengths of these fish is approximately normal.

	a. Big Town Fisheries claims that the mean length of the fish is 8 inches. If the claim is true, which of the following would be more likely?

		A random sample of 15 fish having a mean length that is greater than 10 inches

	or

		A random sample of 50 fish having a mean length that is greater than 10 inches

	Justify your answer.

	b. Suppose the standard deviation of the sampling distribution of the sample mean for random samples of size 50 is 0.3 inch. If the mean length of the fish is 8 inches, use the normal distribution to compute the probability that a random sample of 50 fish will have a mean length less than 7.5 inches.

	c. Suppose the distribution of fish lengths in this lake was nonnormal but had the same mean and standard deviation. Would it still be appropriate to use the normal distribution to compute the probability in *part b* ? Justify your answer.

5. **2009, Free Response, #2**

A tire manufacturer designed a new tread pattern for its all-weather tires. Repeated tests were conducted on cars of approximately the same weight traveling at 60 miles per hour. The tests showed that the new tread pattern enables the cars to stop completely in an average distance of 125 feet with a standard deviation of 6.5 feet and that the stopping distances are approximately normally distributed.

	a. What is the 70th percentile of the distribution of stopping distances?

	b. What is the probability that at least 2 cars out of 5 randomly selected cars in the study will stop in a distance that is greater than the distance calculated in *part a*?

	c. What is the probability that a randomly selected sample of 5 cars in the study will have a mean stopping distance of at least 130 feet?

6. **2010, Free Response, #2**

A local radio station plays 40 rock-and-roll songs during each 4-hour show. The program director at the station needs to know the total amount of airtime for the 40 songs so that time can also be programmed during the show for news and advertisements. The distribution of the lengths of rock-and-roll songs, in minutes, is roughly symmetric with a mean length of 3.9 minutes and a standard deviation of 1.1 minutes.

	a. Describe the sampling distribution of the sample mean song lengths for random samples of 40 rock-and-roll songs.

	b. If the program manager schedules 80 minutes of news and advertisements for the 4-hour (240-minute) show, only 160 minutes are available for music. Approximately what is the probability that the total amount of time needed to play 40 randomly selected rock-and-roll songs exceeds the available airtime?

7. **2019, Free Response, #6**

Emma is moving to a large city and is investigating typical monthly rental prices of available one-bedroom apartments. She obtained a random sample of rental prices for 50 one-bedroom apartments taken from a Web site where people voluntarily list available apartments.

	a. Describe the population for which it is appropriate for Emma to generalize the results from her sample.
	
The distribution of the 50 rental prices of the available apartments is shown in the following histogram.

.. image:: ../../../assets/imgs/classwork/2019_apstats_frp_06a.png
	:align: center
	
Use this histogram to answer the following questions.

	b. Emma wants to estimate the typical rental price of a one-bedroom apartment in the city. Based on the distribution shown, what is a disadvantage of using the mean rather than the median as an estimate of the typical rental price?
	
	c. Instead of using the sample median as the point estimate for the population median, Emma wants to use an interval estimate. However, computing an interval estimate requires knowing the sampling distribution of the sample median for samples of size 50. Emma has one point, her sample median, in that sampling distribution. Using information about rental prices that are available on the Web site, describe how someone could develop a theoretical sampling distribution of the sample median for samples of size 50.

Because Emma does not have the resources to develop the theoretical sampling distribution, she estimates the sampling distribution of the sample median using a process called bootstrapping. In the bootstrapping process, a computer program performs the following steps,

- Take a random sample, with replacement, of size 50 from the original sample.
- Calculate and record the median of the sample.
- Repeat the process to obtain a total of 15,000 medians.

Emma ran the bootstrap process, and the following frequency table is the bootstrap distribution showing her results of generating 15,000 medians.

.. image:: ../../../assets/imgs/classwork/2019_apstats_frp_06b.png
	:align: center
	
The bootstrap distribution provides an approximation of the sampling distribution of the sample median. A confidence interval for the median can be constructed using a percentage of the values in the middle of the bootstrap distribution.

	d. Use the frequency table to find the following.
	
		i. Value of the 5th percentile:
		
		ii. Value of the 95th percentile:

	e. Find the percentage of bootstrap medians in the table that are equal to or between the values found in *part d*.
	
	f. Use your values from *parts d* and *e* to construct and interpret a confidence interval for the median rental price.

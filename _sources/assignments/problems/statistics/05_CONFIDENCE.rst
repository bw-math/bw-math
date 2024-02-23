.. _confidence_interval_classwork: 

====================
Confidence Intervals
====================

Means
=====

Known Standard Deviation 
------------------------

.. topic:: Critical Value

	.. math::
	
		z_{p} \equiv P(\mathcal{Z}<z_{p}) = \frac{p}{100}
	
.. topic:: Margin of Error

	.. math::
	
		\text{MOE} = \lvert z_{1-\frac{\alpha}{2}} \rvert \cdot \frac{s}{sqrt{n}}	

.. topic:: Confidence Interval for Population Mean, Version 1

	.. math::
	
		\bar{x} - z_{1-\frac{\alpha}{2}} \cdot \frac{s}{sqrt{n} } \leq \mu \leq \bar{x} - z_{\frac{\alpha}{2}} \cdot \frac{s}{sqrt{n} } 
		
.. topic:: Confidence Interval For Population Mean, Version 2

	.. math::
	
		\bar{x} - \text{MOE} \leq \mu \leq \bar{x} + \text{MOE}

.. topic:: Confidence Interval for Difference of Population Means

	TODO
		
Unknown Standard Deviation
--------------------------

TODO

1. **2004, Free Response Form B, #4**

The principal at Crest Middle School, which enrolls only sixth-grade students and seventh-grade students, is interested in determining how much time students at that school spend on homework each night. The table below shows the mean and standard deviation of the amount of time spent on homework each night (in minutes) for a random sample of 20 sixth-grade students and a separate random sample of 20 seventh-grade students at this school.

+------------------------+--------------+--------------------+
|                        |     Mean     | Standard Deviation |
+------------------------+--------------+--------------------+
| Sixth-grade students   |      27.3    |       10.8         |
+------------------------+--------------+--------------------+
| Seventh-grade students |      47.0    |       12.4         |
+------------------------+--------------+--------------------+

Based on dotplots of these data, it is not unreasonable to assume that the distribution of times for each grade were approximately normally distributed.

	a. Estimate the difference in mean times spent on homework for all sixth- and seventh-grade students in this school using an interval. Be sure to interpret your interval.

	b. An assistant principal reasoned that a much narrower confidence interval could be obtained if the students were paired based on their responses; for example, pairing the sixth-grade student and the seventh-grade student with the highest number of minutes spent on homework, the sixth-grade student and seventh-grade student with the next highest number of minutes spent on homework, and so on. Is the assistant principal correct in thinking that matching students in this way and then computing a matched-pairs confidence interval for the mean difference in time spent on homework is a better procedure than the one used in *part a* ? Explain why or why not.

2. **2009, Free Response, #4**

One of the two fire stations in a certain town responds to calls in the northern half of the town, and the other fire station responds to calls in the southern half of the town. One of the town council members believes that the two fire stations have different mean response times. Response time is measured by the difference between the time an emergency call comes into the fire station and the time the first fire truck arrives at the scene of the fire.

Data were collected to investigate whether the council member’s belief is correct. A random sample of 50 calls selected from the northern fire station had a mean response time of 4.3 minutes with a standard deviation of 3.7 minutes. A random sample of 50 calls selected from the southern fire station had a mean response time of 5.3 minutes with a standard deviation of 3.2 minutes.

	a. Construct and interpret a 95 percent confidence interval for the difference in mean response times between the two fire stations.

	b. Does the confidence interval in part (a) support the council member’s belief that the two fire stations have different mean response times? Explain.

Proportions
===========

.. topic:: Confidence Interval for Population Proportion

	TODO
	
.. topic:: Confidence Interval for Difference of Two Population Proportions

	TODO
	
1. **2010, Free Response Form B, #4**

A husband and wife, Mike and Lori, share a digital music player that has a feature that randomly selects which song to play. A total of 2,384 songs were loaded onto the player, some by Mike and the rest by Lori. Suppose that when the player was in the random-selection mode, 13 of the first 50 songs selected were songs loaded by Lori.

	a. Construct and interpret a 90 percent confidence interval for the proportion of songs on the player that were loaded by Lori.

	b. Mike and Lori are unsure about whether the player samples the songs with replacement or without replacement when the player is in random-selection mode. Explain why this distinction is not important for the construction of the interval in *part a*.

2. **2010, Free Response, #3**

A humane society wanted to estimate with 95 percent confidence the proportion of households in its county that own at least one dog.

	a. Interpret the 95 percent confidence level in this context.

The humane society selected a random sample of households in its county and used the sample to estimate the proportion of all households that own at least one dog. The conditions for calculating a 95 percent confidence interval for the proportion of households in this county that own at least one dog were checked and verified, and the resulting confidence interval was 0.417 ± 0.119.

	b. A national pet products association claimed that 39 percent of all American households owned at least one dog. Does the humane society's interval estimate provide evidence that the proportion of dog owners in its county is different from the claimed national proportion? Explain.

	c. How many households were selected in the humane society's sample? Show how you obtained your answer.

3. **2022, Free Response, #4**

A survey conducted by a national research center asked a random sample of 920 teenagers in the United States how often they use a video streaming service. From the sample, 59% answered that they use a video streaming service every day.

	a. Construct and interpret a 95% confidence interval for the proportion of all teenagers in the United States who would respond that they use a video streaming service every day.

	b. Based on the confidence interval in *part a*, do the sample data provide convincing statistical evidence that the proportion of all teenagers in the United States who would respond that they use a video streaming service every day is not 0.5 ? Justify your answer.

4. **2018, Free Response, #2**

An environmental science teacher at a high school with a large population of students wanted to estimate the proportion of students at the school who regularly recycle plastic bottles. The teacher selected a random sample
of students at the school to survey. Each selected student went into the teacher’s office, one at a time, and was asked to respond yes or no to the following question.

	Do you regularly recycle plastic bottles?

Based on the responses, a 95 percent confidence interval for the proportion of all students at the school who would respond yes to the question was calculated as :math:`(0.584, 0.816)`.

	a. How many students were in the sample selected by the environmental science teacher?

	b. Given the method used by the environmental science teacher to collect the responses, explain how bias might have been introduced and describe how the bias might affect the point estimate of the proportion of all students at the school who would respond yes to the question.

	c. The statistics teacher at the high school was concerned about the potential bias in the survey. To obtain a potentially less biased estimate of the proportion, the statistics teacher used an alternate method for collecting student responses. A random sample of 300 students was selected, and each student was given the following instructions on how to respond to the question.

- In private, flip a fair coin.
- If heads, you must respond no, regardless of whether you regularly recycle.
- If tails, please truthfully respond yes or no.

	i. What is the expected number of students from the sample of 300 who would be required to respond no because the coin flip resulted in heads?

	ii. The results of the sample showed that 213 of the 300 selected students responded no. Based on the results of the sample, give a point estimate for the proportion of all students at the high school who would respond yes to the question.
	
5. **2017, Free Response, #2**

TODO

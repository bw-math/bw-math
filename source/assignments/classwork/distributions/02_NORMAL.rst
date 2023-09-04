.. _normal_distribution_classwork:

===================
Normal Distribution
===================

TODO

?. **2003, Free Response, #3** 

Men's shirt sizes are determined by their neck sizes. Suppose that men's neck sizes are approximately normally distributed with mean 15.7 inches and standard deviation 0.7 inch. A retailer sells men's shirts in sizes S, M, L, XL, where the shirt sizes are defined in the table below.

.. image:: ../../../assets/imgs/classwork/2003_apstats_frp_3.png
    :align: center

a. Because the retailer only stocks the sizes listed above, what proportion of customers will find that the retailer does not carry any shirts in their sizes? Show your work.

b. Using a sketch of a normal curve, illustrate the proportion of men whose shirt size is M. Calculate this proportion.

c. Of 12 randomly selected customers, what is the probability that exactly 4 will request size M ? Show your work.


?. **2014, Free Response, #3**

Schools in a certain state receive funding based on the number of students who attend the school. To determine the number of students who attend a school, one school day is selected at random and the number of students in attendance that day is counted and used for funding purposes. The daily number of absences at High School A in the state is approximately normally distributed with mean of 120 students and standard deviation of 10.5 students.

a. If more than 140 students are absent on the day the attendance count is taken for funding purposes, the school will lose some of its state funding in the subsequent year. Approximately what is the probability that High School A will lose some state funding?

b. The principals' association in the state suggests that instead of choosing one day at random, the state should choose 3 days at random. With the suggested plan, High School A would lose some of its state funding in the subsequent year if the mean number of students absent for the 3 days is greater than 140. Would High School A be more likely, less likely, or equally likely to lose funding using the suggested plan compared to the plan described in part *#a*? Justify your choice.

.. hint:: 

    Counter-intuitively, this problem can be better understood if you let "*losing funding*" represent a success. In other words, the principal's association is conducting an experiment with a binary outcome: with the school loses funding (*success*) or the school keeps funding (*failure*)
    
    You calculated the probability of success in part *#a*.

    The number of absences on a given day is *independent* of the number of absences on any other day.

    The number of trials is the number of days the principal's association chooses to observe the absentee rate. 

    What kind of :ref:`binomial_random_variable` is this?

d. A typical school week consists of the days Monday, Tuesday, Wednesday, Thursday, and Friday. The principal at High School A believes that the number of absences tends to be greater on Mondays and Fridays, and there is concern that the school will lose state funding if the attendance count occurs on a Monday or Friday. If one school day is chosen at random from each of 3 typical school weeks, what is the probability that none of the 3 days chosen is a Tuesday, Wednesday, or Thursday?
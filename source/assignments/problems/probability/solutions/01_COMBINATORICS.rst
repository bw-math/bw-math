
Solutions
=========

Counting Principle
------------------

TODO

Combinations
------------

TODO 

Probability
-----------

1. TODO

2. The word "*atleast*" is a red flag in problems involving probability. If you see the word "*atleast*", it is a fair bet you will need to find the complement of a set at some point. To see why, note the way this problem is phrase can be interpretted with the :ref:`square_of_opposition`. The *Square of Opposition* is pictured below for quick reference,

.. image:: ../../../assets/imgs/sets/square_of_opposition.jpg
	:align: center

The *Square* tells us the complement of "*some are*" ("atleast one") is "*none are*". Therefore, we can express the probability this problem is seeking with the :ref:`law_of_complements`,

.. math::

	P(A) = 1 - P(A^c)    

Where :math:`A^c` corresponds to the event of getting *no heads*. 

This is equivalent to getting all tails, which is a much simpler event to find, because it only has one outcome, namely ``ttt``. 

To calculate the probability of this event, we apply the :ref:`counting_principle` to find the total number of ways the experiment can occur. Each flip has two outcomes, heads or tails. There are three flips in total. Thus,

.. math::

	n(S) = 2 \cdot 2 \cdot 2 = 8

The probability sought can then be calculated as,

.. math::

        P(A) = 1 - \frac{1}{8} = \frac{7}{8}

.. _confidence_intervals:

====================
Confidence Intervals
====================

Definitions
===========

Critical Value
--------------

TODO

.. topic:: Critical Z Value

	.. math::
	
		z_{p} \equiv P(\mathcal{Z} \leq z_{p}) = \frac{p}{100}

		
.. topic:: Critical T Value

	.. math::
	
		t_{p} \equiv P(\frac{\bar{\mathcal{X}}-\mu}{\mathcal{S}} \leq t_p) = \frac{p}{100}

Standard Error
--------------

TODO 
		
.. topic:: Standard Error, Sample Mean

	.. math::
	
		\text{SE}_{\bar{X}} = \frac{s}{\sqrt{n}}
	
.. topic:: Standard Error, Difference of Means

	.. math::
	
		\text{SE}_{\bar{X}_2 - \bar{X}_1} = \sqrt( \frac{ s_{ \bar{x}_1 } }{n_1} + \frac{ s_{ \bar{x}_2 } }{n_2} )
	
Margin of Error
---------------

.. topic:: Margin of Error, Known Standard Deviation

	.. math::
	
		\text{MOE} = \lvert z_{1-\frac{\alpha}{2}} \rvert \cdot \text{SE}

.. topic:: Margin of Error, Unknown Standard Deviation

	.. math::
	
		\text{MOE} = \lvert t_{1-\frac{\alpha}{2}} \rvert \cdot \text{SE}		
		
Intervals
=========

TODO

Population Mean
---------------
	
TODO

.. topic:: Confidence Interval For Population Mean

	.. math::
	
		\bar{x} - \text{MOE} \leq \mu \leq \bar{x} + \text{MOE}

TODO 

Difference of Population Means
------------------------------

TODO 

.. topic:: Confidence Interval for Difference of Population Means

	.. math::
	
		(\bar{x_2} - \bar{x_1}) - \text{MOE} \leq \mu_2 - \mu_1 \leq (\bar{x_2} - \bar{x_1}) + \text{MOE}

TODO

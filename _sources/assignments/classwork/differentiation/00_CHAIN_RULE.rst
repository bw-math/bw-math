.. _chain_rule_classwork:

==========
Chain Rule 
==========

.. topic:: Composite Functions

	.. math::
	
		f \circ g (x) = f( g(x) )
		
.. topic:: The Chain Rule

	.. math::
	
		\frac{d}{dx}( f \circ g (x) ) = f^{\prime}(g(x)) \cdot g^{\prime} (x)

1. **The Gaussian Function**

The Normal density function, sometimes called the *Gaussian* function in honor of Johann Carl Friedrich Gauss who discovered its formula, is an important function in statistics. 

Graphically, the Normal density curve is a *bell curve*. Roughly speaking, the value of the *Gaussian* function at a point :math:`x` represents the *probability* of making an observation :math:`x`, when the observation is randomly selected from a population of values whose arithmetical average is :math:`\mu`.

The *Gaussian* function is given by,

.. math::

	\rho ( x ) = \frac{ 1 }{ \sqrt{2 \cdot \pi \cdot \sigma^2} } \cdot e ^ { - \frac{ (x-\mu)^2  }{ 2 \cdot \sigma^2} }
	
The constants, :math:`\mu` and :math:`\sigma`, are *parameters* of the density function. These parameters determine the shape and curvature of the bell curve. They are *known* quantities; in other words, they may be held constant and treated as numbers. 

Use the Normal density function to answer the following questions.


a. Find :math:`\frac{d}{dx}(\rho (x) )`


b. Find :math:`\frac{d^2}{{dx}^2}(\rho (x))`


c. Find the value of :math:`x` where :math:`\frac{d}{dx}(\rho (x) ) = 0`. Solve symbolically in terms of :math:`\mu` and :math:`\sigma`.

.. hint::

     :math:`e^x` never equals 0!

d. Find the **values** of :math:`x` where :math:`\frac{d^2}{{dx}^2}(\rho (x)) = 0`. What is the value of :math:`\rho^{\prime}(x)` at these points? Solve symbolically in terms of :math:`\mu` and :math:`\sigma`.

e. Suppose :math:`\mu=10` and :math:`\sigma=2`. Use a graphing utility (`Desmos is good for this <https://desmos.com>`_) to plot the Normal density function. Draw vertical lines at the values of :math:`x` found in *part c* and *part d*. 

f. Suppose :math:`\mu=10` and :math:`\sigma=2`. Find the **equation** of the tangent line at the following points (yes, all of them). Round to four decimal places where appropriate.

	i. :math:`x = 17`
	
	ii. :math:`x = 15`
	
	iii. :math:`x = 13`
	
	iv. :math:`x = 11`
	
	v. :math:`x = 9`
	
	vi. :math:`x = 7`
	
	vii. :math:`x = 5` 
	
	viii. :math:`x = 3`

g. Plot the tangent lines on top of the Normal density function using the same graphing utility as *part e*. 

h. Find the value of :math:`\rho^{\prime \prime}(x)` at each point in *part f*.

i. Suppose :math:`\mu=10` and :math:`\sigma=2`. Plot the first and second derivative of the given Normal density curve on the same graph as *part e*. 

j. What happens to the Normal density function at the point found in *part c*?

k. What happens to the Normal density function at the points found in *part d*?

.. hint:: 

	What happens to the *direction* of the tangent line at each of the *critical points* found in *part d*? Look at the tangent lines plotted in *part g*!


2. **Deriving the Quotient Rule**

Recall the *Product Rule* and *Quotient Rule* for differentiation,
	
.. topic:: The Product Rule

	.. math:: 
		
		\frac{d}{dx}(f(x) \cdot g(x)) = f^{\prime}(x) \cdot g(x) + f(x) \cdot g^{\prime} (x) 
		
.. topic:: The Quotient Rule

	.. math:: 
	
		\frac{d}{dx}( \frac{f(x)}{g(x)} ) = \frac{ f^{\prime}(x) \cdot g(x) - f(x) \cdot g^{\prime} (x) } { (g(x))^2 }

The *Product Rule* is simpler to remember than the *Quotient Rule*. Moreover, the *Quotient Rule* can be *derived* from the *Product Rule* using the *Chain Rule*, if we recall one simple rule of exponents,

.. math::

	\frac{1}{a} = a ^ {-1}
	
In this problem, we will show how to apply this property of exponents to get the *Quotient Rule* from the *Product* and *Chain Rule*. 

a. Write the quotient :math:`\frac{f(x)}{g(x)}` as a product using a negative exponent. 

b. Take the derivative of the expression in *part a* by applying the *Product Rule* and then the *Chain Rule*.

c. Find a common denominator and simplify the expression in *part b*. 

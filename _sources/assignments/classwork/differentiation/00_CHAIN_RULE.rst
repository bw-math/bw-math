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

The Normal density function, sometimes called the *Gaussian* function in honor of Johann Carl Friedrich Gauss who discovered its formula, is an important function in statistics. Graphically, the Normal density curve is a *bell curve*. Its functional form is given by,

.. math::

	\rho ( x ) = \frac{ 1 }{ sqrt{2 \cdot \pi \cdot \sigma^2} } \cdot e ^ { - \frac{ (x-\mu)^2  }{ 2 \cdot \sigma^2} }
	
The constants, :math:`\mu` and :math:`\sigma`, are *parameters* of the density function. These parameters determine the shape and curvature of the bell curve. They are *known* quantities; in other words, they may be held constant and treated as numbers. Use the Normal density function to answer the following questions.


a. Find :math:`\frac{d}{dx}(\rho (x) )`


b. Find :math:`\frac{d^2}{{dx}^2}(\rho (x))`


c. Find the value of :math:`x` where :math:`\frac{d}{dx}(\rho (x) ) = 0`


d. Find the **values** of :math:`x` where :math:`\frac{d^2}{{dx}^2}(\rho (x)) = 0`

e. Suppose :math:`\mu=10` and :math:`\sigma=2`. Use a graphing utility (`Desmos is good<https://desmos.com>`) to plot the Normal density function. Draw vertical lines at the values of :math:`x` found in *part c* and *part d*. 

f. Find the **equation** of the tangent line at the following points (yes, all of them),

	i. :math:`x = 17`
	
	ii. :math:`x = 15`
	
	iii. :math:`x = 13`
	
	iv. :math:`x = 11`
	
	v. :math:`x = 9`
	
	vi. :math:`x = 7`
	
	vii. :math:`x = 5` 
	
	viii. :math:`x = 3`

g. Plot the tangent lines using the same graphing utility 

h. Describe what is happening to the derivative at each point on the curve labelled in *part e*. 

.. hint:: 

	What happens to the *direction* of the tangent line at each of the *critical points* found in *part e*?


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

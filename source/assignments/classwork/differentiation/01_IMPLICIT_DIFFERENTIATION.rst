.. _implicit_differentiation_classwork:

========================
Implicit Differentiation
========================

1. **Introduction**

For each of the following problems:

- Find :math:`y^{\prime}` by solving the equation for :math:`y` and differentiating directly.
- Find :math:`y^{\prime}` by implicit differentiation.
- Check the derivatives obtained through both methods are the same.

a. :math:`\frac{x}{y^3} = 1`

b. :math:`x^2 + y^3 = 4`

2. **Applications**

Use implicit differentiation to solve the following problems:

a. :math:`2 \cdot y^3 + 4 \cdot x^2 - y = x^6` 

b. :math:`7 \cdot y^2 + \sin(3x) = 12 - y^4`

c. :math:`e^x - \sin(y) = x`

d. :math:`\cos(x^2 + 2y) + x \cdot e^{y^2} = 1`

e. :math:`\tan(x^2 \cdot y^4) = 3x + y^2`

3. **A Pointless Problem**

.. important::

	Take time to appreciate the pun here. If you don't get it yet, you will.

Consider the function :math:`f(x,y)`,

.. math::

	x^2 + y^2 = 9

a. Plot this function in the x-y plane. (`Desmos is good for this <https://desmos.com>`_). What kind of graph is this?

.. important::

	Do you get it now?!
	
b. Use implicit differentiation to find :math:`\frac{dy}{dx}`. Express the answer as a function of :math:`x` only.

c. Find the equation of the tangent line at the points :math:`(\pm \frac{3 \cdot \sqrt{2}}{2}, \pm \frac{3 \cdot \sqrt{2}}{2})`

d. Plot the tangent lines on top of the graph you created in *part a*. 

e. Find the points :math:`(x,y)` where the tangent lines found in *part c* intersect. 

f. Plot the points found in *part e* on top of the graphs you created in *part a* and *part d*.

g. What is the *area* of the quadrilateral formed by the tangent lines in *part c*? 

4. **Natural Log Derivative**

The formula for the derivative of the natural log, :math:`ln(x)`, can be derived with *implicit differentiation*. To do so, recall the differentiaion rule for exponential functions,

.. topic:: Exponential Derivative

	.. math::
	
		\frac{d}{dx}(e^x) = e^x
		
Then define *y* as,

.. math::

	y = \ln(x)
	
Use *implicit differentiation* to derive the formula for,

.. math::
	
	\frac{d}{dx}(ln(x)) = \frac{1}{x}
	
.. hint::
	
	Solve for :math:`x` and then apply the *Chain Rule*.
	
5. **Inverse Trigonometric Derivatives**

In class we used *implicit differentiation* to derive, 

.. math::

	\frac{d}{dx}( \arcsin(x) ) = \frac{1}{\sqrt{1-x^2}}
	
Using a similar process, find the derivatives of the following inverse trigonometric functions,

a. :math:`f(x) = \arccos(x)`

b. :math:`f(x) = \arctan(x)`

.. hint::

	Remember to draw a diagram of the unit circle. Express *x* and *y* in terms of lengths and angles!
	
6. **2005, Free Response Form B, #5**

Consider the curve given by,

.. math::

	y ^2 = 2 + xy
	
a. Show that

.. math:: 

	\frac{dy}{dx} = \frac{y}{2y -x}

b. Find all points :math:`(x,y)` on the curve where the line tangent to the curve has slope :math:`\frac{1}{2}`.

c. Show that there are no points :math:`(x,y)` on the curve where the line tangent to the curve is horizontal.

d. Let x and y be functions of time t that are related by the equation :math:`y^2 = 2 + xy` . At time :math:`t = 5`, the value
of :math:`y` is 3 and :math:`\frac{dy}{dt} = 6`. Find the value of :math:`\frac{dx}{dt}` at time :math:`t = 5`.

7. **2023, Free Response, #6**

Consider the curve given by the equation, 

.. math::

	6xy = 2 + y^3
	
a. Show that,

.. math::

	\frac{dy}{dx} = \frac{2y}{y^2 - 2x}
	
b. Find the coordinates of a point on the curve at which the line tangent to the curve is horizontal, or explain why no such point exists.

c. Find the coordinates of a point on the curve at which the line tangent to the curve is vertical, or explain why no such point exists.

d. A particle is moving along the curve. At the instance when the particle is at the point :math:`(\frac{1}{2}, -2)`, its horizontal position is increasing at a rate of :math:`\frac{dx}{dt}=\frac{2}{3}` units per second. What is the value of :math:`\frac{dy}{dt}`, the rate of change of the particle's vertical position, at that instant?

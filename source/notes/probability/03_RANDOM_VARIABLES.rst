.. _random_variables:

================
Random Variables
================

Many things in life are *uncertain*. Nevertheless, *uncertainy* doesn't equate to *unpredictability*. Even though events may be *uncertain*, we can still make *predictions* about their outcome based on our knowledge of the sample space.

Definition
==========

.. _random_variable: 

Random Variable
    :math:`\mathcal{X}`

    A *random variable* is a quantity whose value is *uncertain*; A *random variable* depends on a random event.

Example
    A friend flips a fair, two-sided coin. If it lands on heads, he will pay you five dollars. If it lands on tails, you have to pay him five dollars. 

The sample space for this simple game is given by,
    
.. :math::
    S = \{ h, t \}

The amount of money you win or lose is a *random variable* that depends on the outcome of the coin flip, i.e. whether the event of :math:`H = \{ h \}` or the event :math:`T = \{ *t* \}` from the sample space occurs. Using this information, we can define the *random variable* for the amount of money won or lost playing this game as follows,

.. :math::
    \mathcal{X} = \begin{array}{ c l }
        5       & \quad \textrm{with } p(H) \\
        -5      & \quad \textrm{with } p(T)
    \end{array}


We can use a table to visualize the outcomes of this *random variable* and their associated probabilities,

+------+---------------+
|   x  |   P(X = x)    |
+------+---------------+
|  5   |   P(H) = 0.5  |
+------+---------------+
| -5   |   P(T) = 0.5  |
+------+---------------+

Notice this is similar in form and function to a :ref:`frequency distribution <frequency_distributions>`.

Example
    Suppose you own a car that gets 30 miles per gallon of gasoline. Due to your commute, you drive your car approximately 120 miles every week. Describe the cost of operating your car as a random variable measured in dollars.
    
Your weekly cost of keeping your tank full is given by the expression

    (Weekly Cost of Gas) = (Price per Gallon of Gasoline) :math:`\cdot` (Gallons Used)

If we assume you drive the exactly same amount every week, the second term on the right hand side of the expression can be written as,

    (Gallons Used) = :math:`\frac{120 miles}{30 mpg} = 4 gallons`

The price per gallon of gasoline, however, is an *uncertain* quantity; it depends on many extranenous factors, such as political conditions, shipping costs, taxes and tariffs, weather and climate, etc. Because of this, the price changes from day to day. 

The uncertainty in the price of gasoline becomes uncertainty in the weekly cost of driving your car. Therefore, we can model the weekly cost of gas as a *random variable*,

.. math::
    \mathcal{X} \frac{\$}{gal} \cdot \text{4 gal }
    
where :math:`\mathcal{X}` is the price of gasoline measured in dollars per gallon.

Random Variables
================

A *random variable* is not very well named. A more suitable name would be *random function*. In this section, the reason for this will be explored. We will examine the connection between *random variables* and *functions*.

Review of Functions
-------------------

Recall the concept of a *function* from your other mathematics classes. You probably remember a definition along the lines, "A function :math:`f(x)` receives an input *x* and assigns to it a value *y*." This definition has served you in your mathematics career up to this point, but it will no longer suffice. This is not *precisely* what a function is, though it is a close approximation. In order to understand what a *random variable* is, the concept of a *function* must be extended and enlarged to encompass a larger *set* of ideas (pun intended). 

When the concept of *functions* is first taught, students are encouraged to treat a function as an algebraic expression, such as :math:`f(x) = x^2`. It's an algebraic *thing* that you plug numbers into and out of which you get numbers, which may or may not be the same numbers that were inputted (consider the output of  :math:`f(x) = x` versus :math:`f(x) = x^2`; what is the difference between the set of things output by each of these function?). When `f(x)=x^2`, we put `x = 5` and get `f(5) = 25`, which describes an ordered pair in the **Cartesian** plane, :math:`(5, f(5))`. Students are told about the *domain* and *range*; The :ref:`set <sets>` of all values that are input into a function is called the *domain*. Likewise, the set of all values that is output by the function is called the *range*. You probably remember seeing a diagram to help you visualize this idea and it probably looked like this,

.. image:: ../../assets/imgs/probability/function.png

And then you studied various types of algebraic functions, such as logs and sines. You learned about the joy of factoring and finding roots. You plotted curves and found inflection points. Life was idyllic; It seemed as though nothing could ever shatter the peace and serenity you were blessed with amidst the glory of algebra. However, this is not the whole story.

Extension of The Concept of a Function
--------------------------------------

The concept of a *function* underwent a radical change in the early 20 :sup:`th` century as set theory was developed by people with names like `Guiseppe Peano <https://en.wikipedia.org/wiki/Giuseppe_Peano>`_ and `Ernst Zermelo <https://en.wikipedia.org/wiki/Ernst_Zermelo>`_ to formalize the foundation of mathematics. To see why the notion of a function had to be extended, consider the following propositions,

    The set of all unicorns has zero elements.

    The set of all humans has seven billion elements. 

    The set of all natural numbers is infinite.

    The set of all prime numbers is infinite.

These statements could be translated into :ref:`set theoretic <set_theory>` symbols in the following way,

.. math:: 
    n(\{ \forall x: x \in U \}) = 0

.. math:: 
    n(\{ \forall x: x \in H \}) = 7,000,000,000

.. math::
    n(\mathbb{N}) = \infty

.. math:: 
    n(P) = \infty

If the specifics were abstracted away, this would lead to an expression that looks like,

.. math:: 
    n(x) = y

In each case, the cardinality of *something* is being asserted. In other words, a *value* is being assigned to an input, but what exactly is the input? Each proposition is asserting a property of an entire :ref:`set <sets>`; this suggests the constraint that functions are *numbers* be relaxed so that we may input *sets* into *funtions*.

Put in the parlance of modern mathematics, a function *maps* a value to a given set. The set of all values that are mapped is likewise a set of *things*. This leds to the idea of a *function* as a map between sets. A *function* takes elements from one set and *maps* them to the elements of another set. This slight change in the way functions are talked about leads to a revision of the diagram given at the beginning of this section,

.. image:: ../../assets/imgs/probability/random_variable.png
    :align: center

This suggests we view random variables as *functions* of the outcomes in sample space, 

.. math:: 
    \mathcal{X} = f(A)

.. math:: 
    \text{where} A \subseteq S

This is getting closer to the truth. However, this picture is not yet complete; it doesn't include probability. The outcomes in the sample space are *uncertain*.

The outcomes in a event determine the value of the random variable in the same way the values inputted into a function determine the output of the function. However, the input to a random variable is uncertain, therefore the output is likewise uncertain. The probability of an event occuring in the sample space is transferred, through the outcomes that determine the random variable, into the probability of a random variable assuming a particular value. An event (set) of outcomes in the *sample space* becomes an assignment of a particular value to a *random variable*,

.. image:: ../../assets/imgs/probability/random_variable.png
    :align: center

A random variable shows how events from the sample space (the domain) are transformed into events of the random variable (the range). 

Random Variables and Events
---------------------------


.. _density_function:

Density Function 
    TODO 

    The *density function* should be familiar. We have already encountered its statistical analogue, :ref:`frequency`. The probability density of a random variable at a certain value is analogously to the *frequency* of an observation in a sample of data.
    
.. _distribution_function:

Distribution Function
    TODO 

.. _expectation:

Expectation
===========

TODO

Expectation of a Sum
--------------------

:math:`E(X+Y)=E(X) + E(Y)`
    TODO

.. _variance:

Variance
========

TODO 

.. _bernoulli_distribution:

Bernoulli Random Variable
=========================

.. math::
    p(x) = P(X = x) = \begin{array}{ c l }
        p       & \quad \textrm{if } x = 1 \\
        1 - p   & \quad \textrm{if } x = 0
    \end{array}

.. _uniform_distribution:

Uniform Random Variable
=======================

TODO
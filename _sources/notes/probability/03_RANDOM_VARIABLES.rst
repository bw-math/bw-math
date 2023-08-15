================
Random Variables
================

Many things in life are *uncertain*. Nevertheless, *uncertainy* doesn't equate to *unpredictability*. Even though events may be *uncertain*, we can still make *predictions* about their outcome based on our knowledge of the sample space.

Definition
==========

Random Variable
    A *random variable* is a quantity whose value is *uncertain*; A *random variable* depends on a random event.

.. :collapse:: Scenario

    A friend flips a fair, two-sided coin. If it lands on heads, he will pay you five dollars. If it lands on tails, you have to pay him five dollars. 

    The sample space for this simple game is given by,
        
        .. :math::
            S = \{ h, t \}

    The amount of money you win or lose is a *random variable* that depeonds on the outcome of the coin flip, i.e. whether the event of *h* or the event *t* from the sample space occurs. Using this information, we can define the *random variable* for the amount of money won or lost playing this game as follows,

        .. :math::
            TODO TERNARY DEFINITION


    We can use a table to visualize the outcomes of this *random variable* and their associated probabilities,

    +------+--------+
    |   X  |   P(X) |
    +------+--------+
    |  5   |   0.5  |
    +------+--------+
    | -5   |   0.5  |
    +------+--------+

.. :collapse:: Scenario

    Suppose you own a car that gets 30 miles per gallon of gasoline. Due to your commute, you drive your car approximately 120 miles every week. Then, your weekly cost of keeping your tank full is given by the expression

        (Weekly Cost of Gas) = (Price per Gallon of Gasoline) :math:`\cdot` (Gallons Used)

    If we assume you drive the exactly same amount every week, the second term on the right hand side of the expression can be written as,

        (Gallons Used) = :math:`\frac{120 miles}{30 mpg} = 4 gallons`

    The price per gallon of gasoline, however, is an *uncertain* quantity; it depends on many extranenous factors, such as political conditions, shipping costs, taxes and tariffs, weather and climate, etc. Because of this, the price changes from day to day. 

    The uncertainty in the price of gasoline becomes uncertainty in the weekly cost of driving your car. Therefore, we can model the weekly cost of gas as a *random variable*,

        :math:`4X`
       
    where **X** is the price of gasoline measured in dollars.

.. :warning:: 

    A random variable is a function from the sample space **S** to the real numbers between 0 and 1. 

    TODO

Probability Mass Function 
    TODO 

Distribution Function
    TODO 

Expectation
===========

TODO

Expectation of a Sum
--------------------

:math:`E(X+Y)=E(X) + E(Y)`
    TODO

Variance
========

TODO 
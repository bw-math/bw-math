.. _binomial_distribution:

=====================
Binomial Distribution
=====================

.. _binomial_random_variable:

Binomial Random Variable
========================

Recall a :ref:`bernoulli_random_variable` is defined over a sample space of binary outcomes, a success ``s`` that occurs with probability :math:`p` of success and a failure ``f`` that occurs with probability :math:`1-p`,

.. math::
    Y = \begin{array}{ c l }
        1                 & \quad \textrm{with probability} p \\
        0                 & \quad \textrm{with probability } 1 - p
    \end{array}

Consider a random variable defined as the sum of :math:`n` **Bernoulli** random variables, :math:`Y_i`

.. math:: 
    X = Y_1 + Y_2 + ... + Y_{n-1} + Y_n

Where each :math:`Y_i` takes the value 1 with probability :math:`p` or it takes the value 0 with probabilitiy :math:`1 - p`

TODO 

From :ref:`conditional_probability`, the probability of an intersection of :ref:`independent events <independence>` is the product of individual probabilitiy,

.. math:: 

    P(A \cap B) = P(A) \cdot P(B)

TODO

Probabilitiy Distribution
=========================

TODO 

.. math:: 
    p(x; n, p) = C^{n}_x \cdot p^{x} \cdot (1 - p)^{n-x}

TODO

.. plot:: assets/plots/distributions/binomial/binomial_distribution_01.py

.. plot:: assets/plots/distributions/binomial/binomial_distribution_02.py

.. plot:: assets/plots/distributions/binomial/binomial_distribution_03.py

.. plot:: assets/plots/distributions/binomial/binomial_distribution_04.py



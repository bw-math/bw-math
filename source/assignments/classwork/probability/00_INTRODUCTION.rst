.. _probability_introduction_classwork:

============
Introduction
============

Sample Spaces and Events
========================

1. Describe the sample spaces of the following experiments with a set using :ref:`list_notation`

    a. Flipping a two-sided coin three times
    b. Rolling a six-sided die
    c. Rolling two six-sided dice
    d. Flipping a two-sided coin and if it lands on heads rolling a six-sided die.

.. collapse:: Solution #1

    a. Let *h* represent a single coin flip landing on heads. Let *t* represent a single coin flip landing on tails. A :ref:`tree diagram <tree_diagrams>` is useful for visualizing the sample space here,

    (TODO: insert image)

    Collecting the endpoints of the diagram into a set,

    .. math::

        S = \{ hhh, hht, hth, thh, tth, tht, htt, ttt \}

    b. Let *1*, *2*, *3*, *4*, *5* and *6* represent rolling a die with that number of dots. Then,

    .. math:: 

        S = \{ 1, 2, 3, 4, 5, 6 \}

    c. Construct a table where the first column represents the outcome of the first die and the first row represents the outcome of the second die. Fill in each entry of the table by listing the outcomes as an ordered pair (*x*, *y*),

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   | (1, 1) | (1, 2) |  (1, 3) |  (1, 4)  | (1, 5) | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) | (2, 2) |  (2, 3) |  (2, 4)  | (2, 5) | (2, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   | (3, 1) | (3, 2) |  (3, 3) |  (3, 4)  | (3, 5) | (3, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) | (4, 2) |  (4, 3) |  (4, 4)  | (4, 5) | (4, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   | (5, 1) | (5, 2) |  (5, 3) |  (5, 4)  | (5, 5) | (5, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) | (6, 6) |  (6, 3) |  (6, 4)  | (6, 5) | (6, 6) |
    +-------+--------+--------+---------+----------+--------+--------+

    If we were so included, we could conclude the problem by listing these ordered pairs in :ref:`list_notation`,

    .. math::

        S =\{ (1,1), (1,2), ..., (6,5), (6,6) \}

    If we were presenting this set as a sample of data, we would not be able to "...", unless it was understood by the audience how the set of the ordered pairs were being generated. However, listing all of these elements (6 rows by 6 columns = 36 entries/elements) would be tedious and time consuming. As an alternative, let us write the same set using :ref:`quantifier_notation`. To do so, let the set **A** be ,

    .. math::
        A = \{ 1, 2, 3, 4, 5, 6 \}

    We can *quantify* over the elements in set **A** *twice* to arrive at an alternate solution.

    .. math::

        S = \{ \forall x \in A, y \in A: (x, y) \}

    .. note::

        Technically, in the solution, we are using a bit of short-hand. The way it is written there is *implicitly* two quantification occuring. For all selecting all the elements in **A** through :math:`\forall x`, and then for each element we have selected, we are selecting each element of **A** again through :math:`\forall y` 
        
        If we wanted to be as precise as possible, we should write,

        :math:`S = \{ \forall x \in A: (\forall y \in A: (x,y)) \}`

        However, this is overly complicated and not very clear; There is nothing gained by adopting this notation. If this were an post-graduate level course in the foundations of set theory, we would be much more careful with how we formulate propositions in our symbolic language. However, we will continue using short-hand when applicable.

    d. :math:`S = \{ t, h1, h2, h3, h4, h5, h6 \}`

2. Two dice are rolled. Let **E** be the event the sum of the outcomes is odd. Let **F** be the event of at least one *1* appearing on one of the die. Describe the elements of the following events in :ref:`list_notation` and interpret the meaning of each event.

    a. :math:`E \cap F`
    b. :math:`E^c \cap F`
    c. :math:`E^c \cap F^c`
    d. :math:`E \cup F`
    e. :math:`E \cup F^c`

.. collapse:: Solution #2

    The sample space from #1c will be useful here, so let's copy it for reference,

    Table 1: Outcomes
        The outcomes of two die rolls.

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   | (1, 1) | (1, 2) |  (1, 3) |  (1, 4)  | (1, 5) | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) | (2, 2) |  (2, 3) |  (2, 4)  | (2, 5) | (2, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   | (3, 1) | (3, 2) |  (3, 3) |  (3, 4)  | (3, 5) | (3, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) | (4, 2) |  (4, 3) |  (4, 4)  | (4, 5) | (4, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   | (5, 1) | (5, 2) |  (5, 3) |  (5, 4)  | (5, 5) | (5, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) | (6, 6) |  (6, 3) |  (6, 4)  | (6, 5) | (6, 6) |
    +-------+--------+--------+---------+----------+--------+--------+

    This problem is asking questions about the *sum* of outcomes, so let's rework this table a bit. Instead of entering the outcomes as ordered pairs, we will calculate their sum and enter the result into each entry of the table,

    Table 2: Sum
        The sum of two die rolls.

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |    4     |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    2   |   3    |    4    |    5     |    6   |   7    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    3   |   4    |    5    |    6     |    7   |   8    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |    4   |   5    |    6    |    7     |    8   |   9    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |    5   |   6    |    7    |    8     |    9   |   10   |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |    6   |   7    |    8    |    9     |    10  |   11   |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |    7   |   8    |    9    |    10    |    11  |   12   |
    +-------+--------+--------+---------+----------+--------+--------+

    a. Recall the symbol :math:`\cap` correspond to the English "*and*". :math:`E \cap F` represents the event of rolling atleast one *1* *and* the sum of the rolls being odd. In other words, we need to look at the outcomes **E** and **F** have in common. 

    The outcomes of **F**, the event of getting at least one *1*, are given by the second row and second column of the Table 1 (the row and column with the headings of *1*). We can blank out the other rows, since they don't affect this problem and it will help us keep everythign organized,
    
    Table 1a-1: Outcomes
        The outcomes of **F**.

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   | (1, 1) | (1, 2) |  (1, 3) |  (1, 4)  | (1, 5) | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   | (3, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   | (5, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    
    Similarly, let's blank out the corresponding entries in Table 2,

    Table 2a-1: Sum
        The sum of two die rolls in F.
        
    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |    4     |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    2   |   3    |    4    |    5     |    6   |   7    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    3   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |    4   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |    5   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |    6   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |    7   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+

    Now, we need the outcomes that correspond to event **E**. These are the outcomes whose sum is odd. Removing those entries from the table we get,
    
    Table 1a-2: Outcomes
        The outcomes in :math:`E \cap F`

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |   -    | (1, 2) |    -    |  (1, 4)  |   -    | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |   -    |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |    -   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+

    Table 2a-2: Sum
        The sum of two die rolls in :math:`E \cap F`
        
    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |    4     |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    -   |   3    |    -    |    5     |   -    |   7    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    3   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |    -   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |    5   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |    -   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |    7   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+

    Looking at the second table for outcomes in this column and row that also have a sum that is odd (event **E**), we see the sums that correspond to this event are *3*, *5* and *7*. 
    
    In other words, the only sums that are odd if at least one of the die lands on *1* are *3*, *5* or *7*. 
    
    To say the same thing in a different way, if the sum of two die rolls is *odd*, then the only way to get a *1* is if the sum is *3*, *5* or *7*.

    We collect the ordered pairs that correspond to these sums into a set to complete the problem,
    
    .. math:: 

        E \cap F = \{ (1,2), (2,1), (4,1), (1,4), (6,1), (1,6) \}
 
    b. Recall the operation of :ref:`complementation <complement>` corresponds to the English word "*not*", i.e. the complement of a set is its *negation*.
    
    If a number is not odd, then it is even. Therefore, the set :math:`E^c` is the set of outcomes whose sum is *even*. 

    Thus, the intersection we desire :math:`E^c \cap F` is the set of even sums that have *atleast* one *1*. 
    
    Using a similar method to *part a*, we take Table 2a-1 and remove the outcomes that odd to find the outcomes in the event :math:`E ^c \cap F`,
    
    Table 1b
        The even sums with at least one *1*, :math:`E^c \cap F`

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |    4     |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    2   |    -   |    4    |    -     |    6   |   -    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    -   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |    4   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |    -   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |    6   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |    -   |   -    |   -     |     -    |   -    |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    
    We conclude the desired set is,

    .. math::

        E^c \cap F = \{ (1,1), (1,3), (3,1), (1,5), (5,1) \}

    c. The question requires the complement of **F**. Recall from the :ref:`square_of_opposition`, the complement of getting at least one *1* is getting *no* *1*'s, i.e. the negation of "*some are*" is "*none are*". Therefore, :math:`F^c` represents the event of getting no *1*'s.

    The intersection :math:`F^c \cap E^c` thus represents the event of getting an even sum that has no *1*'s. 
    
    To find the outcomes in the event, first find `F^c` (it doesn't actually matter which event/set you start with, just pick one and go with it)
    
    Table 1c-1
        The outcomes with no *1*'s, :math:`F^c`

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    -   |    -   |   -     |     -    |   -    |   -    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    -   | (2, 2) |  (2, 3) |  (2, 4)  | (2, 5) | (2, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |   -    | (3, 2) |  (3, 3) |  (3, 4)  | (3, 5) | (3, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |   -    | (4, 2) |  (4, 3) |  (4, 4)  | (4, 5) | (4, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |   -    | (5, 2) |  (5, 3) |  (5, 4)  | (5, 5) | (5, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |   -    | (6, 6) |  (6, 3) |  (6, 4)  | (6, 5) | (6, 6) |
    +-------+--------+--------+---------+----------+--------+--------+

    We want to intersect this event with the event of getting an even sum, :math:`E^c`. Thus, we remove entries with a odd sum,

    Table 1c-2
        The outcomes with no *1*'s that have even sums, :math:`E^c \cap F^c`

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    -   |   -    |   -     |     -    |   -    |   -    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    -   | (2, 2) |    -    |  (2, 4)  |   -    | (2, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |   -    |   -    |  (3, 3) |     -    | (3, 5) |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |   -    | (4, 2) |    -    |  (4, 4)  |    -   | (4, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |   -    |   -    |  (5, 3) |    -     | (5, 5) |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |   -    | (6, 6) |     -   |  (6, 4)  |   -    | (6, 6) |
    +-------+--------+--------+---------+----------+--------+--------+

    The desired set is found by collecting the remaining ordered pairs, 

    .. math::

        E^c \cap F^c = \{ (2,2), (2,4), (2,6), (3,3), (3,5), (4,2), (4,4),(4,6), (5,3), (5,5), (6,6), (6,4), (6,6) \}

    d. Recall the symbol :math:`\cup` correspond to the English word "*or*". This problem is therefore asking for the outcomes in the event of getting an odd sum *or* getting atleast one *1*. 

    To find the set :math:`E \cup F`, use the method from the previous part, except in this case, blank out entries that don't satisfy the condition of having odd sum or containing atleast one *1*,

    Table 1d-1
        The outcomes which have an odd sum *or* have atleast one *1*, :math:`E \cup F`

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   | (1, 1) | (1, 2) |  (1, 3) |  (1, 4)  | (1, 5) | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) |    -   |  (2, 3) |    -     | (2, 5) |   -    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   | (3, 1) | (3, 2) |    -    |  (3, 4)  |   -    | (3, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) |   -    |  (4, 3) |    -     | (4, 5) |    -   |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   | (5, 1) | (5, 2) |    -    |  (5, 4)  |  -     | (5, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) |    -   |  (6, 3) |    -     | (6, 5) |    -   |
    +-------+--------+--------+---------+----------+--------+--------+

    Collect these elements into a set to complete the problem,

    .. math::

        E \cup F = \{ \text{todo} \}

    e. This event would correspond to the event of getting an odd sum *or* getting *no 1's*. 
    
    To find the elements in the sets :math:`E \cup F^c`, blank out the entries in Table 1 that satisfy the condition of membership,

    Table 1e-1: Outcomes
        The outcomes which have an odd sum or have no *1*'s, :math:`E \cup F^c`

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    -   | (1, 2) |    -    |  (1, 4)  |   -    | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) | (2, 2) |  (2, 3) |  (2, 4)  | (2, 5) | (2, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |    -   | (3, 2) |  (3, 3) |  (3, 4)  | (3, 5) | (3, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) | (4, 2) |  (4, 3) |  (4, 4)  | (4, 5) | (4, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |   -    | (5, 2) |  (5, 3) |  (5, 4)  | (5, 5) | (5, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) | (6, 6) |  (6, 3) |  (6, 4)  | (6, 5) | (6, 6) |
    +-------+--------+--------+---------+----------+--------+--------+

3. Three red balls and one green ball are placed into a box. Describe the sample spaces of the following experiments with a set using :ref:`list_notation`.

    .. note:: 
        *Hint*: Let *r* :sub:`1`, *r* :sub:`2` and *r* :sub:`3` represent the *outcome* of drawing each of the respective red balls. 

    a. Selecting one ball at random.
    b. Selecting two balls at random and :ref:`with_replacement` (i.e. putting the ball you drew back into the back after you draw it).
    c. Selecting two balls at random and :ref:`without_replacement` (i.e. *not* putting the ball back after you draw it)

.. collapse:: Solution #3

    a. This is easily found by simply enumerating all of the outcomes,

    .. math::

        S = \{ r_1, r_2, r_3, g \}

    b. Any time two things are occuring *with replacement*, it's a good bet a table would be helpful. Let's create one like we did in #2, but instead of listing rolls of a die on the headings, let's use this sample space,

    +-------------+---------------------+--------------------+--------------------+------------------+
    |             |      :math:`r_1`    |      :math:`r_2`   |      :math:`r_3`   |        g         |
    +-------------+---------------------+--------------------+--------------------+------------------+
    | :math:`r_1` |  :math:`(r_1, r_1)` | :math:`(r_1, r_2)` | :math:`(r_1, r_3)` | :math:`(r_1, g)` |
    +-------------+---------------------+--------------------+--------------------+------------------+
    | :math:`r_2` |  :math:`(r_2, r_1)` | :math:`(r_2, r_2)` | :math:`(r_2, r_3)` | :math:`(r_2, g)` |
    +-------------+---------------------+--------------------+--------------------+------------------+
    | :math:`r_3` |  :math:`(r_3, r_1)` | :math:`(r_3, r_2)` | :math:`(r_3, r_3)` | :math:`(r_3, g)` |
    +-------------+---------------------+--------------------+--------------------+------------------+
    |     g       |  :math:`(g, r_1)`   |  :math:`(g, r_2)`  |  :math:`(g, r_3)`  | :math:`(g, g)`   |
    +-------------+---------------------+--------------------+--------------------+------------------+

    Collect all of these elements into a set to complement the problem,

    .. math::

        S = \{ (r_1, r_1), (r_1, r_2), ..., (g, r_3), (g, g) \}

    c. When you hear *with replacement*, think table. When you hear *without replacement*, think :ref:`tree_diagrams`. The reason for this is simple. It is very hard (if not impossible) to represent the act of *removing* an outcome from the sample space in tabular form, whereas it is very natural to represent it with a :ref:`tree diagram`

    (INSERT DIAGRAM)

    Notice that we lose the element just chosen at each branch of the diagram, i.e. as you move down the tree there is one less branch at each step. 
    
    Collecting the endpoints, we can complete the problem,

    .. math::

        S = \{ (r_1, r_2), (r_1, r_3), (r_1, g), (r_2, r_1), (r_2, r_3), (r_2, g), (r_3, r_1), (r_3, r_2), (r_3, g), (g, r_1), (g, r_2), (g, r_3) \}

4. A deck of six cards consists of three black cards numbered *1*, *2*, *3* and three red cards numbered *1*, *2*, *3*. You draw two cards :ref:`without_replacement`. Let **A** be the event the second card has a larger number than the first card. Let **B** be the event the first card has a larger number than the second card.
   
    a. Are **A** and **B** mutually exclusive?
    b. Are **A** and **B** complements?

.. collapse:: Solution #4

    While this problem is possible by listing the outcomes in the sample space in a set and then finding the events that correspond to **A** and **B** in terms of those outcomes and applying the rules of :ref:`set_theory`, let us try instead to reason it out.

    a. Events are *mutually exclusive* if they share no outcomes. If the first card has a larger number than the second card, then the second card cannot possibly be larger than the first card. In the other direction, if the second card is larger than the first card, then the first card cannot possibly be larger than the second card. In other words, there is no possible way for **A** to share any outcomes with **B**. Therefore, **A** and **B** are *mutually exclusive* by definition.

    b. This part is a bit trickier to see. Recall that the union of complements is equal to the sample space (:ref:`universal set`),

    .. image:: ../../../assets/imgs/sets/sets_complement.jpg
        :align: center 

    If you take all of the outcomes in an event **A** and add to them the outcomes *not* in event **A**, then you will have all of the outcomes of the sample space. 

    Then, there are no outcomes outside of the outcomes contained in :math:`A` plus the outcomes contained in :math:`A^c`. For, if there were, these two sets would not be complements of one another.

    If we can show there is an outcome in the sample space **S** that does not belong to *either* :math:`A` *or* :math:`B`, then it must follow that **A** and **B** are *not* complements, since their union does not equal the entire sample space. 

    Consider the outcome of drawing a red card with the number *2* along with a black card with the number *2*. In this case, it is neither true that the first card is larger than the second card nor is it true the second card is larger than the first card. Then, there is atleast one outcome in the sample space that belongs to neither of the events. Therefore, we can conclude **A** and **B** are *not* complements of one another.

Applications
============
   
5. You roll two dice. The find the probability of the following events. 
   
    a. The sum of the numbers rolled is 7.
    b. The sum of the numbers rolled on the dice is 3 or 5.
    c. The numbers rolled are both even. 
    d. One of the numbers rolled is even.
    e. Neither of the numbers rolled are even.
    f. Is part *e* the complement of part *c* or part *d*?

.. collapse:: Solution #5

    Ah, our old friend. We found the sample of this experiment back in *#1* and then examined some events defined on it in *#2*. Let us copy the results over for quick reference,

    Table 1 Redux: Outcomes
        The outcomes of two die rolls.

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |   4      |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   | (1, 1) | (1, 2) |  (1, 3) |  (1, 4)  | (1, 5) | (1, 6) | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   | (2, 1) | (2, 2) |  (2, 3) |  (2, 4)  | (2, 5) | (2, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   | (3, 1) | (3, 2) |  (3, 3) |  (3, 4)  | (3, 5) | (3, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   | (4, 1) | (4, 2) |  (4, 3) |  (4, 4)  | (4, 5) | (4, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   | (5, 1) | (5, 2) |  (5, 3) |  (5, 4)  | (5, 5) | (5, 6) |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   | (6, 1) | (6, 6) |  (6, 3) |  (6, 4)  | (6, 5) | (6, 6) |
    +-------+--------+--------+---------+----------+--------+--------+

    Table 2 Redux: Sum
        The sum of two die rolls.

    +-------+--------+--------+---------+----------+--------+--------+
    |       |    1   |   2    |    3    |    4     |    5   |   6    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   1   |    2   |   3    |    4    |    5     |    6   |   7    | 
    +-------+--------+--------+---------+----------+--------+--------+
    |   2   |    3   |   4    |    5    |    6     |    7   |   8    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   3   |    4   |   5    |    6    |    7     |    8   |   9    |
    +-------+--------+--------+---------+----------+--------+--------+
    |   4   |    5   |   6    |    7    |    8     |    9   |   10   |
    +-------+--------+--------+---------+----------+--------+--------+
    |   5   |    6   |   7    |    8    |    9     |    10  |   11   |
    +-------+--------+--------+---------+----------+--------+--------+
    |   6   |    7   |   8    |    9    |    10    |    11  |   12   |
    +-------+--------+--------+---------+----------+--------+--------+

    Notice the number of elements in the sample space, i.e. its *cardinality*, is equal to 36, i.e.,

    .. math::

        n(S) = 36

    All of the probabilities in this problem can be calculated by crossing out the entries in these tables that do not satisfy the given conditions, counting up the number of entries that remain and then applying the :ref:`classical_definition`.

    a. :math:`\frac{6}{36} = \frac{1}{6}`

    b. :math:`\frac{6}{36} = \frac{1}{6}`

    c. :math:`\frac{9}{36} = \frac{1}{4}`

    d. :math:`\frac{27}{36} = \frac{3}{4}`

    e. :math:`\frac{9}{36} = \frac{1}{4}`

    f. *part d* and *part e* are complements. Part *d* can be rephrased as "*at least one of the die is even*". By the :ref:`square_of_opposition`, the complement of "*atleast one*" is "*none*". This can be verified by summing the probabilities of both events and verifying they add to one, 

6. You have a standard deck of 52 playing cards. You shuffle the cards into a random order and deal yourself exactly one card. Find the probabilities of the following events,

    a. The card is a king.

    b. The card is a spade.

    c. The card is a king or spade.

    d. The card is a 4 or Jack.

    e. The card is black. 

    f. The card is black or a queen. 
    
    g. The card is neither nor a queen.

7. You select a number randomly between 1 and 1000. What is the probability the number selected is divisible by 5?

TODO: ONE MORE

Probability Proofs
==================

8. Let **A** and **B** be two events, not necessarily mutually exclusive. Prove the following inequality

.. math:: 
    P(A \cap B) \geq P(A) + P(B) - 1

.. note:: 
    *Hint*: Use the :ref:`law_of_unions` and :ref:`axiom_1`

9. Let **A** and **B** be two events, not necessarily mutually exclusive. The event,
    
.. math:: 
    (A - B) \cap (B - A)

is called the *symmetric difference of* **A** *and* **B**. Prove the probability of the *symmetric difference of* **A** *and* **B** is equal to,

.. math:: 
    P(A) + P(B) - 2 \cdot P(A \cap B)

.. note:: 
    *Hint #1*: Draw a :ref:`Venn Diagram <venn_diagrams>` of **A** and **B**, assuming the events are *not* mutually exclusive. Label the area that correspodned to the *symmetric difference of* **A** *and* **B**. 

    *Hint #2*: Recall (TODO link) :math:`A - B = A \cap B^C`

TODO: one more

A.P. Exam Practice
==================

12. **2019, Free Response, #3** 
    
A medical researcher surveyed a large group of men and women about whether they take medicine as prescribed.
The responses were categorized as never, sometimes, or always. The relative frequency of each category is
shown in the table.

.. image:: ../../../assets/imgs/classwork/2019_apstats_frp_03.png
    :align: center

One person from those surveyed will be selected at random.

a. What is the probability that the person selected will be someone whose response is never and who is a
woman?

b. What is the probability that the person selected will be someone whose response is never or who is a
woman?

c. What is the probability that the person selected will be someone whose response is never given that the
person is a woman?

d. For the people surveyed, are the events of being a person whose response is never and being a woman
independent? Justify your answer.

e. Assume that, in a large population, the probability that a person will always take medicine as prescribed
is 0.54. If 5 people are selected at random from the population, what is the probability that at least 4 of
the people selected will always take medicine as prescribed? Support your answer.

1.  **2015, Multplie Choice, #32**
    
A survey conducted by a national news network asked a random sample of U.S. adults whether they get most of their information about current events from newspapers, television, the internet, or some
other source. The results, shown in the table below, are reported by age group of the respondents.

+---------+------------+------------+----------+-------+-------+
|         | Newspapers | Television | Internet | Other | Total |
+---------+------------+------------+----------+-------+-------+
| 18 -34  | 12         | 35         | 40       | 6     | 93    |
+---------+------------+------------+----------+-------+-------+
| 35 -54  | 16         | 55         | 20       | 8     | 99    |
+---------+------------+------------+----------+-------+-------+
| Over 55 | 33         | 60         | 5        | 5     | 103   |
+---------+------------+------------+----------+-------+-------+
| Total   | 61         | 150        | 65       | 19    | 295   |
+---------+------------+------------+----------+-------+-------+

If primary news source is independent of age group, which of the following expressions is equal to
the expected number of respondents who are aged 35 to 54, inclusive, and get most of their
information about current events from the internet?

    (A) :math:`\frac{99 \cdot 65}{295}`

    (B) :math:`\frac{99 \cdot 150}{295}`

    (C) :math:`\frac{20 \cdot 65}{99}`

    (D) :math:`\frac{20 \cdot 99}{295}`

    (E) :math:`\frac{20 \cdot 65}{295}`

15.  **2012, Practice Exam, #23** 

A local company is interested in supporting environmentally friendly initiatives such as carpooling among employees. The company surveyed all of the 200 employees at the downtown offices. Employees responded as to whether or not they own a car and to the location of the home where they live. The results are shown in the
table below.

.. image:: ../../../assets/imgs/classwork/2012_apstats_pe_23.png
    :align: center 

Which of the following statements about a randomly chosen person from these 200 employees is true?

    (A) If the person owns a car, he or she is more likely to live elsewhere in the city than to live in the downtown
    area in the city.

    (B) If the person does not own a car, he or she is more likely to live outside the city than to live in the city
    (downtown area or elsewhere).

    (C) The person is more likely to own a car if he or she lives in the city (downtown area or elsewhere) than if he
    or she lives outside the city.

    (D) The person is more likely to live in the downtown area in the city than elsewhere in the city.

    (E) The person is more likely to own a car than not to own a car.
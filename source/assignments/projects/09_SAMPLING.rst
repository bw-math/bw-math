.. _project_nine:

========
Sampling
========

    Democracy is the theory people know what they want and deserve to get it, good and hard.
    - H.L. Mencken

The Student Government elections are an excellent opportunity to put some of your newfound analytical tools to use. In this lab, you will design and perform several experiments to predict who will win president. 

Preamble
========

As you will soon discover in the :ref:`project_nine_instructions`, you will be assigned a partner for this lab. In the spirit of statistics and to put you in the right headspace for this lab, I will be using the following code snippet to randomly assign partners. 

.. code:: python

    import random 

    names = [ "Larry", "Curly", "Moe", "Shemp"]

    randomly_ordered_names = random.shuffle(names)

.. note::

    Obviously, I will be using your real names in class. 

.. _project_nine_instructions:

Instructions
============

You will complete the data collection portion of this project with a partner. You will work together to design a sampling technique and then perform the experiment. Since you are both using the same data, you should both have the same answers. However, you will turn in separate reports and receive separate grades. 

1. Create a Python ``.py`` script named ``LASTNAME_FIRSTNAME_project_four.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``LASTNAME`` and ``FIRSTNAME`` with your last and first name, respectively.
2.  Create four spreadsheet files named ``simple_random.csv``, ``stratified.csv``, ``cluster.csv`` and ``systematic.csv``. Place all of these files in ``Linux Files`` folder on your file system.
3.  Create a :ref:`Python docstring <python_docstring>` at the very top of the ``.py`` script file. Keep all written answers in this area of the script.
4.  Review the sampling techniques found in TODO. Class notes for this seciton can be on the :ref:`sampling_techniques` page.
5.  Perform all exercises and answer all questions in the :ref:`project_nine_project` section. Label your script with comments as indicated in the instructions of each problem.
6.  When you are done, zip your ``.py`` script **and** *all* of your ``.csv`` files into a zip file named ``LASTNAME_FIRSTNAME_project_nine.zip``
7.  Upload the zip file here to the Google Classroom Project Nine assignment.

.. _project_nine_collecting_data:

Collecting Data
===============

Everyone in highschool is eligible to vote in the elections and the population is large enough for draw statistically significant samples. You should, *in theory*, be able to make a reasonable prediction about the the outcome of the Student Government elections.

In order to ensure the accuracy of your predictions, we w

.. _project_nine_project:

Project
=======

1. 

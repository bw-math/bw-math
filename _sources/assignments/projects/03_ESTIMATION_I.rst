.. _project_three:

=====================================
Estimation I: One Variable Statistics
=====================================

    We must be careful not to confuse data with the abstractions we use to analyze them.
    
    - William James, 1907

In this lab, we will use **Python** to calculate sample statistics and graphical representations for a dataset that represents the length of each Roman Emperor's reign. we will use these statistics and graphs to draw conclusions about the distribution of Roman Emperor reigns.

.. _project_three_instructions:

Instructions
============

1. Download the ``.csv`` dataset :ref:`below <project_three_dataset>` and place it in the ``Linux Files`` folder where you saved your *.py* scripts.
2. In the same folder, create a Python ``.py`` script named ``NAME_project_three.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``NAME`` with your  name.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_three_background` section.
5. Read the :ref:`project_three_required_imports` section.
6. Read the :ref:`project_three_functions` section.
7. Read the :ref:`project_three_loading_data` section.
8. Load in the data from the ``.csv`` file using the technique outlined in the :ref:`project_three_loading_data` section.
9. Perform all exercises and answer all questions in the :ref:`project_three_project` section. Label your script with comments as indicated in the instructions of each problem.
10. When you are done, zip your script **and** the *csv* file in a zip file named ``NAME_project_three.zip``
11. Upload the zip file to the Google Classroom Project Three Assignment.
   
.. _project_three_background: 

Background
==========

In 27 BC, Julius Caesar's nephew, Octavian Caesar, was given the title *Augustus* by the Roman Senate. With this event, the city state of Rome had ceased to be `republic <https://en.wikipedia.org/wiki/Republic>`_. Augustus Caesar had become the first emperor of the `Roman Empire <https://en.wikipedia.org/wiki/Roman_Empire>`_. 

The Roman Empire would last for several centuries, absorbing large parts of what is now Europe, Africa and Asia into its boundaries. 

.. image:: ../../assets/imgs/context/roman_empire_evolution.gif
    :align: center

.. topic:: Evolution of the Roman Empire

    Rome from the citystate by the Tiber to the fall of the Western Roman Empire

    `Source: Roman Empire <https://en.wikipedia.org/wiki/File:Romempgif.gif>`_

Many people would go on to claim the title of *Roman Emperor* after Augustus Caesar died.

Some of them, such as `Hadrian <https://en.wikipedia.org/wiki/Hadrian>`_ and `Marcus Aurelius <https://en.wikipedia.org/wiki/Marcus_Aurelius>`_ had long and peaceful reigns. Others, such as `Marcus Otho <https://en.wikipedia.org/wiki/Otho>`_ and `Didius Julianus <https://en.wikipedia.org/wiki/Didius_Julianus>`_, only ruled for several months and their reigns were fraught with political upheaval and violence.

In this project, we are going to look at a dataset that represents the *length* of each Roman Emperor's reign. We will look at the distribution shape and various descriptive statistics of this dataset in order to draw conclusions and tell a story about the leadership of the Roman Empire using empirical evidence.

.. _project_three_required_imports:

Imports
=======

To complete this lab, you will need to import the following packages. Add these lines to the top of your ``.py`` script.

.. code:: python

    import matplotlib.pyplot
    import math 

.. _project_three_functions:

Functions
=========

.. note::

    We will do this part in class together.

.. important::

    Refer to :ref:`python_creating_functions` section for a more information on creating your own function in Python.

We have been only been *using* functions up to this point. In order to complete this lab, we will need to *create* a few functions that will calculate sample statistics. In particular, we are going to create four functions: ``sample_mean``, ``sample_std_deviation``, ``sample_median`` and ``sample_percentile``. These functions will accept a sample of data as an *argument* (or *input*) and then calculate a sample statistic and *return* its value.

We can create the ``sample_mean`` function as follows,

.. code:: python

    def sample_mean(data):
        n = len(data)
        sumx = sum(data)
        xbar = sumx / n
        return xbar

Take note of the *indentation*. Each line of the function is on the same *indentation* level. This is how **Python** separates functions from the commands you are executing. For more information about the syntactical components of a function defintion, refer to the :ref:`python_creating_functions` section.

Now that we have defined our sample mean function, we can *call* it using its *name*,

.. code:: python

    some_data = [ 1, 2, 3, 4, 5 ]
    xbar = sample_mean(some_data)
    print("the sample mean is ", xbar)

Output

    the sample mean is 3.0


In this project, we will create two more functions:

- A function to calculate the sample standard deviation
- A function to calulate a sample percentile.

.. _project_three_loading_data:

Loading In Data
===============

The following code snippet will load in a *CSV* spreadsheet named ``example.csv``, parse it into a list and then print it to screen, assuming that *CSV* file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets in :ref:`project_one_dataset` section.

.. code-block:: python 

    import csv

    # read in data
    with open('example.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file and ensure it's a number (not a string)
    column_1 = [ float(row[0]) for row in columns ]

    print(column_1)

.. _project_three_project:

Project
=======

1. Write a function that accepts a :ref:`list <python_lists>` of data as an argument and computes the following sample statistics. Write a separate function for each exercise and label it with a comment. Name the function appropriately.

    a. The sample mean of a dataset.

    b. The sample percentile of a dataset.

    c. The sample standard deviation of a dataset.

.. tip:: 

    *#1b* will require *two arguments*, the list of data and the percentile you wish to find.

.. note::

    We will do this part in class together.
    
2. Load in the data from the :ref:`project_three_dataset` section. Note the length of a reign is separated in a ``Years`` column, a ``Months`` column and a ``Days``. To clean the data and compute the total length of a Roman Emperor's reign, apply the formula to each row of data, 

.. math:: 

    \text{ length of reign } = \text{ years column } + \frac{ \text{weeks column} }{52} + \frac{ \text{ days column } }{365}

Save the cleaned data in a new list. Label the list with a comment. 

3. Using the functions created in #1, find the following statistics using the :ref:`project_three_dataset`. Label each computation with a comment.

    a. The mean length of a Roman Emperor's reign.

    b. The median length of a Roman Emperor's reign.

    c. The 25 :sup:`th` percentile length of a Roman Emperor's reign.

    d. The 75 :sup:`th` percentile length of a Roman Emperor's reign.

    e. The sample standard deviation of a Roman Emperor's reign length. 

4. Compare the answers to *#2a* and *#2b*. What do these two answers tell you about the skew of this distribution? Interpret the skew in terms of Roman Emperors and the length of their reign, i.e. what does the skew tell you about Roman Emperor's and the length of their reigns? Save your answer in the :ref:`docstring <python_docstring>`.

5. Construct a relative frequency histogram and a cumulative relative frequency using 10 classes for this sample of data. Label the code for creating the plots with a comment. What type of distribution shape does this dataset have? Does this agree with your answer to *#4*? Explain. Save your answer in the :ref:`docstring <python_docstring>`.

6. Construct a boxplot for this sample of data. Label the code for creating the plot with a comment. Based on the boxplot, are there any potential outliers in this dataset? Are the outliers Emperors who had long rules or short rules? Save your answer in the :ref:`docstring <python_docstring>`.

6. Find the coefficient of variation for this dataset. What does this statistic tell you about the distribution? Interpret the coefficient of variation in terms of Roman Emperors  and the length of their reign. Save your answer in the :ref:`docstring <python_docstring>`.

7. Summarize the conclusions you can draw about Roman Emperors and the length of their reign in your :ref:`docstring <python_docstring>`. Answer the following questions in your summary.

    a. What percentage of Roman Emperors had reigns longer than 30 years?

    b. What percentage of Roman Emperors had reigns shorter than 1 year?

    c. Interpret the results of *#a* and *#b*. What does this tell you about the distribution of Roman Emperors?

8. Based on the graphs and descriptive statistics calculated in the previous problems, write a few sentences in the :ref:`docstring <python_docstring>` describing what the distribution of Roman Emperor reigns tells us about the Roman state. 

.. _project_three_dataset:

Dataset
=======

You can download the full dataset :download:`here <../../assets/datasets/roman_emperors_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Roman Emperor Reigns
   :file: ../../assets/datasets/previews/roman_emperors_data_preview.csv

The meaning of the columns is as follows: 

- ``Emperor`` is the name of the Roman Emperor.
- ``Years`` is the number of years in the reign.
- ``Months`` is the number of months in the reign.
- ``Days`` is the number of days in the reign.
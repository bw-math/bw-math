.. _project_three:

=====================================
Estimation I: One Variable Statistics
=====================================

    We must be careful not to confuse data with the abstractions we use to analyze them.
    
    - William James, 1907

In this lab, you will use **Python** to calculate sample statistics and graphical representations for a dataset that represents the length of each Roman Emperor's reign. You will use these statistics and graphs to draw conclusions about the distribution of Roman Emperor reigns.

.. _project_three_instructions:

Instructions
============

1. Download the ``.csv`` dataset :ref:`below <project_three_dataset>` and place it in the ``Linux Files`` folder where you saved your *.py* scripts.
2. In the same folder, create a Python ``.py`` script named ``GROUPNAME_project_three.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``GROUPNAME`` with your last and first name, respectively.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_three_background` section.
5. Read the :ref:`project_three_loading_data` section.
6. Load in the data from the ``.csv`` file using the technique outlined in the :ref:`project_three_loading_data` section.
7. Perform all exercises and answer all questions in the :ref:`project_three_project` section. Label your script with comments as indicated in the instructions of each problem.
8. When you are done, zip your script **and** the *csv* file in a zip file named ``GROUPNAME_project_three.zip``
9. Have *one* member of the group pload the zip file to the Google Classroom Project Three Assignment.
   
.. _project_three_background: 

Background
==========

TODO 

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

1. Write a function that accepts a list of data an argument and computes the following sample statistics. Write a separate function for each exercise and label it with a comment. Name the function appropriately.

    a. The sample mean of a dataset.

    b. The sample median of a dataset.

    c. *Any* percentile of a dataset.

    d. The sample variance of a dataset.

    e. The sample standard deviation of a dataset.

.. tip:: 

    *#1c* will require *two arguments*, the list of data and the percentile you wish to find.

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

4. Compare the answers to *#2a* and *#2b*. What do these two answers tell you about the skew of this distribution? Interpret the skew in terms of Roman Emperors and the length of their reign, i.e. what does the skew tell you about Roman Emperor's and the length of their reigns?

5. Construct a relative frequency histogram and a cumulative relative frequency using 10 classes for this sample of data. Label the code for creating the plots with a comment. What type of distribution shape does this dataset have? Does this agree with your answer to *#4*? Explain.

6. Construct a boxplot for this sample of data. Label the code for creating the plot with a comment. Based on the boxplot, are there any potential outliers in this dataset? Are the outliers Emperors who had long rules or short rules? 

6. Find the coefficient of variation for this dataset. What does this statistic tell you about the distribution? Interpret the coefficient of variation in terms of Roman Emperors  and the length of their reign. 

7. Summarize the conclusions you can draw about Roman Emperors and the length of their reign. Answer the following questions in your summary.

    a. What percentage of Roman Emperors had reigns longer than 30 years?

    b. What percentage of Roman Emperors had reigns shorter than 1 year?

    c. Interpret the results of *#a* and *#b*. What does this tell you about the distribution of Roman Emperors?

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
.. _project_five:

=================
Linear Regression
=================

TODO

Instructions
============

1. Download the *csv* dataset in the :ref:`project_five_dataset` section and place it in the ``Linux Files`` folder on your folder system where you save your ``.py`` scripts.
2. Create a Python ``.py`` script named ``LASTNAME_FIRSTNAME_project_five.py`` in your ``Linux Files`` folder on your file system. You can do this by opening an IDLE session, creating a new file and then saving it. Replace ``LASTNAME`` and ``FIRSTNAME`` with your last and first name, respectively.
3. Create a :ref:`docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_five_background` section.
5. Read the :ref:`project_five_loading_data` section.
6. Load in the data from the ``.csv`` file using the technique outlined in the :ref:`project_three_loading_data` section.
7. Perform all exercises and answer all questions in the :ref:`project_five_project` section. Label your script with comments as indicated in the instructions of each problem.
8. When you are done,zip your script **and** the *csv* file in a zip file named ``LASTNAME_FIRSTNAME_project_five.zip``
9. Upload the zip file to the Google Classroom Project Five Assignment.

.. _project_five_loading_data:

Loading In Data
===============

The following code snippet will load in a *CSV* spreadsheet named ``example.csv``, parse it into a list and then print it to screen, assuming that *CSV* file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets in :ref:`project_two_dataset` section.

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


.. _project_five_background:

Background
==========

TODO 

Old Faithful
------------

TODO

Kentucky Derby
--------------

TODO 

.. _project_five_project:

Project
=======

TODO 

.. _project_five_dataset:

Data Sets
=========

Celebrity Twitter
-----------------

You can download the full dataset :download:`here <../../assets/datasets/celebrity_twitter_data.csv>`

The following table is a preview of the data you will be using for this project.

.. csv-table:: Celebrity Twitter Followers and Tweet Count
    :file: ../../assets/datasets/previews/celebrity_twitter_data_preview.csv-table

The fifth column represents the number of followers for a given Twitter user. The sixth column represents the number of tweets for a given Twitter user.

Old Faithful
------------

You can download the full dataset :download:`here <../../assets/datasets/old_faithful_data.csv>`.

The following table is a preview of the data you will be using for this project. 

.. csv-table:: Old Faithful Eruption and Waiting Times
   :file: ../../assets/datasets/previews/old_faithful_data_preview.csv

The first column represents the length of the eruption in minutes. The second column represents the waiting time in minutes until the next eruption.

Kentucky Derby Winning Times
----------------------------

You can download the full dataset :download:`here <../../assets/datasets/kentucky_derby_winners_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Kentucky Derby Winning Times
   :file: ../../assets/datasets/previews/kentucky_derby_winners_data_preview.csv

The first column represents the year of the race. The ninth column represents the winning time in seconds.

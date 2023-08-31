.. _project_one:

======================
Graphing I: Bar Charts 
======================

    The picture is a model of reality.

    - Ludwig Wittgenstein

In this lab, you will get familiar with the statistical plotting features of **Python** using a dataset we have already seen.

.. _project_one_instructions:

Instructions
============

1. Create a folder named `LASTNAME_FIRSTNAME_project_one`, replacing `LASTNAME` and `FIRSTNAME` with your last name and first name, respectively.
2. Download the *csv* dataset in the :ref:`project_one_dataset` section and place it in the new folder you created in step 1.
3. In the same folder, create a Python *py* script named `project_one.py`. 
4. Create a :ref:`Python docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
5. Read the :ref:`project_one_background` section and the :ref:`project_one_loading_data` section.
6. Perform all exercises and answer all questions in the :ref:`project_one_project` section. Label your script with comments as indicated in the *Project* section.
7. When you are done, zip your folder and all its contents into a file named `LASTNAME_FIRSTNAME_project_one.zip`
8. Upload the zip file here to the Google Classroom Project One Assignment.

.. tip:: 
    
    You may need to refer to the :ref:`python_plotting` page for examples of various types of graphs. 

.. _project_one_background:

Background
==========

Electric Vehicles in Washington State 
-------------------------------------

Recall the dataset from :ref:`graphical_representations_of_data_classwork` *#1*,

    The United States Government General Services Administration maintains a huge database of public available information. One of the datasets they publish is the `Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing <https://catalog.data.gov/dataset/electric-vehicle-population-data>`_

This dataset was taken from `data.gov <https://data.gov/>`_. This is an excellent resource, if you are even in need of some data. We will be using this online database quite a bit once we get fully up to speed on **Python**.

We examined the *Eletric Vehcile* dataset a little bit in class on the first week. We are now prepared to do a little more in-depth analysis. 

.. _project_one_loading_data:

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


Bar Charts
==========

Behold, the power of `matplotlib <https://matplotlib.org/>`_,

.. plot:: assets/plots/other/bar_chart.py

Click on the ``source`` button in the top right corner of the graph to download a *.py* script. Examine the source code contained therein for generating a *Bar Chart*. This script is annotated with lots of comments for you to read. Give them a peak, and then let's meet back here.

.. _project_one_project:

Project
=======

.. _project_one_dataset:

Datasets
========

Electric Vehicle Dataset 
------------------------

You can download the full dataset :download:`here <../../assets/datasets/electric_vehicle_population_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Electric Vehicles in Washington State
   :file: ../../assets/datasets/previews/velocity_of_light_data_preview.csv



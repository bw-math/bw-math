.. _project_one:

========
Graphing
========

    The picture is a model of reality.
    - Ludwig Wittgenstein

In this lab, you will get familiar with the statistical plotting features of **Python** using several famous datasets from the history of science.

.. _project_one_instructions:

Instructions
============

1. Create a folder named `LASTNAME_FIRSTNAME_project_one`, replacing `LASTNAME` and `FIRSTNAME` with your last name and first name, respectively.
2. Download **both** *csv* datasets in the :ref:`project_one_dataset` section and place it in the new folder you created in step 1.
3. In the same folder, create a Python *py* script named `project_one.py`. 
4. Create a :ref:`Python docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
5. Read the :ref:`project_one_background` section and the :ref:`project_one_loading_data` section.
6. Perform all exercises and answer all questions in the :ref:`project_one_project` section. Label your script with comments as indicated in the *Project* section.
7. When you are done, zip your folder and all its contents into a file named `LASTNAME_FIRSTNAME_project_one.zip`
8. Upload the zip file here: TODO

.. tip:: 
    
    You may need to refer to the :ref:`python_plotting` page for examples of various types of graphs. 

.. _project_one_background: 

Background
==========

The Michelson Velocity of Light Experiment 
------------------------------------------

The `Michelson Velocity of Light Experiment<https://www.gutenberg.org/files/11753/11753-h/11753-h.htm>` conducted in 1887 remained one of most accurate estimations of the speed of light until modern times. Using a series of mirrors depicted below,

.. image:: ../../assets/imgs/context/michelson_experiment.png
    :width: 60%
    :align: center

While the theoretical details of the experiment are interesting in their own right (see link above for further detail!), for this lab, we will take the data as given and analyze it from a statistical perspective.


The Cavendish Density of the Earth Experiment
---------------------------------------------

Henry Cavendish performed the first modern, scientific experiment to measure the density of the Earth in 1797. Using the mutual gravitational attraction of two heavy metal balls attached to a `torsion balanace <https://en.wikipedia.org/wiki/Torsion_spring#Torsion_balance>`_ to twist a fiber of string, Cavendish measured the force of the tension produced. With `Newton's Laws of Motion <https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion>`_ , he was able to derive an expression that related this force to the mass of the Earth. 

The estimate produced by Cavendish remained until modern times one of the most accurate and authoritative measures of the Earth's mass. In this lab, we will analyze the data produced by Cavendish.

.. _project_one_loading_data:

Loading In Data
===============

The following code snippet will load in a *CSV* spreadsheet, parse it into a list and then print it to screen, assuming that file is saved in the same folder as your script. Modify this code snippet to fit the datasets in this lab and then use it to load in the provided datasets :ref:`project_one_dataset`

.. code-block:: python 

    import csv, os, sys

    # discover file path of python script
    #   i.e., if your python script is stored in C:\\myuser\Documents\projects\script.py
    #           this command will return "C:\\myuser\Documents\project"
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

    # read in data
    with open(f'{script_directory}/vietnam_draft_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file
    column_1 = [ float(row[0]) for row in columns ]

    print(column_1)

Use this snippet to load in the provided data in order to finish the project. 

.. _project_one_project:

Project
=======

.. _project_one_dataset:

Velocity of Light
-----------------

1. Load the :ref:`Velocity of Light <project_one_dataset>` data into a :ref:`Python Script <python_scripts>` using the tecnique outlined in the :ref:`project_one_loading_data` section.

2. Construct a histogram plot for this data sets using eight classes. Answer the following questions in the body of your docstring.

    a. What is the class width of your histogram? 
    
    b. What are the class limits for each class? 

    c. What is the most frequent class?

    d. What type of shape does this distribtion of data have? Is this expected? Why or why not?

3. Construct a boxplot for this data set. Using the boxplot, answer the following questions in the body of your docstring.

    a. Estimate the 75 :sup:`th` percentile of this data set. 

    b. Estimate the 25 :sup:`th` percentile of this data set. 

4. The actual value of the speed of light, according to the best estimates we have today, is :math:`299,792,458 \frac{m}{s}`. Use this information to answer the following questions in the body of your docstring.

    a. What is the sample mean of the dataset?

    b. What is the percent error of this estimate with respect to the actual value.

.. tip:: 

    Recall the formula for *percent error* is given by,

    .. math::

        \text{percent error} = \frac{ \text{estimated - actual} }{ \text{actual} } \cdot 100

Density of the Earth 
--------------------

5.514 g/cm3


Data Set
========

Velocity of Light Data
----------------------

You can download the full dataset :download:`here <../../assets/datasets/velocity_of_light_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Michelson's Velocity of Light Data
   :file: ../../assets/datasets/previews/velocity_of_light_data_preview.csv

The meaning of the column is clear from the column header: each observation measures the speed of light in meters per second, :math:`\frac{m}{s}`.

Density of the Earth Data
-------------------------

You can download the full dataset :download:`here <../../assets/datasets/earth_density_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Michelson's Velocity of Light Data
   :file: ../../assets/datasets/previews/density_of_the_earth_data_preview.csv

The first column corresponds to the experiment number (first, second, third, etc.). The second column is the *ratio of the density of Earth to the density of water*. Recall the density of water by definition is :math:`1 \frac{g}{cm^3}`.

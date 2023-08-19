.. _project_one:

==========
Estimation
==========

In this lab, you will use **Python** to calculate sample statistics.

.. _project_one_instructions:

Instructions
============

1. Create a folder named `LASTNAME_FIRSTNAME_project_one`, replacing `LASTNAME` and `FIRSTNAME` with your last name and first name, respectively.
2. Download the *csv* dataset :ref:`below <project_one_dataset>` and place it in the new folder you created in step 1.
3. In the same folder, create a Python *py* script named `project_one.py`
4. Read the :ref:`project_one_project` section.
5. Answer the indicated questions in the :ref:`project_one_project` section in the *.docx* document file.
6. When you are done, zip your folder and all its contents in a file named `LASTNAME_FIRSTNAME_project_one.zip`
7. Upload the zip file here: TODO
   
.. _project_one_background: 

Background
==========

Henry Cavendish performed the first modern, scientific experiment to measure the density of the Earth in 1797. Using the mutual gravitational attraction of two heavy metal balls attached to a `torsion balanace <https://en.wikipedia.org/wiki/Torsion_spring#Torsion_balance>`_ to twist a fiber of string, Cavendish measured the force of the tension produced. With `Newton's Laws of Motion <https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion>`_ , he was able to derive an expression that related this force to the mass of the Earth. 

The estimate produced by Cavendish remained until modern times one of the most accurate and authoritative measures of the Earth's mass. In this lab, we will analyze the data produced by Cavendish.

Loading In Data
===============

The following code snippet will load in a *CSV* spreadsheet, parse it into a list and then print it to screen, assuming that file is saved in the same folder as your script. 

.. code-block:: python 

    import csv, os, sys

    # discover file path of python script
    #   i.e., if your python script is stored in C:\\myuser\Documents\projects\script.py
    #           this command will return "C:\\myuser\Documents\project"
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

    # read in data
    with open(f'{script_directory}/earth_density_data.csv') as csv_file:
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

Data Set
========

You can download the full dataset :download:`here <../../assets/datasets/earth_density_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Cavendish's Density of the Earth
   :file: ../../assets/datasets/previews/earth_density_data_preview.csv

The meaning of the columns is as follows.
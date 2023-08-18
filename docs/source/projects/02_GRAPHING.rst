.. _project_two:

=====
Plots
=====

In this lab, you will get familiar with the statistical features of **Python** using a famous dataset from the history of physics.

.. _project_two_instructions:

Instructions
============

1. Create a folder named `LASTNAME_FIRSTNAME_project_two`, replacing `LASTNAME` and `FIRSTNAME` with your last name and first name, respectively.
2. Download the *csv* dataset :ref:`below <project_two_dataset>` and place it in the new folder you created in step 1.
3. In the same folder, create a Microsoft Word *docx* document named `project_two.docx`.
4. In the same folder, create a Python *py* script named `project_two.py`
5. Read the :ref:`project_two_project` section.
6. Answer the indicated questions in the :ref:`project_two_project` section in the *.docx* document file.
7. When you are done, zip your folder and all its contents in a file named `LASTNAME_FIRSTNAME_project_two.zip`
8. Upload the zip file here: TODO
   
.. _project_two_background: 

Background
==========

The `Michelson Velocity of Light Experiment<https://www.gutenberg.org/files/11753/11753-h/11753-h.htm>` conducted in 1887 remained one of most accurate estimations of the speed of light until modern times. Using a series of mirrors depicted below,

.. image:: ../assets/imgs/context/michelson_experiment.png
    :width: 60%
    :align: center

While the theoretical details of the experiment are interesting in their own right (see link above for further detail!), for this lab, we will take the data as given and analyze it from a statistical perspective.

.. _project_two_loading_data:

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

.. _project_two_project:

Project
=======

.. _project_two_dataset:

Data Set
========

You can download the full dataset :download:`here <../assets/datasets/velocity_of_light_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Michelson's Velocity of Light Data
   :file: ../assets/datasets/previews/velocity_of_light_data_preview.csv

The meaning of the columns is as follows.
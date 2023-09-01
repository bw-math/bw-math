.. _project_one:

======================
Graphing I: Bar Charts 
======================

    The picture is a model of reality.

    - Ludwig Wittgenstein

In this lab, you will get familiar with the statistical plotting features of **Python** using a dataset we have already seen. We will explore the association between two categorical variables and determine if a relationship exists.

.. _project_one_instructions:

Instructions
============

1. Create a folder named ``LASTNAME_FIRSTNAME_project_one``, replacing ``LASTNAME`` and ``FIRSTNAME`` with your last name and first name, respectively.
2. Download the *csv* dataset in the :ref:`project_one_dataset` section and place it in the new folder you created in step 1.
3. In the same folder, create a Python ``.py`` script named ``project_one.py``. 
4. Create a :ref:`Python docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
5. Read the :ref:`project_one_background` section.
6. Read the :ref:`project_one_loading_data` section.
7. Read the :ref:`bar_chart` section. Download the script files in that section onto your ChromeBook. Read through and execute them on your computer. 
8. Read the :ref:`project_one_set_operations` section. 
9. Perform all exercises and answer all questions in the :ref:`project_one_project` section. Label your script with comments as indicated in the *Project* section.
10. When you are done, zip your folder and all its contents into a file named ``LASTNAME_FIRSTNAME_project_one.zip``
11. Upload the zip file here to the Google Classroom Project One Assignment.

.. _project_one_background:

Background
==========

Electric Vehicles in Washington State 
-------------------------------------

Recall the dataset from :ref:`graphical_representations_of_data_classwork` *#1*,

    The United States Government General Services Administration maintains a huge database of public available information. One of the datasets they publish is the `Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing <https://catalog.data.gov/dataset/electric-vehicle-population-data>`_

This dataset was taken from `data.gov <https://data.gov/>`_. This is an excellent resource, if you ever find yourself in need of some data. We will be using this online database quite a bit once we get fully up to speed on **Python**.

We examined the *Eletric Vehcile* dataset a little bit in class on the first week. We are now prepared to do a little more in-depth analysis. 

First, let's take about some of the variables being observed in this dataset.

Make
****

The **Make** variable represents the manufacturer of the car. The possible values for this variable are listed below,

- FIAT
- MINI
- LEXUS
- CHRYSLER
- LINCOLN
- ALFA ROMEO
- RIVIAN
- TOYOTA
- AZURE DYNAMICS
- GENESIS
- VOLKSWAGEN
- JEEP
- PORSCHE
- MERCEDES-BENZ
- CADILLAC
- KIA
- JAGUAR
- POLESTAR
- FISKER
- FORD
- TESLA
- SMART
- HYUNDAI
- BENTLEY
- NISSAN
- MITSUBISHI
- TH!NK
- VOLVO
- LUCID
- CHEVROLET
- WHEEGO ELECTRIC CARS
- HONDA
- LAND ROVER
- SUBARU
- AUDI
- MAZDA
- BMW
  
Clean Alternative Fuel Vehicle (CAFV) Eligibility
*************************************************

`The state of Washington offers many incentives for vehicle owners to invest in an electric vehicle <https://www.dol.wa.gov/vehicles-and-boats/taxes-fuel-tax-and-other-fees/tax-exemptions-alternative-fuel-vehicles-and-plug-hybrids>`_,

    In 2019, Washington State reinstated the sales and use tax exemption for the sales of vehicles powered by a clean alternative fuel and certain plug-in hybrids.

However, not all cars are eligible for this tax exemption. The exemption depends on the battery range of the electric vehicle. If your electric vehicle does not have a large enough range, your vehicle is deemed ineligible for a tax exemption.

The **Clean Alternative Fuel Vehicle (CAFV) Eligibility** variable in this dataset records whether or not an individual car is eligible. The possible values of this variable are:

- Not eligible due to low battery range
- Eligibility unknown as battery range has not been researched
- Clean Alternative Fuel Vehicle Eligible

Electric Vehicle Type
*********************

Electric vehicles come in two varieties: vehicles that are fully electric and hybrid vehicles that revert to a gasoline engine when they run out of electric power. This `article from PC Magazine goes into greater detail about the differences between these two types of electric vehicles <https://www.pcmag.com/how-to/ev-vs-hev-vs-phev-what-are-the-types-of-electric-vehicles>`_

The possible values of this variable are:

- Battery Electric Vehicle (BEV)
- Plug-in Hybrid Electric Vehicle (PHEV)

*BEV* electric vehicles are *fully electric*. *PHEV* use hybrid engines; when *PHEV* engines run out of power, they start using gasoline.

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


.. _bar_charts:

Bar Charts
==========

.. _standard_bar_charts:

No Frills
---------

Recall a standard bar chart is a way of visually representing the marginal frequency distribution for a sample of categorical data,

.. math::

	f(A) = \frac{n(A)}{n(S)}
	
	
Up until now we have been living in the stone age, creating these graphs by hand. Welcome to the twenty-first century. Behold, the power of `matplotlib <https://matplotlib.org/>`_,

.. plot:: assets/plots/other/bar_chart.py

Click on the ``source`` button in the top left corner of the graph to download the *.py* script used to generate this graph. Examine the source code contained therein for generating a *Bar Chart*. Be sure to read the comments before you execute it, as you will need to tweak a setting to get it to run on your computer. 

This script is annotated with lots of comments for you to read. Give them a peak, and then let's meet over in the next section.

.. _stacked_bar_charts:

Stacked
-------

Recall a *stacked bar chart* is a way of visually representing a *conditional distribution* of one categorical variable with respect to another,

.. math::

	P(A \mid B) = \frac{n(A \cap B)}{n(B)}
	
.. plot:: assets/plots/other/stacked_bar_chart.py

This one is extremely tricky. `matplotlib <https://matplotlib.org/>`_ does not have a nice way of making stacked bar charts; Unforunately, the twenty-first century isn't all it's cracked up to be. In this timeline, you have to "stack" your bar charts yourself. Make sure to download this one and go through it step by step. The script has been well commented; every step has been detailed. 

.. hint::
	
	Your script comments should look like the ones in the scripts you just downloaded.

.. _project_one_set_operations:
	
Set Operations
==============

A set in **Python** is defined with a pair of curly brackets ``{ }``. 

.. code:: python

	this_is_a_set = { "some", "things" }
	
A :ref:`set variable <python_sets>` in **Python** is a special type of variable.  When you create a set, it won't distinguish between identical elements. In other words, *sets* do not allow duplicates. As an example,

.. code:: python

	set_of_dupes = { "a", "a", "b", "b" }
	
	print(set_of_dupes)
	
Output:

	{'a', 'b'}
	
Notice the repetitions of *a* and *b* are ignored. This property of *sets* is extremely useful for categorical data.

Suppose you have a list of categorical data such as,

.. code ::

	some_list = [ "A", "A", "B", "C", "D", "D", "D" ]
	
Suppose, further, you didn't know how many values the categorical variable took on. In this particular case, it's easy to see what the values are just by looking at the list (i.e. ``A``, ``B``, ``C`` and ``D``), but in real world datasets, you could have *thousands of individual observations* to sort through to determine exactly how many values a categorical variable can assume. 

Rather than trying to determine what the *distinct* values are by hand, let **Python** do the hard work for you by converting the *list* into a *set*,

.. code::
	
	set(some_list)
	
Output:

	{'A', 'B', 'C', 'D'}

.. _project_one_project:

Project
=======

No Frills 
---------

1. Calculate the relative frequency of the following **Makes** of *Electric Vehicles*,

- TESLA
- CHEVROLET
- NISSAN
- TOYOTA
- VOLKWAGEN

Save your commands and label them with comments. In a :ref:`python_docstring`, answer the following question: Out of these five values, what is the most frequent **Make** of *Electric Vehicle* in Washington State?

2. Using your answers to #1, construct a bar chart for *only* these five values of the **Make** categorical variable.

.. note:: 

    If you want to construct the entire frequency distribution and make a bar chart for it, I won't stop you, but make sure it's readable.

Stacked
-------

1. Before starting this part of project, answer the following in a :ref:`python_docstring`: Based on the information provided in the :ref:`project_one_background` section, how would you expect the *conditional distribution* of **Clean Alternative Fuel Vehicle (CAFV) Eligibility** given the **Electric Vehicle Type** to look? Do you expect fully electric vehicles to have greater eligibility for tax credits than hybrid vehicles? Why or why not?
   
2. Answer the following questions. Label any commands you use to solve the problem with comments. Write your answers in the :ref:`python_docstring` at the top of the script.

a. What percentage of *electric vehicles* in Washington State are both *Battery Electric Vehicles (BEV)* and "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** ?

b. What percentage of *Battery Electric Vehicles (BEV)* are "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility**?

c. What percentage of "*Not eligible due to low battery range*" for **Clean Alternative Fuel Vehicle (CAFV) Eligibility** vehicles are *Battery Electric Vehicles (BEV)*?


3. Using this information obtained in *#3* and any additional information required, create a stacked bar chart for the *conditional distribution* of the **Clean Alternative Fuel Vehicle (CAFV) Eligibility** given the **Electric Vehicle Type**.

4. What does your stacked bar chart from #3 tell you about the *association* between the **Clean Alternative Fuel Vehicle (CAFV) Eligibility** and the **Electric Vehicle Type**? Write your answer in your script's :ref:`python_docstring` and label the problem.

5. Write a few sentences explaining the results from #2 - #4. Did the result turn out the way you expected? Why or why not?
   
.. _project_one_dataset:

Datasets
========

Electric Vehicle Dataset 
------------------------

You can download the full dataset :download:`here <../../assets/datasets/electric_vehicle_population_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Electric Vehicles in Washington State
   :file: ../../assets/datasets/previews/electric_vehicle_population_data_preview.csv

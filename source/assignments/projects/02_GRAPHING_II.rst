.. _project_two:

=======================
Graphing II: Histograms
=======================

    What can be shown, cannot be said.

    - Ludwig Wittgenstein

In this lab, you will get *even more* familiar with the statistical plotting features of **Python** using several famous datasets from the history of science.

.. _project_two_instructions:

Instructions
============

1. Download **both** *csv* datasets in the :ref:`project_two_dataset` section and place them in the *Linux Files* folder on your file system.
2. In the same folder, create a Python *py* script named `project_two.py`. 
3. Create a :ref:`Python docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
4. Read the :ref:`project_two_background` section and the :ref:`project_two_loading_data` section.
5. Perform all exercises and answer all questions in the :ref:`project_two_project` section. Label your script with comments as indicated in the *Project* section.
6. When you are done, zip your script **and** the *csv* files into a zip file named ``LASTNAME_FIRSTNAME_project_two.zip``
7. Upload the zip file to the Google Classrom Project Two asignment.

Formulae
========

Recall the formula for *percent error* is given by,

.. math::

    \text{percent error} = \frac{ \text{estimated - actual} }{ \text{actual} } \cdot 100

.. _project_two_background: 

Background
==========

The Michelson Velocity of Light Experiment 
------------------------------------------

The `Michelson Velocity of Light Experiment<https://www.gutenberg.org/files/11753/11753-h/11753-h.htm>` conducted in 1887 was the first time `Albert A. Michelson <https://en.wikipedia.org/wiki/Albert_A._Michelson>`_ successfully measured the speed of light. He would go on to do so several more times, eventually teaming up with `Edward Morley <https://en.wikipedia.org/wiki/Edward_W._Morley>`_. Together, using the principles Michelson first developed in 1887, Michelson and Morley would demonstrate the speed of light was the same regardless of the state of motion of the emitting body. This would go on to have profound effects for physics in the early twentieth century. It would lead `Albert Einstein <https://en.wikipedia.org/wiki/Albert_Einstein>`_ to propose the `theory of relativity <https://en.wikipedia.org/wiki/Theory_of_relativity>`_, one of the most significant intellectual developments in history of humanity. 

Michelson's 1887 experimental results remained one of most accurate estimations of the speed of light until modern times. Using a series of mirrors depicted below,

.. image:: ../../assets/imgs/context/michelson_experiment.png
    :width: 60%
    :align: center

He was able to divert light rays from an emitting body along separate paths and measure the fractional time difference it took for the rays to reach the same location.

In this lab, we will be using his dataset to perform some statistical analysis. 


The Cavendish Density of the Earth Experiment
---------------------------------------------

Henry Cavendish performed the first modern, scientific experiment to measure the density of the Earth in 1797. Using the mutual gravitational attraction of two heavy metal balls attached to a `torsion balanace <https://en.wikipedia.org/wiki/Torsion_spring#Torsion_balance>`_ to twist a fiber of string, Cavendish measured the force of the tension produced. With `Newton's Laws of Motion <https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion>`_ , he was able to derive an expression that related this force to the mass of the Earth. 

The estimate produced by Cavendish remained until modern times one of the most accurate and authoritative measures of the Earth's mass. In this lab, we will analyze the data produced by Cavendish.

.. _project_two_loading_data:

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

.. _project_two_graphs:

Graphical Representations
=========================

Histogram
---------

Recall a histogram is a way of visualizing the frequency distribution of a sample of data,

.. math:: 

    f(x_i) = \frac{n(x_i)}{n}

The following plot is a histogram generated with :ref:`matplotlib` using *6* classes. Click on the ``source`` button in the top left corner to download the script. Read through the comments to see how it was constructed. 

.. plot:: assets/plots/histograms/histogram_normal.py

The sample in this graph was randomly generated using a combination of the :ref:`range() function <python_range_function>` and the :ref:`random() function <python_random_package>`.

The line you want to pay attention in the script you just downloaded is,

.. code:: python 

    axs.hist(data, bins=6, align='left', color='lightblue', ec='red')

Notice the first argument of this function is passed alone, without a name (i.e. without an expression ``x=y``). The first argument of the ``hist()`` function is *always* the sample of data you wish to plot; The ``data`` argument is simply a :ref:`list <python_lists>` of data. 

The rest of the arguments are *named* (i.e. with an expression ``x=y``). The *named* arguments can be passed into the ``hist()`` function is any order. For example, this line will generate the same histogram,

.. code:: python

    axs.hist(data, align='left', bins=6, ec='red', color='lightblue')

The only requirement is *data* must be passed in first. The other arguments may be passed in as you please.

And there are many arguments you can pass into the ``hist()`` function. You can check out the `hist() documentation on the matplotlib website <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html>`_ for a full list of arguments. The only *required* is the ``data`` argument. 

The ``bin`` argument is the number of *classes*.

.. important:: 

    *bins* is a term you will frequently see when using computer programs that generate histograms. *bins* are *classes*.

The other arguments, ``align``, ``color`` and ``ec``, affect the *styling* of the graph. 

``align`` tells :ref:`matplotlib` where to align the histogram bar. Valid values are ``left``, ``mid`` and ``right``. ``left`` aligns the histogram bars to the lower class limit. ``mid`` centers the histogram bars over the midpoint of each class. ``right`` will align the histogram bars with the upper class limit.

``color`` is the color that fills the histogram bars. You can find a list of all the *named* colors on the `color page of the matplotlib documentation <https://matplotlib.org/stable/gallery/color/named_colors.html>`_. Some of them are printed below for quick reference,

- maroon
- salmon
- chocolate
- darkorange
- springgreen
- navy
- hotpink

As you can see, there are lots of options to make your graph nice and pretty.

Boxplots
--------

TODO 

.. _project_two_project:

Project
=======

Velocity of Light
-----------------

1. Load the :ref:`Velocity of Light <project_two_dataset>` data into a :ref:`Python Script <python_scripts>` using the tecnique outlined in the :ref:`project_two_loading_data` section.

2. Construct a histogram plot for this data sets using eight classes. Answer the following questions in the body of your docstring.

    a. What is the class width of your histogram? 
    
    b. What are the class limits for each class? 

    c. What is the most frequent class?

    d. What type of shape does this distribtion have? Is this expected? Why or why not? 

3. Construct a boxplot for this data set. Using the boxplot, answer the following questions in the body of your docstring.

    a. Estimate the 75 :sup:`th` percentile of this data set. 

    b. Estimate the 25 :sup:`th` percentile of this data set.

    c. Estimate the median of this data set.

    d. Estimate the range of this data set.

    e. Based on the boxplot, do you detect any possible outliers?  

4. The actual value of the speed of light, according to the best estimates we have today, is :math:`299,792,458 \frac{m}{s}`. Use this information to answer the following questions in the body of your docstring.

    a. What is the sample mean of the dataset?

    b. What is the percent error of this estimate with respect to the actual value?

Density of the Earth 
--------------------

1. Load the :ref:`Density of the Earth <project_two_dataset>` data into a :ref:`Python Script <python_scripts>` using the tecnique outlined in the :ref:`project_two_loading_data` section.

2. Construct a histogram plot for this data sets using eight classes. Answer the following questions in the body of your docstring.

    a. What is the class width of your histogram? 
    
    b. What are the class limits for each class? 

    c. What is the most frequent class?

    d. What type of shape does this distribtion have? Is this expected? Why or why not?

3. Construct a boxplot for this data set. Using the boxplot, answer the following questions in the body of your docstring.

    a. Estimate the 75 :sup:`th` percentile of this data set. 

    b. Estimate the 25 :sup:`th` percentile of this data set.

    c. Estimate the median of this data set.

    d. Estimate the range of this data set. 

    e. Based on the boxplot, do you detect any possible outliers?  

4. The actual denity of the Earth, according to the best estimates we have today, is :math:`5.514 \frac{g}{cm^3}`. Use this information to answer the following questions in the body of your docstring.

    a. What is the sample mean of the dataset?

    b. What is the percent error of this estimate with respect to the actual value?

.. _project_two_dataset:

Datasets
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

.. csv-table:: Cavendish's Density of the Earth Data
   :file: ../../assets/datasets/previews/earth_density_data_preview.csv

The first column corresponds to the experiment number (first, second, third, etc.). The second column is the *ratio of the density of Earth to the density of water*. Recall the density of water by definition is :math:`1 \frac{g}{cm^3}`.

References
==========

- `matplotlib colors <https://matplotlib.org/stable/gallery/color/named_colors.html>`_
- `matplotlib histogram function <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html>`_
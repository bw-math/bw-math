.. _project_three:

====
Bias
====

In this lab, you will perform some graphical analysis on a famously biased data set and use statistical reasoning to draw conclusions about the method of observation used to generate the data.

Instructions
============

1. Create a folder named `LASTNAME_FIRSTNAME_project_three`, replacing `LASTNAME` and `FIRSTNAME` with your last name and first name, respectively.
2. Download the *csv* dataset `below <project_three_dataset>`_ and place it in the new folder you created in step 1.
4. In the same folder, create a Python *py* script named `project_three.py`
5. Create a :ref:`Python docstring <python_docstring>` at the very top of the script file. Keep all written answers in this area of the script.
6. Read the :ref:`project_three_project` section.
7. Perform all exercises and answer all questions in the :ref:`project_one_project` section. Label your script with comments as indicated in the instructions of each problem.
8. When you are done, zip your folder and all its contents in a file named `LASTNAME_FIRSTNAME_project_three.zip`
9. Upload the zip file here: TODO

.. _project_three_loading_data:

Loading In Data
===============

TODO

.. _project_three_background:

Background
==========

In the years 1969, 1970, 1971 and 1972, the Selective Service System in the United States held a draft lottery by order of President Lyndon B. Johnson for men born between the dates of January 1, 1944 and December 31, 1950 [*]_. 

.. [*] Vietnam War Draft Lottery
    `source <https://en.wikipedia.org/wiki/Draft_lottery_(1969)>`_

Individuals born between these dates were to be selected at random and drafted into military service to fight in the Vietnam War.

Method of Observation
---------------------

The method used to select individuals for service is highly controversial. Many argued it was not truly random and unfairly selected certain groups of individuals over others. 

365 days of the year were printed on sheets of paper and placed in a shoebox.

    { January 1, January 2, ... , Feburary 1, February 2, ... , December 30, December 31 }

Slips of paper were then selected at random and anyone of eligible age who had a birthday on the date indicated would be drafted. The important point is *individuals who shared the same birthday* would be drafted at the same time. As example, two men who had the birthdays April 5:sup:`th`, 1946 and April 5:sup:`th`, 1947 would both be drafted in the event a slip of paper *"April 5"* was selected.

.. _project_three_project:

Project
=======

1. Discuss the following questions
   
    a. Is the selection method used for the draft random? Why or why not?
    
    b. If the selection method used for the draft were truly random, what shape would you expect a frequency distribution of the sample to have? 
    
    c. Given the information provided on the selection method, what shape do you expect a frequency distribution of the sample to have?
    
    d. What are some possible sources of bias in the draft lottery? List the cases and identify the *type* of bias in each case.

2. During the first year of the draft, 1969, months were put into the shoebox in ascending order. In other words, the birth dates in the month of December were first put in the bottom of the shoebox, then birth dates in November were placed on top of the December birth dates, then October birth dates were placed on top of the November birth dates, and so on up to January. The slips of paper were not mixed any further before the draft was selected. 

    a. How does this information affect your answer to *#1a*? 

    b. How does this information affect your answer to *#1c*?

    c. How does this information affect your answer to *#1d*?

3. Using the birth month of the drafted individual as the bins, construct histograms for the years 1969, 1970, 1971, 1972. 

3. Based on the histograms constructed, describe the shape of the distribution for each year's draft lottery. 
   
   a. Are the graphs skewed, uniform, normal or bimodal?
   
   b. What is the mode of the birth month for each year? 
   
   c. What can we conclude about the relative likelihood of a male with a birthday in January being drafted versus a male with a birthday in December being drafted for the year of 1969? Does this same result appear to hold for 1970, 1971 and 1972?
   
   d. Discuss the results. Was the draft lottery fair? If not, why not? If so, why? Justify your answer.  

.. _project_three_dataset:

Dataset
=======

You can download the full dataset :download:`here <../../assets/datasets/vietnam_draft_data.csv>`.

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Vietnam Draft Lottery Data
   :file: ../../assets/datasets/previews/vietnam_draft_data_preview.csv

The meaning of the columns is as follows.

*M* represents the birth month of the draftee,
    
    M = 1, 2, 3, ... , 11, 12

*D* represents the birth day of the draftee,

    D = 1, 2, 3, ... , 30, 31 

And *N69*, *N70*, *N71* and *N72* represent the number of individuals selected with a given birth date in the years 1969, 1970, 1971 and 1972, respectively.

Cleaning the Data Set
---------------------

The *experimental unit* in this lab is a date. Each entry in the datasets corresponds to a particular birthdate, i.e. a month and day. For example, the first row of the dataset looks like,

| M | D | N69 | N70 | N71 | N72 |
| 1 | 1 | 305 | 133 | 207 | 150 |
| 1 | 2 | 159 | 195 | 225 | 328 |

The lab is asking to group the data into monthly classes so the sample can be visualized with a histogram. Since we are only interested in *birth months*, we may ignore the **D** column. That leaves us with our class data broken up across multiple rows of the list. We will need to manually group the data to calculate the total number of draftees per month.  

In other words, we will need to step (*iterate*) over the dataset and look at each row. As we do so, we will need to check if the first column **M** is 1, 2, 3, ..., 11 or 12. Then, based on the value of the first column **M**, we will grab the entries from the ``N69``, ``N70``, ``N71`` and ``N72`` columns and add them to the corresponding monthly totals. 

To re-iterate, to *clean the data*, we will need to perform the following steps:
    
    1.  create a list, named ``data_1969``, of twelve *0*'s, ``[0, 0, 0, ... , 0, 0]``, one for each month.
    
    2.  step through ``column_1`` with the ``row_number``.
    
    3.  grab the corresponding entry of the third column, ``column_3[row_number]``
    
    4.  add the value of the third column to the list entry in ``data_1969`` that represents that month. 

The following code snippet implements this algorithm, assuming you have the **M** column stored in ``column_1`` and the ``N69`` column stored in ``column_3``. Use this logic in the lab to clean your data,

.. code:: python 

    data_1969 = [ 0 ] * 12

    for row_number, entry in enumerate(column_1):
        data_1969[int(entry) - 1] += column_3[row_number]
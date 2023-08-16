================
Statistical Bias
================

In this project, you will perform some graphical analysis on a famously biased data set. 

Instructions
============

1. Download the dataset spreadsheet below and rename it `LASTNAME_FIRSTNAME_YYYYMMDD_Project_1.csv`, replacing `LASTNAME`, `FIRSTNAME` and `YYYYMMDD` with your last name, first name and the date, respectively.
2. affects
3. adsf
   

Background
==========

In the years 1969, 1970, 1971 and 1972, the Selective Service System in the United States held a draft lottery by order of Lyndon B. Johnson for men born between the dates of January 1, 1944 and December 31, 1950 [*]_. 

.. [*] Vietnam War Draft Lottery
    `source <https://en.wikipedia.org/wiki/Draft_lottery_(1969)>`_

Individuals born between these dates were to be selected at random and drafted into military service.

Method of Observation
---------------------

The method used to select individuals for service is highly controversial. Many argued it was not truly random and unfairly selected certain groups of individuals over others. 

365 days of the year were printed on sheets of paper and placed in a shoebox.

    { January 1, January 2, ... , Feburary 1, February 2, ... , December 30, December 31 }

Slips of paper were then selected at random and anyone of eligible age who had a birthday on the date indicated would be drafted. The important point is *individuals who shared the same birthday* would be drafted at the same time. As example, two men who had the birthdays April 5 :sup:`th`, 1946 and April 5:sup:`th`, 1947 would both be drafted in the event a slip of paper *"April 5"* was selected.

Project
=======

1. Discuss the following questions
   - If the selection method used for the draft were truly random, what shape would you expect a frequency distribution of the sample to have? 
   - What are some possible sources of bias in the draft lottery? List the cases and identify the *type* of bias in each case.
2. Using the birth month of the drafted individual as the bins, construct histograms for the years 1969, 1970, 1971, 1972. Include **both** the frequency distributions and the  histograms in your report. 
3. Based on the histograms constructed, describe the shape of the distribution for each year's draft lottery. 
   - Are the graphs skewed, uniform or modal?
   - What is the mode of the birth month for each year?
   - What can we conclude about the relative likelihood of a male with a birthday in January being drafted versus a male with a birthday in December being drafted?
   - Discuss the results and how the draft lottery could have been improved. 

Data Set
========

The following table is the a preview of the data you will be using for this project. 

.. csv-table:: Vietnam Draft Lottery Data
   :file: ../datasets/previews/vietnam_draft_data_preview.csv


Where *M* represents the birth month of the draftee,
    
    M = 1, 2, 3, ... , 11, 12

*D* represents the birth day of the draftee,

    D = 1, 2, 3, ... , 30, 31 

And *N69*, *N70*, *N71* and *N72* represent the number of individuals selected with the birth date in the years 1969, 1970, 1971 and 1972, respectively.

You can download the full dataset :download:`here <../datasets/vietnam_draft_data.csv>`.
"""
Bar Chart
=========
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a bar chart for a (hard-coded) distribution of quiz grades.

.. note:: 

    This script is written to run in a `Continuous Integration Pipeline <https://about.gitlab.com/topics/ci-cd/>`_. It is used to render images for the `AP Stats Bishop Walsh website <https://bishopwalshmath.org>`_. In other words, it is running in an environment without a desktop. Read comments below for more information on running it on your computer. 
"""

##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib

## NOTE: How-To: Run This Script On Your Computer
#
# To render the website, I have to use a "headless" backend to generate the images. 
# If you want to run this script on your computer, comment out the following line 
# with the "#" you see appended to each line of this comment:

matplotlib.use('agg')

# And uncomment this line: 

# matplotlib.use('tkagg')

import matplotlib.pyplot as plt

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
fig, axs = plt.subplots()

# Generate Data
    # ``data``` is a dictionary. see python docs for more information: 
    # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    #
    # Dictionaries are "key-value" pairs, i.e. a set of (key, value)
    #  
    #   { 
    #       'key_1': value_1,
    #       'key_2': value_2 
    # }
    # 
    # "keys" are strings. they are like the "index" of a list. 
    #
    # Recall the third element of 
    # 
    #   this_list = [0, 1, 2]
    # 
    # Is accessed by through the bracket [] notation,
    #
    #   this_list[2]
    #
    # Dictionaries are a way of setting your own "index". Try loading the 
    # the following dictionary into your Python shell and executing,
    #
    #   data['A']
    #
    #   data['B']
    #
    #   etc.
data = {
    'A': 12,
    'B': 10,
    'C': 8,
    'D': 6,
    'E': 4,
    'F': 2
}

# find the sum of frequencies
    # frequencies are the "values", i.e. right-hand side, of the dictionary.
total_observations = sum(data.values())

# create the relative frequency distribution
    # iterate over all (key, value) pairs in the dictionary, and divide each value by 
    # the total number of observations
relative_freq = { key: (value / total_observations) for key,value in data.items() }

# Label the graph appropriately
plt.suptitle("Bar Chart of Quiz Grades")

# you can "template" strings with variables using f-strings. See python docs for more information:
    # https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
    # essentially, we are "injecting" the value of the variable in the string before it gets 
    # interpretted by Python and printed to screen.
plt.title(f"n = {total_observations}")
# Set the axes labels
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
    # access dictionary "keys", i.e. 'A', 'B', 'C', 'D', 'E', 'F', with data.keys() (or relative_freq.keys())
    # access dictionary "values", i.e. 12, 10, 8, 6, 4, 2 with data.values() (or relative_freq.values())

# Frequency Distribution 
# axs.bar(data.keys(), data.values(), color="lightblue", ec="red", width=0.5)

# RELATIVE Frequency Distribution
axs.bar(relative_freq.keys(), relative_freq.values(), color="lightblue", ec="red", width=0.5)
plt.show()
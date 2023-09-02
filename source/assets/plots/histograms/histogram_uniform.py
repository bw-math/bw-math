"""
Stacked Bar Chart
=================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a histogram for a sample of quiz grades.

.. note:: 

    This script is written to run in a `Continuous Integratiquiz gradeson Pipeline <https://about.gitlab.com/topics/ci-cd/>`_. It is used to render images for the `AP Stats Bishop Walsh website <https://bishopwalshmath.org>`_. In other words, it is running in an environment without a desktop. Read comments below for more information on running it on your computer. 
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
data = ( 
    [ 'F' for _ in range(33) ] +  
    [ 'E' for _ in range(74) ] + 
    [ 'D' for _ in range(32) ] + 
    [ 'C' for _ in range(35) ] + 
    [ 'B' for _ in range(67) ] +
    [ 'A' for _ in range(30) ] 
)

# Label the graph appropriately
plt.suptitle("Histogram of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
axs.hist(data, bins=6, range=(0,6), align='left', color="lightblue", ec="red")
plt.show()

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

# Create new Figure and Axes
fig, axs = plt.subplots()

# Generate data
data = ( 
    [ 'F' for _ in range(5) ] +  
    [ 'E' for _ in range(4) ] + 
    [ 'D' for _ in range(5) ] + 
    [ 'C' for _ in range(5) ] + 
    [ 'B' for _ in range(4) ] +
    [ 'A' for _ in range(4) ] 
)

# Label everything
plt.suptitle("Histogram of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
axs.hist(data, bins=6, range=(0,6), align='left', color="lightblue", ec="red")
plt.show()
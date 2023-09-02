"""
Bimodal Histogram
=================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a histogram for a sample of quiz grades.

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
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
fig, axs = plt.subplots()

# Generate Data
# NOTE: You can add the contents of lists together with "+"
data = ( 
    [ 50*rand.random() for _ in range(33) ] + # generate some random F's, 0 - 49
    [ 9*rand.random() + 50 for _ in range(74) ] + # generate some random E's, 50 - 59 
    [ 9*rand.random() + 60 for _ in range(32) ] + # generate some random D's, 60 -69
    [ 9*rand.random() + 70 for _ in range(35) ] + # generate some random C's, 70- 79
    [ 9*rand.random() + 80 for _ in range(67) ] + # generate some random B's, 80 - 89
    [ 10*rand.random() + 90 for _ in range(30) ] # generate some random A's, 90 - 100
)

# Label the graph appropriately
plt.suptitle("Histogram of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
axs.hist(data, bins=6, align='left', color="lightblue", ec="red")
plt.show()
"""
Relative Frequency Histogram
============================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a histogram for a sample of random data.

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
from matplotlib.ticker import PercentFormatter
import random as rand

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
fig, axs = plt.subplots()

# Generate data
#   NOTE: Range*(Random Number Between 0 and 1) will give us a dataset of samples 
#   between 0 and Range. In other words, the following command generates a list of 
#   length 100 where each element is a number between 0 and 50
data = [ 50*rand.random() for _ in range(100 ) ]
bins = [ 10, 20, 30, 40, 50 ]
bin_labels = [ "0 - 10", "11 - 20", "21 - 30", "31 - 40", "41 - 50"]

# NOTE: for the hist() function to plot percentages on the y-axis, each 
#       observation must be assigned a weight that represents what "proportion
#       of the sample it is.
weights = [ 1/len(data) for _ in data ]

# Label everything appropriately
plt.suptitle("Relative Frequency Histogram of Random Numbers between 0 and 50")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Classes")
axs.set_ylabel("Frequency")
axs.yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(ticks=bins, labels=bin_labels)

# Generate and output
axs.hist(data, bins=bins, weights=weights, align='left', color="lightblue", ec="red")
plt.show()
"""
The Effects of Outliers
=======================
Grant Moore
-----------
Some Point In The Distant Past
******************************

This script will generate a dot plot for a (hard-coded) distribution of quiz grades. It will then calculate the sample mean and sample median and plot them with red and green lines, respectively. We will alter the distribution of grades in class to see how it affects the sample mean and sample median.

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

# matplotlib.use('agg')

# And uncomment this line: 

# matplotlib.use('tkagg')

import matplotlib.pyplot as plt
import math

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

# Create New Figures and Axes
fig, axs = plt.subplots()

# Generate Data
# NOTE: the y-variable in the ordered pair is being increased by 1 in every iteration
#       of range(). This is so the dots can be stacked.
data = \
[ (3, i+1) for i in range(2) ] +\
[ (4, i+1) for i in range(3) ] +\
[ (5, i+1) for i in range(2) ] +\
[ (6, i+1) for i in range(6) ] +\
[ (7, i+1) for i in range(2) ] +\
[ (9, i+1) for i in range(1) ] 

# calculate number of samples
n = len(data)

# Label the graph appropriately
plt.suptitle("Dot Plot of Quiz Grades")
plt.title(f"n = {n}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Get the x-coordinates and get the y-coordinates
x_values = [bit[0] for bit in data]
y_values = [bit[1] for bit in data]

# Calculate sample mean
# NOTE: Only the x-coordinate is required. The y-value is only used 
#       to stack the dots.
sample_mean = sum(x_values) / n

# Find order statistics.
# NOTE: x_values are already sorted.
order = 0.5 * ( n + 1 )
order_floor = math.floor(order)
order_ceiling = math.ceil(order)
lower_percentile = x_values[order_floor]
upper_percentile = x_values[order_ceiling]
percentile_delta = (upper_percentile - lower_percentile)

# Calculate sample median
sample_median = lower_percentile + percentile_delta * (order - order_floor)

# Generate dotplot
axs.scatter(x_values, y_values)

# Plot the mean as a vertical line
plt.plot([sample_mean, sample_mean], [0, 10], linestyle="--", color="red")
# Plot sample median as a vertical line
plt.plot([sample_median, sample_median], [0, 10], linestyle="--", color="green")
# Label
plt.text(sample_mean + 1, 5, f"Sample Mean = {sample_mean}", color="red")
plt.text(sample_mean + 1, 4.5, f"Sample Median = {sample_median}", color="green")

plt.show()
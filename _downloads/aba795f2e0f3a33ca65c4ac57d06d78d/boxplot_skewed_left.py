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
#   NOTE: Range x (Random Number Between 0, 1) + Lower Limit
data = ( 
    [ 50*rand.random() for _ in range(10) ] + # generate some random F's, 0 - 49
    [ 9*rand.random() + 50 for _ in range(9) ] + # generate some random E's, 50 - 59 
    [ 9*rand.random() + 60 for _ in range(4) ] + # generate some random D's, 60 -69
    [ 9*rand.random() + 70 for _ in range(4) ] + # generate some random C's, 70- 79
    [ 9*rand.random() + 80 for _ in range(5) ] + # generate some random B's, 80 - 89
    [ 10*rand.random() + 90 for _ in range(3) ] # generate some random A's, 90 - 100
)
bins = [50, 60, 70, 80, 90, 100]

# Label the graph appropriately
plt.suptitle("Histogram and Box Plot of Quiz Scores")
plt.title(f"n = {len(data)}")
## Label Histogram Axes
axs[0].set_xlabel("Score")
axs[1].set_ylabel("Frequency")
## Label Boxplot Axes
axs[1].set_xlabel("Score")
axs[1].set_ylabel("Observation")

# Generate and output
## Plot Histogram
axs[0].hist(data,bins=bins,align='left', color="lightblue", ec="red")
## Plot Boxplot
axs[1].boxplot(data)
plt.show()
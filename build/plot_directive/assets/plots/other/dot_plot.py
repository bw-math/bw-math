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
data = \
[ (3, i+1) for i in range(2) ] +\
[ (4, i+1) for i in range(3) ] +\
[ (5, i+1) for i in range(2) ] +\
[ (6, i+1) for i in range(6) ] +\
[ (7, i+1) for i in range(2) ] +\
[ (9, 1) ]

# Label the graph appropriately
plt.suptitle("Dot Plot of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
axs.scatter([bit[0] for bit in data], [bit[1] for bit in data])
plt.show()
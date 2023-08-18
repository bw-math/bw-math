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
data = {
    'A': 12,
    'B': 10,
    'C': 8,
    'D': 6,
    'E': 4,
    'F': 2
}
# Label the graph appropriately
plt.suptitle("Bar Chart of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Generate and output
axs.bar(data.keys(), data.values(), color="lightblue", ec="red", width=1.0)
plt.show()
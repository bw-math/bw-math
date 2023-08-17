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
    # NOTE: 2 axes are being created!
    #       1 to graph the histogram
    #       1 to graph the ogive
fig, axs = plt.subplots(1,2)

# Generate data
data = ( 
    [ 'F' for _ in range(2) ] +  
    [ 'E' for _ in range(4) ] + 
    [ 'D' for _ in range(5) ] + 
    [ 'C' for _ in range(5) ] + 
    [ 'B' for _ in range(3) ] +
    [ 'A' for _ in range(2) ] 
)

# Label everything
plt.suptitle("Histogram and Ogive of Quiz Scores")
plt.title(f"n = {len(data)}")
## Label Histogram 
axs[0].set_xlabel("Grades")
axs[0].set_ylabel("Frequency")
## Label Ogive
axs[1].set_xlabel("Grades")
axs[1].set_ylabel("Cumulative Frequency")

# Generate and output
## Plot histogram
axs[0].hist(data, bins=6, range=(0,6), align='left', color="lightblue", ec="red")
## Plot ogive
axs[1].hist(data, bins=6, range=(0,6), align='left', color="lightblue", ec="red", cumulative=True)

plt.show()
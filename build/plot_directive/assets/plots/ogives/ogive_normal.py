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

# Generate data
data = ( 
    [ 'F' for _ in range(30) ] +  
    [ 'E' for _ in range(40) ] + 
    [ 'D' for _ in range(60) ] + 
    [ 'C' for _ in range(60) ] + 
    [ 'B' for _ in range(40) ] +
    [ 'A' for _ in range(30) ] 
)

# Label axes
plt.suptitle("Histogram of Quiz Grades")
plt.title(f"n = {len(data)}")
axs.set_xlabel("Grades")
axs.set_ylabel("Frequency")

# Plot data
axs.hist(data, bins=6, range=(0,6), align='left', color="lightblue", ec="red", cumulative=True)

# Show results
plt.show()
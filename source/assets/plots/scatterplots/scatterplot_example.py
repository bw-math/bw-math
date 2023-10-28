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

##################################################################################
###                                SCRIPT                                      ###
##################################################################################

import matplotlib.pyplot as mpl
import statistics as stat

bivariate_data = [ (1,2), (3,8), (5,6), (7, 13), (9, 21), (11, 19) ]
(fig, axes) = mpl.subplots()

x_data = [ obs[0] for obs in bivariate_data ]
y_data = [ obs[1] for obs in bivariate_data ]


axes.scatter(x_data, y_data)

axes.set_ylabel("y observation")
axes.set_xlabel("x observation")
mpl.show()

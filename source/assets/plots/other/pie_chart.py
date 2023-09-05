"""
Pie Chart
=========
Grant Moore
-----------
Some Point In The Distant Past
******************************

MMMM. Pie.

"""

##################################################################################
###                           IMPORT LIBRARIES                                 ###
##################################################################################

import matplotlib.pyplot as plot
import random

##################################################################################
###                           SCRIPT                                           ###
##################################################################################

def frequency(sample, x):
	freq = sum(1 for obs in data if obs == x)
	return freq
	 
sodas = ["Coke", "Pepsi", "Sprite", "RC"]

sample = [ random.choice(sodas) for _ in range(30) ]

fig, axes = plot.subplots()

axes.pie(sample, sodas)

plot.show()

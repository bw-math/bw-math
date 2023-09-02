import random 
import matplotlib as mpl
import matplotlib.pyplot as plot 

mpl.use("tkagg")

def sum_dice(dice): 
    roll = sum([random.randint(1, 6) for _ in range(dice) ])
    return roll

# number of experiments
n = 30
# number of rolls per experiment
m = 5

die_rolls = [ sum_dice(m) for _ in range(n) ]

fig, axes = plot.subplots()

axes.set_xlabel(f"Sum of {m} Die Rolls, {n} times")
axes.set_ylabel("Frequency")
axes.hist(die_rolls)

plot.show()

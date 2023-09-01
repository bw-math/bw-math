import random 
import matplotlib.pyplot as plot 

def sum_dice(): 
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll

n = 10

die_rolls = [ sum_dice() for _ in range(n) ]

fig, axes = plot.subplots()

axes.set_xlabel(f"Sum of {n} Die Rolls")
axes.set_ylabel("Frequency")
axes.hist(die_rolls, 6)

plot.show()

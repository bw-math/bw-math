import matplotlib

matplotlib.use('agg')

# matplotlib.use('tkagg')

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

fig, axs = plt.subplots()

plt.suptitle("Histogram of Quiz Scores")
plt.title("n = 100 students")

data = [ 0, 0, 1, 1, 1, 2, 2, 2, 2, 2 ]
weights = [ 1/len(data) for _ in data ]

axs.hist(data, bins=3, weights=weights, range=(0,3))

axs.yaxis.set_major_formatter(PercentFormatter(1))
axs.set_xlabel("Scores")
axs.set_ylabel("Percentage")

plt.show()
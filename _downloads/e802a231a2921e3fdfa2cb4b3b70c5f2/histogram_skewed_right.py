import matplotlib

matplotlib.use('tkagg')

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

fig, axs = plt.subplots()

axs.hist([ 0, 0, 1, 1, 1, 2, 2, 2, 2, 2], bins=3)

axs.yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
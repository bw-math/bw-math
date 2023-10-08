import csv
import statistics as stat
import matplotlib.pyplot as mpl

with open("velocity_of_light_data.csv") as infile:
    raw_data = [ obs for obs in csv.reader(infile) ]

headers = raw_data[0]
data = raw_data[1:]
clean_data = [ float(obs[0]) for obs in data ]
n = len(clean_data)

sample_mean = stat.mean(clean_data)
sample_median = stat.median(clean_data)
std_dev = stat.stdev(clean_data)
quartiles = stat.quantiles(clean_data, n = 4)
percentiles = stat.quantiles(clean_data, n = 100)
sample_min = min(clean_data)
sample_max = max(clean_data)

q1 = quartiles[0]
q3 = quartiles[2]
p95 = percentiles[-5]
p05 = percentiles[4]

print(" sample mean ", sample_mean)
print(" sample median ", sample_median)
print(" standard deviation ", std_dev)
print(" quartiles ", quartiles)
print(" percentiles ", percentiles)
print(" q1 ", q1)
print(" q3 ", q3)
print(" p95 ", p95)
print(" p05 ", p05)
print(" min ", sample_min)
print(" max ", sample_max)

(fig, axes) = mpl.subplots(3)

mpl.suptitle("Velocity of Light Graphs")

axes[0].hist(clean_data, color="lightblue", ec="red")
axes[0].plot([sample_mean, sample_mean], [0, 35], color="purple", label="sample mean")
axes[0].set_ylabel("Frequency")

axes[1].hist(clean_data, color="lightblue", ec="red", cumulative=True)
axes[1].set_ylabel("Cumulative Frequency")

axes[2].boxplot(clean_data, vert=False)
axes[2].set_ylabel("Sample")
axes[2].set_xlabel("km/s")

axes[0].legend()

mpl.show()

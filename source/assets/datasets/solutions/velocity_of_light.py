import csv, os, sys

import matplotlib

# matplotlib.use('tkagg')

import matplotlib.pyplot as plt

# determine which directory the script is in.
data_directory = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

fig, axs = plt.subplots()
# fig, axs = plt.subplots(1, 4)

# read in data
with open(f'{data_directory}/velocity_of_light_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]
    
# grab first column from csv file
column_1 = [ float(row[0]) for row in columns ]

print(column_1)

axs.hist(column_1, bins=8)

plt.show()
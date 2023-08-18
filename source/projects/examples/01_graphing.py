import csv, os, sys

# discover file path of python script
#   i.e., if your python script is stored in C:\\myuser\Documents\projects\script.py
#           this command will return "C:\\myuser\Documents\project"
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# read in data
with open(f'{script_directory}/example_univariate.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    raw_data = [ row for row in csv_reader ]

# separate headers from data
headers = raw_data[0]
columns = raw_data[1:]

# grab first column from csv file
column_1 = [ float(row[0]) for row in columns ]

print(column_1)

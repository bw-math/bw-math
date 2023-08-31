.. _files:

=====
Files
=====

CSV Files
=========

The following examples will load in a *CSV* file named ``example.csv``.

.. important:: 
    
    This example will only work if the script *py* file is saved in the same directory as the data *CSV* file.

.. code-block:: python 

    import csv

    # read in data
    with open(f'example.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        raw_data = [ row for row in csv_reader ]

    # separate headers from data
    headers = raw_data[0]
    columns = raw_data[1:]

    # grab first column from csv file and ensure it's a number (not a string)
    column_1 = [ float(row[0]) for row in columns ]

    print(column_1)
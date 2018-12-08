import os
import csv

csvpath = os.path.join('../Resources/budget_data.csv')

months = []
total_revenue = []



with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        total_revenue.append(int(row[1]))
import os
import csv

csvpath = os.path.join('../Resources/election_data.csv')


poll = {}

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

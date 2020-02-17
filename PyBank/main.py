import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Read CSV
with open(csvpath, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")
    #skip headers
    next(budget_csv)
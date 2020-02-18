import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables to hold data
Number_Months = 0
Net_Total = 0
Average_Change = 0
Greatest_Profit_Gain = 0
Greatest_Profit_Loss = 0
Profit_Loss = []
Changes = []

# Read CSV
with open(csvpath, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")
    #skip headers
    header = next(budget_csv)

    # Loop through data
    for row in budget_csv:
        # Find total number of months
        if row[0] != 0:
            Number_Months = Number_Months + 1

        # Find total amount of profits/losses
        Net_Total = Net_Total + int(row[1])

    for x in 

        # Find greatest increase/decrease in profit/loss
        # Add all profit/loss amounts to list
        MonthA = row[1]
        MonthB = row[1]
        monthly_change = MonthA - MonthB
        Changes.append(monthly_change)
        # Find average change
       # Average_Change = 

    Greatest_Profit_Gain = max(Profit_Loss)
    Greatest_Profit_Loss = min(Profit_Loss)


    # Print out report:
    print("  Financial Analysis")
    print("----------------------------")
    print(f"Total Number of Months: ${Number_Months}")
    print(f"Total Amount: ${Net_Total}")
    print(f"Average Change: {Average_Change}")
    print(f"Greatest Increase in Profits: {Greatest_Profit_Gain}")
    print(f"Greatest Decrease in Profits: {Greatest_Profit_Loss}")
    print("----------------------------")
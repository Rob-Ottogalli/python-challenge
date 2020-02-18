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
Months = []
Month_Change = {}

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

        # Add each row to list of Profit Loss
        amount = row[1]
        Profit_Loss.append(amount)

    # Calculate change in profit and loss for each month
    for x in range(0, len(Profit_Loss)-1):
        if x+1 == "":
            monthly_change = 0
        else:
            MonthA = int(Profit_Loss[x])
            MonthB = int(Profit_Loss[x+1])
            monthly_change = MonthB - MonthA
        Changes.append(monthly_change)

        #add each month to the list
        Month_Entry = row[0]
        Months.append(Month_Entry)
    # Calculate average change in profit and loss for all months
    Changes_Sum = sum(Changes)
    Average_Change = Changes_Sum/len(Profit_Loss)

    # Find max profit and max loss
    Greatest_Profit_Gain = max(Changes)
    Greatest_Profit_Loss = min(Changes)


    # Print out report:
    print("  Financial Analysis")
    print("----------------------------")
    print(f"Total Number of Months: ${Number_Months}")
    print(f"Total Amount: ${Net_Total}")
    print(f"Average Change: {Average_Change}")
    print(f"Greatest Increase in Profits: {Greatest_Profit_Gain}")
    print(f"Greatest Decrease in Profits: {Greatest_Profit_Loss}")
    print("----------------------------")

# Write to txt file
Report = open(w 'Report.txt', "Access_Mode")
Report.write("  Financial Analysis")
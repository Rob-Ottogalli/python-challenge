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

# Read CSV
with open(csvpath, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")
    #skip headers
    header = next(budget_csv)

    # Loop through data
    for row in budget_csv:
        # Find total number of months
        if row[0] != "":  #if row is not empty
            Number_Months = Number_Months + 1

        # Find total amount of profits/losses
        Net_Total = Net_Total + int(row[1])

        # Add each row to list of Profit Loss
        amount = row[1]
        Profit_Loss.append(amount)

        # Add each month to the list of Months
        Month_Entry = row[0]
        Months.append(Month_Entry)

    # Calculate change in profit and loss for each month
    for x in range(0, len(Profit_Loss)-1):
        # Calculate Monthly Change
        if x+1 == "":
            monthly_change = 0
        else:
            MonthA = int(Profit_Loss[x])
            MonthB = int(Profit_Loss[x+1])
            monthly_change = MonthB - MonthA
        Changes.append(monthly_change)

    # Calculate average change in profit and loss for all months
    Changes_Sum = sum(Changes)
    Average_Change = Changes_Sum/(len(Profit_Loss)-1)
    Average_Change = round(Average_Change, 2)

    # Find max profit and max loss
    Greatest_Profit_Gain = max(Changes)
    Greatest_Profit_Loss = min(Changes)

    # Find month of max profit and max loss
    # Find positions (index) of max profit and max losses in list of Changes
    Ind_Max = Changes.index(Greatest_Profit_Gain)
    Ind_Min = Changes.index(Greatest_Profit_Loss)
    
    # Find corresponding month in Months list
    Month_Max_Change = Months[Ind_Max+1]
    Month_Min_Change = Months[Ind_Min+1]
    

#List strings for report:
Rep_Header = "Financial Analysis"
Rep_Dash = "----------------------------"
Rep_Months = f"Total Number of Months: {Number_Months}"
Rep_Net_Total = f"Total Amount: ${Net_Total}"
Rep_Avg_Change = f"Average Change: ${Average_Change}"
Rep_Inc_Profits = f"Greatest Increase in Profits: {Month_Max_Change} (${Greatest_Profit_Gain})"
Rep_Dec_Profits = f"Greatest Decrease in Profits: {Month_Min_Change} (${Greatest_Profit_Loss})"

# Print report to Terminal:
print(Rep_Header)
print(Rep_Dash)
print(Rep_Months)
print(Rep_Net_Total)
print(Rep_Avg_Change)
print(Rep_Inc_Profits)
print(Rep_Dec_Profits)
print(Rep_Dash)

# Write report to txt file
with open("Financial Report.txt", "w") as csvwrite:
    csvwrite.write(f"{Rep_Header}\n"
            f"{Rep_Dash}\n"
            f"{Rep_Months}\n"
            f"{Rep_Net_Total}\n"
            f"{Rep_Avg_Change}\n"
            f"{Rep_Inc_Profits}\n"
            f"{Rep_Dec_Profits}\n"
            f"{Rep_Dash}\n")
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_test.csv')

# Initialize variables to hold data
Total_Votes = 0
Candidates = []
Candidate1 = ""
Candidate2 = ""


# Read CSV
with open(csvpath, newline="") as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")
    # skip headers
    header = next(election_csv)

    # Loop through data 
    for row in election_csv:
        # Find total number of votes
        if row[0] != 0:
            Total_Votes = Total_Votes + 1

        # Find unique Candidates.  Append to list
        if str(row[2]) not in Candidates:
            Candidates.append(str(row[2])) 
    Num_Cand = len(Candidates)


print(Total_Votes)
print(Candidates)
print(Num_Cand)
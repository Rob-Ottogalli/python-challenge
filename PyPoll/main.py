import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables to hold data
Total_Votes = 0
Candidates = []
Candidate1 = ""
Candidate2 = ""
Candidate3 = ""
Candidate4 = ""



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

    # Loop through data
    # for row in election_csv:
        # find discrete candidates
        Candidate1 = row[2]
        if row[2] != Candidate1 or row[2] != Candidate2:
            Candidate3 = row[2]
        if row[2] != Candidate1:
            Candidate2 = row[2]


print(Total_Votes)
print(Candidate1)
print(Candidate2)
print(Candidate3)
print(Candidate4)
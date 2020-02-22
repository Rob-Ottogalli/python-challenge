import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_test.csv')

# Initialize variables to hold data
Total_Votes = 0
Candidates = []
Final_Count = {}

# Define function for counting a candidates number of votes
def Vote_Tally(candidate):
    Candidate_Votes = 0
    for row in election_csv:
        candidate = Candidates[0]
        if row[2] == candidate:
            Candidate_Votes = Candidate_Votes + 1
    print(Candidate_Votes)
    Final_Count.update(candidate = Candidate_Votes)
    print(Final_Count)



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

   # Find number of Candidates
    Num_Cand = len(Candidates)

    print(Vote_Tally(Candidates[0]))



print(Total_Votes)
print(Candidates)
print(Num_Cand)
print(Candidates[0])
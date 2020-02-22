import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_test.csv')

# Initialize variables to hold data
Total_Votes = 0
Candidates = []
Final_Count = {}
Candidate_Votes = 0

# Define function for counting a candidates number of votes
# def Vote_Tally(candidate):
#     Candidate_Votes = 0
#     for row in election_csv:
#         candidate = Candidates[0]
#         if row[2] == candidate:
#             Candidate_Votes = Candidate_Votes + 1
#     print(Candidate_Votes)
#     Final_Count.update(candidate = Candidate_Votes)
#     print(Final_Count)

# TEst here
def Vote_Tally(candidate):
    Candidate_Votes = 0
    candidate = Candidates[x]
    for row in election_csv:
        # candidate = Candidates[0]
        if row[2] == Candidates[x]:
            Candidate_Votes = Candidate_Votes + 1
        # x = candidate
    y = Candidate_Votes
    Final_Count.update([(candidate, y)])
    # print(Final_Count)
    # print(Candidate_Votes)


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

    # print(Vote_Tally(Candidates[0]))

for x in range(0, Num_Cand):
    Cand = Candidates[x]

# Read CSV
with open(csvpath, newline="") as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")

    # Code works - finds correct count
    # for x in range(0, Num_Cand):
    #     for row in election_csv:
    #         if row[2] == Cand:
    #             Candidate_Votes = Candidate_Votes + 1
    #             j = Candidates[x]
    #             y = Candidate_Votes
    #             Final_Count.update(j = y)
    for x in range(0, Num_Cand):
        candidate = Candidates[x]
        count = Vote_Tally(Candidates[x])
        # Final_Count.update( = count)


print(f"Total Votes = {Total_Votes}")
print(Candidates)
print(f"Number of Candidates: {Num_Cand}")
print(Final_Count)
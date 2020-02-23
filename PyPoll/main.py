import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_test.csv')

# Initialize variables to hold data
Total_Votes = 0
Candidates = []
Final_Count = {}
Candidate_Votes = 0

# Vote Tally function to count the number of votes for a single candidate
def Vote_Tally(candidate):
    Candidate_Votes = 0             # Initialize variable for number of candidate votes
    # candidate = Cand       # Set candidate to be equal to candidate in list.  Applicable in a for loop.
    for row in election_csv:        # Search for candidate's number of occurrences in the CSV. 
        if row[2] == candidate:         # Increase the # of candidate votes if candidates' name is found
            Candidate_Votes = Candidate_Votes + 1
    y = Candidate_Votes             # Set value for dictionary
    Final_Count.update([(candidate, y)])    # Append key:value to dictionary, where candidate's name is the key and candidate votes is the value
    return Final_Count
    # Candidate_Votes = 0

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

# for x in range(0, Num_Cand):
#     Cand = Candidates[x]

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
    
    # Count votes for each candidate.  Loop through each candidate
    for x in range(0, Num_Cand):
        Cand = Candidates[x]
        count = Vote_Tally(Cand)
       
        # Final_Count.update( = count)
        # y = Candidate_Votes             # Set value for dictionary
        # Final_Count.update([(candidate, count)])    # Append key:value to dictionary, where candidate's name is the key and candidate votes is the value

    # Khan = Vote_Tally("Khan")
    # Correy = Vote_Tally("Correy")
    # Li = Vote_Tally("Li")


### NOTE:  The function above only calculates for Candidate 0.  Need to debug to get it through the

print(f"Total Votes = {Total_Votes}")
print(Candidates)
print(f"Number of Candidates: {Num_Cand}")
print(Final_Count)

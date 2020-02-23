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
# "candiate" in the input of the function will be the candidate's name
def Vote_Tally(candidate):
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Count number of candidate votes
        Candidate_Votes = 0                             # Initialize variable for number of candidate votes
        for row in election_csv:                        # Loop through rows of CSV.
            if row[2] == candidate:                     # Search for candidate's name in each row. 
                Candidate_Votes = Candidate_Votes + 1   # Increase the # of candidate votes if candidates' name is found.
        y = Candidate_Votes                             # Set value for dictionary to # of occurrences of candidate's name
        Final_Count.update([(candidate, y)])            # Append key:value to dictionary, where candidate's name is the key and candidate votes is the value
        return Final_Count                              # Return updated dictionary, with new candidate/vote counts added


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

    # Count votes for each candidate.  Loop through each candidate
    for x in range(0, Num_Cand):
        Cand = Candidates[x]
        count = Vote_Tally(Cand)
    # print(Vote_Tally(Candidates[0]))

# for x in range(0, Num_Cand):
#     Cand = Candidates[x]

        # Final_Count.update( = count)
        # y = Candidate_Votes             # Set value for dictionary
        # Final_Count.update([(candidate, count)])    # Append key:value to dictionary, where candidate's name is the key and candidate votes is the value


### NOTE:  The function above only calculates for Candidate 0.  Need to debug to get it through the

print(f"Total Votes = {Total_Votes}")
print(Candidates)
print(f"Number of Candidates: {Num_Cand}")
print(Final_Count)

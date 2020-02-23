import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables to hold data
Total_Votes = 0
Candidates = []
Final_Count = {}
Final_Percents = {}

# Vote Tally function to count the number of votes cast for a single candidate
# "candidate" in the input of the function will be the candidate's name
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

# Find the total number of votes cast
def Total_Votes_Counter():
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Initialize variable
        Total_Votes = 0
        # Loop through data 
        # FIND TOTAL VOTES
        for row in election_csv:
            # Find total number of votes
            if row[0] != 0:
                Total_Votes = Total_Votes + 1
        return Total_Votes

# Find the unique candidates
def Unique_Candidates():
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Find unique Candidates.  Append to list
        for row in election_csv:
            if str(row[2]) not in Candidates:
                Candidates.append(str(row[2])) 
        return Candidates

# Loop through each candidate's name to find votes cast for all candidates
def Loop_Vote_Tally():
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Find number of Candidates
        Num_Cand = len(Candidates)

        # Count votes for each candidate.  Loop through each candidate
        for x in range(0, Num_Cand):
            Cand = Candidates[x]
            count = Vote_Tally(Cand)
        return count


def Loop_Percent_Tally():
    # Find number of Candidates
    Num_Cand = len(Candidates)

    Final_Count = {}
    Final_Count = Loop_Vote_Tally()

    # Sort dictionary by values
    # Final_Count = sorted(Final_Count.values())

    # Find percent of votes for each candidate.  Loop through each candidate
    # for k,v in Final_Count.items():


    for x in range(0, Num_Cand):
        Cand = Candidates[x]
        j = Cand
        Percent_Vote = Final_Count[j] /Total_Votes * 100
        y = round(Percent_Vote, 4)
        Final_Percents.update([(j,y)])
    return Final_Percents



Total_Votes = Total_Votes_Counter()
Candidates = Unique_Candidates()
Num_Cand = len(Candidates)
Final_Count = Loop_Vote_Tally()
Final_Percents = Loop_Percent_Tally()

# Determine Winner
Winning_Total = max(Final_Percents.values())
Winner = [k for k, v in Final_Percents.items() if v == Winning_Total]


#####################################
# GENERATE REPORT
#####################################

# Use 
Report_Header = "Election Results"
Dash = "----------------------------"
Report_Total_Votes = f"Total Votes: {Total_Votes}"
Report_Winner = f"Winner: {Winner}"

# Print to Terminal
print(Report_Header)
print(Dash)
print(Report_Total_Votes)
print(Dash)
# Loop through Candidate data
for k,v in Final_Percents.items():
    print(f"{k}: {v}% ({Final_Count[k]})")
print(Dash)
print(Report_Winner)
print(Dash)

# Write report to txt file
with open("Election Results.txt", "w") as csvwrite:
    csvwrite.write(
        f"{Report_Header}\n"
        f"{Dash}\n"
        f"{Report_Total_Votes}\n"
        f"{Dash}\n"
        )
    for k,v in Final_Percents.items():
        csvwrite.write(f"{k}: {v}% ({Final_Count[k]})\n")
    csvwrite.write(
        f"{Dash}\n"
        f"{Report_Winner}\n"
        f"{Dash}\n"
    )
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

#####################################
# Initialize variables to hold data
#####################################

Total_Votes = 0                                         # Variable to hold total of all votes
Candidates = []                                         # Variable to hold list of all unique candiate names
Final_Count = {}                                        # Dictionary to hold candidate names as keys, and the votes cast for each candidate as values.
Final_Percents = {}                                     # Dictionary to hold candidate names as keys, and the percentage of votes cast for each candidate as values.


#####################################
# Define functions to calculate data
#####################################

# Find each unique candidate's name.  Add each candidate's name to a list.
def Unique_Candidates():
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Loop through data
        for row in election_csv:                    
            if str(row[2]) not in Candidates:           # Look unique candidate's names. (I.e. names not already in Candidates[] list)
                Candidates.append(str(row[2]))          # Append to list.
        return Candidates                               # Return updated list of Candidates.

# Find the total number of votes cast.
def Total_Votes_Counter():
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Initialize variable inside function.
        Total_Votes = 0

        # Loop through data        
        for row in election_csv:            
            if row[0] != 0:                             # If Voter ID row is not empty,
                Total_Votes = Total_Votes + 1           # then add 1 vote to list of total votes.
        return Total_Votes                              # Return total number of votes in variable. 

# Count the number of votes cast for a single candidate;
def Vote_Tally(candidate):                              # "candidate" in the input of the function will be the candidate's name.
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
        return Final_Count                              # Return updated dictionary, with new candidate/vote counts added.



# Loop through each candidate's name to find votes cast for all candidates.
def Loop_Vote_Tally():
    # Read CSV
    with open(csvpath, newline="") as csvfile:
        election_csv = csv.reader(csvfile, delimiter=",")
        # skip headers
        header = next(election_csv)

        # Find number of Candidates
        Num_Cand = len(Candidates)                      

        # Count votes for each candidate. 
        for x in range(0, Num_Cand):                    # Loop through each candidate in list of candidates.
            Cand = Candidates[x]                        # Set variable to hold candidate's name. Candidate's name will change for each loop.
            count = Vote_Tally(Cand)                    # Run function to tally votes for that candidate. Set count variable to hold candidate vote number.
        return count                                    # Return count variable

# Find Percent of each candidate's vote count vs. total votes.
def Loop_Percent_Tally():
    # Initialize local variables to hold data                  
    Num_Cand = len(Candidates)                          # Find number of Candidates
    Final_Count = {}                                    # Dictionary to hold candidate names as keys, and the votes cast for each candidate as values.
    Final_Count = Loop_Vote_Tally()                     # Dictionary to hold candidate names as keys, and the percentage of votes cast for each candidate as values.
                                                        # Values for Final_Count determined by the Loop_Vote_Tally function above
    # Loop through range of candidates
    for x in range(0, Num_Cand):
        j = Candidates[x]                                   # Set variable j to hold candidate name
        Percent_Vote = Final_Count[j] /Total_Votes * 100    # Calculcate percent vote for that candidate. Use j to call candidate's vote number from Final_Count dictionary. Divide by total votes.
        y = round(Percent_Vote, 4)                          # Set variable y to hold Percent vote for that candidate. Round Percent Vote to 4 decimal places.
        Final_Percents.update([(j,y)])                      # Append candidate name as key, and candidate percent vote as value to dictionary.
    return Final_Percents                                   # Return updated dictionary of candidate names/percents.


Total_Votes = Total_Votes_Counter()                     # Set Total_Votes variable to hold total number of votes.
Candidates = Unique_Candidates()                        # Set Candidates list to hold names of all candidates.
Num_Cand = len(Candidates)                              # Set variable to hold number of candidates.
Final_Count = Loop_Vote_Tally()                         # Set Final_Count dictionary to hold each candidate's name and number of votes.
Final_Percents = Loop_Percent_Tally()                   # Set Final_Percents dictionary to hold each candidate's name and percentage of votes.

# Determine Winner
Winning_Total = max(Final_Percents.values())            # Set variable to find greatest number of votes. (Value in the Final_Percents dictionary.)
Winner = [k for k, v in Final_Percents.items() if v == Winning_Total]   # Set variable to find name of candidate who had the greatest percent of votes.


#####################################
# GENERATE REPORT
#####################################

# Print to Terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {Total_Votes}")
print("----------------------------")
# Loop through Candidate data
for k,v in Final_Percents.items():
    print(f"{k}: {v}% ({Final_Count[k]})")
print("----------------------------")
print(f"Winner: {Winner}")
print("----------------------------")

# Write report to txt file
with open("Election Results.txt", "w") as csvwrite:
    csvwrite.write(
        f"Election Results\n"
        f"----------------------------\n"
        f"Total Votes: {Total_Votes}\n"
        f"----------------------------\n"
        )
    for k,v in Final_Percents.items():
        csvwrite.write(f"{k}: {v}% ({Final_Count[k]})\n")
    csvwrite.write(
        f"----------------------------\n"
        f"Winner: {Winner}\n"
        f"----------------------------\n"
    )
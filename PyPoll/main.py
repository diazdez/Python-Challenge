# PYPOLL: Homework
# 	PyPoll CSV File: election_data.csv  
# 	CSV has to 3 headers: "Voter ID", "County" & “Candidate”
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
#   Put together final script should both print the analysis to the terminal 
#   Export a text file with the analysis/results.

# Identify Variables
vote_count = 0 
candidates_with_votes = []
candidate_vote_num = []
pct_of_votes = []

# create file path across Operating Systems (os)
# module for reading the csv file 
import os
import csv

# file path
csvpath = os.path.join('Resources', 'election_data.csv')
# open/read file 
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
# number of rows equals the number of votes: 
        vote_count = vote_count + 1

    for row in csvreader:
# Candidates are listed in Column 3 (Index = 2)
        listed_candidate = (row[2])


#RESULTS 
print()
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_count))
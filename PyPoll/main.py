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

#Variables
votes = 0
differCandidate =[]
candidatevotes= []

# create file path across Operating Systems (os)
# module for reading the csv file 
import os
import csv

# file path
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
# Total # of votes:  will sum the # of rows
        votes = votes + 1
#review the candidate is listed on column 3 (index position 2) & will calculate total # of candidates. 
        listedCandidate = (row[2])

#will need to dicipher each listed candidate: gather the number of times a specific candidate is listed.
        if listedCandidate in differCandidate: 
            candidatenumber = differCandidate.index(listedCandidate)
            candidatevotes[candidatenumber] = candidatevotes[candidatenumber] +1
        
        elif
#if candidate is not a differCandidate then use the append function 
#add 1 vote for differCandidate
            differCandidate.append(listedCandidate)
            candidatevotes(row[2]) = 1
        
    for differCandidate in candidatevotes
        print(differCandidate + candidatenumber)

# % votes each differCandidate won

# print()
# print("Election Results")
# print("-------------------------")
# print("Total Votes " + str(votes))
# print("-------------------------")
# print (results)
# print("-------------------------")
# print("Winner: " + str(winner[0]))
# print("-------------------------")
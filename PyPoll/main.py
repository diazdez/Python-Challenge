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
candidate_vote_num = [0,0,0,0]
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

# Candidates are listed in Column 3 (Index = 2)
        listed_candidate = (row[2])

# Need to find the different candidates in the Column 3
# Need to find the vote count for each candidate

        if listed_candidate not in candidates_with_votes:
#index the candidate to the list
            candidates_with_votes.append(listed_candidate)
        else:
            pass

# print(candidates_with_votes) = found a total of 4 different types of candidates
#increase vote count by 1
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        if row[2] == candidates_with_votes[0]:
            candidate_vote_num[0] = candidate_vote_num[0] +1
        elif row[2] == candidates_with_votes[1]:
            candidate_vote_num[1] = candidate_vote_num[1] +1
        elif row[2] == candidates_with_votes[2]:
            candidate_vote_num[2] = candidate_vote_num[2] +1
        elif row[2] == candidates_with_votes[3]:
            candidate_vote_num[3] = candidate_vote_num[3] +1
#print(candidate_vote_num)

high_vote_count = 0
votecount_index = 0


for x in range(len(candidates_with_votes)):
#calculate the percentage of votes received per candidate: (CandidateVote#/TotalVote#)*100
    pct = round(candidate_vote_num[x]/vote_count*100, 3)
    pct_of_votes.append(pct)
    
    if candidate_vote_num[x] > high_vote_count:
        high_vote_count = candidate_vote_num[x]
        votecount_index = x

winner = candidates_with_votes[votecount_index] 
# print(winner)


# RESULTS 
print()
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------")
for x in range(len(candidates_with_votes)):
    print(str(candidates_with_votes[x]) + ": " +str(pct_of_votes[x])+"%" + "  "+ "(" +str(candidate_vote_num[x]) +")") 
print("-------------------------")
print("Winner: " + (winner)) 
print("-------------------------")

# save output file path
# output_file = os.path.join("output.csv")
# open the output file
# with open(output_file,"w") as txt_file: 
# txt_file.write("Total Votes: " + str(vote_count))
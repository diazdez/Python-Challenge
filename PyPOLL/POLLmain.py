# create file path across Operating Systems (os)
# module for reading the csv file 
import os 
import csv

#file path
pypollcsvpath = os.path.join("..",'Resources_PyPoll', 'PyPoll_Resources_election_data.csv')
print(pypollcsvpath)

with open(pypollcsvpath, "r") as data:
    print("In file")

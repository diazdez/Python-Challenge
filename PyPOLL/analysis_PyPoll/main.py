
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period


# create file path across Operating Systems (os)
# module for reading the csv file 
import OS
import csv

# file path
csvpath = os.path.join('Resources','election_data.csv')
# read/open the Budget csv file
with open(csvpath) as election_data

    csvreader = csv.reader(belection_data, delimiter=",")

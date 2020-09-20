# 	PyBank CSV File: budget_data.csv  
# 	CSV has to 2 headers: “Date” & “Profit/Losses”


# create file path across Operating Systems (os)
# module for reading the csv file 
import os
import csv

# file path
budget_data = os.path.join('..','Resources','budget_data.csv')

# read/open the Budget csv file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

# HOMEWORK ASSIGNMENT: 
# Calculate total number of months included in the dataset
# Calculate the net total amount of "Profit/Losses" over the entire period
# Calculate the average of the changes in "Profit/Losses" over the entire period
# Calculate the greatest increase in profits (date and amount) over the entire period
# Calculate the greatest decrease in losses (date and amount) over the entire period
# * print the analysis to the terminal AND export a text file with the results.

#create some variables
# TOTALMONTHS = total_months
# TOTALPL = total_profitlosses
# AvgProfitLosses = average_PL


# # need to review the data
    

# #calculate total number of months by counting total rows in Date Column. 
# total_months = len(row["Date"])

# #calculate net total amount of "Profit/Losses"
# total_profitlosses = sum(row["Profit/Losses"])

# #average of the changes in "Profit/Losses": divide TOTALPL by TOTALMONTHS (bc it equals the # of rows)
# average_PL = total_profitlosses / total_months


#print("Financial Analysis")
# print("------------------------------")
# print(f"Total Months: {str(TOTALMONTHS)}")
# print(f"Total: + "$"+ {str(TOTALPL)}")
# print(f"Average Change: + "$" + {str(TOTALPL)})
# print(f"Greatest Increase in Profits: ")
# print(f"Greatest Decrease in Profits: ")
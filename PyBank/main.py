# PYBANK: Homework
# 	PyBank CSV File: budget_data.csv  
# 	CSV has to 2 headers: “Date” & “Profit/Losses”
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
#   Put together final script should both print the analysis to the terminal 
#   Export a text file with the analysis/results.

# Variables
TotalMonths = 0
TotalPL= 0
PLlastrow = 0 
AveragePL = 0

TotalDif = 0
max_increase = 0 
max_decrease = 0 
max_inc_month = []
max_dec_month = []


# create file path across Operating Systems (os)
# module for reading the csv file 
import os
import csv

# file path
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

#need to calculate total number of months included in the dataset... each month is designated to their own row. 
#confirmed csvheader will not include the header in the count. 
    for row in csvreader:
        TotalMonths = TotalMonths +1

#the Profit/Losses (PL) value is found in the second column (index = 1) 
        TotalPL = TotalPL + int(row[1])

#need to calculate the average of the changes in "Profit/Losses" (PL) Column
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

#clarified that the average can be calculated by subtracting the value from the 1st and the Last Month. Then divide that by the total rows of data. 
#total number of row = the # for total months... will divide by TotalMonths
    for row in csvreader:
        PLdiffer = int(row[1]) - PLlastrow
        TotalPL = TotalPL + PLdiffer
        PLlastrow = int(row[1])
        AveragePL = TotalPL/TotalMonths

# Calculate greatest increase in profits (date and amount)  
# Calculate greatest decrease in losses (date and amount) 
# obtain the Date from Column 1(Index 0)
        if PLdiffer > max_increase: 
                max_increase = PLdiffer
                max_inc_month= row[0]
        elif PLdiffer < max_decrease: 
                max_decrease = PLdiffer
                max_dec_month= row[0]


#RESULTS: 
        print(" ")
        print("Financial Analysis")
        print("-------------------------")
        print("Total Months: " + str(TotalMonths))
        print("Total: " + "$" + str(TotalPL))
        print("Average Change: " + "$" + str(AveragePL))
        print("Greatest Increase in Profits: " + str(max_inc_month) + " ($" +  str(max_increase) + ")") 
        print("Greatest Decrease in Profits: " + str(max_dec_month) + " ($" +  str(max_decrease) + ")")

# save output file path as text
pybank_output_file = os.path.join("..", "pybank_output.txt")

# open the output file with write mode
with open(pybank_output_file,"w") as text:
    text.write(("   ")+ '\n')
    text.write(("Financial Analysis")+ '\n')
    text.write(("-------------------------")+ '\n')
    text.write(("Total Months: " + str(TotalMonths))+ '\n')
    text.write(("Total: " + "$" + str(TotalPL))+ '\n')
    text.write(("Average Change: " + "$" + str(AveragePL))+ '\n')
    text.write(("Greatest Increase in Profits: " + str(max_inc_month) + " ($" +  str(max_increase) + ")") + '\n')
    text.write(("Greatest Decrease in Profits: " + str(max_dec_month) + " ($" +  str(max_decrease) + ")")+ '\n')
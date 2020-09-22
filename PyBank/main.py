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
AveragePL = 0
PLdata = []



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
    print(TotalMonths)

#need to calculate sum of the values found in "Profit/Losses" (PL) column
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

#the Profit/Losses (PL) value is found in the second column (index = 1) is an Integer
    for row in csvreader:
        TotalPL = TotalPL + int(row[1])
    print(TotalPL)


#need to calculate the average of the changes in "Profit/Losses" (PL) Column
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

#clarified that the average can be calculated by subtracting the value from the 1st and the Last Month. Then divide that by the total rows of data. 
    for row in csvreader:
        PLdata.append(row[1])
        PLdiffer = (int(PLdata[0])-int(PLdata[85]))
        print(PLdiffer)

    #     PLdata.append(row[1])
    #     print(int(PLdata[0]))
    #     print(int(PLdata[85]))
    # AveragePL = (int(PLdata[85])-int(PLdata[0]))/85
    # print(AveragePL)


# Calculate greatest increase in profits (date and amount)  
# Calculate greatest decrease in losses (date and amount) 

#RESULTS: 
# print()
# print("Financial Analysis")
# print("-------------------------")
# print("Total Months: " + str(TotalMonths))
# print("Total: " + "$" + str(TotalPL))
# print("Average Change: " + "$" + str(AveragePL))
# print("Greatest Increase in Profits: " ) 
# print("Greatest Increase in Profits: " )

## save output file path
# output_file = os.path.join("output.csv")
## open the output file
# with open(output_file,"w") as txt_file: 
#   txt_file.write("Total Months: " + str(TotalMonths)
#   txt_file.write("Total: " + "$" + str(TotalPL))
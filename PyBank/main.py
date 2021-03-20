import os
import csv

#Path to collect data from the Resources folder
pollData_csv = os.path.join("..","Resources","budget_data.csv")

#Calculate total number of months in the data set
months = 0
#Calculate net total number of profit/losses
netTotal = 0
#Calculate the changes in profit/losses over entire period, and then find the average of those changes
profit_loss = []
change = []
#The greatest increase in profits (date and amount) over the entire period
greatest_increase_date = ""
greatest_increase_amount = 0
#Greatest decrease in losses (date and amount) over the entire period
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Read csv file
with open (pollData_csv, "r") as csvfile:
    
    #split the data on commas
    csvreader = csv.read(csvfile, delimiter= ",")

    #loop through the data
    for row in csvreader:
        months = months + 1
        netTotal = netTotal + row[1]
        profit_loss.append(row[1])
        if row[1] > greatest_increase_amount:
            greatest_increase_amount = row[1]
            greatest_decrease_date = row[0]
        elif row[1] < greatest_decrease_amount:
            greatest_decrease_amount = row[1]
            greatest_decrease_date = row[0]
        else:
            pass 

#loop through profit and loss and calculate change, append to change list
for value in profit_loss:
    difference = value + ()
    


#print analysis to terminal and and export a test file with the resutls.
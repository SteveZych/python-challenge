import os
import csv

#Path to collect data from the Resources folder
bankData_csv = os.path.join("Resources","budget_data.csv")

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
with open (bankData_csv, "r") as csvfile:
    
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter= ",")

    header = next(csvreader)

    #loop through the data
    for i, row in enumerate(csvreader):
        months = months + 1
        #netTotal = netTotal + int(row[1])
        profit_loss.append(int(row[1]))
        if i > 0:
            change_row = int(row[1]) - int(previous_row[1])
            change.append(change_row)
            if  change_row > greatest_increase_amount:
                greatest_increase_amount = change_row
                greatest_increase_date = row[0]
            if change_row < greatest_decrease_amount:
                greatest_decrease_amount = change_row
                greatest_decrease_date = row[0]
        previous_row = row
        
sum_profit_loss = sum(profit_loss)
average_change = sum(change) / len(change)
avg_change_rounded = round(average_change, 2)      

output = (f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${sum_profit_loss}
Average  Change: ${avg_change_rounded}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})
Greatest Decrease in Profits:  {greatest_decrease_date} (${greatest_decrease_amount})
''')
#print analysis to terminal 
print(output)

#export a test file with the resutls
analysis = os.path.join("Analysis", "analysis.txt")

with open(analysis, "w", ) as writer:
    writer.writelines(output)
    

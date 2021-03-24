import os 
import csv

pollData_csv = os.path.join("Resources", "election_data.csv")

#The total number of votes cast
total_votes = 0

#A complete list of candidates who received votes
candidates = {}



with open (pollData_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")

    header = next(csvreader)
  
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        if row[2] not in candidates.keys():
            candidates.update({row[2]:1})
        
    print(candidates)






 # The percentage of votes each candidate won

  #The total number of votes each candidate won

  # The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:

  #output = (f'''
  #Election Results
  #-------------------------
 # Total Votes: 3521001
  #-------------------------
 # Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
 # -------------------------
  #''')
  #In addition, your final script should both print the analysis to the terminal and 

  #export a text file with the results

  #analysis = os.path.join("Analysis", "analysis.txt")

  #with open(analysis, "w") as writer:
      #writer.writelines()


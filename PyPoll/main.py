import os 
import csv

pollData_csv = os.path.join("Resources", "election_data.csv")

#The total number of votes cast
total_votes = 0

#A complete list of candidates who received votes
candidates = {}

# The percentage of votes each candidate won
#The total number of votes each candidate won
candidates_percent_toal =[]

# The winner of the election based on popular vote.
winning_percent = 0
winner = []

with open (pollData_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")

    header = next(csvreader)
  
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        if row[2] not in candidates.keys():
            candidates.update({row[2]:1})
    for key in candidates:
        vote_percentage = round(((candidates[key]/total_votes) * 100),2)
        candidates_percent_toal.append(f"{key}: {vote_percentage}% ({candidates[key]})")
        if vote_percentage > winning_percent:
            winning_percent = vote_percentage
            winner = key

output = (f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates_percent_toal}
-------------------------
Winner: {winner}
-------------------------
""")
print(output)


#In addition, your final script should both print the analysis to the terminal and 

#export a text file with the results

analysis = os.path.join("Analysis", "analysis.txt")

with open(analysis, "w") as writer:
    writer.writelines(output)


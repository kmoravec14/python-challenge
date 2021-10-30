# Modules
import os
import csv

total_votes=0
khan_votes=0
correy_votes=0
otooley_votes=0
 
# creating empty lists
voterid_list = []
county_list = []
candidate_list = []

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        voterid_list.append(int(row[0]))
        county_list.append(str(row[1]))
        candidate_list.append(str(row[2]))

print(" ")
total_votes=len(voterid_list)
print(total_votes)

# Modules
import os
import csv
from posix import X_OK

total_votes=0
li_votes =0
khan_votes=0
correy_votes=0
otooley_votes=0
numcandidates=0
 
# creating empty lists
voterid_list = []
county_list = []
candidate_list = []
candidates = []
tally = []

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        voterid_list.append(int(row[0]))
        county_list.append(str(row[1]))
        candidate_list.append(str(row[2]))

# Determine the number of votes
total_votes=len(voterid_list)
print(total_votes)

# Determine number of candidates and their names
candidate_set = set(candidate_list)
print(candidate_set)

numcandidates=len(candidate_set)
print(numcandidates)

candidate_setlist = list(candidate_set)

tally = [0,0,0,0]   # Need to automatically generate this - for loop below not working for some reason

# for i in range(1,numcandidates):
#    tally[i-1].append("Fun") 

for i in range(1,total_votes+1):
    for j in range(1,numcandidates+1):
      if str(candidate_list[i-1]) == str(candidate_setlist[j-1]):
        tally[j-1] = int(tally[j-1]) + 1

print(tally)
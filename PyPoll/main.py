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

candidate_setlist = list(candidate_set)

""" tally = []

for i in range(1,total_votes+1):
    if candidate_setlist[0] == candidate_list[i]:
        tally[0]=tally[0]+1
    if candidate_setlist[0] == candidate_list[i]:
        tally[1]=tally[0]+1
    if candidate_setlist[0] == candidate_list[i]:
        tally[2]=tally[0]+1
    if candidate_setlist[0] == candidate_list[i]:
        tally[3]=tally[0]+1 """

for i in range(1,total_votes):
      if candidate_list[i] == "Li":
        li_votes = li_votes + 1
print(li_votes)

khan_votes=0
correy_votes=0
otooley_votes=0


# print(tally)

""" 

a = candidate_setlist[0]
b = candidate_setlist[1]
c = candidate_setlist[2]
d = candidate_setlist[3]

print (a)
print (b)
print (c)
print (d)

votes = 0

#for i in range(1,numcandidates+1):
for i in range(2,2):
    def condition(x):
        return x == b #candidate_setlist[i-1]
    votes = sum(condition(x) for x in candidate_list)
print(votes)


 """
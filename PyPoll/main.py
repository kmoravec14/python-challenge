# Modules
import os
import csv

total_votes=0
numcandidates=0
Win_pct = 0
 
# creating empty lists
voterid_list = []
county_list = []
candidate_list = []
candidates = []
tally = []
pct = []

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

# Determine number of candidates and their names
candidate_set = set(candidate_list)
numcandidates=len(candidate_set)

# Convert set to list so it can be used in for loop 
candidate_setlist = list(candidate_set)

# Size Tally list to match number of candidates
for i in range(1,numcandidates+1):
    tally.append(0) 

# Size Pct list to match number of candidates
for i in range(1,numcandidates+1):
    pct.append(0)

# Count number of votes for each candidate
for i in range(1,total_votes+1):
    for j in range(1,numcandidates+1):
      if str(candidate_list[i-1]) == str(candidate_setlist[j-1]):
        tally[j-1] = int(tally[j-1]) + 1

# Calculate the percent of votes for each candidate
for i in range(1,numcandidates+1):
    pct[i-1] = (tally[i-1]/total_votes)*100

# Determine the winner of the election
for i in range(1,numcandidates+1):
    if pct[i-1] > Win_pct:
        Win_pct = pct[i-1]
        Win_index = i-1


# Print Output
print(" ")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for i in range(1,numcandidates+1):
    print(f"{candidate_setlist[i-1]}: {pct[i-1]:.2f}% ({tally[i-1]:.0f})")
print("--------------------------")
print(f"Winner: {candidate_setlist[Win_index]}")
print("--------------------------")

# Store the file path associated with the output file (note the backslash may be OS specific)

output_file = os.path.join("Analysis", "Output.txt")

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("--------------------------\n")
    for i in range(1,numcandidates+1):
        file.write(f"{candidate_setlist[i-1]}: {pct[i-1]:.2f}% ({tally[i-1]:.0f})\n")
    file.write("--------------------------\n")
    file.write(f"Winner: {candidate_setlist[Win_index]}\n")
    file.write("--------------------------\n")

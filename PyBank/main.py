# Modules
import os
import csv

total_months=0
total_profit=0


print(" ")
print("PyBank Class Homework #3")
print(" ")

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row[1])
        monthly_profit=int(row[1])
        total_profit=total_profit+monthly_profit
        total_months=total_months+1

    
    
    print(f"Total Months = {total_months}")
    print(f"Total Profit = {total_profit}")
    #print(f"Average Change in Profit = {ave_profit}")




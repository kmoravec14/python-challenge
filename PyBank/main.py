# Modules
import os
import csv

total_months=0
total_profit=0
#last_month_profit=0
total_change_profit=0
monthly_profit_list = []


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
        
        monthly_profit_list.append(int(row[1]))

        monthly_profit=int(row[1])
        """ if row == 1:
            last_month_profit=monthly_profit
        else:
            change_profit=monthly_profit-last_month_profit
            last_month_profit=monthly_profit
            total_change_profit=total_change_profit+change_profit    """   
        total_profit=total_profit+monthly_profit
        total_months=total_months+1
        

    total_months_alt=len(monthly_profit_list)
    last_month_profit=int(monthly_profit_list[0])

    # Lets try this again with index we just created in block above
    # In hindsight - probably easier to calculate change in profit with list and i, i-1....  / Change Later
    for i in range(1,total_months_alt):
        # print(monthly_profit_list[i])
        monthly_profit=int(monthly_profit_list[i])
        change_profit=monthly_profit-last_month_profit
        last_month_profit=int(monthly_profit_list[i])
        total_change_profit=total_change_profit+change_profit  

    ave_change_profit=total_change_profit/(total_months-1)
    
    print(f"Total Months = {total_months}")
    print(f"Total Months = {total_months_alt}")
    print(f"Total Profit = {total_profit}")
    print(f"Average Change in Profit = {ave_change_profit}")




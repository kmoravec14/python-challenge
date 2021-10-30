# Modules
import os
import csv

total_months=0
total_profit=0
total_change_profit=0
max_increase_profit=0
max_decrease_profit=0
monthly_profit_list = []
month_list = []


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
        month_list.append(str(row[0]))

    total_months=int(len(monthly_profit_list))
    last_month_profit=float(monthly_profit_list[0])
    total_profit=last_month_profit

    # Use monthly profit list to calculate desired financial information

    for i in range(1,total_months):
        monthly_profit=float(monthly_profit_list[i])
        month=str(month_list[i])
        total_profit=total_profit+monthly_profit
        change_profit=monthly_profit-last_month_profit
        last_month_profit=float(monthly_profit_list[i])
        total_change_profit=total_change_profit+change_profit  
        if change_profit > max_increase_profit:
            max_increase_profit_month=month
            max_increase_profit = change_profit
        if change_profit < max_decrease_profit:
            max_decrease_profit_month=month
            max_decrease_profit = change_profit

    ave_change_profit=total_change_profit/(total_months-1)

    print(f"Total Months: {total_months}")
    print(f"Total Profit: $ {total_profit:.0f}")
    print(f"Average Change in Profit: $ {ave_change_profit:.2f}")
    print(f"Greatest Increase in Profit: {max_increase_profit_month} (${max_increase_profit:.0f})")
    print(f"Greatest Decrease in Profit: {max_decrease_profit_month} (${max_decrease_profit:.0f})")
    print(" ")



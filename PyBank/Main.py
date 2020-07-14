# First we'll import the modules
# This will allow us to create file paths across operating systems
import os
import csv
import decimal
# identify csv file of interest
budget_csv = os.path.join('..','PyBank/Resources','budget_data.csv')

# blank variable lists to hold values
date = []
profit_loss = []
diff_from_prior_month = []
max_iv_month = []
max_dv_month = []

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header row for now
    header = next(csvreader)
    # Loop through the csv in source file
    # assign values to variable lists
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
    # loop through single list that has profit_loss values
    # create the diff between months    
    for r in range(len(profit_loss)-1):
            diff_from_prior_month.append(profit_loss[r+1]-profit_loss[r])
    # assign the max increase difference to a variable 
    max_iv = max(diff_from_prior_month)
    # assign the max decrease difference to a variable 
    max_dv = min(diff_from_prior_month)
# Set variable for output file
output_file = os.path.join("analysis","analysis.txt")

# print all summaries to terminal
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {(len(date))}")
print(f"Total: ${(sum(profit_loss))}")
print(f"Average Change: ${(round(float(sum(diff_from_prior_month)/(len(date)-1)),2))}")
print(f"Greatest Increase in Profits: {max_iv_month} ${max_iv}")
print(f"Greatest Decrease in Profits: {max_dv_month} ${max_dv}")

#  Open the output file
with open(output_file, "w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("-----------------------\n")
    analysis.write(f"Total Months: {(len(date))}\n")
    analysis.write(f"Total: ${(sum(profit_loss))}\n")
    analysis.write(f"Average Change: ${(round(float(sum(diff_from_prior_month)/(len(date)-1)),2))}\n")
    analysis.write(f"Greatest Increase in Profits: {max_iv_month} ${max_iv}\n")
    analysis.write(f"Greatest Decrease in Profits: {max_dv_month} ${max_dv}\n")

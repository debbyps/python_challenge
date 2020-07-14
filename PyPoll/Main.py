# First we'll import the modules
# This will allow us to create file paths across operating systems
import os
import csv
from collections import Counter

# identify csv file of interest
election_csv = os.path.join('..','PyPoll/Resources','election_data.csv')

# blank variable lists to hold values
candidates = []
winner = []
# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header row for now
    header = next(csvreader)
    # Loop through the csv in source file assign values to variable lists
    for row in csvreader:
        candidates.append(row[2])
total_count = len(candidates)
candidate_count = Counter(candidates)

#Find the maximum number of votes 
max_votes=max(candidate_count.values()) 
#Search for people having maximum votes and store in a list 
for i in candidate_count.keys():
    if candidate_count[i]==max_votes:
        winner = i

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_count}")
print("-------------------------")
# Prints the nicely formatted dictionary
# but can i load this into a variable????????????????????????????????????????????
for key,value in candidate_count.items():
    print(f"{key}: {(round(float(value/total_count),2)*100)}% ({value})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Set variable for output file
output_file = os.path.join("analysis","analysis.txt")
#  Open the output file
with open(output_file, "w") as analysis:
    analysis.write("Election Results\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Total Votes: {total_count}\n")
    analysis.write("-------------------------\n")
    # Prints the nicely formatted dictionary
    # but can i load this into a variable????????????????????????????????????????????
    for key,value in candidate_count.items():
        analysis.write(f"{key}: {(round(float((value)/(total_count)),2))*100}% ({value})\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Winner: {winner}\n")
    analysis.write("-------------------------\n")
    
# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
changes_pl = []
greatest_increase = ["",0]
greatest_decrease = ["", 999999999]
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months = 1
    total_net = int(first_row[1])
    previous = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months +=1
        total_net +=int(row[1])
        # Track the net change
        current_net = int(row[1]) - previous
        previous = int(row[1])
        changes_pl.append(current_net)

        # Calculate the greatest increase in profits (month and amount)
        if current_net > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = current_net

        # Calculate the greatest decrease in losses (month and amount)
        if current_net < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = current_net


# Calculate the average net change across the months
average_change = sum(changes_pl)/len(changes_pl)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os
import sys

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
vote_counts = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = None
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list: 
            candidate_list.append(candidate_name)
            vote_counts[candidate_name] = 0

        # Add a vote to the candidate's count
        vote_counts[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(total_votes)

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")
    
    output = "Election Results \n\n" + "-" * 12 + "\n\n" + "Total Votes: " + str(total_votes) + "\n\n" + "-" * 12 + "\n\n"
    print(output)

    # Loop through the candidates to determine vote percentages and identify the winner
    candidate_output = ""
    for candidate, votes in vote_counts.items(): 

        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100 if total_votes > 0 else 0

        # Update the winning candidate if this one has more votes
        if votes > winning_count: 
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        vote_percentage_rounded = format(vote_percentage, '.3f')
        candidate_output += candidate + ": " + str(vote_percentage_rounded) + "% " + "(" + str(votes) + ")" + "\n\n"
        print(candidate + ": " + str(vote_percentage_rounded) + "% " + "(" + str(votes) + ")" + "\n\n")
    
        # Output candidate
        winner_output = "-" * 12 + "\n\n" + "Winner: " + winning_candidate + "\n\n" + "-" * 12 + "\n\n"
    output += candidate_output + winner_output
    print(winner_output)
        

# File export
    file = open("analysis/election_analysis1.txt", "w")
    # Save the winning candidate summary to the text file

    file.write(output)
    file.close()